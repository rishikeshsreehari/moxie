# HQ Repo Health Audit (ongoing)

Owner: Moxie
Frequency: weekly (Sundays 10:00 UTC)

Purpose: keep /root/moxie_hq tidy by removing clearly stale files and reporting any suspicious duplicates.

## What we remove (safe list)
- Empty directories
- `__pycache__/` folders
- `*.pyc`, `*.pyo`
- `.DS_Store`
- Editor swap files (`*.swp`, `*.swo`)
- Duplicate backup files (`*.bak`, `copy*`)
- Stale logs older than 30 days (only under `cmo/logs/` if exists)

## What we NEVER remove
- Anything under `cmo/sops/`, `cmo/resources/`, `cmo/employees/`, `cmo/strategy/`, `templates/`
- `delegation-queue.md`, `dispatch-queue.md`, `orchestration.md`
- `rishi_review.md`, `issues_rishi.md`
- Any file with a linked task in `delegation-queue.md` (even if completed)
- Files modified in the last 14 days (conservative window)

## Output
- `/root/moxie_hq/cmo/reports/repo-health-audit-YYYY-MM-DD.md` with:
  - Files/dirs to delete (with sizes)
  - Reason for each
  - Actual deletions performed
- Git commit with message `Housekeeping: repo health cleanup <date>`

## First run
Schedule: next Sunday 2026-04-06 10:00 UTC via cron.
