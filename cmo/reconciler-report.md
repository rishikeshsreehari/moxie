# Reconciliation Report — 2026-04-01T18:13:00Z

## Drift Fixed

### 1. Active Crons Table (orchestration.md)
- Updated Last verified timestamp: 2026-04-01T17:30:00Z → 2026-04-01T18:13:00Z
- Updated repeat counters for 15 worker/governance jobs (+1 run each):
  - moxie-daily-governance: 42 → 43
  - vale-worker: 44 → 45
  - astra-worker: 43 → 44
  - kiro-worker: 42 → 43
  - ember-worker: 42 → 43
  - forge-worker: 43 → 44
  - jax-worker: 42 → 43
  - rumi-worker: 42 → 43
  - nova-worker: 41 → 42
  - luna-worker: 43 → 44
  - pax-worker: 41 → 42
  - orion-worker: 43 → 44
  - moxie-orchestration-reconciler: 33 → 34
- Updated next-run times for 16 hourly jobs (advanced ~1 hour per schedule)
- Updated moxie-hq-autocommit-push next run: 17:34:56 → 18:42:06

### 2. Dispatch Queue Cleanup (dispatch-queue.md)
- Removed 2 malformed/deleted task entries (corrupted formatting)
- Preservedactive tasks:
  - [IN_PROGRESS][P0] Forge:GSC indexing issues
  - [IN_PROGRESS][P1] Ember: Reddit tracker maintenance
  - [IN_PROGRESS][P1] Jax: Directory submission tracking
  - [P1] Kiro: Blog draft approval
  - [P1] Jax: Directory day-plan

###3. Issues File Cleanup (issues_rishi.md)
- Fixed malformed content (line numbers appearing in text)
- Preserved all existing blocker items
- No new blockers added

## Summary

| Item | Before | After |
|------|--------|-------|
| Cron jobs documented | 31 (all present) | 31 (all present) |
| Repeat counts | ~1 run stale | Synced to live registry |
| Next-run times | ~1 hour stale | Current |
| Dispatch queue | 7 entries (2 corrupted) | 5 entries (clean) |
| Issues file | Malformed content | Fixed formatting |

## Open Issues (No Change)

Blockers remain as documented in issues_rishi.md:
1. WordPress plugin resubmission — Rishi-owned
2. Directory submissions — awaiting credentials
3. Reddit execution — awaiting credentials
4. Platform marketplace portal access — awaiting credentials
5. Umami Cloud API access — blocker being investigated

## System Status

- All 31 cron jobs active and synced
- 1 worker IN_PROGRESS (Forge: GSC indexing)
- No new crons scheduled (safety rule honored)
- No stale/paused/missing jobs
- Dispatch queue cleaned and valid