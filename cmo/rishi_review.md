# Rishi Review Queue (Founder attention)

Purpose: single place to track everything that needs Rishi’s attention (reviews, manual execution, decisions).  
Rule: When Rishi asks “what needs my attention?”, Moxie reads this file and presents items **one by one**.

Last updated: 2026-04-01

---

## NOW (next 24h)

### [REVIEW] HQ repo cleanup run (tidy-up)
- Owner: Rishi (review), Moxie (executed)
- Report: /root/moxie_hq/cmo/reports/repo-health-audit-2026-04-02.md
- What happened: only removed 3x __pycache__ dirs (safe junk)
- Code/SOP:
  - /root/moxie_hq/cmo/sops/repo-health-audit.md
  - /root/moxie_hq/cmo/scripts/repo_cleanup.py
- Decision: approve this as the ongoing cleanup policy (yes/no + any exclusions)

### [REVIEW] Execution OS v3 deployment (process change)
- Owner: Rishi (review/approve), Moxie (deployed)
- SOP: /root/moxie_hq/cmo/sops/execution-os-v3.md
- Template: /root/moxie_hq/cmo/templates/execution-packet.md
- What changed: daily 13:00 GST execution window + last-mile contract + “not done until reported + Rishi marks DONE”
- Decision: approve OS v3 as the operating rule going forward (yes/no + edits)

## TODAY 13:00 GST (09:00 UTC) — Founder Execution Window
Rule: Moxie provides paste-ready execution packet(s) by 12:45 GST. Rishi executes 1 action and reports back with URL/outcome.


1) [ACTION] Directory submissions — Today’s 2 picks (manual)
- Owner: Rishi (execute), Jax (prep)
- File: /root/moxie/products/formbeep/directory-submissions-today-pick.md
- Picks (per latest Jax plan):
  - BetaList
  - AlternativeTo
- Done when: submitted + listing URL logged in /root/moxie/products/formbeep/distribution/directory-submissions-log.md

2) [REVIEW] Landing page — pick 1 change to ship this week
- Owner: Rishi (decision), Moxie (ship)
- File (single decision doc): /root/moxie/products/formbeep/analytics/landing-change-decision.md
- Source data (optional): /root/moxie/products/formbeep/analytics/landing-hero-funnel-30d.md
- Decision needed: reply with A/B/C/D from the decision doc

---

## WAITING ON OUTPUT (check when ready)

NOTE: “Platform marketplace submissions” is deferred until an engineering scope exists. It is not a pure submission/credentials task.

3) [REVIEW] Google Search Console quick audit (indexing + queries)
- Owner: Rishi (review), Forge (creating)
- Output: /root/moxie/products/formbeep/seo/gsc-quick-audit.md
- Decision: which 1–2 indexing/SEO fixes to implement next

4) [REVIEW] Rubric reality check (are scorecards real? who is underperforming?)
- Owner: Rishi (review), Moxie (creating)
- Output (to be created): /root/moxie_hq/cmo/reports/rubric-audit.md
- Decision: whether to fix wiring or remove rubric from docs; any corrective actions per employee

---

## WAITING (external)

5) [WAITING] WordPress plugin approval
- Owner: Rishi
- Status: Submitted, waiting (~10 days)
- Next action: when approved, trigger WP launch plan

---

## SYSTEMS TO MAINTAIN (ongoing)

0) [SETUP] New product onboarding questionnaire (answer once per product)
- Owner: Rishi
- File: /root/moxie_hq/cmo/resources/product-onboarding/product-onboarding-questions.md
- When used: the moment you give me Product #2 details

6) [SETUP/MAINTAIN] Reddit posting tracker (rules + “have we posted?”)
- Owner: Rishi (manual posting), Ember (planning)
- File: /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md
- Next action: pick 5–10 subs for this week, fill rules + viral patterns; then post manually

7) [SETUP/MAINTAIN] Directory tracking
- Owner: Rishi (execute), Jax (ops)
- Files:
  - /root/moxie/products/formbeep/directory-submissions-tracker.md
  - /root/moxie/products/formbeep/distribution/directory-submissions-log.md
- Next action: keep logging every submission/approval to avoid duplicates

8) [REVIEW TOMORROW] US SMS SERP demand research (FormBeep) — DONE
- Owner: Rishi (review), Astra (completed)
- Output: /root/moxie/products/formbeep/seo/us-sms-serp-demand-brief.md
- What you’ll decide: GO/NO-GO on emphasizing US SMS vs India WhatsApp first, and which 3 pages to ship first.

9) [REVIEW TOMORROW] Content strategy (all projects): Founder Voice + Build-in-Public for X + IndieHackers
- Owner: Rishi (review), Moxie (creating)
- Output (will be created): /root/moxie_hq/cmo/strategy/founder-voice-x-indiehackers.md
- Includes Golden Rule: where/why/how/when (UTC+country)/why-that-time for every planned post.

10) [REVIEW TOMORROW] FormBeep: GSC vs Umami (last 28d) — what ranks vs what converts
- Owner: Rishi (review), Mira (creating)
- Output (will be created): /root/moxie/products/formbeep/analytics/gsc-vs-umami-28d.md
- Goal: pick the 3 highest-leverage pages to fix this week.

(Directory tracking remains ongoing)
- Owner: Rishi (execute), Jax (ops)
- Files:
  - /root/moxie/products/formbeep/directory-submissions-tracker.md
  - /root/moxie/products/formbeep/distribution/directory-submissions-log.md
- Next action: keep logging every submission/approval to avoid duplicates
