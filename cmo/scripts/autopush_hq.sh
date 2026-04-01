#!/usr/bin/env bash
set -euo pipefail

cd /root/moxie_hq
LOCKFILE="/root/moxie_hq/.git/moxie_autopush.lock"

# Acquire lock (wait up to 60s) without using bash -c/-lc
exec 9>"$LOCKFILE"
if ! flock -w 60 9; then
  echo "LOCK_TIMEOUT"
  exit 3
fi

git add -A

if [[ -z "$(git status --porcelain)" ]]; then
  echo "NO_CHANGES"
  exit 0
fi

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Commit (will fail if somehow empty; we already checked)
git commit -m "Autopush: $TS" >/tmp/moxie_autopush_commit.log
COMMIT=$(git rev-parse --short HEAD)

# Push to origin main
if git push origin main >/tmp/moxie_autopush_push.log 2>/tmp/moxie_autopush_push.err; then
  echo "PUSHED $COMMIT"
  exit 0
else
  echo "PUSH_FAILED $COMMIT"
  echo "--- push stderr ---"
  cat /tmp/moxie_autopush_push.err
  exit 2
fi
