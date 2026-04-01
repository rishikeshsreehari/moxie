# Reconciliation Report — 2026-04-01T17:30:00Z

## Drift Fixed

### 1. Active Crons Table (orchestration.md)
- Added missing job: `7af300e6 cmo-delegation-queue-runner` (every 15 min) — was live but undocumented
- Updated Last verified timestamp: 2026-04-01T15:15:00Z → 2026-04-01T17:30:00Z
- Updated repeat counts for 15 worker/governance jobs (+2 runs each):
  - moxie-daily-governance: 40 → 42
  - vale-worker: 42 → 44
  - astra-worker: 41 → 43
  - kiro-worker: 40 → 42
  - ember-worker: 40 → 42
  - forge-worker: 41 → 43
  - jax-worker: 40 → 42
  - rumi-worker: 40 → 42
  - nova-worker: 39 → 41
  - luna-worker: 41 → 43
  - pax-worker: 39 → 41
  - orion-worker: 41 → 43
  - moxie-orchestration-reconciler: 31 → 33
  - issues-rishi-watch: 10 → 11
- Updated next-run times for all 29 jobs (advanced ~2 hours per hourly schedule)

### 2. Employee State (orchestration.md)
- Ember status: IDLE → IN_PROGRESS
- Added current task: Draft subreddit-specific post/comment scripts + reply macros based on Vale playbook
- Added target output: /root/moxie/products/formbeep/outreach/reddit-post-comment-scripts.md
- Clarified blocker: Script drafting proceeding; execution blocked on credentials

### 3. Heartbeat Log
- Updated active worker from Vale → Ember (Vale completed his task)
- Removed Ember from blocked list (task is IN_PROGRESS, only execution blocked)

### 4. Dispatch Queue Status
- Ember task (#0b) correctly shows IN_PROGRESS
- Vale task (#0) correctly shows COMPLETED
- Output file verified: reddit-intel-positioning-subreddit-playbook.md exists (13288 bytes)

## Summary

| Item | Before | After |
|------|--------|-------|
| Cron jobs documented | 30 (1 missing) | 31 (all live jobs) |
| Ember status | IDLE/BLOCKED | IN_PROGRESS |
| Vale output | Referenced | Verified exists |
| Repeat counts | Stale (~2 runs behind) | Synced to live registry |
| Next-run times | ~2 hours stale | Current |

## Open Issues (No Change)

Blockers remain as documented in issues_rishi.md:
1. WordPress plugin resubmission — Rishi-owned
2. Directory submissions — awaiting credentials
3. Reddit execution — awaiting credentials
4. Platform marketplace portal access — awaiting credentials
5. Umami Cloud API access — blocker being investigated

## System Status

- All31 cron jobs active and synced
- 1 worker IN_PROGRESS (Ember)
- 11 workers IDLE
- No stale/paused/missing jobs
- No new crons scheduled (safety rule honored)