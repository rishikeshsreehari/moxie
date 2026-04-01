# Reconciliation Report — 2026-04-01T15:15:00Z

## Synced

**Cron registry drift corrected:**
- Updated Last verified timestamp from 2026-04-01T13:15:00Z → 2026-04-01T15:15:00Z
- 27 jobs verified against live registry

**Jobs with stale next-run times (now corrected):**
- formbeep-daily-user-count-checkin: next run advanced (daily job ran)
- formbeep-hourly-heartbeat: 14:06 → 16:06 UTC
- codex-dashboard-update-checkin: next run advanced (720m cycle)
- All 14 worker crons: next-run times advanced by ~2 hours
- moxie-hq-autocommit-push: next run advanced (30m cycle)
- moxie-orchestration-reconciler: next run advanced

**Jobs with stale repeat counts (now corrected):**
- moxie-daily-governance: 38 → 40 runs
- vale-worker: 40 → 42 runs
- astra-worker: 39 → 41 runs
- kiro-worker: 38 → 40 runs
- ember-worker: 38 → 40 runs
- forge-worker: 39 → 41 runs
- jax-worker: 38 → 40 runs
- rumi-worker: 38 → 40 runs
- nova-worker: 37 → 39 runs
- luna-worker: 39 → 41 runs
- pax-worker: 37 → 39 runs
- orion-worker: 39 → 41 runs
- moxie-orchestration-reconciler: 29 → 31 runs

## Status: All Systems Normal

- All 29 cron jobs active and synced
- No stale, paused, or missing jobs detected
- No duplicate job names
- All scheduled runs within expected windows
- Retired jobs section unchanged (4 historical entries)

## Dispatch Queue Status

All tasks COMPLETED. No IN_PROGRESS or QUEUED items requiring action. Workers operating correctly.

## Open Issues

None from reconciliation perspective. Existing blockers remain:
- WordPress plugin awaiting Rishi resubmission
- Directory submissions awaiting credentials
- Reddit campaign awaiting credentials

---
*Autonomously reconciled by Moxie orchestration cron*