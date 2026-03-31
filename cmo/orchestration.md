     1|# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
     2|# Last updated: 2026-03-31T07:12:00Z
     3|# 
     4|# HOW THIS WORKS:
     5|# Every cron job reads this file for context. When done, it updates relevant sections.
     6|# Moxie (CMO) reviews this file and decides next actions.
     7|# No manual prompt updates needed — agents read state from here.
     8|# 
     9|# SYSTEM IMPROVEMENTS (v2):
    10|# - Atomic state updates: workers write to tmp files first, then rename
    11|# - Retry logic: failed tasks get marked RETRY(1/3) before escalation
    12|# - Task prioritization: P0 (blockers), P1 (revenue), P2 (growth), P3 (ops)
    13|# - KPI tracking: every task completion updates KPI progress metrics
    14|# - Cron collision mitigation: workers staggered across the hour (no longer all at :05)
    15|# - Model stability: worker crons pinned to Codex-compatible models (avoid max_retries_exhausted from provider/model mismatch)
    16|
    17|---
    18|
    19|## Mission
    20|- Company: Sapiens Technology LLC (SapiensTech)
    21|- Goal: grow a portfolio of indie products to consistent revenue via repeatable acquisition + conversion systems
    22|
    23|## Active Product (current sprint)
    24|- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
    25|- Target: English-speaking SMBs, agencies, freelance devs
    26|- 30-day goals: 10 paid users, $100 MRR, more organic traffic
    27|- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
    28|- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory
    29|
    30|---
    31|
    32|## Known Blockers
    33|| Blocker | Owner | Status | Action Needed |
    34||---------|-------|--------|---------------|
    35|| Codex 5-hour limit hit | System | RESOLVED | Premium window available now (reset completed) |
    36|| WordPress plugin pending review changes | Forge + Rishi | BLOCKED | Forge audit complete; Rishi to apply suggested changes + resubmit (see /root/moxie/products/formbeep/wp-plugin-fixes.md) |
    37|| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
    38|| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked “worker not configured” | Moxie | IN_PROGRESS | Fixed cron providers to OpenRouter where needed; unblocked queue rows from BLOCKED→QUEUED; verify next run produces outputs and governance promotes safely |
    39|| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
    40|---
    41|
    42|## Employee State
    43|
    44|### Vale — Competitor Intelligence Lead
    45|- SOUL: /root/moxie/cmo/employees/vale-soul.md
    46|- Output dir: /root/moxie/products/formbeep/
    47|- Status: IN_PROGRESS
    48|- Current task: Monthly competitor monitoring (pricing changes, new features, blog posts) + founder Reddit signal scan (which subs + what angles worked) — **IN_PROGRESS**
    49|- Last output: /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
    50|- Output (this task): /root/moxie/products/formbeep/competitor-monitoring.md
    51|- Next task after completion: Quarterly competitor positioning refresh (pricing page screenshots + feature diff + “what changed”) 
    52|- Blockers: Reddit founder profile analysis may be blocked by Reddit network policy in this environment; attempt via public endpoints; if blocked, require login/dev token
    53|- Competitor founder intel:
    54|  - Beepmate: u/adambengur
    55|  - Web2Phone: u/ConferenceOnly1415
    56|  - Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n
    57|
    58|### Astra — Growth Research Lead
    59|- SOUL: /root/moxie/cmo/employees/astra-soul.md
    60|- Output dir: /root/moxie/products/formbeep/
    61|- Status: IN_PROGRESS
    62|- Current task: Tally Forms growth teardown (channels, SEO/templates, PLG loops, distribution) + what we can copy for FormBeep
    63|- Inputs: /root/moxie/products/formbeep/keyword-briefing.md + /root/moxie/products/formbeep/analytics-report.md
    64|- Output: /root/moxie/products/formbeep/tally-growth-teardown.md
    65|- Next task after completion: Keyword v2 expansion (top-50 prioritized with intent/difficulty)
    66|- Blockers: None
    67|
    68|### Kiro — Conversion Copy Lead
    69|- SOUL: /root/moxie/cmo/employees/kiro-soul.md
    70|- Output dir: /root/moxie/products/formbeep/copy/
    71|- Status: COMPLETED
    72|- Current task: 2 blog posts from Astra's keyword list — **COMPLETED**
    73|- Last output: /root/moxie/products/formbeep/copy/blog-posts-v1.md
    74|- Next task after completion: Draft 2–3 platform “money pages” (WordPress form → WhatsApp, Webflow form → WhatsApp, Framer form notifications) and one comparison page (FormBeep vs Web2Phone)
    75|- Blockers: None
    76|
    77|### Ember — Outreach & Distribution Lead
    78|- SOUL: /root/moxie/cmo/employees/ember-soul.md
    79|- Output dir: /root/moxie/products/formbeep/outreach/
    80|- Status: IN_PROGRESS
    81|- Current task: Reddit campaign launch plan (calendar + posting SOP + partnerships tie-in + ideal posting day/time based on active userbase)
    82|- Next task after completion: Community posting schedule, partnership outreach list
    83|- Blockers: None
    84|
    85|### Forge — Product/Codebase Inspector
    86|- SOUL: /root/moxie/cmo/employees/forge-soul.md
    87|- Output dir: /root/moxie/products/formbeep/
    88|- Status: COMPLETED
    89|- Current task: Technical SEO audit (page speed, structured data, meta tags) — **COMPLETED**
    90|- Last output: /root/moxie/products/formbeep/technical-seo-audit.md
    91|- Next task: (if approved) implement SEO fixes in Hugo templates: image optimization pipeline + taxonomy noindex + keywords delimiter
    92|- Blockers: None for audit. WP plugin still awaiting Rishi to implement/apply suggested changes + resubmit on WP.org (see /root/moxie/products/formbeep/wp-plugin-fixes.md)
    93|
    94|### Mira — Analytics & Reporting Lead
    95|- SOUL: /root/moxie/cmo/employees/mira-soul.md
    96|- Output dir: /root/moxie/products/formbeep/
    97|- Status: IN_PROGRESS
    98|- Current task: Traffic vs keyword opportunity map (use Umami + Astra keyword briefing)
    99|- Last output: /root/moxie/products/formbeep/analytics-report.md
   100|- Umami: cloud.umami.is, website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d
   101|- Next task after completion: Set up weekly automated KPI report cron
   102|- Blockers: None
   103|- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv
   104|
   105|### Nova — Paid Acquisition Lead
   106|- SOUL: /root/moxie/cmo/employees/nova-soul.md
   107|- Output dir: /root/moxie/cmo/sops/
   108|- Status: COMPLETED
   109|- Current task: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) — **COMPLETED**
   110|- Last output: /root/moxie/cmo/sops/paid-ads-sop.md
   111|- Next task after completion: Formalize campaign naming + UTM taxonomy in configs/templates + ship first tracked campaign for FormBeep (Google Search BOF)
   112|- Blockers: None
   113|
   114|### Jax — SaaS Growth Operations Lead
   115|- SOUL: /root/moxie/cmo/employees/jax-soul.md
   116|- Output dir: /root/moxie/products/formbeep/
   117|- Status: COMPLETED
   118|- Current task: 40+ SaaS directory master list — **COMPLETED**
   119|- Last output: /root/moxie/products/formbeep/directory-submissions.md
   120|- Next task after completion: Prepare P1 directory submission assets (logos, banners, screenshots, copy) from the GitHub repo, then begin submissions (ProductHunt, AlternativeTo, BetaList, SaaSHub)
   121|- Blockers: None
   122|- If directory submissions need founder credentials/email verification: note in this file and flag for Rishi
   123|
   124|### Rumi — Blog & Content Analyst
   125|- SOUL: /root/moxie/cmo/employees/rumi-soul.md
   126|- Output dir: /root/moxie/products/formbeep/
   127|- Status: COMPLETED
   128|- Current task: Competitor blog analysis + 30-day content calendar — **COMPLETED**
   129|- Keyword seed: /root/moxie/products/formbeep/seo-keywords.md
   130|- Next task after completion: Weekly content gap scan (what new topics emerged, what's trending)
   131|- Blockers: None
   132|
   133|---
   134|
   135|## Active Crons (System-managed, DO NOT EDIT manually)
   136|| Cron ID | Name | Schedule | Employee | Last Run | Status |
   137||---------|------|----------|----------|----------|--------|
   138|| ae770f4f9ff8 | formbeep-hourly-heartbeat | every 60m | Moxie | See logs | OK |
   139|| aba07be535ec | formbeep-daily-traffic-check | 0 10 * * * | Mira | Not yet fired | SCHED |
   140|| 513b777e84ea | formbeep-search-check | 0 10 * * 1,4 | Astra/Mira | Not yet fired | SCHED |
   141|| 753d42f32fbb | formbeep-weekly-growth-review | 0 11 * * 1 | Moxie/Mira | Not yet fired | SCHED |
   142|| 1e17a419b9e4 | codex-5hr-resume-premium | 03:30 GST daily | Moxie | Pending | SCHED |
   143|| ca6591a837b7 | codex-weekly-resume-premium | 2026-04-06 17:30 GST | Moxie | Pending | SCHED |
   144|| f63bfbc548a6 | vale-competitor-deepdive | one-shot | Vale | Running | ACTIVE |
   145|| c35598f90ddf | astra-wordpress-market | one-shot | Astra | Running | ACTIVE |
   146|| 98f011592fdc | jax-saas-directory-list | one-shot | Jax | Pending | SCHED |
   147|| a230996e123a | rumi-content-analysis | one-shot | Rumi | Pending | SCHED |
   148|| e3d998d1f127 | mira-umami-audit | one-shot | Mira | Pending | SCHED |
   149|| 069296011969 | ember-reddit-research | one-shot | Ember | Pending | SCHED |
   150|| 97eacc1cb3fa | codex-online-check | every 30m x12 | Moxie | Pending | SCHED |
   151|
   152|---
   153|
   154|## Completed Deliverables
   155|| Date | Employee | File | Status |
   156||------|----------|------|--------|
   157|| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
   158|| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
| 2026-03-31 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED |
   159|| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
   160|| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
   161|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
   162|| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
   163|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
   164|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
   165|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
   166|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |
| 2026-03-31 | Luna | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md | COMPLETED |
   167|
   168|---
   169|
   170|## Rishi Action Items (Requires Human)
   171|1. WordPress plugin resubmission — apply Forge’s fix list and resubmit (see /root/moxie/products/formbeep/wp-plugin-fixes.md)
   172|2. Review/approve Forge’s WP plugin patch notes/package when ready
   173|3. Directory submissions — inbox confirmed as hello@formbeep.com; share any existing directory accounts (for Jax)
   174|4. Review/approve Kiro’s 2 blog drafts for publishing: /root/moxie/products/formbeep/copy/blog-posts-v1.md
   175|5. (Ops) If HQ pushes are needed: confirm MOXIE_GITHUB_WRITE_PAT in /opt/data/.env has write access to rishikeshsreehari/moxie
   176|
   177|---
   178|
   179|## Note it down and see if it's unnecessary:
   180|- Hourly crons may burn too many free model tokens. Plan to reduce to every 2h or 4h if quota gets tight. Governance cron will check token usage and adjust if needed.
   181|- If workers report "no pending tasks" for 3+ consecutive cycles, pause their cron to save tokens.
   182|- Monitor daily token usage across all workers. If we hit free model limits, stagger workers so only 2 fire per hour.
   183|- Worker SOULs are company-framed and must read product assignments from orchestration.md before each cycle.
   184|
   185|## Codex Deep Audit (ONE-SHOT)
   186|- Cron ID: 1e17a419b9e4 (codex-5hr-resume-premium)
   187|- Fires: once at 2026-03-31 03:30 GST
   188|- This is a ONE-TIME task. It does NOT repeat. After firing, the system continues with the hourly worker schedule below.
   189|- Audit output: /root/moxie/cmo/orchestration-audit.md
   190|
   191|## Product Assignments (Multi-product ready)
   192|| Product | Status | Priority | Assigned Employees |
   193||---------|--------|----------|-------------------|
   194|| FormBeep | Active (Sprint 1) | P0 | All employees |
   195|| Product 2 | Not yet launched | N/A | TBD |
   196|| Product 3 | Not yet launched | N/A | TBD |
   197|
   198|**How this works:** When a second product is added, update this table. Workers read orchestration.md, see which products are active, and allocate their time accordingly. By default, all effort goes to the currently active product(s); FormBeep is just the current sprint.
   199|
   200|**Employee flexibility:** All employees are designed to be product-agnostic. Their SOUL files define their role (research, outreach, analytics, etc.) — not the product. The product assignments above determine where they focus their effort each cycle. Workers should read this table before each cycle to know which product(s) to work on.
   201|