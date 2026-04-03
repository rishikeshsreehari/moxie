#!/usr/bin/env python3
import sys
from datetime import datetime, timezone
from pathlib import Path

ISSUES_PATH = Path("/root/moxie_hq/cmo/issues_rishi.md")


def main():
    if len(sys.argv) < 2:
        print("Usage: append_issue_open.py <message>")
        sys.exit(2)

    msg = " ".join(sys.argv[1:]).strip()
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # Check operating assumptions before adding issue
    try:
        sys.path.insert(0, '/root/moxie_hq/cmo/scripts')
        from read_operating_assumptions import get_operating_assumptions, should_suppress_issue
        assumptions = get_operating_assumptions()
        
        # Check if this issue should be suppressed based on operating assumptions
        if should_suppress_issue(msg, assumptions):
            print(f"[SILENT] Issue suppressed per operating assumptions: {msg}")
            return
    except Exception:
        # Fall back to original behavior if assumptions can't be loaded
        pass

    bullet = f"- [ ] ({ts}) {msg}\n"

    if not ISSUES_PATH.exists():
        ISSUES_PATH.parent.mkdir(parents=True, exist_ok=True)
        ISSUES_PATH.write_text("# issues_rishi.md\n\n##Open\n" + bullet + "\n##Resolved\n", encoding="utf-8")
        return

    text = ISSUES_PATH.read_text(encoding="utf-8")
    lines = text.splitlines(True)  # keep \n

    # Find the Open heading (supports '##Open' or '## Open')
    open_idx = None
    for i, line in enumerate(lines):
        if line.strip().lower().replace(" ", "") == "##open":
            open_idx = i
            break

    if open_idx is None:
        # If no heading, prepend
        new = "##Open\n" + bullet + "\n" + text
        ISSUES_PATH.write_text(new, encoding="utf-8")
        return

    # Insert bullet after the heading and any blank lines immediately following
    j = open_idx + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1

    lines.insert(j, bullet)
    ISSUES_PATH.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
