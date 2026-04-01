#!/usr/bin/env bash
set -euo pipefail

cd /root/moxie_hq

git add -A
if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
msg="Autopush: ${ts}"

git commit -m "$msg"
commit_hash="$(git rev-parse --short HEAD)"

set +e
push_out=$(git push origin main 2>&1)
push_code=$?
set -e

if [ $push_code -ne 0 ]; then
  echo "$push_out" | tail -n 25
  python - <<PY
from pathlib import Path
import datetime, re

issues = Path("/root/moxie_hq/cmo/issues_rishi.md")
issues.parent.mkdir(parents=True, exist_ok=True)
text = issues.read_text() if issues.exists() else "# Issues for Rishi\n\n## Open\n\n## Closed\n"

err = """$push_out""".strip().splitlines()
err_summary = (err[-1] if err else "git push failed")[:200]
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
bullet = f"- [{now}] HQ autopush failed: {err_summary}"

lines = text.splitlines()
open_idx = None
for i, l in enumerate(lines):
    if re.match(r"^##+\\s+Open\\s*$", l):
        open_idx = i
        break

if open_idx is None:
    lines = ["# Issues for Rishi", "", "## Open", "", "## Closed", ""]
    open_idx = 2

insert_at = open_idx + 1
if insert_at >= len(lines) or lines[insert_at].strip() != "":
    lines.insert(insert_at, "")
    insert_at += 1

lines.insert(insert_at, bullet)
issues.write_text("\n".join(lines).rstrip() + "\n")
print("WROTE_ISSUE")
PY
  exit 2
fi

echo "PUSHED ${commit_hash}"
