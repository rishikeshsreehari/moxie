#!/usr/bin/env bash
set -euo pipefail

# Run from anywhere; anchor to repo root
repo_root=$(git rev-parse --show-toplevel 2>/dev/null || true)
if [[ -z "${repo_root}" ]]; then
  echo "ERROR: not inside a git repo" >&2
  exit 2
fi
cd "${repo_root}"

# Stage everything
git add -A

# Do not create empty commits
if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
git commit -m "Autopush: ${ts}" >/dev/null
commit=$(git rev-parse --short HEAD)

git push origin main

echo "PUSHED=${commit}"
