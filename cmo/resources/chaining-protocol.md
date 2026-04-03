# Chaining Protocol (HQ) — stop context loss

Goal: every task + every deliverable must be self-contained, auditable, and reusable without “remembering” chat.

This protocol is **mandatory** for all employees (Astra/Ember/Forge/Jax/Kiro/Pax/Rumi/Vale/Mira/etc).

---

## 1) READ-FIRST chain (start of every task)

Before doing any work:

1) Read **active orchestration state**
- `/root/moxie_hq/cmo/orchestration.md`

2) Identify the **active product slug** (examples: formbeep, stackstats).

3) Load the product context pack (if present):
- `/root/moxie_hq/products/<product_slug>/status.md` (latest stats + truth-layer)
- `/root/moxie_hq/products/<product_slug>/overview.md`
- `/root/moxie_hq/products/<product_slug>/briefings/canonical-facts.md`
- `/root/moxie_hq/products/<product_slug>/positioning.md`
- `/root/moxie_hq/products/<product_slug>/icp.md`
- `/root/moxie_hq/products/<product_slug>/competitors.md` (or `competitor-intel.md`)

If a file is missing, do NOT guess. Use what exists and cite it.

4) Read any task-specific upstream artifacts referenced by the task (dispatch queue output paths, previous reports, scripts).

---

## 2) Deliverable must start with a CHAIN HEADER

Every output file you write MUST begin with this header (fill it in):

CHAIN:
- Task ID:
- Seat:
- Product:
- Product context used (file paths):
- Upstream inputs used (file paths + URLs):
- Truth-layer notes (what we are NOT claiming):
- Output file:
- Verification steps (how to confirm it’s correct):
- Downstream links (where to log results / next tasks to create):

---

## 3) Hard rules (non-negotiable)

- Evidence-first: every claim should be backed by a file pointer or URL.
- Don’t claim unshipped features; cite canonical-facts.md or shipped UI.
- If work requires credentials/paid APIs: mark BLOCKED and write to `/root/moxie_hq/cmo/issues_rishi.md`.
- If you can’t find required context: stop and report exactly what file is missing.

---

## 4) Enforcement points

- Employee SOUL files must reference this protocol.
- Execution packets must include the chain header.
- Delegation queue rows should include “notes” with upstream context pointers when possible.
