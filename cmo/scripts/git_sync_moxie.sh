#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/root/moxie"
cd "$REPO_DIR"

git config user.name "Moxie"
git config user.email "moxie@rishikeshs.com"

git add -A

if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

ts=$(date -u +"%Y-%m-%d %H:%M UTC")
git commit -m "docs: update Moxie HQ state (${ts})"
git push origin main

echo "Committed and pushed Moxie HQ updates."
