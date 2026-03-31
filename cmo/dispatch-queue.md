# Moxie CMO Dispatch Queue
# This file drives the autonomous orchestration system.
# The orchestrator cron reads this, finds the next READY task, and spawns the right employee.
# Employees update orchestration.md when done, which triggers the next dispatch.

---

## Queue (ordered by priority)
Format: [STATUS] Employee | (Product) Task | Depends on | Output file

1. [COMPLETED] Vale | (FormBeep) Beepmate + Web2Phone deep-dive + founder Reddit analysis | None | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
2. [IN_PROGRESS] Astra | (FormBeep) SEO: WP plugin market analysis + 30 keywords mapped to pages (7d) | None | /root/moxie/products/formbeep/wordpress-market-analysis.md
3. [IN_PROGRESS] Ember | (FormBeep) Reddit: 6 post drafts + 20 comments plan + 2 posts to publish (7d sprint) | None | /root/moxie/products/formbeep/reddit-strategy.md
4. [IN_PROGRESS] Jax | (FormBeep) Directories: 40+ master list + submit to 10 (stretch 20) in 7d | None | /root/moxie/products/formbeep/directory-submissions.md
5. [IN_PROGRESS] Rumi | (FormBeep) Content: competitor blog analysis + 30-day calendar + 4 post outlines (7d) | None | /root/moxie/products/formbeep/content-calendar.md
6. [COMPLETED] Mira | (FormBeep) Umami traffic audit + funnel analysis | None | /root/moxie/products/formbeep/analytics-report.md
7. [IN_PROGRESS] Nova | (FormBeep) Paid acquisition plan + tracking + 3 starter campaigns (Google, Meta, Reddit) | None | /root/moxie/products/formbeep/paid-ads/plan.md
8. [QUEUED] Nova | (SapiensTech) Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) | None | /root/moxie/cmo/sops/paid-ads-sop.md
9. [QUEUED] Luna | (FormBeep) Lifecycle onboarding + activation emails (Day 0/1/3/7/14) | None | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
10. [QUEUED] Pax | (FormBeep) Partnership target list (agencies + no-code builders + form tools) + outreach templates | None | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md
11. [QUEUED] Kiro | (FormBeep) Landing page copy (headline, features, pricing, FAQ) + 2 blog drafts | Vale COMPLETED + Astra/Rumi outputs | /root/moxie/products/formbeep/copy/landing-page-v1.md
12. [QUEUED] Orion | (FormBeep) Outbound pack: 150 prospects + 3-step cold email sequence + 5 subjects | None | /root/moxie_hq/products/formbeep/outbound/outbound-pack.md
13. [QUEUED] Forge | (FormBeep) WordPress plugin code audit and fixes (resubmission support) | None | /root/moxie/products/formbeep/wp-plugin-fixes.md
14. [QUEUED] Ember | (FormBeep) Reddit campaign launch plan (calendar + posting SOP + partnerships tie-in) | Ember drafts COMPLETED | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md
15. [QUEUED] Kiro | (FormBeep) 2 blog posts from Astra keyword research (finalize after outlines) | Astra + Rumi COMPLETED | /root/moxie/products/formbeep/copy/
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
