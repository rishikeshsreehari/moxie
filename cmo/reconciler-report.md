# Reconciler Report

Timestamp (UTC): 2026-03-31T09:15:33Z

## What changed (fixed drift)
- **orchestration.md**
  - Updated `Last updated` timestamp.
  - Reconciled **Active Crons** table to match `hermes cron list --all` (schedule/deliver/next-run/state), including:
    - Added jobs that were missing from docs but exist live: `codex-online-check` (completed), `cmo-dispatch-orchestrator` (paused), `moxie-forward-reports-to-telegram` (paused).
    - Corrected delivery routing for `moxie-daily-self-improvement` to `telegram:6699776435` (was `telegram`).
    - Set **Last status** column to `—` across the table because `hermes cron list` does not expose last-run status (avoids stale/incorrect “ok” flags).
  - Reconciled stale **Codex Deep Audit (ONE-SHOT)** section: old job ID is not present in live registry; pointed to the current live one-shot (`ca6591a837b7`).

## Verified queue/output state
- Dispatch queue left unchanged (conservative):
  - `/root/moxie/products/formbeep/copy/money-pages-v1.md` **missing** → task remains `[QUEUED]`.
  - `/root/moxie/products/formbeep/directory-submissions-p1.md` **missing** → task remains `[BLOCKED]` pending credentials.

## Still open
- No new human blockers discovered during reconciliation (existing blockers remain as documented).
