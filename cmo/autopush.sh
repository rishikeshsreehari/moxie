#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="/root/moxie_hq"
LOCKFILE="$REPO_ROOT/.git/moxie_autopush.lock"
ISSUES_FILE="$REPO_ROOT/cmo/issues_rishi.md"

cd "$REPO_ROOT"
mkdir -p "$(dirname "$LOCKFILE")"

# Acquire lock on FD 9 (no bash -c/-lc)
exec 9>"$LOCKFILE"
flock -w 60 9

# Stage everything

git add -A

# Exit if nothing staged
if git diff --cached --quiet; then
  echo "__MOXIE_STATUS__ NO_CHANGES"
  exit 0
fi

ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
msg="Autopush: $ts"

git commit -m "$msg" >/tmp/moxie_autopush_commit.txt 2>&1
hash=$(git rev-parse --short HEAD)

push_out=$(git push origin main 2>&1)
rc=$?
if [ $rc -eq 0 ]; then
  echo "__MOXIE_STATUS__ PUSHED $hash"
  exit 0
fi

# On push failure, write ONE bullet to issues_rishi.md under Open
summary=$(echo "$push_out" | tr -d "\r" | awk 'NF{print; exit}' | head -c 220)

python3 - <<PY
from pathlib import Path
import re

ts = "${ts}"
hash = "${hash}"
rc = ${rc}
summary = "${summary}".strip()
path = Path("${ISSUES_FILE}")
path.parent.mkdir(parents=True, exist_ok=True)

if path.exists():
    txt = path.read_text(encoding="utf-8", errors="replace")
else:
    txt = "# Issues for Rishi\n\n## Open\n\n## Closed\n"

bullet = f"- [AUTOPUSH] {ts} push failed (rc={rc}, commit={hash}): {summary}\n"

lines = txt.splitlines(True)
open_idx = None
for i, line in enumerate(lines):
    if re.match(r"^##\\s+Open\\s*$", line.strip()):
        open_idx = i
        break

if open_idx is None:
    new_txt = "# Issues for Rishi\n\n## Open\n\n" + bullet + "\n" + txt
    path.write_text(new_txt, encoding="utf-8")
else:
    j = open_idx + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    lines.insert(j, bullet)
    path.write_text("".join(lines), encoding="utf-8")
PY

echo "__MOXIE_STATUS__ PUSH_FAILED $hash rc=$rc"
echo "__MOXIE_PUSH_ERR__"
echo "$push_out"
exit $rc
