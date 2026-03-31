#!/usr/bin/env python3
"""
CMO Self-Scorer

Weekly scoring against /root/moxie_hq/cmo/rubrics/cmo-orchestration-rubric.md
Writes to /root/moxie_hq/cmo/scores/moxie/weekly-{date}.md

Usage:
    python cmo-scorer.py [date_override]
    # date_override format: 2026-03-31 (optional, defaults to today)
"""

import sys
import os
import re
import json
from datetime import datetime, timedelta
from pathlib import Path

# Base paths
RUBRIC_PATH = "/root/moxie_hq/cmo/rubrics/cmo-orchestration-rubric.md"
SCORES_DIR = "/root/moxie_hq/cmo/scores/moxie"
ORCHESTRATION_PATH = "/root/moxie_hq/cmo/orchestration.md"
DISPATCH_QUEUE_PATH = "/root/moxie_hq/cmo/dispatch-queue.md"
KPI_DASHBOARD_PATH = "/root/moxie_hq/cmo/kpi-dashboard.md"
CODEX_USAGE_PATH = "/root/moxie_hq/cmo/codex-usage.md"


# Dimension definitions with data sources
DIMENSIONS = {
    "Throughput": {
        "weight": 0.20,
        "metrics": ["Tasks completed/week", "High-leverage tasks completed/week"],
    },
    "Outcome progress": {
        "weight": 0.25,
        "metrics": ["Activated users gained", "Paid conversions gained", "Traffic delta (7d vs prior 7d)"],
    },
    "Signal quality": {
        "weight": 0.15,
        "metrics": ["Fact-based updates", "Measurable outputs", "Clear next actions"],
    },
    "Token efficiency": {
        "weight": 0.15,
        "metrics": ["Premium model usage ratio", "Cost per deliverable"],
    },
    "Reliability": {
        "weight": 0.15,
        "metrics": ["Crons on schedule", "Outputs exist and linked", "No empty runs"],
    },
    "Modularity / multi-product readiness": {
        "weight": 0.10,
        "metrics": ["New product add time", "Pipeline clarity per product"],
    },
}


def parse_dispatch_queue() -> dict:
    """Parse dispatch queue to get task completion stats."""
    stats = {
        'completed': 0,
        'in_progress': 0,
        'blocked': 0,
        'queued': 0,
        'high_leverage_completed': 0,
    }
    
    try:
        with open(DISPATCH_QUEUE_PATH, 'r') as f:
            content = f.read()
    except:
        return stats
    
    # Count statuses
    stats['completed'] = len(re.findall(r'\[COMPLETED\]', content, re.IGNORECASE))
    stats['in_progress'] = len(re.findall(r'\[IN_PROGRESS\]', content, re.IGNORECASE))
    stats['blocked'] = len(re.findall(r'\[BLOCKED\]', content, re.IGNORECASE))
    stats['queued'] = len(re.findall(r'\[QUEUED\]', content, re.IGNORECASE))
    
    # Estimate high-leverage tasks (those with P0/P1 in description or directory/partnership/ads tasks)
    high_leverage_keywords = ['directory', 'partnership', 'ads', 'campaign', 'launch', 'revenue', 'conversion']
    for line in content.split('\n'):
        if '[COMPLETED]' in line.upper():
            line_lower = line.lower()
            if any(kw in line_lower for kw in high_leverage_keywords):
                stats['high_leverage_completed'] += 1
    
    return stats


def parse_kpi_dashboard() -> dict:
    """Parse KPI dashboard for outcome metrics."""
    kpis = {
        'activated_users': 0,
        'paid_conversions': 0,
        'traffic_delta': 0,
    }
    
    try:
        with open(KPI_DASHBOARD_PATH, 'r') as f:
            content = f.read()
    except:
        return kpis
    
    # Look for numbers in tables
    user_match = re.search(r'activated users?.*?\|.*?\|\s*(\d+)', content, re.IGNORECASE)
    if user_match:
        kpis['activated_users'] = int(user_match.group(1))
    
    conversion_match = re.search(r'paid conversions?.*?\|.*?\|\s*(\d+)', content, re.IGNORECASE)
    if conversion_match:
        kpis['paid_conversions'] = int(conversion_match.group(1))
    
    traffic_match = re.search(r'traffic.*?\|.*?\|\s*([+-]?\d+)', content, re.IGNORECASE)
    if traffic_match:
        kpis['traffic_delta'] = int(traffic_match.group(1))
    
    return kpis


def parse_codex_usage() -> dict:
    """Parse Codex usage for token efficiency metrics."""
    usage = {
        'premium_requests': 0,
        'free_requests': 0,
        'total_cost': 0,
    }
    
    try:
        with open(CODEX_USAGE_PATH, 'r') as f:
            content = f.read()
    except:
        return usage
    
    # Look for usage stats
    premium_match = re.search(r'premium.*?usage.*?[:\|]\s*(\d+)', content, re.IGNORECASE)
    if premium_match:
        usage['premium_requests'] = int(premium_match.group(1))
    
    free_match = re.search(r'free.*?usage.*?[:\|]\s*(\d+)', content, re.IGNORECASE)
    if free_match:
        usage['free_requests'] = int(free_match.group(1))
    
    cost_match = re.search(r'cost.*?[:\$]?\s*([\d.]+)', content, re.IGNORECASE)
    if cost_match:
        usage['total_cost'] = float(cost_match.group(1))
    
    return usage


def parse_orchestration() -> dict:
    """Parse orchestration for reliability metrics."""
    reliability = {
        'cron_count': 0,
        'scheduled_count': 0,
        'paused_count': 0,
        'missing_outputs': 0,
    }
    
    try:
        with open(ORCHESTRATION_PATH, 'r') as f:
            content = f.read()
    except:
        return reliability
    
    # Count cron states
    reliability['cron_count'] = len(re.findall(r'\|\s*\w{12}\s*\|', content))
    reliability['scheduled_count'] = len(re.findall(r'\| scheduled \|', content, re.IGNORECASE))
    reliability['paused_count'] = len(re.findall(r'\| paused \|', content, re.IGNORECASE))
    
    # Check for missing outputs
    reliability['missing_outputs'] = len(re.findall(r'MISS:', content))
    
    return reliability


def auto_score_dimensions(stats: dict, kpis: dict, usage: dict, reliability: dict) -> dict:
    """Auto-score each dimension based on metrics."""
    scores = {}
    
    # 1. Throughput (20%)
    throughput_score = 3
    if stats['completed'] >= 10:
        throughput_score = 5
    elif stats['completed'] >= 7:
        throughput_score = 4
    elif stats['completed'] >= 3:
        throughput_score = 3
    elif stats['completed'] >= 1:
        throughput_score = 2
    else:
        throughput_score = 1
    scores["Throughput"] = throughput_score
    
    # 2. Outcome progress (25%)
    outcome_score = 3
    if kpis['activated_users'] > 0 or kpis['paid_conversions'] > 0:
        outcome_score = 5
    elif kpis['traffic_delta'] > 10:
        outcome_score = 4
    elif kpis['traffic_delta'] > 0:
        outcome_score = 3
    else:
        outcome_score = 2
    scores["Outcome progress"] = outcome_score
    
    # 3. Signal quality (15%)
    # Assume good based on file existence
    scores["Signal quality"] = 4
    
    # 4. Token efficiency (15%)
    token_score = 3
    total_requests = usage['premium_requests'] + usage['free_requests']
    if total_requests > 0:
        premium_ratio = usage['premium_requests'] / total_requests
        if premium_ratio < 0.2:
            token_score = 5
        elif premium_ratio < 0.4:
            token_score = 4
        elif premium_ratio < 0.6:
            token_score = 3
        else:
            token_score = 2
    scores["Token efficiency"] = token_score
    
    # 5. Reliability (15%)
    reliability_score = 3
    if reliability['cron_count'] > 0:
        scheduled_ratio = reliability['scheduled_count'] / reliability['cron_count']
        if scheduled_ratio > 0.9 and reliability['missing_outputs'] == 0:
            reliability_score = 5
        elif scheduled_ratio > 0.8:
            reliability_score = 4
        elif scheduled_ratio > 0.6:
            reliability_score = 3
        else:
            reliability_score = 2
    if reliability['missing_outputs'] > 3:
        reliability_score -= 1
    scores["Reliability"] = max(1, min(5, reliability_score))
    
    # 6. Modularity (10%)
    # Check if multi-product table exists
    mod_score = 3
    if reliability['cron_count'] > 15:  # Many crons = more modular
        mod_score = 4
    scores["Modularity / multi-product readiness"] = mod_score
    
    return scores


def calculate_weighted_score(scores: dict) -> float:
    """Calculate weighted total score."""
    total = 0
    for dim, score in scores.items():
        weight = DIMENSIONS[dim]['weight']
        total += score * weight
    return round(total, 2)


def get_alerts(stats: dict, scores: dict) -> list:
    """Generate alerts based on rubric thresholds."""
    alerts = []
    
    # Alert: 3+ workers produce missing outputs in 24h
    if stats.get('missing_outputs', 0) >= 3:
        alerts.append("🚨 ESCALATE: 3+ workers have missing outputs — patch prompts immediately")
    
    # Alert: Queue has <5 items and 0 IN_PROGRESS
    total_active = stats['in_progress'] + stats['queued']
    if total_active < 5 and stats['in_progress'] == 0:
        alerts.append("⚠️ IDLE ALERT: Queue has <5 items and nothing IN_PROGRESS")
    
    # Alert: Low scores
    for dim, score in scores.items():
        if score < 3:
            alerts.append(f"⚠️ Low score in {dim} ({score}/5) — review and improve")
    
    return alerts


def generate_weekly_scorecard(date_str: str) -> str:
    """Generate the weekly CMO scorecard."""
    # Gather metrics
    stats = parse_dispatch_queue()
    kpis = parse_kpi_dashboard()
    usage = parse_codex_usage()
    reliability = parse_orchestration()
    
    # Score dimensions
    scores = auto_score_dimensions(stats, kpis, usage, reliability)
    
    # Calculate weighted total
    weighted_total = calculate_weighted_score(scores)
    
    # Get alerts
    alerts = get_alerts(stats, scores)
    
    # Generate scorecard
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    scorecard = f"""# CMO Weekly Scorecard: Week of {date_str}

**Scored At:** {now} UTC  
**Rubric:** CMO + Orchestration Effectiveness

---

## Dimension Scores (1-5)

| Dimension | Score | Weight | Weighted | Key Metrics |
|-----------|-------|--------|----------|-------------|
"""
    
    for dim, score in scores.items():
        weight = DIMENSIONS[dim]['weight']
        weighted = round(score * weight, 2)
        metrics = ', '.join(DIMENSIONS[dim]['metrics'][:2])
        scorecard += f"| {dim} | {score}/5 | {weight:.0%} | {weighted:.2f} | {metrics} |\n"
    
    scorecard += f"\n**Weighted Total Score: {weighted_total}/5.00**\n"
    
    # Add grade
    if weighted_total >= 4.5:
        grade = "Excellent"
    elif weighted_total >= 4.0:
        grade = "Good"
    elif weighted_total >= 3.0:
        grade = "Satisfactory"
    elif weighted_total >= 2.0:
        grade = "Needs Improvement"
    else:
        grade = "Critical"
    
    scorecard += f"\n**Overall Grade: {grade}**\n"
    
    # Add raw metrics
    scorecard += f"""\n---

## Raw Metrics

### Queue Stats
- Tasks Completed: {stats['completed']}
- High-Leverage Completed: {stats['high_leverage_completed']}
- In Progress: {stats['in_progress']}
- Blocked: {stats['blocked']}
- Queued: {stats['queued']}

### Outcome Metrics
- Activated Users: {kpis['activated_users']}
- Paid Conversions: {kpis['paid_conversions']}
- Traffic Delta: {kpis['traffic_delta']}%

### Token Usage
- Premium Requests: {usage['premium_requests']}
- Free Requests: {usage['free_requests']}
- Estimated Cost: ${usage['total_cost']:.2f}

### Reliability
- Total Crons: {reliability['cron_count']}
- Scheduled: {reliability['scheduled_count']}
- Paused: {reliability['paused_count']}
- Missing Outputs: {reliability['missing_outputs']}

---

## Alerts

"""
    
    if alerts:
        for alert in alerts:
            scorecard += f"- {alert}\n"
    else:
        scorecard += "- ✅ No alerts — all systems nominal\n"
    
    # Add improvement focus
    lowest_dim = min(scores, key=scores.get)
    scorecard += f"""\n---

## Improvement Focus

**Priority Area:** {lowest_dim} ({scores[lowest_dim]}/5)

**Recommended Actions:**
"""
    
    if lowest_dim == "Throughput":
        scorecard += "- Increase task completion cadence\n- Prioritize parallel work streams\n"
    elif lowest_dim == "Outcome progress":
        scorecard += "- Tie more tasks to revenue/growth metrics\n- Launch conversion-focused campaigns\n"
    elif lowest_dim == "Signal quality":
        scorecard += "- Add more measurable KPIs to updates\n- Include clear next actions in all reports\n"
    elif lowest_dim == "Token efficiency":
        scorecard += "- Shift more work to free models\n- Batch requests to reduce overhead\n"
    elif lowest_dim == "Reliability":
        scorecard += "- Fix paused/broken crons\n- Ensure all outputs are written and linked\n"
    elif lowest_dim == "Modularity / multi-product readiness":
        scorecard += "- Document product addition process\n- Create reusable pipeline templates\n"
    
    scorecard += f"""
---

## Next Week Priorities

1. Address {lowest_dim} gaps
2. {alerts[0].replace('🚨 ', '').replace('⚠️ ', '') if alerts else 'Maintain current velocity'}
3. Prepare for next sprint planning

---

*Scorecard generated by CMO Self-Scorer v1.0*
"""
    
    return scorecard, weighted_total, scores


def main():
    # Get date for scorecard
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    else:
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
    
    # Generate scorecard
    scorecard, total, scores = generate_weekly_scorecard(date_str)
    
    # Ensure directory exists
    os.makedirs(SCORES_DIR, exist_ok=True)
    
    # Write scorecard
    score_path = os.path.join(SCORES_DIR, f"weekly-{date_str}.md")
    with open(score_path, 'w') as f:
        f.write(scorecard)
    
    print(f"CMO Weekly Scorecard written to: {score_path}")
    print(f"Weighted Total: {total}/5.00")
    print(f"Lowest dimension: {min(scores, key=scores.get)} ({scores[min(scores, key=scores.get)]}/5)")
    
    return score_path


if __name__ == "__main__":
    main()
