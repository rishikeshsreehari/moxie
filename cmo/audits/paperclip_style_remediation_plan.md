# Paperclip-style remediation plan for Moxie HQ (Hermes)

Timestamp: 2026-04-06
Owner: Moxie
Repo: /root/moxie_hq

## Executive summary (what’s actually wrong)

The system *is not primarily failing at execution* — it is failing at **accountability**:
- Outputs and claims are not anchored to a durable audit log.
- “Employees” are prompt identities, not ticket-scoped workers with checkout + receipts.
- Founder-facing files (issues + rishi_review + dispatch-queue) drift out of sync.
- Performance degradation comes from repeated large-context reasoning + re-reading big files.

Paperclip solves this by making everything ticketed, budgeted, heartbeat-driven, and auditable.

This plan delivers 80% of Paperclip’s value quickly, then optionally migrates to Paperclip proper.

---

## Phase 0 (today): Stop truth drift

### 0.1 Immutable run ledger (DONE)
- Added: `cmo/scripts/hq_pipeline_run.py`
- Purpose: run delegation + artifacts and append JSONL entries to `cmo/state/run_ledger.jsonl`.
- Output contract: prints `OK:` / `BLOCKED:` / `ERROR:` one-liners for cron parsing.

### 0.2 “No claim without evidence” rule
- Any report must reference at least one of:
  - git commit hash
  - ledger entry (run_id + step)
  - artifact path + mtime
  - exact error line

### 0.3 Fix known deprecation (IN PROGRESS)
- Patch `datetime.utcnow()` → `datetime.now(timezone.utc)` in `cmo/scripts/process_delegation_queue.py`.

---

## Phase 1 (24–48h): Paperclip-lite inside Hermes (no new infrastructure)

### 1.1 Ticket checkout (dispatch queue as the ticket system)
- Enforce state machine:
  - PENDING → IN_PROGRESS (run_id, assignee) → COMPLETED (artifact path + commit) OR BLOCKED (evidence)
- One ticket per agent at a time.

### 1.2 Receipts (artifact requirements)
For any ticket to be marked COMPLETED:
- Artifact must exist at the stated path
- Artifact must include:
  - timestamp
  - inputs used
  - commands run / API endpoints queried (masked secrets)
  - “limitations / next steps” section

### 1.3 QA gate before founder review
- Every founder-facing packet passes a lightweight QA check:
  - capability claims match truth layer
  - no missing script references
  - no “all zeros” dashboards without an explanation

### 1.4 Performance improvements
- Add caching / derived-state files under `cmo/state/` instead of repeatedly parsing markdown.
- Keep prompts short by using:
  - `dispatch-queue.md` (single task)
  - `run_ledger.jsonl` (last 20 lines)
  - specific artifact paths

---

## Phase 2 (optional, recommended): Deploy Paperclip + Hermes adapter

### Why
Paperclip provides:
- real ticket system + immutable audit log
- per-agent budgets + spend throttling
- org chart + goal ancestry
- mobile dashboard

### Feasibility snapshot
- Node 20 is present on this host.
- `pnpm` is currently missing; install required.

### Steps
1) Install pnpm
2) Clone + start Paperclip (server on :3100)
3) Install `hermes-paperclip-adapter`
4) Register adapter in Paperclip
5) Create Hermes agents as employees (toolset-scoped)
6) Route existing dispatch queue tasks into Paperclip issues
7) Put Hermes employees on heartbeats; enforce budgets

### Cutover plan
- Run Paperclip side-by-side for 48h.
- Once stable: freeze the old markdown-based dispatcher.

---

## Success criteria

- Founder sees **one** accurate list of “needs attention” (rishi_review.md) that is always consistent.
- No alerts unless a true blocker exists.
- Every completed task has a verifiable artifact + ledger line + commit.
- Pipeline runs produce deterministic OK/BLOCKED/ERROR.
