# Moxie CMO Dispatch Queue
# This file drives the autonomous orchestration system.
# The orchestrator cron reads this, finds the next READY task, and spawns the right employee.
# Employees update orchestration.md when done, which triggers the next dispatch.

---

## Queue (ordered by priority)
Format: [STATUS] Employee | (Product) Task | Depends on | Output file

1. [RETRY(1/3)] Vale | Beepmate + Web2Phone deep-dive + founder Reddit analysis | None | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
2. [RETRY(1/3)] Astra | WordPress form-notification plugin market analysis | None | /root/moxie/products/formbeep/wordpress-market-analysis.md
3. [RETRY(1/3)] Ember | Reddit landscape research + 3 post drafts | None | /root/moxie/products/formbeep/reddit-strategy.md
4. [RETRY(1/3)] Jax | 40+ SaaS directory master list | None | /root/moxie/products/formbeep/directory-submissions.md
5. [RETRY(1/3)] Rumi | Competitor blog analysis + 30-day content calendar | None | /root/moxie/products/formbeep/content-calendar.md
6. [IN_PROGRESS] Mira | (FormBeep) Umami traffic audit + funnel analysis | None | /root/moxie/products/formbeep/analytics-report.md
7. [QUEUED] Nova | (FormBeep) Paid acquisition plan + tracking + 3 starter campaigns (Google, Meta, Reddit) | None | /root/moxie/products/formbeep/paid-ads/plan.md
8. [QUEUED] Nova | (SapiensTech) Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) | None | /root/moxie/cmo/sops/paid-ads-sop.md
9. [QUEUED] Luna | (FormBeep) Lifecycle onboarding + activation emails (Day 0/1/3/7/14) | None | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
10. [QUEUED] Pax | (FormBeep) Partnership target list (agencies + no-code builders + form tools) + outreach templates | None | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md
11. [QUEUED] Kiro | (FormBeep) Landing page copy (headline, features, pricing, FAQ) | Vale COMPLETED | /root/moxie/products/formbeep/copy/landing-page-v1.md
10. [QUEUED] Kiro | (FormBeep) 2 blog posts from Astra keyword research | Astra + Rumi COMPLETED | /root/moxie/products/formbeep/copy/
11. [QUEUED] Ember | (FormBeep) Full Reddit campaign launch + partnership outreach | Vale COMPLETED | /root/moxie/products/formbeep/outreach/
10. [QUEUED] Forge | WordPress plugin code audit and fixes | Codex premium available | /root/moxie/products/formbeep/wp-plugin-fixes.md
11. [QUEUED] Forge | Technical SEO audit (page speed, structured data, meta tags) | None | /root/moxie/products/formbeep/technical-seo-audit.md
12. [QUEUED] Jax | Begin P1 directory submissions (ProductHunt, AlternativeTo, BetaList) | Jax directory list COMPLETED + Rishi approves | /root/moxie/products/formbeep/directory-submissions.md
13. [QUEUED] Vale | Monthly competitor monitoring (pricing changes, new features) | Initial intel COMPLETED | /root/moxie/products/formbeep/competitor-monitoring.md

---

## Dispatch Rules
- Priority 1-6: Currently dispatched. Wait for completion.
- After any IN_PROGRESS task completes → check dependency chain → promote first QUEUED task with satisfied dependencies to IN_PROGRESS
- Kiro cannot start until Vale's intel is COMPLETED (needs competitor positioning gaps)
- Forge cannot start until Codex 5-hour quota resets (check orchestration.md blockers)
- Jax directory submissions cannot start until directory list COMPLETED and Rishi provides account credentials
- Ember full campaign cannot start without Vale's competitor intel (needs positioning wedge)

## Recurring Task Schedule
| Employee | Frequency | Task |
|----------|-----------|------|
| Mira | Daily 10:00 UTC | Traffic check + usage snapshot |
| Mira | Weekly Monday 11:00 UTC | Growth review compilation |
| Vale | Monthly 1st | Competitor pricing/feature scan |
| Astra | Bi-weekly Wednesday | Keyword ranking check + new keyword ideas |
| Rumi | Bi-weekly Friday | Content gap scan + trending topic check |
