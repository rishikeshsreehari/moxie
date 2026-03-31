# Org-style review loop (Moxie as CMO)

Principle: specialists produce drafts + artifacts; CMO is the only layer that presents conclusions/decisions to the founder.

## 1) Output routing rule (presentation layer)
- Workers (Astra/Mira/Ember/Vale/Jax/Rumi/Luna/Pax/Orion/etc.) write outputs to disk only.
- Workers do NOT message Telegram directly.
- Moxie (CMO) is the only Telegram sender.

Enforcement mechanism:
- Worker crons deliver to `local` (cron output files only).
- Governance/heartbeat crons deliver to `telegram:<rishi_dm>`.

## 2) Review gate checklist (CMO)
Before I present anything from a worker to you, I run this check:
1) Does the deliverable file exist and have real content (not boilerplate / partial)?
2) Evidence: are claims backed by links, screenshots, logs, or reproducible steps?
3) Commercial relevance: what changes revenue, activation, retention, or CAC?
4) Risk: any hallucination risk, missing assumptions, or access limitations?
5) Next action: one concrete step + owner + ETA.

If any item fails: I label it “DRAFT/UNVERIFIED” internally and either (a) re-run with better prompt/model, (b) request missing access once, or (c) discard.

## 3) Closed feedback loop (cron + ops)
- Heartbeat must run hourly and check:
  - crons fired recently
  - new outputs created
  - dispatch/orchestration state drift
  - new blockers in issues_rishi.md
- Any detected drift becomes either:
  - an auto-fix (schedule/delivery/model mismatch), OR
  - a single-line escalation in issues_rishi.md

## 4) What you should see
- Fewer noisy worker pings.
- More “manager updates”: synthesized, prioritized, and action-oriented.
