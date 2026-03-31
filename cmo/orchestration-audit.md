# Deep Audit — Cron + Orchestration Autonomy (FormBeep)

Date (UTC): 2026-03-31T07:04:49Z
Scope: Hermes cron scheduler, worker crons, governance/promotion logic, delivery + GitHub hygiene, state-file drift.

## Executive summary
Orchestration was *running* (cron outputs were being generated), but autonomy was broken in two critical ways:
1) Multiple worker crons were repeatedly failing with HTTP 400 provider/model mismatches (Codex endpoint + OpenRouter models, and `gpt-5.3-codex-spark` not supported).
2) “Work happened” but it wasn’t being reliably versioned/pushed, which made it look like the system was asleep.

We have now:
- fixed the known provider/model mismatch on the main affected workers (including Luna).
- added an autocommit+push watchdog cron for HQ.
- unblocked Luna/Pax/Orion queue rows that were incorrectly marked as “worker not configured”.

## Ground truth checks (verified)

### A) Cron is firing
Cron outputs exist under: `$HERMES_HOME=/opt/data/cron/output/<job_id>/...`
Example: heartbeat outputs at ~2h cadence were present (00:07Z, 00:55Z, 02:08Z, 04:10Z, 06:08Z).

### B) High-severity failure mode: provider/model mismatch
Pattern seen repeatedly in cron outputs:
- `HTTP 400 ... 'qwen/qwen3-coder-480b-a35b:free' model is not supported when using Codex with a ChatGPT account.`
This indicates a job was implicitly routed through the Codex base_url while using an OpenRouter-only model.

Second failure:
- `HTTP 400 ... 'gpt-5.3-codex-spark' model is not supported when using Codex with a ChatGPT account.`
This broke Luna repeatedly.

Impact:
- Workers looked IN_PROGRESS in state, but deliverables were not being produced.

Fix applied (now):
- Updated the affected workers to run on `provider=openrouter` with the free model explicitly.
- Updated Luna-worker specifically off `gpt-5.3-codex-spark` onto OpenRouter.

### C) Deliverables truth beats status
We checked the current IN_PROGRESS output paths:
- MISS: `/root/moxie_hq/products/formbeep/tally-growth-teardown.md` (Astra)
- OK:   `/root/moxie_hq/products/formbeep/traffic-vs-keywords.md` (Mira)
- MISS: `/root/moxie_hq/products/formbeep/outreach/reddit-campaign-plan.md` (Ember)
- MISS: `/root/moxie_hq/products/formbeep/competitor-monitoring.md` (Vale)

Meaning: at least 3 tasks are “IN_PROGRESS” with missing deliverables; likely due to prior worker failures.

## Orchestration logic gaps (what prevents autonomy)

1) State-file drift (false blockers)
- Orchestration + dispatch queue claimed Luna/Pax/Orion “workers not configured”.
- Reality: those cron workers exist; they were failing due to model/provider config.
- Fix applied: queue rows changed from BLOCKED → QUEUED; orchestration blocker rewritten.

2) “Active Crons” table is stale and misleading
- File says “System-managed, DO NOT EDIT”, but there is no job that syncs it.
- It also listed heartbeat as “every 60m” while we were running it at 2h cadence.
Recommendation:
- Add a cron that syncs the “Active Crons” section from `cronjob list` daily (or remove the section entirely).

3) No guaranteed GitHub push loop
- Work can be written to disk, but without an automatic push, the system *appears offline*.
- Fix applied: added cron `moxie-hq-autocommit-push` every 30m (HQ only) using a lock and no empty commits.

4) Concurrency/race risk on shared markdown state
- Multiple workers + governance can edit `orchestration.md` / `dispatch-queue.md`.
- “Atomic rename” doesn’t prevent last-writer-wins collisions.
Recommendation:
- Implement a shared file lock (`flock`) for any write to those state files, OR move to per-worker state files + governance merge.

5) “IN_PROGRESS forever” risk
- If a worker fails repeatedly, the queue remains IN_PROGRESS.
Recommendation:
- Governance should check file existence; if missing after N runs, flip to RETRY(1/3) and/or pause the worker cron.

## Fixes applied in this audit (immediate hardening)
- Updated `luna-worker` (job 3e93c4f54be5) to provider=openrouter model=qwen/qwen3-coder-480b-a35b:free.
- Unblocked queue rows: Luna/Pax/Orion set to QUEUED.
- Updated orchestration Last updated timestamp.
- Created cron job `moxie-hq-autocommit-push` (job 868bd30fe7c1) every 30m, deliver=local.

## Next fixes (recommended, high leverage)
1) Standardize worker messaging: workers should output [SILENT] when nothing changes (avoid spam), and only message on completion/blocker.
2) Add a cron “cron-health-scan”: greps latest outputs for HTTP 400/429 and auto-patches provider/model (where safe), else writes a single issue.
3) Add an “Active Cron Inventory Sync” job to keep orchestration.md truthful.
4) Add a governance check: if deliverable path missing while IN_PROGRESS, set RETRY with a next attempt window.

