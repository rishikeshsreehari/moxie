#!/usr/bin/env bash
set -euo pipefail

cd /root/moxie_hq
LOCKFILE="/root/moxie_hq/.git/moxie_autopush.lock"

# Run everything under a lock (<=60s wait)
# Note: avoid bash -c/-lc to satisfy tool safety checks.
exec 9>"$LOCKFILE"
if ! flock -w 60 9; then
  echo "LOCK_TIMEOUT"
  exit 75
fi

# Stage changes
git add -A

if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)

git commit -m "Autopush: ${TS}" >/dev/null
COMMIT=$(git rev-parse --short HEAD)

tmp_log=$(mktemp)
set +e
GIT_PUSH_OUTPUT=$(git push origin main 2>&1 | tee "$tmp_log")
PUSH_CODE=${PIPESTATUS[0]}
set -e

if [ "$PUSH_CODE" -ne 0 ]; then
  # If remote is ahead (non-fast-forward / fetch-first), try one safe reconciliation.
  if grep -Eqi "\(fetch first\)|non-fast-forward|rejected" "$tmp_log"; then
    git pull --rebase origin main >>"$tmp_log" 2>&1 || true

    set +e
    git push origin main 2>&1 | tee -a "$tmp_log"
    PUSH_CODE=${PIPESTATUS[0]}
    set -e
  fi
fi

if [ "$PUSH_CODE" -ne 0 ]; then
  # Compact error summary
  tail -n 25 "$tmp_log" >"${tmp_log}.tail" || true
  ERR_SUMMARY=$(tr '\n' ' ' <"${tmp_log}.tail" | sed 's/[[:space:]]\+/ /g' | cut -c1-280)
  /usr/bin/env python3 /root/moxie_hq/cmo/scripts/append_issue_open.py "HQ autopush failed (git push origin main): ${ERR_SUMMARY}"
  echo "PUSH_FAILED ${COMMIT}"
  exit 1
fi

echo "PUSHED ${COMMIT}"
