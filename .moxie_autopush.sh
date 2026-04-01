#!/usr/bin/env bash
set -euo pipefail

cd /root/moxie_hq

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "NOT_A_GIT_REPO"
  exit 2
fi

git add -A

if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
git commit -m "Autopush: ${TS}" >/dev/null
HASH=$(git rev-parse --short HEAD)

if git push origin main > /tmp/moxie_autopush_push.log 2>&1; then
  echo "PUSH_OK ${HASH}"
  exit 0
else
  echo "PUSH_FAIL ${HASH}"
  tail -n 60 /tmp/moxie_autopush_push.log
  exit 3
fi
