# CMO Delegation Queue (Founder/CMO input)
# Purpose: a low-friction place to append work orders during live chat WITHOUT running tooling.
# The processors under /root/moxie_hq/cmo/scripts/ read this file and promote items into:
#   - /root/moxie_hq/cmo/dispatch-queue.md (worker execution)
#
# RULE: Do not run tooling during live chat; queue work orders instead.

---

## Format (spec)

This file is a single markdown table under "## Queue".

Column meanings:
- id: unique identifier you create (free text). Suggest: dq-YYYYMMDD-HHMM-shortslug
- status: one of NEW | DISPATCHED | CANCELLED
- created_utc: ISO-8601 timestamp (UTC). Suggest: 2026-04-01T16:00:00Z
- seat: employee seat (e.g., Vale, Astra, Ember, Kiro, Mira, Nova, Jax, Pax, Luna, Orion, Iris, Forge)
- priority: P0 | P1 | P2 | P3 (P0 highest)
- product: free text product tag (e.g., FormBeep, SapiensTech, <NewProduct>)
- task: the actual work request (imperative, specific)
- depends_on: "None" or free-text deps (can reference another id)
- output_file: absolute path where deliverable should be written
- dispatched_utc: filled by processor when promoted
- notes: optional

Processing rules:
- Rows with status != DISPATCHED are eligible.
- Processor promotes eligible rows into dispatch-queue.md as [QUEUED] tasks.
- Processor is idempotent: if a row id was already promoted, it will not be duplicated.

---

## Queue

| id | status | created_utc | seat | priority | product | task | depends_on | output_file | dispatched_utc | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| dq-20260401-1600-reddit-playbook | DISPATCHED | 2026-04-01T16:00:00Z | Vale | P0 | FormBeep | Review latest Reddit intel artifact and produce concise positioning + subreddit playbook. Include: target subs, angle hypotheses, do/don't list, and 10 post/comment hooks. | None | /root/moxie/products/formbeep/outreach/reddit-intel-positioning-subreddit-playbook.md | 2026-04-01T17:20:42Z | Source artifact: /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md |
| dq-20260401-1610-directory-exec | DISPATCHED | 2026-04-01T16:10:00Z | Jax | P1 | FormBeep | Execute P1 directory submissions using the prepared pack. Capture confirmation URLs/screenshots in the output doc. | Depends: founder provides credentials (see issues_rishi.md) | /root/moxie/products/formbeep/directory-submissions-execution-log.md | 2026-04-01T17:20:42Z | BLOCKED until credentials |
| dq-20260401-1620-ads-template | DISPATCHED | 2026-04-01T16:20:00Z | Nova | P2 | SapiensTech | Create a generic paid-ads campaign naming + UTM template (copy/paste) suitable for any new product onboarding. | None | /root/moxie/cmo/templates/paid-ads-utm-template.md | 2026-04-01T17:20:42Z | Keep it product-agnostic |
