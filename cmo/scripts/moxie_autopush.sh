#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="/root/moxie_hq"
LOCKFILE="$REPO_ROOT/.git/moxie_autopush.lock"
ISSUES_FILE="$REPO_ROOT/cmo/issues_rishi.md"

# Acquire lock (<=60s) and run the push sequence.
exec 9>"$LOCKFILE"
if ! flock -w 60 9; then
  echo "LOCK_TIMEOUT"
  exit 2
fi

cd "$REPO_ROOT"

git config user.name "Moxie" >/dev/null 2>&1 || true
git config user.email "moxie@rishikeshs.com" >/dev/null 2>&1 || true

git add -A

if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
if ! git commit -m "Autopush: ${TS}" >/tmp/moxie_autopush_commit.log 2>&1; then
  echo "COMMIT_FAILED"
  cat /tmp/moxie_autopush_commit.log
  exit 10
fi

HASH=$(git rev-parse --short HEAD)
echo "COMMITTED:${HASH}"

if ! git push origin main >/tmp/moxie_autopush_push.log 2>&1; then
  echo "PUSH_FAILED:${HASH}"
  cat /tmp/moxie_autopush_push.log

  # Add ONE bullet under "Open" with the error summary.
  # Summary: first non-empty line from push log.
  ERR_LINE=$(grep -m 1 -E '\S' /tmp/moxie_autopush_push.log || true)
  if [[ -z "${ERR_LINE}" ]]; then ERR_LINE="git push failed (no log output)"; fi

  # Ensure issues file exists and has an Open section.
  if [[ ! -f "$ISSUES_FILE" ]]; then
    mkdir -p "$(dirname "$ISSUES_FILE")"
    cat >"$ISSUES_FILE" <<'EOF'
# issues_rishi.md

## Open

## Closed
EOF
  fi

  if ! grep -q '^## Open' "$ISSUES_FILE"; then
    # Prepend an Open section if missing.
    tmp=$(mktemp)
    {
      echo "## Open"
      echo
      cat "$ISSUES_FILE"
    } > "$tmp"
    mv "$tmp" "$ISSUES_FILE"
  fi

  # Insert bullet directly after ## Open header.
  tmp=$(mktemp)
  awk -v msg="$ERR_LINE" '
    BEGIN{inserted=0}
    {print}
    $0 ~ /^## Open/ && inserted==0 {
      getline nextline
      print nextline
      print "- [HQ autopush] " msg
      inserted=1
    }
  ' "$ISSUES_FILE" > "$tmp" || true

  # If awk logic failed to insert (edge cases), do a safer append under Open.
  if ! grep -q "\[HQ autopush\]" "$tmp"; then
    cp "$ISSUES_FILE" "$tmp"
    # Append at end (still a single bullet addition).
    echo "- [HQ autopush] ${ERR_LINE}" >> "$tmp"
  fi

  mv "$tmp" "$ISSUES_FILE"

  exit 20
fi

echo "PUSHED:${HASH}"
exit 0
