#!/usr/bin/env bash
set -euo pipefail
cd /root/moxie_hq

git add -A
if git diff --cached --quiet; then
  echo "NOCHANGES"
  exit 0
fi

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
git commit -m "Autopush: ${TS}"
git push origin main

git rev-parse --short HEAD
