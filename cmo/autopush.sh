#!/usr/bin/env bash
set -euo pipefail
cd /root/moxie_hq

git add -A

if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
git commit -m "Autopush: ${TS}"
HASH=$(git rev-parse --short HEAD)

git push origin main

echo "PUSHED ${HASH}"
