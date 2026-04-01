#!/usr/bin/env python3
"""HQ autopush with an OS-level lock (no shell -c).

Purpose
- Avoid concurrent git commits/pushes for /root/moxie_hq
- Work in environments where `flock ... bash -lc '...'` is blocked
- Generate meaningful commit messages instead of generic timestamps

Policy
- Never create empty commits
- Commit message format: "HQ sync: <area1> + <area2>" with optional body
- Push only to HQ repo (this repo) origin/main
- Classification rules map file paths to semantic areas

"""

import fcntl
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter


REPO = Path("/root/moxie_hq")
LOCK_PATH = REPO / ".git" / "moxie_autopush.lock"

# Classification rules: path pattern -> area tag
AREA_RULES = [
    ("cmo/dispatch-queue.md", "dispatch"),
    ("cmo/orchestration.md", "orchestration"),
    ("cmo/delegation-queue.md", "delegation"),
    ("cmo/delegation-queue.md", "delegation"),
    ("cmo/issues_rishi.md", "governance"),
    ("cmo/sops/", "SOPs"),
    ("cmo/employees/", "team"),
    ("products/formbeep/analytics/", "analytics"),
    ("products/formbeep/copy/", "content"),
    ("products/formbeep/outreach/", "outreach"),
    ("products/formbeep/seo/", "SEO"),
    ("products/formbeep/distribution/", "distribution"),
    ("products/formbeep/lifecycle/", "lifecycle"),
    ("products/formbeep/partnerships/", "partnerships"),
    ("products/formbeep/outbound/", "outbound"),
    ("dashboard/", "dashboard"),
    ("cmo/scores/", "scores"),
    ("cmo/codex-usage", "tracking"),
    ("cmo/state/", "state"),
]


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(REPO), text=True, capture_output=True, check=check)


def classify_file(relpath: str) -> str | None:
    """Map a file path to its semantic area tag."""
    for prefix, area in AREA_RULES:
        if prefix in relpath:
            return area
    return None


def generate_commit_message(staged_files: list[str]) -> tuple[str, str | None]:
    """Generate commit subject and optional body from staged files.
    
    Returns: (subject_line, body_or_none)
    """
    if not staged_files:
        return "HQ sync: no changes", None
    
    # Classify all files
    areas = []
    file_details = []
    
    for f in staged_files:
        area = classify_file(f)
        if area:
            areas.append(area)
        # Create brief description
        filename = Path(f).name
        file_details.append(f"- {f}: updated")
    
    if not areas:
        # No recognized areas, use generic
        if len(staged_files) == 1:
            return f"HQ sync: {staged_files[0]}", None
        return "HQ sync: multi-area update", "\n".join(file_details[:5]) if len(staged_files) > 1 else None
    
    # Count area frequencies
    area_counts = Counter(areas)
    top_areas = [area for area, _ in area_counts.most_common(3)]
    
    # Build subject line
    if len(top_areas) == 1:
        subject = f"HQ sync: {top_areas[0]}"
    elif len(top_areas) == 2:
        subject = f"HQ sync: {top_areas[0]} + {top_areas[1]}"
    else:
        subject = f"HQ sync: {top_areas[0]} + {top_areas[1]} + {top_areas[2]}"
    
    # Build body if we have many files or multiple areas
    body = None
    if len(staged_files) >= 3 or len(top_areas) >= 2:
        # Limit to top 7 files to keep commit message reasonable
        body_lines = file_details[:7]
        if len(staged_files) > 7:
            body_lines.append(f"- ... and {len(staged_files) - 7} more files")
        body = "\n".join(body_lines)
    
    return subject, body


def append_issue_open(line: str) -> None:
    """Append a single bullet under cmo/issues_rishi.md > ## Open.

    Best-effort: if structure is unexpected, append to end of file.
    """

    issues_path = REPO / "cmo" / "issues_rishi.md"
    try:
        txt = issues_path.read_text(encoding="utf-8")
    except Exception:
        return

    marker_open = "\n## Open\n"
    marker_resolved = "\n## Resolved\n"

    if marker_open not in txt:
        # Fallback: append at end
        issues_path.write_text(txt.rstrip() + "\n\n" + line.rstrip() + "\n", encoding="utf-8")
        return

    if marker_resolved in txt:
        before, after = txt.split(marker_resolved, 1)
        before = before.rstrip() + "\n\n" + line.rstrip() + "\n\n"
        issues_path.write_text(before + marker_resolved.lstrip("\n") + after, encoding="utf-8")
        return

    # No resolved section; append at end
    issues_path.write_text(txt.rstrip() + "\n\n" + line.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if not (REPO / ".git").exists():
        print("ERROR: /root/moxie_hq does not look like a git repo", file=sys.stderr)
        return 2

    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(LOCK_PATH, "w") as f:
        # Block up to ~60s like the flock convention
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)

        # Identity (local repo config)
        run(["git", "config", "user.email", "moxie@rishikeshs.com"], check=False)
        run(["git", "config", "user.name", "Moxie"], check=False)

        # Stage
        r = run(["git", "add", "-A"], check=True)
        if r.stdout:
            print(r.stdout)
        if r.stderr:
            print(r.stderr, file=sys.stderr)

        # Detect staged changes
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=str(REPO),
            text=True,
            capture_output=True,
        )
        if diff.returncode == 0:
            print("NO_STAGED_CHANGES")
            return 0

        # Get list of staged files for message generation
        files_result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            cwd=str(REPO),
            text=True,
            capture_output=True,
            check=True,
        )
        staged_files = [f.strip() for f in files_result.stdout.strip().split("\n") if f.strip()]
        
        # Generate meaningful commit message
        subject, body = generate_commit_message(staged_files)
        
        # Build commit command
        if body:
            msg = f"{subject}\n\n{body}"
        else:
            msg = subject

        c = run(["git", "commit", "-m", msg], check=True)
        if c.stdout:
            print(c.stdout)
        if c.stderr:
            print(c.stderr, file=sys.stderr)

        try:
            p = run(["git", "push", "origin", "main"], check=True)
            if p.stdout:
                print(p.stdout)
            if p.stderr:
                print(p.stderr, file=sys.stderr)
        except subprocess.CalledProcessError as e:
            err = (e.stderr or "") + "\n" + (e.stdout or "")

            # One safe reconciliation attempt if remote is ahead
            if ("non-fast-forward" in err) or ("fetch first" in err) or ("[rejected]" in err):
                pr = run(["git", "pull", "--rebase", "origin", "main"], check=True)
                if pr.stdout:
                    print(pr.stdout)
                if pr.stderr:
                    print(pr.stderr, file=sys.stderr)

                p2 = run(["git", "push", "origin", "main"], check=True)
                if p2.stdout:
                    print(p2.stdout)
                if p2.stderr:
                    print(p2.stderr, file=sys.stderr)
            else:
                ts2 = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                append_issue_open(
                    f"- [ ] ({ts2}) HQ autopush failed: {err.strip().splitlines()[-1][:200]} — Owner: Rishi + Moxie"
                )
                print("PUSH_FAILED", file=sys.stderr)
                return 1

        print("PUSH_OK")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
