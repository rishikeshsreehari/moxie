#!/usr/bin/env bash
# HQ autopush helper
# - Locks on .git/moxie_autopush.lock (<=60s)
# - Never creates empty commits
# - Commits as: "Autopush: <UTC timestamp>"
# - Pushes: origin main
#
# Usage:
#   /root/moxie_hq/cmo/scripts/hq_autopush.sh

set -euo pipefail

REPO_DIR="/root/moxie_hq"
LOCKFILE="${REPO_DIR}/.git/moxie_autopush.lock"

cd "$REPO_DIR"

mkdir -p "$(dirname "$LOCKFILE")"
# Ensure lockfile exists for flock
: > "$LOCKFILE" || true

flock -w 60 "$LOCKFILE" bash -eu -o pipefail <<'LOCKED'
cd /root/moxie_hq

git add -A

if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

# Stable commit identity (local repo only)
git config user.name "Moxie"
git config user.email "moxie@rishikeshs.com"

TS="$(date -u +"%Y-%m-%d %H:%M:%S UTC")"
git commit -m "Autopush: ${TS}"

echo "COMMIT_HASH=$(git rev-parse --short HEAD)"

git push origin main

echo "PUSH_OK"
LOCKED
