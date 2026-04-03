# Moxie HQ — Performance Improvements (Deep Analysis)

Date: 2026-04-03
Scope: Reduce latency + token burn + queue-script runtime; improve reliability (no duplicate dispatches); keep founder notifications clean.

## Executive Summary (what’s actually slowing things down)
1) **Context bloat / token burn**: Workers and governance loops repeatedly read large state files (notably orchestration.md + dispatch-queue.md + delegation-queue.md). Even if each file isn’t “huge”, repeated reads across many hourly agents compound into latency and quota burn.
2) **O(n²) membership scans in queue automation**: `process_delegation_queue.py` previously did `any(tag in line for line in dispatch_lines)` inside a loop over delegation rows. As delegation grows, runtime increases and re-dispatch risk increases if you ever compact dispatch-queue.
3) **Redundant dedupe checks in artifact watcher**: `process_artifacts.py` was doing repeated `any(tag in line ...)` scans; functionally OK, but unnecessary work and increases runtime linearly with dispatch size.
4) **Operational truth drift**: Not a “speed” issue per se, but it causes repeated “already resolved” blockers to reappear, producing extra human cycles and tool calls.

## Changes implemented immediately (verified)

### 1) Delegation dispatch dedupe state (major correctness + speed win)
File changed: `/root/moxie_hq/cmo/scripts/process_delegation_queue.py`

What changed:
- Added a persistent state file: `/root/moxie_hq/cmo/state/delegation_dispatched_ids.json`
- `process_delegation_queue.py` now checks **O(1)** membership (`row_id in dispatched_ids`) instead of repeatedly scanning the entire dispatch queue per row.
- On first run, it bootstraps the set by extracting `[DELEGATION:<id>]` tags from `cmo/dispatch-queue.md`.

Why this matters:
- Speeds up each run as queues grow.
- Enables future compaction/archival of dispatch-queue **without risking duplicate re-dispatch**.

Verification:
- Ran `python3 cmo/scripts/process_delegation_queue.py` successfully; it created/updated `cmo/state/delegation_dispatched_ids.json`.

### 2) Artifact watcher membership scan optimization
File changed: `/root/moxie_hq/cmo/scripts/process_artifacts.py`

What changed:
- Pre-computes `dispatch_text` and `delegation_text` once.
- Replaces repeated `any(tag in line for line in ...)` with `tag in dispatch_text` / `tag in delegation_text`.

Verification:
- Ran `python3 cmo/scripts/process_artifacts.py` successfully (no changes detected).

## High-leverage next improvements (recommended)

### A) Compact/Archive dispatch-queue while keeping correctness
Current issue:
- `cmo/dispatch-queue.md` trends upward and gets re-read by workers and scripts.

Recommendation:
- Introduce `cmo/dispatch-queue.archive.md` and keep `dispatch-queue.md` active-only.
- Because we now have `delegation_dispatched_ids.json`, delegation promotion remains safe even if dispatch history is archived.

Impact:
- Immediate token burn reduction (workers read smaller file).
- Faster script membership checks and lower latency in runs.

### B) Split orchestration.md into (1) active state vs (2) reference appendices
Current issue:
- `cmo/orchestration.md` includes both operational state and long appendices (completed deliverables, rubric, large tables).

Recommendation:
- Keep `orchestration.md` as a compact “active state” file only.
- Move appendices into:
  - `cmo/resources/completed_deliverables.md`
  - `cmo/resources/rubric.md`

Impact:
- Lower context length per worker cycle.
- Faster responses + fewer compactions.

### C) Worker idle auto-pause (cost + noise reduction)
Current issue:
- Workers fire hourly even when dispatch queue has no tasks for them.

Recommendation:
- Governance cron checks: if a worker has had 0 queued items for N hours (e.g., 6h), pause that worker cron automatically; resume when a task appears.

Impact:
- Fewer model calls, lower spend, less noise.

### D) Structured state snapshots for workers
Recommendation:
- Generate `cmo/state/worker_context.md` (or JSON) that contains ONLY:
  - Active sprint product
  - Known blockers
  - The worker’s next task row(s)
  - Links to relevant deliverables

Impact:
- Workers stop loading full orchestration + full queues.

## Notes / Risks
- Dispatch queue compaction should be implemented together with a safe archival plan so no system depends on historic lines being present.
- Worker prompt updates (cron prompts) would be ideal for maximum savings, but we can get most of the win by shrinking the files they already read.

## Next action I can take
1) Implement dispatch-queue archival + keep active-only.
2) Split orchestration.md appendices into separate files.
3) Add idle worker auto-pause/resume logic.
