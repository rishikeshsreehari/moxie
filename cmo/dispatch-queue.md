     1|# Moxie CMO Dispatch Queue
     2|# This file drives the autonomous orchestration system.
     3|# The orchestrator cron reads this, finds the next READY task, and spawns the right employee.
     4|# Employees update orchestration.md when done, which triggers the next dispatch.
     5|
     6|---
     7|
## Queue (ordered by priority)
Format: [STATUS] Employee | (Product) Task | Depends on | Output file

0. [QUEUED] Vale | (FormBeep) Review latest Reddit intel artifact and produce concise positioning + subreddit playbook. Include: target subs, angle hypotheses, do/don't list, and 10 post/comment hooks. [DELEGATION:dq-20260401-1600-reddit-playbook] | None | /root/moxie/products/formbeep/outreach/reddit-intel-positioning-subreddit-playbook.md
1. [QUEUED] Jax | (FormBeep) Execute P1 directory submissions using the prepared pack. Capture confirmation URLs/screenshots in the output doc. [DELEGATION:dq-20260401-1610-directory-exec] | Depends: founder provides credentials (see issues_rishi.md) | /root/moxie/products/formbeep/directory-submissions-execution-log.md
2. [QUEUED] Nova | (SapiensTech) Create a generic paid-ads campaign naming + UTM template (copy/paste) suitable for any new product onboarding. [DELEGATION:dq-20260401-1620-ads-template] | None | /root/moxie/cmo/templates/paid-ads-utm-template.md
0. [COMPLETED] Vale | (FormBeep) Analyze newly-pushed Reddit intel artifact → produce actionable FormBeep positioning + subreddit playbook | Source: /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md | /root/moxie/products/formbeep/outreach/reddit-intel-positioning-subreddit-playbook.md ✅
0b. [IN_PROGRESS] Ember | (FormBeep) Draft subreddit-specific post/comment scripts + reply macros based on Vale playbook | Depends: Vale playbook COMPLETED (execution still needs Reddit creds) | /root/moxie/products/formbeep/outreach/reddit-post-comment-scripts.md
    13|
    14|1. [COMPLETED] Vale | (FormBeep) Beepmate + Web2Phone deep-dive + founder Reddit analysis | None | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
    15|2. [COMPLETED] Astra | (FormBeep) SEO: WP plugin market analysis + 30 keywords mapped to pages (7d) | None | /root/moxie/products/formbeep/wordpress-market-analysis.md
    16|2b. [COMPLETED] Astra | (FormBeep) Tally Forms growth teardown (how they got big: channels, SEO/templates, PLG loops, distribution) + what we can copy for FormBeep | None | /root/moxie/products/formbeep/tally-growth-teardown.md
    17|2c. [COMPLETED] Astra | (FormBeep) SMS demand + keyword analysis (is there search intent? which platforms/modifiers? landing pages to build) | None | /root/moxie/products/formbeep/sms-keyword-analysis.md
    18|3. [COMPLETED] Ember | (FormBeep) Reddit: 6 post drafts + 20 comments plan + 2 posts to publish (7d sprint) | None | /root/moxie/products/formbeep/reddit-strategy.md
    19|4. [COMPLETED] Jax | (FormBeep) Directories: 40+ master list + submit to 10 (stretch 20) in 7d | None | /root/moxie/products/formbeep/directory-submissions.md
    20|5. [COMPLETED] Rumi | (FormBeep) Content: competitor blog analysis + 30-day calendar + 4 post outlines (7d) | None | /root/moxie/products/formbeep/content-calendar.md
    21|6. [COMPLETED] Mira | (FormBeep) Umami traffic audit + funnel analysis | None | /root/moxie/products/formbeep/analytics-report.md
    22|7. [COMPLETED] Mira | (FormBeep) Traffic vs keyword opportunity map (use Umami + Astra keyword briefing) | Mira analytics COMPLETED + Astra keyword briefing COMPLETED | /root/moxie/products/formbeep/traffic-vs-keywords.md
    23|8. [COMPLETED] Nova | (FormBeep) Paid acquisition plan + tracking + 3 starter campaigns (Google, Meta, Reddit) | None | /root/moxie/products/formbeep/paid-ads/plan.md
    24|8. [COMPLETED] Nova | (SapiensTech) Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) | None | /root/moxie/cmo/sops/paid-ads-sop.md
    25|9. [COMPLETED] Luna | (FormBeep) Lifecycle onboarding + activation emails (Day 0/1/3/7/14) | None | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
    26|10. [COMPLETED] Pax | (FormBeep) Partnership target list (agencies + no-code builders + form tools) + outreach templates | None | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md
    27|11. [COMPLETED] Kiro | (FormBeep) Landing page copy (headline, features, pricing, FAQ) + 2 blog drafts | Vale COMPLETED + Astra/Rumi outputs | /root/moxie/products/formbeep/copy/landing-page-v1.md
    28|12. [COMPLETED] Orion | (FormBeep) Outbound pack: 150 prospects + 3-step cold email sequence + 5 subjects | None | /root/moxie/products/formbeep/outbound/outbound-pack.md
    29|13. [COMPLETED] Forge | (FormBeep) WordPress plugin code audit and fixes (resubmission support) | None | /root/moxie/products/formbeep/wp-plugin-fixes.md
    30|14. [COMPLETED] Ember | (FormBeep) Reddit campaign launch plan (calendar + posting SOP + partnerships tie-in + ideal posting day/time based on active userbase) | Ember drafts COMPLETED | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md
    31|15. [COMPLETED] Kiro | (FormBeep) 2 blog posts from Astra keyword research (finalize after outlines) | Astra + Rumi COMPLETED | /root/moxie/products/formbeep/copy/blog-posts-v1.md
    32|16. [COMPLETED] Forge | (FormBeep) Technical SEO audit (page speed, structured data, meta tags) | None | /root/moxie/products/formbeep/technical-seo-audit.md
    33|12. [COMPLETED] Jax | (FormBeep) Begin P1 directory submissions (ProductHunt, AlternativeTo, BetaList) — full submission pack ready; actual submissions await credentials | Jax directory list COMPLETED + Rishi credentials/approval (see issues_rishi.md) | /root/moxie/products/formbeep/directory-submissions-p1.md
    34|13. [COMPLETED] Vale | (FormBeep) Monthly competitor monitoring + founder Reddit signal scan (Beepmate u/adambengur, Web2Phone u/ConferenceOnly1415): which subs + what angles worked | Initial intel COMPLETED | /root/moxie/products/formbeep/competitor-monitoring.md — **APRIL 2026 SCAN COMPLETED**
    35|14. [COMPLETED] Rumi | (FormBeep) Bi-weekly content gap scan + trending topic check | Previous content COMPLETED | /root/moxie/products/formbeep/content-gap-scan.md
    36|15. [COMPLETED] Kiro | (FormBeep) Draft platform "money pages" (WordPress form→WhatsApp, Webflow form→WhatsApp, Framer form notifications) + 1 comparison page (FormBeep vs Web2Phone) | Astra keyword set COMPLETED + Kiro landing copy COMPLETED | /root/moxie/products/formbeep/copy/money-pages-v1.md
    37|16. [COMPLETED] Pax | (FormBeep) P0 platform partner program outreach (Webflow, Framer, Glide, Softr, Bubble) + application copy + Bubble plugin spec | Pax targets COMPLETED | /root/moxie/products/formbeep/partnerships/platform-partner-outreach.md
    38|17. [COMPLETED] Pax | (FormBeep) Week 1 platform applications execution — prepared application packages for Webflow Apps, Framer Marketplace, Glide Integrations (copy, metadata, submission steps) | Pax P0 outreach COMPLETED | /root/moxie/products/formbeep/partnerships/platform-applications-week1.md
    39|18. [COMPLETED] Pax | (FormBeep) Week 2 submissions: Softr integration + follow up on Week 1 application reviews + assign Bubble plugin build task to Forge | Week 1 execution COMPLETED | /root/moxie/products/formbeep/partnerships/platform-applications-week2.md
    40|19. [COMPLETED] Pax | (FormBeep) Week 3 submissions (Carrd + Typedream integration packages + agency outreach to top 15 targets) | Week 2 submissions COMPLETED | /root/moxie/products/formbeep/partnerships/platform-applications-week3.md
    41|---
    42|
    43|## Dispatch Rules
    44|- Priority 1-6: Currently dispatched. Wait for completion.
    45|- After any IN_PROGRESS task completes → check dependency chain → promote first QUEUED task with satisfied dependencies to IN_PROGRESS
    46|- Kiro cannot start until Vale's intel is COMPLETED (needs competitor positioning gaps)
    47|- Forge premium tasks: only run when Codex premium window is available (see orchestration.md blocker table); currently RESOLVED per orchestration.md
    48|- Jax directory submissions cannot start until directory list COMPLETED and Rishi provides account credentials
    49|- Ember campaign: Planning assets READY; execution remains BLOCKED on Reddit account credentials (see issues_rishi.md)
    50|
    51|## Task Completion Protocol (Rubric Wired)
    52|When marking a task COMPLETED, the employee MUST:
    53|1. Write deliverable to specified output file
    54|2. Update orchestration.md status to COMPLETED
    55|3. **Auto-trigger scoring:** System runs `task-scorer.py <employee> <task_id> <output_file>`
    56|4. Review scorecard at `/root/moxie_hq/cmo/scores/{employee}/{task_id}.md`
    57|5. Complete "Dreaming" reflection: What worked? What would I change? Update SOUL.md Learnings
    58|6. Suggest next task based on score improvement focus
    59|
    60|**Scoring is automatic.** All deliverables graded on 7 dimensions (1-5). Scores appear in SOUL.md under ## Recent Scores.
    61|
    62|## Recurring Task Schedule
    63|| Employee | Frequency | Task |
    64||----------|-----------|------|
    65|| Mira | Daily 10:00 UTC | Traffic check + usage snapshot |
    66|| Mira | Weekly Monday 11:00 UTC | Growth review compilation |
    67|| Vale | Monthly 1st | Competitor pricing/feature scan |
    68|| Astra | Bi-weekly Wednesday | Keyword ranking check + new keyword ideas |
    69|| Rumi | Bi-weekly Friday | Content gap scan + trending topic check |
    70|
## Vale Status (Current Session)
- Status: **COMPLETED** — Reddit intel analysis → positioning + subreddit playbook ✅
- Output delivered: /root/moxie/products/formbeep/outreach/reddit-intel-positioning-subreddit-playbook.md
- Follow-on (Ember): IN_PROGRESS — drafting post/comment scripts based on Vale playbook
- Next recurring: Monthly scan 2026-05-01 (cron: vale-monthly-competitor-scan)
    77|
    78|## Astra Status (Current Session)
    79|- All 3 sprint tasks COMPLETED as of 2026-03-31 (WP market analysis, Tally teardown, SMS keyword analysis)
    80|- **IDLE** — no queued or blocked tasks (checked 2026-04-01T08:17)
    81|- Next recurring: Bi-weekly Wed keyword ranking check (not yet due)
    82|- Awaiting new growth research assignments from Moxie
