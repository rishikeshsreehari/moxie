#!/usr/bin/env python3
"""
SOUL Updater

Reads latest scorecard and updates employee SOUL.md:
- Updates section: `## Recent Scores`
- Adds: `## Improvement Focus` based on lowest-scoring dimension
- Appends: `## Suggested Next Task` based on pattern

Usage:
    python soul-updater.py <employee_name> <task_id>
"""

import sys
import os
import re
from datetime import datetime
from pathlib import Path

# Base paths
SOUL_BASE_DIR = "/root/moxie_hq/cmo/employees"
SCORES_BASE_DIR = "/root/moxie_hq/cmo/scores"


def get_employee_soul_path(employee: str) -> str:
    """Get the path to employee's SOUL file."""
    return os.path.join(SOUL_BASE_DIR, f"{employee.lower()}-soul.md")


def get_scorecard_path(employee: str, task_id: str) -> str:
    """Get the path to the scorecard file."""
    return os.path.join(SCORES_BASE_DIR, employee.lower(), f"{task_id}.md")


def parse_scorecard(scorecard_path: str) -> dict:
    """Parse the scorecard and extract key information."""
    try:
        with open(scorecard_path, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading scorecard: {e}")
        return None
    
    data = {
        'task_id': '',
        'scores': {},
        'total': 0,
        'grade': '',
        'improvement_dim': '',
        'improvement_score': 0,
        'improvement_suggestion': '',
        'suggested_next_task': '',
    }
    
    # Extract task ID from header
    task_match = re.search(r'# Task Scorecard: (.+)', content)
    if task_match:
        data['task_id'] = task_match.group(1)
    
    # Extract dimension scores from table
    score_pattern = r'\|\s*([^|]+?)\s*\|\s*(\d+)/5\s*\|\s*([\d%.]+)\s*\|\s*([\d.]+)\s*\|'
    for match in re.finditer(score_pattern, content):
        dim = match.group(1).strip()
        score = int(match.group(2))
        if dim not in ['Dimension', '---'] and not dim.startswith('---'):
            data['scores'][dim] = score
    
    # Extract weighted total
    total_match = re.search(r'\*\*Weighted Total Score: ([\d.]+)/5\.00\*\*', content)
    if total_match:
        data['total'] = float(total_match.group(1))
    
    # Extract grade
    grade_match = re.search(r'\*\*Grade: ([^*]+)\*\*', content)
    if grade_match:
        data['grade'] = grade_match.group(1).strip()
    
    # Extract improvement focus
    lowest_match = re.search(r'\*\*Lowest Dimension:\*\* ([^(]+) \((\d+)/5\)', content)
    if lowest_match:
        data['improvement_dim'] = lowest_match.group(1).strip()
        data['improvement_score'] = int(lowest_match.group(2))
    
    # Extract improvement suggestion
    suggestion_match = re.search(r'\*\*Suggestion:\*\* (.+?)(?=\n\n---|\Z)', content, re.DOTALL)
    if suggestion_match:
        data['improvement_suggestion'] = suggestion_match.group(1).strip()
    
    # Extract suggested next task
    next_task_match = re.search(r'## Suggested Next Task\n\n(.+?)(?=\n\n---|\Z)', content, re.DOTALL)
    if next_task_match:
        data['suggested_next_task'] = next_task_match.group(1).strip()
    
    return data


def read_soul_content(soul_path: str) -> str:
    """Read the SOUL file content."""
    try:
        with open(soul_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading SOUL file: {e}")
        return None


def update_recent_scores_section(content: str, score_data: dict) -> str:
    """Update or add the ## Recent Scores section."""
    now = datetime.utcnow().strftime("%Y-%m-%d")
    
    score_entry = f"""| {now} | {score_data['task_id']} | {score_data['total']:.2f} | {score_data['grade']} |
"""
    
    # Check if Recent Scores section exists
    if '## Recent Scores' in content:
        # Find the section and append to table
        pattern = r'(## Recent Scores\n\n\| Date \| Task \| Score \| Grade \|\n\|[-|]+\n)([^#]*?)(?=\n## |\Z)'
        
        def replace_section(match):
            header = match.group(1)
            existing = match.group(2)
            return header + score_entry + existing
        
        new_content = re.sub(pattern, replace_section, content, flags=re.DOTALL)
        
        # If pattern didn't match, section exists but table format differs
        if new_content == content:
            # Try to find just the header and add table
            pattern = r'(## Recent Scores\n\n)'
            replacement = r'\1| Date | Task | Score | Grade |\n|------|------|-------|-------|\n' + score_entry
            new_content = re.sub(pattern, replacement, content)
        
        content = new_content
    else:
        # Add new section before the first ## section or at end
        section = f"""## Recent Scores

| Date | Task | Score | Grade |
|------|------|-------|-------|
{score_entry}
"""
        # Insert before first ## or at end
        first_section = content.find('\n## ')
        if first_section > 0:
            content = content[:first_section] + '\n' + section + content[first_section:]
        else:
            content = content.rstrip() + '\n\n' + section
    
    return content


def update_improvement_focus_section(content: str, score_data: dict) -> str:
    """Update or add the ## Improvement Focus section."""
    section_content = f"""## Improvement Focus

**Current Gap:** {score_data['improvement_dim']} ({score_data['improvement_score']}/5)

**Action:** {score_data['improvement_suggestion']}

**Last Updated:** {datetime.utcnow().strftime("%Y-%m-%d")}
"""
    
    if '## Improvement Focus' in content:
        # Replace existing section
        pattern = r'## Improvement Focus.*?(?=\n## |\Z)'
        content = re.sub(pattern, section_content.rstrip(), content, flags=re.DOTALL)
    else:
        # Add after Recent Scores or at appropriate location
        if '## Recent Scores' in content:
            # Find end of Recent Scores section
            pattern = r'(## Recent Scores.*?\n)(?=\n## |\Z)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                insert_pos = match.end()
                content = content[:insert_pos] + '\n' + section_content + content[insert_pos:]
        else:
            # Add before first ## or at end
            first_section = content.find('\n## ')
            if first_section > 0:
                content = content[:first_section] + '\n' + section_content + content[first_section:]
            else:
                content = content.rstrip() + '\n\n' + section_content
    
    return content


def update_suggested_next_task_section(content: str, score_data: dict) -> str:
    """Update or add the ## Suggested Next Task section."""
    section_content = f"""## Suggested Next Task

{score_data['suggested_next_task']}

**Based on:** Performance in {score_data['task_id']} (Grade: {score_data['grade']})
"""
    
    if '## Suggested Next Task' in content:
        # Replace existing section
        pattern = r'## Suggested Next Task.*?(?=\n## |\Z)'
        content = re.sub(pattern, section_content.rstrip(), content, flags=re.DOTALL)
    else:
        # Add after Improvement Focus or at end
        if '## Improvement Focus' in content:
            pattern = r'(## Improvement Focus.*?\n)(?=\n## |\Z)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                insert_pos = match.end()
                content = content[:insert_pos] + '\n' + section_content + content[insert_pos:]
        elif '## Recent Scores' in content:
            pattern = r'(## Recent Scores.*?\n)(?=\n## |\Z)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                insert_pos = match.end()
                content = content[:insert_pos] + '\n' + section_content + content[insert_pos:]
        else:
            first_section = content.find('\n## ')
            if first_section > 0:
                content = content[:first_section] + '\n' + section_content + content[first_section:]
            else:
                content = content.rstrip() + '\n\n' + section_content
    
    return content


def update_soul(employee: str, task_id: str) -> bool:
    """Update the employee SOUL file with latest scorecard data."""
    soul_path = get_employee_soul_path(employee)
    scorecard_path = get_scorecard_path(employee, task_id)
    
    # Check if files exist
    if not os.path.exists(scorecard_path):
        print(f"Scorecard not found: {scorecard_path}")
        return False
    
    if not os.path.exists(soul_path):
        print(f"SOUL file not found: {soul_path}")
        return False
    
    # Parse scorecard
    score_data = parse_scorecard(scorecard_path)
    if not score_data:
        return False
    
    # Read SOUL content
    content = read_soul_content(soul_path)
    if content is None:
        return False
    
    # Update sections
    content = update_recent_scores_section(content, score_data)
    content = update_improvement_focus_section(content, score_data)
    content = update_suggested_next_task_section(content, score_data)
    
    # Write updated SOUL
    try:
        with open(soul_path, 'w') as f:
            f.write(content)
        print(f"SOUL updated: {soul_path}")
        return True
    except Exception as e:
        print(f"Error writing SOUL file: {e}")
        return False


def main():
    if len(sys.argv) < 3:
        print("Usage: python soul-updater.py <employee_name> <task_id>")
        print("Example: python soul-updater.py jax directory-submissions-p1")
        sys.exit(1)
    
    employee = sys.argv[1].lower()
    task_id = sys.argv[2]
    
    success = update_soul(employee, task_id)
    
    if success:
        print(f"✅ Successfully updated {employee}'s SOUL with scores from {task_id}")
    else:
        print(f"❌ Failed to update SOUL")
        sys.exit(1)


if __name__ == "__main__":
    main()
