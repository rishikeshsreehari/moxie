     1|# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
     2|# Last updated: 2026-04-02T12:40:00Z
     3|     3|     3|# 
     4|     4|     4|# HOW THIS WORKS:
     5|     5|     5|# Every cron job reads this file for context. When done, it updates relevant sections.
     6|     6|     6|# Moxie (CMO) reviews this file and decides next actions.
     7|     7|     7|# No manual prompt updates needed — agents read state from here.
     8|     8|     8|# 
     9|     9|     9|# SYSTEM IMPROVEMENTS (v2):
    10|    10|    10|# - Atomic state updates: workers write to tmp files first, then rename
    11|    11|    11|# - Retry logic: failed tasks get marked RETRY(1/3) before escalation
    12|    12|    12|# - Task prioritization: P0 (blockers), P1 (revenue), P2 (growth), P3 (ops)
    13|    13|    13|# - KPI tracking: every task completion updates KPI progress metrics
    14|    14|    14|# - Cron collision mitigation: workers staggered across the hour (no longer all at :05)
    15|    15|    15|# - Model stability: worker crons pinned to Codex-compatible models (avoid max_retries_exhausted from provider/model mismatch)
    16|    16|    16|#
    17|    17|    17|# DELEGATION SYSTEM (HQ, product-agnostic):
    18|    18|    18|# - "Do not run tooling during live chat; queue work orders instead." Append to: /root/moxie_hq/cmo/delegation-queue.md
    19|    19|    19|# - During ops cycle (or by the orchestration reconciler when appropriate), run:
    20|    20|    20|#     python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py
    21|    21|    21|#     python3 /root/moxie_hq/cmo/scripts/process_artifacts.py
    22|    22|    22|# - These processors ONLY edit HQ files under /root/moxie_hq/cmo and do not require new cron scheduling.
    23|    23|    23|
    24|    24|    24|---
    25|    25|    25|
    26|    26|    26|## Mission
    27|    27|    27|- Company: Sapiens Technology LLC (SapiensTech)
    28|    28|    28|- Goal: grow a portfolio of indie products to consistent revenue via repeatable acquisition + conversion systems
    29|    29|    29|
    30|    30|    30|## Active Product (current sprint)
    31|    31|    31|- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
    32|    32|    32|- Target: English-speaking SMBs, agencies, freelance devs
    33|    33|    33|- 30-day goals: 10 paid users, $100 MRR, more organic traffic
    34|    34|    34|- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
    35|    35|    35|- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory
    36|    36|    36|
    37|    37|    37|---
    38|    38|    38|
    39|    39|    39|## Known Blockers
    40|    40|    40|| Blocker | Owner | Status | Action Needed |
    41|    41|    41||---------|-------|--------|---------------|
    42|    42|    42|| Codex 5-hour limit hit | System | RESOLVED | Premium window available now (reset completed) |
    43|    43|    43|| WordPress plugin resubmission (WP.org) | Rishi | BLOCKED (Founder-owned) | Do not touch/iterate in automation. Rishi will implement + resubmit. After approval, execute post-approval launch plan. |
    44|    44|    44|| Directory submissions (P1) require founder credentials/verification | Jax + Rishi | BLOCKED | Provide any existing directory accounts / inbox verification access for hello@formbeep.com (see issues_rishi.md) |
    45|    45|    45|| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
    46|    46|    46|| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked "worker not configured" | Moxie | RESOLVED | Fixed cron providers to OpenRouter where needed; all workers producing outputs; Pax first task COMPLETED |
    47|    47|    47|| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
    48|    48|    48|| Hermes config backup | Moxie | COMPLETED | Config backed up to /root/moxie_hq/infrastructure/hermes/ |
    49|    49|    49|---
    50|    50|    50|
    51|    51|    51|## Employee State
    52|    52|
    53|    53|NOTE: All employees are SapiensTech (HQ) employees (role-based, product-agnostic). The current sprint focus is FormBeep, so most tasks route there, but no one is “hired for a product”.
    54|    54|    52|
    55|    55|    53|### Vale — Competitor Intelligence Lead
    56|    56|    54|- SOUL: /root/moxie/cmo/employees/vale-soul.md
    57|    57|    55|- Current output dir (sprint): /root/moxie/products/formbeep/
    58|    58|- Status: COMPLETED
    59|    59|- Current task: (StackStats) Reddit scanning plan — **COMPLETED** (2026-04-02T10:00Z)
    60|    60|- Last output: /root/moxie/products/stackstats/outreach/reddit-scan-plan.md
    61|    61|- Source intel artifact: /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md (generated 2026-04-01)
    62|    62|- Blockers: None for analysis. Note: Reddit execution still needs credentials (see issues_rishi.md)
    63|    63|- Founder activity (from new intel): Beepmate u/adambengur (2 posts, 25 comments) and Web2Phone u/ConferenceOnly1415 (25 posts, 25 comments)
    64|    64|- Key April findings: WPForms native WA (Mar 5), Getform WA live + SMS Q2 roadmap, WANotifier commerce integrations, 4 new direct competitors detected (FormToWA, SendForm.io, PingForms, NotifyStack)
    65|    65|- Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n, FormToWA, SendForm.io, PingForms, NotifyStack
    66|    66|- Idle-cycle deliverable: /root/moxie/products/formbeep/pricing-war-room-april-2026.md — Pricing decision analysis ($4 vs $4.99), feature gap matrix, recommend hold price + lean into SMS moat
    67|### Astra — Growth Research Lead
    68|- SOUL: /root/moxie/cmo/employees/astra-soul.md
    69|- Current output dir (sprint): /root/moxie/products/formbeep/
    70|- Status: IDLE / COMPLETED
    71|- Last completed task: (FormBeep) Run DataForSEO SERP sampling for keyword discovery — **COMPLETED** (2026-04-02T12:15Z)
    72|- Output: /root/moxie/products/formbeep/seo/serp-opportunity-brief.md
    73|- Previous: (StackStats) SERP brief — COMPLETED (2026-04-02T12:00Z)
    74|- Previous: (FormBeep) SERP demand probe + keyword roadmap — COMPLETED (2026-04-02T07:00Z)
    75|- Next task after completion: Ready for next assignment — SERP briefs shipped for both products; Rumi's 6-page outlines for both products are done
    76|- Blockers: None
    77|    79|### Kiro — Conversion Copy Lead
    78|    80||- SOUL: /root/moxie/cmo/employees/kiro-soul.md
    79|    81||- Current output dir (sprint): /root/moxie/products/formbeep/copy/
    80|    82||- Status: COMPLETED
    81|    83||- Current task: REWORK 2 blog posts per founder feedback (length + factual fixes + Zapier/WhatsApp research + comparison table + thumbnail prompts) — **COMPLETED** (2026-04-01T22:45Z)
    82|    84||- Last output:
    83|    85|  - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md (~1,650 words, slug: whatsapp-without-zapier)
    84|    86|  - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md (~1,720 words, slug: formbeep-vs-zapier)
    85|    87||- Deliverables: Both posts expanded to target length, factual fixes applied (hello@formbeep.com, 15 submissions/month), frontmatter updated (slug + thumb_prompt), Zapier→WhatsApp API requirements research incorporated, comparison table added to vs post
    86|    88||- Blockers: None
    87|    89|    84|
    88|    90|    85|### Ember — Outreach & Distribution Lead
    89|    91|    86|- SOUL: /root/moxie/cmo/employees/ember-soul.md
    90|    92|    87|- Current output dir (sprint): /root/moxie/products/formbeep/outreach/
    91|    93|    88|- Status: COMPLETED (execution blocked on creds)
    92|    94|    89|- Current task: Manual Reddit posting plan (Non-US/GST focus) + subreddit rules checklist + posting windows + verification steps — **COMPLETED** (2026-04-01T17:32Z)
    93|    95|- Last output: /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md (2026-04-02 — full rules table + activity log + quick-ref)
    94|    96|- Previous outputs: reddit-manual-posting-plan-gst-nonus-v1.md (2026-04-01), reddit-post-comment-scripts.md (2026-04-01), reddit-campaign-plan.md (2026-03-31), reddit-strategy.md (2026-03-31)
    95|    97|    92|- Completed deliverables: reddit-strategy.md, reddit-campaign-plan.md, reddit-post-comment-scripts.md, manual-posting-plan-gst-nonus-v1.md
    96|    98|    93|- Next task after completion: Execute Week 1 posting — **BLOCKED** on Reddit account credentials (see issues_rishi.md)
    97|    99|    94|- Blockers: Reddit account credentials required for all posting execution (see issues_rishi.md)
    98|   100|    95|
    99|### Forge — Full Stack Engineer
   100|- SOUL: /root/moxie/cmo/employees/forge-soul.md
   101|- Current output dir (sprint): /root/moxie/products/formbeep/
   102|- Status: COMPLETED
   103|- Current task: (FormBeep) Repo audit for Umami event tracking — **COMPLETED** (2026-04-02T03:37Z)
   104|- Task ID: forge-20260402_001211-30bb2a
   105|- Output path: /root/moxie_hq/products/formbeep/dev-notes/tracking-implementation-notes.md
   106|- Last completed task: (FormBeep) Repo audit, identified all CTAs, proposed Umami event tracking + UTM hygiene — **COMPLETED** (2026-04-02T03:37Z)
   107|- Last output: /root/moxie_hq/products/formbeep/dev-notes/tracking-implementation-notes.md
   108|- Key findings: 6 existing tracked CTAs identified, 3 recommended additions, UTM hygiene standards documented
   109|- Blockers: None
   110|   112|   105|
   111|   113|### Mira — Analytics & Reporting Lead
   112|   114|- SOUL: /root/moxie/cmo/employees/mira-soul.md
   113|   115|- Current output dir (sprint): /root/moxie/products/stackstats/
   114|   116|- Status: IN_PROGRESS
   115|   117|- Current task: (StackStats) Pull Umami Cloud analytics for StackStats (website_id 52a19925-9bf4-4efe-9a42-ecc2a7f08d81): last 7d + last 30d. Include top sources, top pages, geo split, and any events — **IN_PROGRESS** (promoted 2026-04-02T00:06Z)
   116|   118|- Task ID: mira-20260401_233129-5c8b35
   117|   119|- Output path: /root/moxie/products/stackstats/analytics/umami-summary.md
   118|   120|- Umami: cloud.umami.is, website ID: 52a19925-9bf4-4efe-9a42-ecc2a7f08d81
   119|   121|- Last output: /root/moxie/products/formbeep/traffic-vs-keywords.md
   120|   122|- Next task after completion: Continue analytics support for StackStats growth plan
   121|   123|- Blockers: None
   122|   124|- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv
   123|   125|   116|
   124|   126|   117|### Nova — Paid Acquisition Lead
   125|   127|   118|- SOUL: /root/moxie/cmo/employees/nova-soul.md
   126|   128|   119|- Current output dir (sprint): /root/moxie/cmo/sops/
   127|   129|   120|- Status: COMPLETED
   128|   130|   121|- Current task: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) — **COMPLETED**
   129|   131|   122|- Last output: /root/moxie/cmo/sops/paid-ads-sop.md
   130|   132|   123|- Next task after completion: Formalize campaign naming + UTM taxonomy in configs/templates + ship first tracked campaign for FormBeep (Google Search BOF)
   131|   133|   124|- Blockers: None
   132|   134|   125|
   133|### Jax — SaaS Growth Operations Lead
   134|   135|   136|- SOUL: /root/moxie/cmo/employees/jax-soul.md
   135|   137|   137|- Current output dir (sprint): /root/moxie/products/formbeep/
   136|   138|   138|- Status: IDLE (BLOCKED: awaiting founder credentials for directory submission execution — hello@formbeep.com inbox verification + existing directory accounts)
   137|   139|   139|- Current task: (FormBeep) Replace failed directory picks with 2 actionable directories (verified requirements + submission bundles) — COMPLETED (2026-04-02T02:00Z)
   138|   140|   140|- Task ID: jax-20260401_223121-f3bb3a
   139|   141|   141|- Output path: /root/moxie/products/formbeep/distribution/directory-submissions-today-pick.md
   140|   142|   142|- Blockers: None
   141|   143|   134|
   142|### Rumi — Blog & Content Analyst
   143|- SOUL: /root/moxie/cmo/employees/rumi-soul.md
   144|- Current output dir (sprint): /root/moxie/products/formbeep/
   145|- Status: COMPLETED
   146|- Current task: (HQ) X content OS (like Reddit tracker): build local script to infer founder tone from X export + analyze what worked; output a daily plan that includes 1 original post + "reply guy" mode (10 replies/day). — **COMPLETED** (2026-04-02T09:04Z)
   147|- Task ID: rumi-20260402_083000-x1e9c
   148|- Output path: /root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md
   149|- Last completed task: (HQ) Platform×product posting matrix — **COMPLETED** (2026-04-02T03:15Z)
   150|- Output: /root/moxie_hq/cmo/strategy/channel-matrix-all-products.md
   151|- Previous completed task: (StackStats) 6 SEO landing page outlines — **COMPLETED** (2026-04-02T03:27Z)
   152|- Output: /root/moxie/products/stackstats/seo/page-outlines.md
   153|- Next task after completion: Await next assigned task
   154|- Blockers: None
   155|   154|   144|
   156|   155|   145|### Pax — Partnerships / BD Lead
   157|   156|   146|- SOUL: /root/moxie/cmo/employees/pax-soul.md
   158|   157|   147|- Current output dir (sprint): /root/moxie/products/formbeep/partnerships/
   159|   158|   148|- Status: COMPLETED
   160|   159|   149|- Current task: Week 3 submissions (Carrd + Typedream integration packages + agency outreach to top 15 targets) — **COMPLETED**
   161|   160|   150|- Last output: /root/moxie/products/formbeep/partnerships/platform-applications-week3.md
   162|   161|   151|- Next task after completion: Send agency outreach emails once verified contact info obtained; publish formbeep.com/integrations reciprocal directory; follow up on Week 1-2 platform application reviews
   163|   162|   152|- Blockers: Portal credentials (Webflow/Framer/Glide/Softr), Reddit account for community posts, verified agency email contacts, hello@formbeep.com access for sending
   164|   163|   153|
   165|   164|### Luna — Lifecycle / CRM Lead
   166|   165||- SOUL: /root/moxie/cmo/employees/luna-soul.md
   167|   166||- Current output dir (sprint): /root/moxie/products/formbeep/lifecycle/
   168|   167||- Status: COMPLETED
   169|   168||- Current task: Win-back email sequence for churned users — **COMPLETED** (2026-04-02T08:52Z)
   170|   169||- Last output: /root/moxie/products/formbeep/lifecycle/win-back-emails.md
   171|   170||- Previous output: /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
   172|   171||- Next task after completion: Continue lifecycle optimization (retention triggers, segmentation)
   173|   172||- Blockers: None
   174|   173|   162|
   175|   174|### Orion — Outbound Lead (Cold Email)
   176|   175||- SOUL: /root/moxie/cmo/employees/orion-soul.md
   177|   176||- Current output dir (sprint): /root/moxie/products/formbeep/outbound/
   178|   177||- Status: COMPLETED
   179|   178||- Current task: Prospect list refresh from competitor intel — **COMPLETED** (2026-04-02T08:15Z)
   180|   179||- Last output: /root/moxie/products/formbeep/outbound/prospect-refresh.md
   181|   180||- Previous output: /root/moxie/products/formbeep/outbound/outbound-pack.md
   182|   181||- Next task after completion: Continue outbound optimization (subject tests, sequence refinement)
   183|   182||- Blockers: Sending infrastructure (email warmup/domain setup) required for actual outreach execution
   184|   183|   171|
   185|   184|### Iris — Repo Copy Auditor
   186|   185|- SOUL: /root/moxie/cmo/employees/iris-soul.md
   187|   186|- Current output dir (sprint): /root/moxie_hq/products/formbeep/dev-notes/
   188|   187|- Status: IN_PROGRESS
   189|   188|- Current task: (FormBeep) Inspect the ACTUAL current landing page content in the repo (headlines, breadcrumbs, free-tier claims) and deliver 10 exact copy/UX improvements with file+section pointers — **IN_PROGRESS** (promoted 2026-04-02T00:06Z)
   190|   189|- Task ID: iris-20260401_224900-eab63b
   191|   190|- Output path: /root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md
   192|   191|- Last output: N/A (first run)
   193|   192|- Next task after completion: Weekly copy/UX audit of landing + docs content
   194|   193|- Blockers: None
   195|   194|   180|
   196|   195|   181|
### Moxie — CMO / Orchestrator
- SOUL: /root/moxie_hq/SOUL.md
- Current output dir (sprint): /root/moxie_hq/cmo/
- Status: COMPLETED (all P0 tasks done; awaiting next assignments)
- Current task: (FormBeep) Postmortem: detailed failure analysis — **COMPLETED** (2026-04-02T15:33Z)
- Previous: (HQ) Create all-products Founder Voice / Build-in-Public strategy — **COMPLETED** (2026-04-02T11:00Z)
- Last output: /root/moxie_hq/cmo/postmortems/2026-04-01-formbeep-failures.md
- Next task: Deep CMO self-review (queued in dispatch-queue.md) — **READY TO START**
- Blockers: None
206|     206|---
207|     207|   182|
208|     208|   183|### Forge — Full Stack Engineer (additional task)
- Current task: (*) Review analytics report and update growth metrics — **COMPLETED** (completed 2026-04-02T12:40Z)
- Output path: /root/moxie_hq/cmo/analytics/review-{artifact_relpath}.md
- Blockers: None
   206|   205|---
   207|   206|   182|
   208|   207|   183|## Active Crons (Source of truth: `hermes cron list`)
   209|
   210|**Editing rule:** do not edit jobs via this table. Update jobs using `hermes cron edit <cron_id> ...` and then reconcile this table to match.
   211|
   212|Last verified: 2026-04-02T16:23:33Z
   213|
   214|||| Cron ID | Name | Schedule | Deliver | Next run (UTC) | Repeats | State |||---|---|---|---|---|---|---|
   215||| 6effbb32 | formbeep-daily-user-count-checkin | every 1440m | local | 2026-04-02T14:06:30+00:00 | ∞ | active |
   216||| aba07be5 | formbeep-daily-traffic-check | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | ∞ | active |
   217||| 513b777e | formbeep-search-check | 0 10 * * 1,4 | local | 2026-04-02T10:00:00+00:00 | ∞ | active |
   218||| 753d42f3 | formbeep-weekly-growth-review | 0 11 * * 1 | local | 2026-04-06T11:00:00+00:00 | ∞ | active |
   219||| ae770f4f | formbeep-hourly-heartbeat | 6 * * * * | local | 2026-04-02T05:06:00+00:00 | ∞ | active |
   220||| 52af5ec9 | codex-dashboard-update-checkin | every 720m | local | 2026-04-02T14:43:36+00:00 | ∞ | active |
   221||| b0492991 | moxie-memory-skill-audit | every 720m | local | 2026-04-02T07:30:09+00:00 | ∞ | active |
   222||| ca6591a8 | codex-weekly-resume-premium | once at 2026-04-06 17:30 | local | 2026-04-06T17:30:00+04:00 | 0/1 | active |
   223||| 0526cbc1 | weekly-free-models-reminder | 0 17 * * 2 | local | 2026-04-07T17:00:00+00:00 | ∞ | active |
   224||| 647387ae | mira-daily-kpi | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | 10/100 | active |
   225||| a468835d | vale-monthly-competitor-scan | 0 10 1 * * | local | 2026-05-01T10:00:00+00:00 | 1/100 | active |
   226||| 2553a683 | moxie-daily-governance | 0 * * * * | local | 2026-04-02T11:00:00+00:00 | 61/100 | active |
   227||| 8bcfe505 | vale-worker | 12 * * * * | local | 2026-04-02T13:12:00+00:00 | 63/100 | active |
   228||| 7067633e | astra-worker | 17 * * * * | local | 2026-04-02T13:17:00+00:00 | 64/100 | active |
   229||| 3171d2c2 | kiro-worker | 42 * * * * | local | 2026-04-02T12:42:00+00:00 | 61/100 | active |
   230||| eb803b7d | ember-worker | 32 * * * * | local | 2026-04-02T13:32:00+00:00 | 61/100 | active |
   231||| 401e59cc | forge-worker | 37 * * * * | local | 2026-04-02T12:37:00+00:00 | 62/100 | active |
   232||| 4bdcef11 | jax-worker | 22 * * * * | local | 2026-04-02T13:22:00+00:00 | 61/100 | active |
   233||| affd389a | rumi-worker | 27 * * * * | local | 2026-04-02T12:27:00+00:00 | 62/100 | active |
   234||| af7f3c07 | moxie-daily-self-improvement | 0 20 * * * | local | 2026-04-02T20:00:00+00:00 | 2/100 | active |
   235||| 91520aa6 | nova-worker | 47 * * * * | local | 2026-04-02T13:47:00+00:00 | 60/100 | active |
   236||| 5b9c6eb7 | issues-rishi-watch | every 240m | local | 2026-04-02T12:46:52+00:00 | 15/200 | active |
   237||| 3e93c4f5 | luna-worker | 52 * * * * | local | 2026-04-02T13:52:00+00:00 | 62/100 | active |
   238||| cf1a8f9e | pax-worker | 57 * * * * | local | 2026-04-02T13:57:00+00:00 | 60/100 | active |
   239||| b0e9c513 | iris-weekly-formbeep-repo-copy-audit | 30 9 * * 1 | local | 2026-04-06T09:30:00+00:00 | 0/200 | active |
   240||| 0ed491f6 | orion-worker | 2 * * * * | local | 2026-04-02T13:02:00+00:00 | 62/200 | active |
   241||| 868bd30f | moxie-hq-autocommit-push | every 30m | local | 2026-04-02T10:42:51+00:00 | ∞ | active |
   242||| 1c008e06 | moxie-orchestration-reconciler | 13 * * * * | local | 2026-04-02T13:13:00+00:00 | 52/100 | active |
   243||| c342e174 | opencode-go-weekly-limit-reset-reminder | 26 13 * * 1 | local | 2026-04-06T13:26:00+00:00 | ∞ | active |
   244|||| 7af300e6 | cmo-delegation-queue-runner | */15 * * * * | local | 2026-04-02T04:15:00+00:00 | ∞ | active |
   246|
**Retired/Removed jobs** (no longer in live registry):
- `01471699` cmo-deep-audit-5-4-2026-04-02 — one-shot deep audit job, completed/retired
- `97eacc1cb3fa` codex-online-check — one-shot job, completed
- `6b5fe0d2220c` cmo-dispatch-orchestrator — removed from registry
- `415e88f0` wp-plugin-rishi-reminder — removed from registry
- `904c65910bfe` moxie-forward-reports-to-telegram — removed from registry
   252|   251|   227|
   253|   252|   228|---
   254|   253|   229|
   255|   254|   230|## Completed Deliverables
   256|   255|   231|| Date | Employee | File | Status |
   257|   256|   232||------|----------|------|--------|
   258|   257|   233|| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
   259|   258|   234|| 2026-03-31 | Mira | /root/moxie/products/formbeep/traffic-vs-keywords.md | COMPLETED |
   260|   259|   235|| 2026-03-31 | Orion | /root/moxie/products/formbeep/outbound/outbound-pack.md | COMPLETED |
   261|   260|   236|| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
   262|   261|   237|| 2026-03-31 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED |
   263|   262|   238|| 2026-04-01 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED — Monthly competitor scan (WPForms WA live, Getform WA+SMS roadmap, 4 new entrants) |
   264|   263|   239|| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
   265|   264|   240|| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
   266|   265|   241|| 2026-03-31 | Ember | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md | COMPLETED |
   267|   266|   242|| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-post-comment-scripts.md | COMPLETED |
   268|   267|   243|| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-manual-posting-plan-gst-nonus-v1.md | COMPLETED |
   269|   268||| 2026-04-02 | Ember | /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md | COMPLETED — Full subreddit rules table (28 subs) + activity log + quick-ref + posting guardrails |
   270|   269|   244|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
   271||| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions-p1.md | COMPLETED (P1 submission pack ready; execution awaits credentials) |
   272||| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
   273||| 2026-04-02 | Rumi | /root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md | COMPLETED — fallback corpus tone fingerprint + daily reply-guy workflow + reply log format |
   274||| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
   275|   273|   248|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
   276|   274|   249|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
   277|   275|   250|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |
   278|   276|   251||| 2026-03-31 | Luna | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md | COMPLETED |
   279|   277|   252||| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md | COMPLETED
   280|   278|   253||| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/platform-partner-outreach.md | COMPLETED
   281|   279|   254||| 2026-04-01 | Pax | /root/moxie/products/formbeep/partnerships/platform-applications-week3.md | COMPLETED
   282|   280|||| 2026-04-02 | Luna | /root/moxie/products/formbeep/lifecycle/win-back-emails.md | COMPLETED — 3-email win-back sequence (Day 1/3/7) + pre-churn triggers + segmentation matrix + behavioral onboarding handoff
   283|   281|   255|
   284|   282|   256|---
   285|   283|   257|
   286|   284|## Rishi Action Items (Requires Human)
   287|   285|1. WordPress plugin resubmission (founder-owned) — implement fixes + resubmit when you're ready (see /root/moxie/products/formbeep/wp-plugin-fixes.md)
   288|   286|2. After approval: execute post-approval WP launch plan (I'll keep it ready on disk)
   289|   287|3. Directory submissions — inbox confirmed as hello@formbeep.com; share any existing directory accounts (for Jax)
   290|   288|4. **REWORK REQUESTED** Kiro blog posts (do not publish yet):
   291|   289|   - Drafts:
   292|   290|     - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md
   293|   291|     - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md
   294|   292|   - Required fixes:
   295|   293|     - Make them longer / more rankable (~1200–1800 words)
   296|   294|     - Correct: contact email = hello@formbeep.com
   297|   295|     - Correct: free tier = 15 submissions/month
   298|   296|     - Set slugs: whatsapp-without-zapier/ and formbeep-vs-zapier/
   299|   297|     - Research Zapier→WhatsApp reality (out-of-the-box vs needs WhatsApp Business API provider like Twilio/360dialog/Meta Cloud API)
   300|   298|     - Add a comparison table in the “vs Zapier” post
   301|   299|     - Add `thumb_prompt:` frontmatter to each post (thumbnail generation prompt text)
   302|   300|5. (Ops) If HQ pushes are needed: confirm MOXIE_GITHUB_WRITE_PAT in /opt/data/.env has write access to rishikeshsreehari/moxie
   303|   301|   267|
   304|   302|   268|---
   305|   303|   269|
   306|   304|   270|## Rubric & Scoring System (NEW — Auto-wired)
   307|   305|   271|**Every completed task is automatically scored against the Employee Rubric.**
   308|   306|   272|
   309|   307|   273|### How it works:
   310|   308|   274|1. Task completes → Employee updates orchestration.md
   311|   309|   275|2. `task-scorer.py` auto-runs: scores 7 dimensions (1-5), weighted overall
   312|   310|   276|3. Scorecard saved to: `/root/moxie_hq/cmo/scores/{employee}/{task_id}.md`
   313|   311|   277|4. SOUL.md auto-updated with: Recent Scores table + Current Improvement Focus
   314|   312|   278|5. "Dreaming" reflection triggered: employee reflects on what worked/didn't
   315|   313|   279|
   316|   314|   280|### Scoring Dimensions (weights):
   317|   315|   281|- Output completeness: 20%
   318|   316|   282|- Business impact: 25% (30% for Copy/Distribution/Paid)
   319|   317|   283|- Accuracy & evidence: 15% (25% for Analytics)
   320|   318|   284|- Speed/cycle time: 10%
   321|   319|   285|- Autonomy & unblockability: 10% (15% for Distribution)
   322|   320|   286|- Reusability/systemization: 10%
   323|   321|   287|- Communication quality: 10%
   324|   322|   288|
   325|   323|   289|### Auto Pass/Fail Gates:
   326|   324|   290|- FAIL: No output file written
   327|   325|   291|- FAIL: Claims "working" without verification
   328|   326|   292|- FAIL: Violates scope (pushes to product repo)
   329|   327|   293|
   330|   328|   294|### CMO Self-Scoring:
   331|   329|   295|- Weekly self-assessment against CMO Orchestration Rubric
   332|   330|   296|- Saved to: `/root/moxie_hq/cmo/scores/moxie/weekly-{date}.md`
   333|   331|   297|- Dimensions: Throughput, Outcome progress, Signal quality, Token efficiency, Reliability, Modularity
   334|   332|   298|
   335|   333|   299|### Tools:
   336|   334|   300|- `python3 /root/moxie_hq/cmo/tools/task-scorer.py <employee> <task_id> <output_file>`
   337|   335|   301|- `python3 /root/moxie_hq/cmo/tools/token-optimizer.py [--apply]`
   338|   336|   302|- `python3 /root/moxie_hq/cmo/tools/cmo-self-score.py`
   339|   337|   303|
   340|   338|   304|## Token Optimization Rules
   341|   339|   305|- Hourly crons: **All workers currently scheduled** — monitor for idle
   342|   340|   306|- Auto-pause threshold: 6+ hours idle (no tasks completed)
   343|   341|   307|- Governance cron checks usage daily; pauses idle workers automatically
   344|   342|   308|- If free model quota tight: stagger to 2 workers per hour max
   345|   343|   309|- Worker SOULs are company-framed and must read product assignments from orchestration.md before each cycle
   346|   344|   310|
   347|   345|   311|## Codex Deep Audit (ONE-SHOT)
   348|   346|   312|- Previous one-shot job `codex-5hr-resume-premium` (Cron ID: 1e17a419b9e4) is **no longer present** in the live cron registry (treat as completed/retired).
   349|   347|   313|- Current premium “resume” job in the live registry: `codex-weekly-resume-premium` (Cron ID: ca6591a837b7) — schedule: once at 2026-04-06 17:30 (GST, +04:00)
   350|   348|   314|- Expected audit output path (if/when run): /root/moxie/cmo/orchestration-audit.md
   351|   349|   315|
   352|   350|   316|## Product Assignments (Multi-product ready)
   353|   351|   317|| Product | Status | Priority | Assigned Employees |
   354|   352|   318||---------|--------|----------|-------------------|
   355|   353|   319|| FormBeep | Active (Sprint 1) | P0 | All employees |
   356|   354|   320|| Product 2 | Not yet launched | N/A | TBD |
   357|   355|   321|| Product 3 | Not yet launched | N/A | TBD |
   358|   356|   322|
   359|   357|   323|**How this works:** When a second product is added, update this table. Workers read orchestration.md, see which products are active, and allocate their time accordingly. By default, all effort goes to the currently active product(s); FormBeep is just the current sprint.
   360|   358|   324|
   361|   359|   325|**Employee flexibility:** All employees are designed to be product-agnostic. Their SOUL files define their role (research, outreach, analytics, etc.) — not the product. The product assignments above determine where they focus their effort each cycle. Workers should read this table before each cycle to know which product(s) to work on.
   362|   360|   326|