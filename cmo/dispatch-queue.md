     1|# Moxie CMO Dispatch Queue
     2|# This file drives the autonomous orchestration system.
     3|# The orchestrator cron reads this, finds the next READY task, and spawns the right employee.
     4|# Employees update orchestration.md when done, which triggers the next dispatch.
     5|
     6|---
     7|
     8|## Queue (ordered by priority)
     9|Format: [STATUS] Employee | (Product) Task | Depends on | Output file
    10|
    11|1. [COMPLETED] Vale | (FormBeep) Beepmate + Web2Phone deep-dive + founder Reddit analysis | None | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
    12|2. [COMPLETED] Astra | (FormBeep) SEO: WP plugin market analysis + 30 keywords mapped to pages (7d) | None | /root/moxie/products/formbeep/wordpress-market-analysis.md
    13|2b. [IN_PROGRESS] Astra | (FormBeep) Tally Forms growth teardown (how they got big: channels, SEO/templates, PLG loops, distribution) + what we can copy for FormBeep | None | /root/moxie/products/formbeep/tally-growth-teardown.md
    14|2c. [QUEUED] Astra | (FormBeep) SMS demand + keyword analysis (is there search intent? which platforms/modifiers? landing pages to build) | None | /root/moxie/products/formbeep/sms-keyword-analysis.md
    15|3. [COMPLETED] Ember | (FormBeep) Reddit: 6 post drafts + 20 comments plan + 2 posts to publish (7d sprint) | None | /root/moxie/products/formbeep/reddit-strategy.md
    16|4. [COMPLETED] Jax | (FormBeep) Directories: 40+ master list + submit to 10 (stretch 20) in 7d | None | /root/moxie/products/formbeep/directory-submissions.md
    17|5. [COMPLETED] Rumi | (FormBeep) Content: competitor blog analysis + 30-day calendar + 4 post outlines (7d) | None | /root/moxie/products/formbeep/content-calendar.md
    18|6. [COMPLETED] Mira | (FormBeep) Umami traffic audit + funnel analysis | None | /root/moxie/products/formbeep/analytics-report.md
    19|7. [IN_PROGRESS] Mira | (FormBeep) Traffic vs keyword opportunity map (use Umami + Astra keyword briefing) | Mira analytics COMPLETED + Astra keyword briefing COMPLETED | /root/moxie/products/formbeep/traffic-vs-keywords.md
    20|8. [COMPLETED] Nova | (FormBeep) Paid acquisition plan + tracking + 3 starter campaigns (Google, Meta, Reddit) | None | /root/moxie/products/formbeep/paid-ads/plan.md
    21|8. [COMPLETED] Nova | (SapiensTech) Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) | None | /root/moxie/cmo/sops/paid-ads-sop.md
    22|9. [COMPLETED] Luna | (FormBeep) Lifecycle onboarding + activation emails (Day 0/1/3/7/14) | None | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
    23|10. [QUEUED] Pax | (FormBeep) Partnership target list (agencies + no-code builders + form tools) + outreach templates | None | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md
    24|11. [COMPLETED] Kiro | (FormBeep) Landing page copy (headline, features, pricing, FAQ) + 2 blog drafts | Vale COMPLETED + Astra/Rumi outputs | /root/moxie/products/formbeep/copy/landing-page-v1.md
    25|12. [QUEUED] Orion | (FormBeep) Outbound pack: 150 prospects + 3-step cold email sequence + 5 subjects | None | /root/moxie/products/formbeep/outbound/outbound-pack.md
    26|13. [COMPLETED] Forge | (FormBeep) WordPress plugin code audit and fixes (resubmission support) | None | /root/moxie/products/formbeep/wp-plugin-fixes.md
    27|14. [IN_PROGRESS] Ember | (FormBeep) Reddit campaign launch plan (calendar + posting SOP + partnerships tie-in + ideal posting day/time based on active userbase) | Ember drafts COMPLETED | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md
    28|15. [COMPLETED] Kiro | (FormBeep) 2 blog posts from Astra keyword research (finalize after outlines) | Astra + Rumi COMPLETED | /root/moxie/products/formbeep/copy/blog-posts-v1.md
    29|16. [COMPLETED] Forge | (FormBeep) Technical SEO audit (page speed, structured data, meta tags) | None | /root/moxie/products/formbeep/technical-seo-audit.md
    30|12. [QUEUED] Jax | Begin P1 directory submissions (ProductHunt, AlternativeTo, BetaList) | Jax directory list COMPLETED + Rishi approves | /root/moxie/products/formbeep/directory-submissions-p1.md
13. [IN_PROGRESS] Vale | (FormBeep) Monthly competitor monitoring + founder Reddit signal scan (Beepmate u/adambengur, Web2Phone u/ConferenceOnly1415): which subs + what angles worked | Initial intel COMPLETED | /root/moxie/products/formbeep/competitor-monitoring.md
    32|
    33|---
    34|
    35|## Dispatch Rules
    36|- Priority 1-6: Currently dispatched. Wait for completion.
    37|- After any IN_PROGRESS task completes → check dependency chain → promote first QUEUED task with satisfied dependencies to IN_PROGRESS
    38|- Kiro cannot start until Vale's intel is COMPLETED (needs competitor positioning gaps)
    39|- Forge premium tasks: only run when Codex premium window is available (see orchestration.md blocker table); currently RESOLVED per orchestration.md
    40|- Jax directory submissions cannot start until directory list COMPLETED and Rishi provides account credentials
    41|- Ember full campaign cannot start without Vale's competitor intel (needs positioning wedge)
    42|
    43|## Recurring Task Schedule
    44|| Employee | Frequency | Task |
    45||----------|-----------|------|
    46|| Mira | Daily 10:00 UTC | Traffic check + usage snapshot |
    47|| Mira | Weekly Monday 11:00 UTC | Growth review compilation |
    48|| Vale | Monthly 1st | Competitor pricing/feature scan |
    49|| Astra | Bi-weekly Wednesday | Keyword ranking check + new keyword ideas |
    50|| Rumi | Bi-weekly Friday | Content gap scan + trending topic check |
    51|