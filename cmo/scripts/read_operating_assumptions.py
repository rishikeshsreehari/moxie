#!/usr/bin/env python3
"""
Helper script to read and parse OPERATING_ASSUMPTIONS.md
Returns a structured dictionary of assumptions for automation scripts.
"""

import re
import os
from pathlib import Path

def get_operating_assumptions():
    """Read and parse OPERATING_ASSUMPTIONS.md into a structured format"""
    assumptions_file = Path("/root/moxie_hq/cmo/resources/OPERATING_ASSUMPTIONS.md")
    
    if not assumptions_file.exists():
        return {}
    
    with open(assumptions_file, 'r') as f:
        content = f.read()
    
    # Parse sections
    sections = {}
    current_section = None
    
    for line in content.split('\n'):
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            if line.startswith('## ') and len(line) > 3:
                current_section = line[3:].strip()
                sections[current_section] = []
            continue
            
        if current_section and line:
            sections[current_section].append(line)
    
    return sections

def should_suppress_issue(issue_text, assumptions):
    """
    Check if an issue should be suppressed based on operating assumptions.
    
    Args:
        issue_text (str): The issue text to check
        assumptions (dict): Parsed assumptions from get_operating_assumptions()
    
    Returns:
        bool: True if issue should be suppressed, False if it should be surfaced
    """
    issue_lower = issue_text.lower()
    
    # Check Reddit-related issues
    if any(keyword in issue_lower for keyword in ['reddit', 'credential', 'post']):
        # If it's about Reddit posting, check if Rishi posts himself
        if 'rishi posts' in ' '.join(assumptions.get('Reddit & Social Media', [])).lower():
            return True
            
        # If it's asking for Reddit credentials, suppress
        if 'credential' in issue_lower and 'reddit' in issue_lower:
            return True
    
    # Check GSC-related issues
    if any(keyword in issue_lower for keyword in ['search console', 'gsc', 'google']):
        # If GSA exists, suppress missing flags unless there's an actual error
        if 'service account exists' in ' '.join(assumptions.get('Credentials & Service Accounts', [])).lower():
            return True
    
    # Check Dashboard QA issues
    if any(keyword in issue_lower for keyword in ['dashboard', 'qa', 'quality assurance']):
        # If QA is signed off, suppress
        if 'signed off' in ' '.join(assumptions.get('Quality Assurance', [])).lower():
            return True
    
    return False

def categorize_issue(issue_text, assumptions):
    """
    Categorize an issue based on operating assumptions.
    
    Args:
        issue_text (str): The issue text to categorize
        assumptions (dict): Parsed assumptions from get_operating_assumptions()
    
    Returns:
        str: Category ('CURRENT BLOCKER', 'HISTORICAL/RESOLVED', 'REQUIRES CLARIFICATION')
    """
    if should_suppress_issue(issue_text, assumptions):
        return 'HISTORICAL/RESOLVED'
    
    # Simple heuristics for categorization
    issue_lower = issue_text.lower()
    
    # If it contains error indicators, it's a current blocker
    if any(keyword in issue_lower for keyword in ['error', 'failed', 'exception', 'missing file']):
        return 'CURRENT BLOCKER'
    
    # If it's about credentials or setup, it might require clarification
    if any(keyword in issue_lower for keyword in ['credential', 'setup', 'account', 'access']):
        return 'REQUIRES CLARIFICATION'
    
    # Default to current blocker for safety
    return 'CURRENT BLOCKER'

if __name__ == "__main__":
    assumptions = get_operating_assumptions()
    print("Parsed Operating Assumptions:")
    for section, items in assumptions.items():
        print(f"  {section}:")
        for item in items:
            print(f"    - {item}")
    print(f"\nTotal sections: {len(assumptions)}")