#!/usr/bin/env python3
"""
Task Scorer — Auto-evaluate employee deliverables against rubric
Usage: python task-scorer.py <employee> <task_id> <output_file>
"""
import sys
import json
import os
from datetime import datetime
from pathlib import Path

RUBRIC_PATH = "/root/moxie_hq/cmo/rubrics/employee-rubric.md"
SCORES_DIR = "/root/moxie_hq/cmo/scores"

# Dimension weights (default)
DEFAULT_WEIGHTS = {
    "output_completeness": 0.20,
    "business_impact": 0.25,
    "accuracy_evidence": 0.15,
    "speed_cycle": 0.10,
    "autonomy": 0.10,
    "reusability": 0.10,
    "communication": 0.10
}

# Per-role weight adjustments
ROLE_WEIGHTS = {
    "mira": {"accuracy_evidence": 0.25, "speed_cycle": 0.05},
    "kiro": {"business_impact": 0.30, "accuracy_evidence": 0.10},
    "iris": {"business_impact": 0.30, "accuracy_evidence": 0.10},
    "jax": {"autonomy": 0.15, "business_impact": 0.30},
    "ember": {"autonomy": 0.15, "business_impact": 0.30},
    "pax": {"autonomy": 0.15, "business_impact": 0.30},
    "nova": {"accuracy_evidence": 0.20, "business_impact": 0.30}
}

def get_weights(employee):
    weights = DEFAULT_WEIGHTS.copy()
    adjustments = ROLE_WEIGHTS.get(employee.lower(), {})
    for dim, new_weight in adjustments.items():
        # Normalize: reduce others proportionally
        old_weight = weights[dim]
        delta = new_weight - old_weight
        other_dims = [d for d in weights if d != dim]
        for other in other_dims:
            weights[other] -= delta * (weights[other] / (1 - old_weight))
        weights[dim] = new_weight
    return weights

def score_task(employee, task_id, output_file):
    """Generate scorecard for completed task."""
    weights = get_weights(employee)
    
    # Check if output file exists (automatic pass/fail gate)
    output_exists = Path(output_file).exists() if output_file else False
    
    scorecard = {
        "employee": employee,
        "task_id": task_id,
        "output_file": output_file,
        "scored_at": datetime.utcnow().isoformat(),
        "auto_fail": not output_exists,
        "dimensions": {},
        "overall_score": 0,
        "improvement_focus": None
    }
    
    if not output_exists:
        scorecard["notes"] = "AUTO-FAIL: Output file not found"
        return scorecard
    
    # Read output file for auto-scoring heuristics
    try:
        content = Path(output_file).read_text()
        content_lower = content.lower()
    except:
        content = ""
        content_lower = ""
    
    # Auto-score heuristics (can be overridden by manual review)
    dims = {}
    
    # Output completeness: check for sections, checklists, file paths
    has_checklist = "- [ ]" in content or "- [x]" in content
    has_sections = content.count("##") >= 2
    dims["output_completeness"] = 5 if (has_checklist and has_sections) else (3 if has_sections else 1)
    
    # Business impact: look for revenue/acquisition/conversion mentions
    impact_keywords = ["revenue", "acquisition", "conversion", "mrr", "paid", "signup", "traffic"]
    impact_score = sum(1 for k in impact_keywords if k in content_lower)
    dims["business_impact"] = 5 if impact_score >= 3 else (3 if impact_score >= 1 else 1)
    
    # Accuracy & evidence: look for links, data, quotes
    has_links = "http" in content
    has_data = any(x in content for x in ["%", "$", "users", "visits", "traffic"])
    dims["accuracy_evidence"] = 5 if (has_links and has_data) else (3 if (has_links or has_data) else 1)
    
    # Speed: default to 3 (normal), manual override needed
    dims["speed_cycle"] = 3
    
    # Autonomy: check for issues_rishi references (blocker logging)
    has_blocker_log = "issues_rishi" in content_lower
    dims["autonomy"] = 5 if has_blocker_log else 3
    
    # Reusability: look for templates, SOPs, checklists
    reusable_keywords = ["template", "sop", "checklist", "how to", "workflow"]
    reusable_score = sum(1 for k in reusable_keywords if k in content_lower)
    dims["reusability"] = 5 if reusable_score >= 2 else (3 if reusable_score >= 1 else 1)
    
    # Communication: check for exec-ready structure
    has_summary = "summary" in content_lower or "deliverable" in content_lower
    has_next_actions = "next" in content_lower or "action" in content_lower
    dims["communication"] = 5 if (has_summary and has_next_actions) else (3 if has_summary else 1)
    
    scorecard["dimensions"] = dims
    
    # Calculate weighted overall score
    overall = sum(dims[d] * weights[d] for d in dims)
    scorecard["overall_score"] = round(overall, 1)
    
    # Identify lowest dimension for improvement focus
    lowest_dim = min(dims, key=dims.get)
    dim_names = {
        "output_completeness": "Output Completeness",
        "business_impact": "Business Impact",
        "accuracy_evidence": "Accuracy & Evidence",
        "speed_cycle": "Speed/Cycle Time",
        "autonomy": "Autonomy & Unblockability",
        "reusability": "Reusability/Systemization",
        "communication": "Communication Quality"
    }
    scorecard["improvement_focus"] = dim_names[lowest_dim]
    
    return scorecard

def save_scorecard(scorecard):
    """Save scorecard to disk."""
    employee = scorecard["employee"].lower()
    task_id = scorecard["task_id"]
    
    # Create scores directory
    emp_dir = Path(SCORES_DIR) / employee
    emp_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON
    score_path = emp_dir / f"{task_id}.json"
    with open(score_path, 'w') as f:
        json.dump(scorecard, f, indent=2)
    
    # Save human-readable MD
    md_path = emp_dir / f"{task_id}.md"
    with open(md_path, 'w') as f:
        f.write(f"# Scorecard: {employee} — {task_id}\n\n")
        f.write(f"**Scored:** {scorecard['scored_at']}\n\n")
        f.write(f"**Output:** `{scorecard['output_file']}`\n\n")
        f.write(f"**Auto-Fail:** {'YES' if scorecard['auto_fail'] else 'No'}\n\n")
        f.write(f"## Overall Score: {scorecard['overall_score']}/5.0\n\n")
        
        if scorecard.get('notes'):
            f.write(f"**Notes:** {scorecard['notes']}\n\n")
        
        f.write("## Dimension Scores\n\n")
        for dim, score in scorecard['dimensions'].items():
            f.write(f"- {dim}: {score}/5\n")
        
        f.write(f"\n## Improvement Focus\n\n")
        f.write(f"**Priority area:** {scorecard['improvement_focus']}\n\n")
        f.write("Suggested prompt/SOUL update to improve this dimension.\n")
    
    return str(score_path), str(md_path)

def update_soul(employee, scorecard):
    """Update employee SOUL.md with latest score."""
    soul_path = Path(f"/root/moxie_hq/cmo/employees/{employee.lower()}-soul.md")
    if not soul_path.exists():
        return None
    
    content = soul_path.read_text()
    
    # Check if Recent Scores section exists
    if "## Recent Scores" not in content:
        content += "\n\n## Recent Scores\n\n"
        content += "| Date | Task | Overall | Focus Area |\n"
        content += "|------|------|---------|------------|\n"
    
    # Add new score row
    new_row = f"| {scorecard['scored_at'][:10]} | {scorecard['task_id']} | {scorecard['overall_score']}/5 | {scorecard['improvement_focus']} |\n"
    
    # Insert after header row
    lines = content.split('\n')
    header_idx = None
    for i, line in enumerate(lines):
        if '| Date | Task | Overall |' in line:
            header_idx = i + 1  # After the separator row
            break
    
    if header_idx:
        lines.insert(header_idx + 1, new_row.rstrip())
        content = '\n'.join(lines)
    
    # Update Improvement Focus section
    focus_section = f"\n\n## Current Improvement Focus\n\n"
    focus_section += f"**Dimension:** {scorecard['improvement_focus']}\n\n"
    focus_section += f"**Latest Score:** {scorecard['overall_score']}/5\n\n"
    focus_section += f"**Action:** Review and strengthen {scorecard['improvement_focus']} in next deliverable.\n"
    
    if "## Current Improvement Focus" in content:
        # Replace existing section
        import re
        content = re.sub(r'## Current Improvement Focus.*?(?=\n## |\Z)', focus_section.strip() + '\n\n', content, flags=re.DOTALL)
    else:
        content += focus_section
    
    soul_path.write_text(content)
    return str(soul_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python task-scorer.py <employee> <task_id> [output_file]")
        sys.exit(1)
    
    employee = sys.argv[1]
    task_id = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    scorecard = score_task(employee, task_id, output_file)
    json_path, md_path = save_scorecard(scorecard)
    soul_path = update_soul(employee, scorecard)
    
    print(f"Scorecard saved: {md_path}")
    print(f"Overall: {scorecard['overall_score']}/5")
    print(f"Focus: {scorecard['improvement_focus']}")
    if soul_path:
        print(f"SOUL updated: {soul_path}")
