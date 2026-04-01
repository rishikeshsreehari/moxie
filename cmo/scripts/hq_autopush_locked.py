#!/usr/bin/env python3
"""HQ autopush with an OS-level lock (no shell -c).

Purpose
- Avoid concurrent git commits/pushes for /root/moxie_hq
- Work in environments where `flock ... bash -lc '...'` is blocked

Policy
- Never create empty commits
- Commit message format: `Autopush: <UTC timestamp>`
- Push only to HQ repo (this repo) origin/main

"""

import fcntl
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO = Path("/root/moxie_hq")
LOCK_PATH = REPO / ".git" / "moxie_autopush.lock"


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(REPO), text=True, capture_output=True, check=check)


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

        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        msg = f"Autopush: {ts}"

        c = run(["git", "commit", "-m", msg], check=True)
        if c.stdout:
            print(c.stdout)
        if c.stderr:
            print(c.stderr, file=sys.stderr)

        p = run(["git", "push", "origin", "main"], check=True)
        if p.stdout:
            print(p.stdout)
        if p.stderr:
            print(p.stderr, file=sys.stderr)

        print("PUSH_OK")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
