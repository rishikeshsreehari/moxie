#!/usr/bin/env bash
set -euo pipefail

cd /root/moxie_hq

git add -A

# No empty commits
if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
git commit -m "Autopush: ${TS}"
HASH=$(git rev-parse --short HEAD)

# Always push to origin main, regardless of local branch name
git push origin HEAD:main

echo "PUSHED ${HASH}"
