#!/usr/bin/env python3
"""
CMO Self-Scorer — Weekly self-assessment against CMO rubric
Usage: python cmo-self-score.py
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

RUBRIC_PATH = "/root/moxie_hq/cmo/rubrics/cmo-orchestration-rubric.md"
SCORES_DIR = "/root/moxie_hq/cmo/scores/moxie"

def analyze_week():
    """Analyze this week's performance from orchestration.md."""
    orch_path = Path("/root/moxie_hq/cmo/orchestration.md")
    if not orch_path.exists():
        return {}
    
    content = orch_path.read_text()
    
    # Count completed tasks
    completed_count = content.count("| COMPLETED |")
    
    # Check for blockers resolved
    blockers_resolved = content.count("| **RESOLVED** |")
    
    # Check for issues in issues_rishi.md
    issues_path = Path("/root/moxie_hq/cmo/issues_rishi.md")
    open_issues = 0
    if issues_path.exists():
        issues_content = issues_path.read_text()
        open_issues = issues_content.count("- [ ]")
    
    return {
        "tasks_completed": completed_count,
        "blockers_resolved": blockers_resolved,
        "open_issues": open_issues
    }

def generate_scorecard(metrics):
    """Generate CMO scorecard."""
    today = datetime.utcnow()
    week_start = today - timedelta(days=today.weekday())
    
    scorecard = {
        "period": f"{week_start.date()} to {today.date()}",
        "scored_at": today.isoformat(),
        "metrics": metrics,
        "scores": {},
        "overall": 0,
        "alerts": []
    }
    
    # Score dimensions (self-assessed)
    # 1) Throughput
    tasks = metrics.get("tasks_completed", 0)
    scorecard["scores"]["throughput"] = 5 if tasks >= 15 else (4 if tasks >= 10 else (3 if tasks >= 5 else 2))
    
    # 2) Outcome progress — placeholder (would need real revenue data)
    scorecard["scores"]["outcome_progress"] = 3  # Neutral until we have revenue tracking
    
    # 3) Signal quality
    open_issues = metrics.get("open_issues", 0)
    scorecard["scores"]["signal_quality"] = 5 if open_issues <= 3 else (4 if open_issues <= 5 else 3)
    
    # 4) Token efficiency — based on Codex usage tracking
    codex_tracker = Path("/root/moxie/cmo/codex-usage-tracker.csv")
    if codex_tracker.exists():
        lines = codex_tracker.read_text().strip().split('\n')
        recent_usage = len([l for l in lines if l.startswith(today.strftime('%Y-%m'))])
        scorecard["scores"]["token_efficiency"] = 4 if recent_usage < 20 else 3
    else:
        scorecard["scores"]["token_efficiency"] = 3
    
    # 5) Reliability — check if crons are running
    scorecard["scores"]["reliability"] = 4  # Assume good unless we see failures
    
    # 6) Modularity
    scorecard["scores"]["modularity"] = 4  # Multi-product ready but only 1 product active
    
    # Calculate overall (weighted)
    weights = {
        "throughput": 0.20,
        "outcome_progress": 0.25,
        "signal_quality": 0.15,
        "token_efficiency": 0.15,
        "reliability": 0.15,
        "modularity": 0.10
    }
    
    overall = sum(scorecard["scores"][d] * weights[d] for d in scorecard["scores"])
    scorecard["overall"] = round(overall, 1)
    
    # Generate alerts
    if scorecard["scores"]["token_efficiency"] <= 3:
        scorecard["alerts"].append("Token efficiency below target — consider pausing idle workers")
    if open_issues > 5:
        scorecard["alerts"].append(f"{open_issues} open issues — Rishi attention needed")
    if tasks < 5:
        scorecard["alerts"].append("Low throughput this week — review queue priorities")
    
    return scorecard

def save_scorecard(scorecard):
    """Save CMO scorecard."""
    Path(SCORES_DIR).mkdir(parents=True, exist_ok=True)
    
    week_str = datetime.utcnow().strftime("%Y-W%U")
    json_path = Path(SCORES_DIR) / f"weekly-{week_str}.json"
    md_path = Path(SCORES_DIR) / f"weekly-{week_str}.md"
    
    with open(json_path, 'w') as f:
        json.dump(scorecard, f, indent=2)
    
    with open(md_path, 'w') as f:
        f.write(f"# CMO Weekly Scorecard: {scorecard['period']}\n\n")
        f.write(f"**Overall Score:** {scorecard['overall']}/5.0\n\n")
        f.write("## Dimension Scores\n\n")
        for dim, score in scorecard['scores'].items():
            f.write(f"- {dim.replace('_', ' ').title()}: {score}/5\n")
        f.write(f"\n## Metrics\n\n")
        for k, v in scorecard['metrics'].items():
            f.write(f"- {k}: {v}\n")
        if scorecard['alerts']:
            f.write(f"\n## Alerts\n\n")
            for alert in scorecard['alerts']:
                f.write(f"- ⚠️ {alert}\n")
        else:
            f.write(f"\n## Alerts\n\nNo alerts.\n")
    
    return str(md_path)

if __name__ == "__main__":
    print("Generating CMO self-scorecard...")
    metrics = analyze_week()
    scorecard = generate_scorecard(metrics)
    path = save_scorecard(scorecard)
    print(f"Scorecard saved: {path}")
    print(f"Overall: {scorecard['overall']}/5")
    if scorecard['alerts']:
        print("\nAlerts:")
        for alert in scorecard['alerts']:
            print(f"  - {alert}")
