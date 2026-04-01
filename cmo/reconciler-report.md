# Reconciliation Report — 2026-04-01T19:17:00Z

## Drift Fixed

### 1. Active Crons Table (orchestration.md)
- Updated Last verified timestamp: 2026-04-01T18:13:00Z→ 2026-04-01T19:17:00Z
- Synced 15 worker/governance job repeat counters to live registry values:
  - moxie-daily-governance: 43/100 → 44/100
  - vale-worker: 45/100 → 46/100
  - astra-worker: 44/100 → 45/100
  - kiro-worker: 43/100 → 44/100
  - ember-worker: 43/100 → 44/100
  - forge-worker: 44/100 → 45/100
  - jax-worker: 43/100 → 44/100
  - rumi-worker: 43/100 → 44/100
  - nova-worker: 42/100 → 43/100
  - luna-worker: 44/100 → 45/100
  - pax-worker: 42/100 → 43/100
  - orion-worker: 44/200 → 45/200
  - moxie-orchestration-reconciler: 34/100 → 35/100- Updated all next-run times to current values (advanced ~1 hour per hourly schedule)

### 2. Dispatch Queue Cleanup (dispatch-queue.md)
- Removed corrupted line 12 with `[---]` marker artifact
- Queue now contains 6 valid task entries

### 3. Issues File Cleanup (issues_rishi.md)
- Moved Umami analytics blocker from Open→ Resolved (orchestration.md already showed RESOLVED; analytics-report.md exists)
- Drift reconciled between issues file and orchestration.md Known Blockers table

## Summary

| Item | Before | After |
|------|--------|-------|
| Cron jobs documented | 31 (all present) | 31 (all present) |
| Repeat counts | ~1 run stale | Synced to live registry |
| Next-run times| ~1 hour stale | Current |
| Dispatch queue | 7 entries (1 corrupted) | 6 entries (clean) |
| Issues file | 7 Open (1 resolved) | 6 Open (truthful) |

## Open Issues (No New Blockers)

Remaining blockers in issues_rishi.md:
1. Reddit network/APIaccess — needs decision on Data API application
2. WordPress plugin resubmission — Rishi-owned
3. Directory submissions — awaiting credentials
4. Platform marketplace portal access — awaiting credentials

## System Status

- All 31 cron jobs active and synced
- 1 worker IN_PROGRESS: Astra (SERP demand probe)
- No new crons scheduled (safety rule honored)
- No stale/paused/missing jobs
- Dispatch queue clean and valid
- Employee states match dispatch queue assignments