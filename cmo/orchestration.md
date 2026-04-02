# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
# Last updated: 2026-04-02T02:00:00Z
     3|     3|# 
     4|     4|# HOW THIS WORKS:
     5|     5|# Every cron job reads this file for context. When done, it updates relevant sections.
     6|     6|# Moxie (CMO) reviews this file and decides next actions.
     7|     7|# No manual prompt updates needed — agents read state from here.
     8|     8|# 
     9|     9|# SYSTEM IMPROVEMENTS (v2):
    10|    10|# - Atomic state updates: workers write to tmp files first, then rename
    11|    11|# - Retry logic: failed tasks get marked RETRY(1/3) before escalation
    12|    12|# - Task prioritization: P0 (blockers), P1 (revenue), P2 (growth), P3 (ops)
    13|    13|# - KPI tracking: every task completion updates KPI progress metrics
    14|    14|# - Cron collision mitigation: workers staggered across the hour (no longer all at :05)
    15|    15|# - Model stability: worker crons pinned to Codex-compatible models (avoid max_retries_exhausted from provider/model mismatch)
    16|    16|#
    17|    17|# DELEGATION SYSTEM (HQ, product-agnostic):
    18|    18|# - "Do not run tooling during live chat; queue work orders instead." Append to: /root/moxie_hq/cmo/delegation-queue.md
    19|    19|# - During ops cycle (or by the orchestration reconciler when appropriate), run:
    20|    20|#     python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py
    21|    21|#     python3 /root/moxie_hq/cmo/scripts/process_artifacts.py
    22|    22|# - These processors ONLY edit HQ files under /root/moxie_hq/cmo and do not require new cron scheduling.
    23|    23|
    24|    24|---
    25|    25|
    26|    26|## Mission
    27|    27|- Company: Sapiens Technology LLC (SapiensTech)
    28|    28|- Goal: grow a portfolio of indie products to consistent revenue via repeatable acquisition + conversion systems
    29|    29|
    30|    30|## Active Product (current sprint)
    31|    31|- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
    32|    32|- Target: English-speaking SMBs, agencies, freelance devs
    33|    33|- 30-day goals: 10 paid users, $100 MRR, more organic traffic
    34|    34|- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
    35|    35|- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory
    36|    36|
    37|    37|---
    38|    38|
    39|    39|## Known Blockers
    40|    40|| Blocker | Owner | Status | Action Needed |
    41|    41||---------|-------|--------|---------------|
    42|    42|| Codex 5-hour limit hit | System | RESOLVED | Premium window available now (reset completed) |
    43|    43|| WordPress plugin resubmission (WP.org) | Rishi | BLOCKED (Founder-owned) | Do not touch/iterate in automation. Rishi will implement + resubmit. After approval, execute post-approval launch plan. |
    44|    44|| Directory submissions (P1) require founder credentials/verification | Jax + Rishi | BLOCKED | Provide any existing directory accounts / inbox verification access for hello@formbeep.com (see issues_rishi.md) |
    45|    45|| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
    46|    46|| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked "worker not configured" | Moxie | RESOLVED | Fixed cron providers to OpenRouter where needed; all workers producing outputs; Pax first task COMPLETED |
    47|    47|| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
    48|    48|| Hermes config backup | Moxie | COMPLETED | Config backed up to /root/moxie_hq/infrastructure/hermes/ |
    49|    49|---
    50|    50|
    51|    51|## Employee State
    52|
    53|NOTE: All employees are SapiensTech (HQ) employees (role-based, product-agnostic). The current sprint focus is FormBeep, so most tasks route there, but no one is “hired for a product”.
    54|    52|
    55|    53|### Vale — Competitor Intelligence Lead
    56|    54|- SOUL: /root/moxie/cmo/employees/vale-soul.md
    57|    55|- Current output dir (sprint): /root/moxie/products/formbeep/
    58|- Status: COMPLETED
    59|- Current task: (StackStats) Reddit scanning plan — **COMPLETED** (2026-04-02T10:00Z)
    60|- Last output: /root/moxie/products/stackstats/outreach/reddit-scan-plan.md
    61|- Source intel artifact: /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md (generated 2026-04-01)
    62|- Blockers: None for analysis. Note: Reddit execution still needs credentials (see issues_rishi.md)
    63|- Founder activity (from new intel): Beepmate u/adambengur (2 posts, 25 comments) and Web2Phone u/ConferenceOnly1415 (25 posts, 25 comments)
    64|- Key April findings: WPForms native WA (Mar 5), Getform WA live + SMS Q2 roadmap, WANotifier commerce integrations, 4 new direct competitors detected (FormToWA, SendForm.io, PingForms, NotifyStack)
    65|- Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n, FormToWA, SendForm.io, PingForms, NotifyStack
    66|- Idle-cycle deliverable: /root/moxie/products/formbeep/pricing-war-room-april-2026.md — Pricing decision analysis ($4 vs $4.99), feature gap matrix, recommend hold price + lean into SMS moat
### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: COMPLETED
- Last completed task: (StackStats) Run DataForSEO SERP sampling for keyword discovery — **COMPLETED** (2026-04-02T12:00Z)
- Output: /root/moxie/products/stackstats/seo/serp-opportunity-brief.md
- Last completed task: (FormBeep) Run DataForSEO SERP sampling for keyword discovery — **COMPLETED** (2026-04-02T12:15Z)
- Output: /root/moxie/products/formbeep/seo/serp-opportunity-brief.md
- Last output: /root/moxie/products/formbeep/seo/serp-opportunity-brief.md
- Next task after completion: Await next assigned task (Rumi can now draft 6 SEO pages for both products)
- Blockers: None
    72|
    79|### Kiro — Conversion Copy Lead
    80||- SOUL: /root/moxie/cmo/employees/kiro-soul.md
    81||- Current output dir (sprint): /root/moxie/products/formbeep/copy/
    82||- Status: COMPLETED
    83||- Current task: REWORK 2 blog posts per founder feedback (length + factual fixes + Zapier/WhatsApp research + comparison table + thumbnail prompts) — **COMPLETED** (2026-04-01T22:45Z)
    84||- Last output:
    85|  - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md (~1,650 words, slug: whatsapp-without-zapier)
    86|  - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md (~1,720 words, slug: formbeep-vs-zapier)
    87||- Deliverables: Both posts expanded to target length, factual fixes applied (hello@formbeep.com, 15 submissions/month), frontmatter updated (slug + thumb_prompt), Zapier→WhatsApp API requirements research incorporated, comparison table added to vs post
    88||- Blockers: None
    89|    84|
    90|    85|### Ember — Outreach & Distribution Lead
    91|    86|- SOUL: /root/moxie/cmo/employees/ember-soul.md
    92|    87|- Current output dir (sprint): /root/moxie/products/formbeep/outreach/
    93|    88|- Status: COMPLETED (execution blocked on creds)
    94|    89|- Current task: Manual Reddit posting plan (Non-US/GST focus) + subreddit rules checklist + posting windows + verification steps — **COMPLETED** (2026-04-01T17:32Z)
    95|- Last output: /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md (2026-04-02 — full rules table + activity log + quick-ref)
    96|- Previous outputs: reddit-manual-posting-plan-gst-nonus-v1.md (2026-04-01), reddit-post-comment-scripts.md (2026-04-01), reddit-campaign-plan.md (2026-03-31), reddit-strategy.md (2026-03-31)
    97|    92|- Completed deliverables: reddit-strategy.md, reddit-campaign-plan.md, reddit-post-comment-scripts.md, manual-posting-plan-gst-nonus-v1.md
    98|    93|- Next task after completion: Execute Week 1 posting — **BLOCKED** on Reddit account credentials (see issues_rishi.md)
    99|    94|- Blockers: Reddit account credentials required for all posting execution (see issues_rishi.md)
   100|    95|
### Forge — Full Stack Engineer
- SOUL: /root/moxie/cmo/employees/forge-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: (StackStats) Clone repo, identify Gumroad/CTA links, propose Umami event tracking + UTM hygiene — **COMPLETED** (2026-04-02T02:37Z)
- Task ID: forge-20260401_233521-647619
- Output path: /root/moxie/products/stackstats/dev-notes/tracking-implementation-notes.md
- Last completed task: (FormBeep) Build marketplace requirements matrix + feasibility memo — **COMPLETED** (2026-04-02T01:45Z)
- Last output: /root/moxie_hq/products/formbeep/dev-notes/marketplace-integration-scope.md (delivered 2026-04-02T01:45Z)
- Key findings: Webflow/Framer require full app/plugin (DEFER); Glide/Typedream use existing integrations (BUILD NOW)
- Next task after completion: (FormBeep) Repo tracking audit (queued)
- Blockers: None
   112|   105|
   113|### Mira — Analytics & Reporting Lead
   114|- SOUL: /root/moxie/cmo/employees/mira-soul.md
   115|- Current output dir (sprint): /root/moxie/products/stackstats/
   116|- Status: IN_PROGRESS
   117|- Current task: (StackStats) Pull Umami Cloud analytics for StackStats (website_id 52a19925-9bf4-4efe-9a42-ecc2a7f08d81): last 7d + last 30d. Include top sources, top pages, geo split, and any events — **IN_PROGRESS** (promoted 2026-04-02T00:06Z)
   118|- Task ID: mira-20260401_233129-5c8b35
   119|- Output path: /root/moxie/products/stackstats/analytics/umami-summary.md
   120|- Umami: cloud.umami.is, website ID: 52a19925-9bf4-4efe-9a42-ecc2a7f08d81
   121|- Last output: /root/moxie/products/formbeep/traffic-vs-keywords.md
   122|- Next task after completion: Continue analytics support for StackStats growth plan
   123|- Blockers: None
   124|- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv
   125|   116|
   126|   117|### Nova — Paid Acquisition Lead
   127|   118|- SOUL: /root/moxie/cmo/employees/nova-soul.md
   128|   119|- Current output dir (sprint): /root/moxie/cmo/sops/
   129|   120|- Status: COMPLETED
   130|   121|- Current task: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) — **COMPLETED**
   131|   122|- Last output: /root/moxie/cmo/sops/paid-ads-sop.md
   132|   123|- Next task after completion: Formalize campaign naming + UTM taxonomy in configs/templates + ship first tracked campaign for FormBeep (Google Search BOF)
   133|   124|- Blockers: None
   134|   125|
### Jax — SaaS Growth Operations Lead
   135|   136|- SOUL: /root/moxie/cmo/employees/jax-soul.md
   137|   137|- Current output dir (sprint): /root/moxie/products/formbeep/
   138|   138|- Status: READY
   139|   139|- Current task: (FormBeep) Replace failed directory picks with 2 actionable directories (verified requirements + submission bundles) — COMPLETED (2026-04-02T02:00Z)
   140|   140|- Task ID: jax-20260401_223121-f3bb3a
   141|   141|- Output path: /root/moxie/products/formbeep/distribution/directory-submissions-today-pick.md
   142|   142|- Blockers: None
   143|   134|
### Rumi — Blog & Content Analyst
- SOUL: /root/moxie/cmo/employees/rumi-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: IN_PROGRESS
- Current task: (HQ) Platform×product posting matrix (X, Reddit, IndieHackers, directories, forums/communities) — **IN_PROGRESS** (promoted 2026-04-02T02:00Z)
- Task ID: rumi-20260402_002635-fda614
- Output path: /root/moxie_hq/cmo/strategy/channel-matrix-all-products.md
- Last completed task: (FormBeep) 6 SEO landing page outlines (Hugo-ready) — **COMPLETED** (2026-04-02T13:00Z)
- Previous completed task: (StackStats) 6 SEO landing page outlines (Hugo-ready) — **COMPLETED** (2026-04-02T10:30Z)
- Last output: /root/moxie_hq/products/formbeep/seo/page-outlines.md (FormBeep), /root/moxie/products/stackstats/seo/page-outlines.md (StackStats)
- Next task after completion: Await next assigned task
- Blockers: None
   154|   144|
   155|   145|### Pax — Partnerships / BD Lead
   156|   146|- SOUL: /root/moxie/cmo/employees/pax-soul.md
   157|   147|- Current output dir (sprint): /root/moxie/products/formbeep/partnerships/
   158|   148|- Status: COMPLETED
   159|   149|- Current task: Week 3 submissions (Carrd + Typedream integration packages + agency outreach to top 15 targets) — **COMPLETED**
   160|   150|- Last output: /root/moxie/products/formbeep/partnerships/platform-applications-week3.md
   161|   151|- Next task after completion: Send agency outreach emails once verified contact info obtained; publish formbeep.com/integrations reciprocal directory; follow up on Week 1-2 platform application reviews
   162|   152|- Blockers: Portal credentials (Webflow/Framer/Glide/Softr), Reddit account for community posts, verified agency email contacts, hello@formbeep.com access for sending
   163|   153|
   164|### Luna — Lifecycle / CRM Lead
   165||- SOUL: /root/moxie/cmo/employees/luna-soul.md
   166||- Current output dir (sprint): /root/moxie/products/formbeep/lifecycle/
   167||- Status: COMPLETED
   168||- Current task: Win-back email sequence for churned users — **COMPLETED** (2026-04-02T08:52Z)
   169||- Last output: /root/moxie/products/formbeep/lifecycle/win-back-emails.md
   170||- Previous output: /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
   171||- Next task after completion: Continue lifecycle optimization (retention triggers, segmentation)
   172||- Blockers: None
   173|   162|
   174|### Orion — Outbound Lead (Cold Email)
   175||- SOUL: /root/moxie/cmo/employees/orion-soul.md
   176||- Current output dir (sprint): /root/moxie/products/formbeep/outbound/
   177||- Status: COMPLETED
   178||- Current task: Prospect list refresh from competitor intel — **COMPLETED** (2026-04-02T08:15Z)
   179||- Last output: /root/moxie/products/formbeep/outbound/prospect-refresh.md
   180||- Previous output: /root/moxie/products/formbeep/outbound/outbound-pack.md
   181||- Next task after completion: Continue outbound optimization (subject tests, sequence refinement)
   182||- Blockers: Sending infrastructure (email warmup/domain setup) required for actual outreach execution
   183|   171|
   184|### Iris — Repo Copy Auditor
   185|- SOUL: /root/moxie/cmo/employees/iris-soul.md
   186|- Current output dir (sprint): /root/moxie_hq/products/formbeep/dev-notes/
   187|- Status: IN_PROGRESS
   188|- Current task: (FormBeep) Inspect the ACTUAL current landing page content in the repo (headlines, breadcrumbs, free-tier claims) and deliver 10 exact copy/UX improvements with file+section pointers — **IN_PROGRESS** (promoted 2026-04-02T00:06Z)
   189|- Task ID: iris-20260401_224900-eab63b
   190|- Output path: /root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md
   191|- Last output: N/A (first run)
   192|- Next task after completion: Weekly copy/UX audit of landing + docs content
   193|- Blockers: None
   194|   180|
   195|   181|
   196|### Moxie — CMO / Orchestrator
   197|- SOUL: /root/moxie_hq/SOUL.md
   198|- Current output dir (sprint): /root/moxie_hq/cmo/
   199|- Status: IN_PROGRESS
   200|- Current task: (HQ) Create all-products Founder Voice / Build-in-Public strategy — **IN_PROGRESS** (promoted 2026-04-02T01:11Z)
   201|- Task ID: moxie-20260402_011100-founder-voice
   202|- Output path: /root/moxie_hq/cmo/strategy/founder-voice-x-indiehackers.md
   203|- Task details: X + IndieHackers strategy with WHERE/WHY/HOW patterns, WHEN (UTC + geo), 30-day cadence template, content pillars, proof/credibility loop, and multi-product narrative routing
   204|- Blockers: None
   205|---
   206|   182|
   207|   183|## Active Crons (Source of truth: `hermes cron list`)

**Editing rule:** do not edit jobs via this table. Update jobs using `hermes cron edit <cron_id> ...` and then reconcile this table to match.

Last verified: 2026-04-02T02:13:00Z

||| Cron ID | Name | Schedule | Deliver | Next run (UTC) | Repeats | State |||---|---|---|---|---|---|---|
| 6effbb32 | formbeep-daily-user-count-checkin | every 1440m | local | 2026-04-02T14:06:30+00:00 | ∞ | active |
| aba07be5 | formbeep-daily-traffic-check | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | ∞ | active |
| 513b777e | formbeep-search-check | 0 10 * * 1,4 | local | 2026-04-02T10:00:00+00:00 | ∞ | active |
| 753d42f3 | formbeep-weekly-growth-review | 0 11 * * 1 | local | 2026-04-06T11:00:00+00:00 | ∞ | active |
| ae770f4f | formbeep-hourly-heartbeat | 6 * * * * | local | 2026-04-02T02:06:00+00:00 | ∞ | active |
| 52af5ec9 | codex-dashboard-update-checkin | every 720m | local | 2026-04-02T02:38:58+00:00 | ∞ | active |
| b0492991 | moxie-memory-skill-audit | every 720m | local | 2026-04-02T07:30:09+00:00 | ∞ | active |
| ca6591a8 | codex-weekly-resume-premium | once at 2026-04-06 17:30 | local | 2026-04-06T17:30:00+04:00 | 0/1 | active |
| 0526cbc1 | weekly-free-models-reminder | 0 17 * * 2 | local | 2026-04-07T17:00:00+00:00 | ∞ | active |
| 647387ae | mira-daily-kpi | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | 9/100 | active |
| a468835d | vale-monthly-competitor-scan | 0 10 1 * * | local | 2026-05-01T10:00:00+00:00 | 1/100 | active |
| 2553a683 | moxie-daily-governance | 0 * * * * | local | 2026-04-02T03:00:00+00:00 | 51/100 | active |
| 8bcfe505 | vale-worker | 12 * * * * | local | 2026-04-02T03:12:00+00:00 | 53/100 | active |
| 7067633e | astra-worker | 17 * * * * | local | 2026-04-02T02:17:00+00:00 | 52/100 | active |
| 3171d2c2 | kiro-worker | 42 * * * * | local | 2026-04-02T02:42:00+00:00 | 51/100 | active |
| eb803b7d | ember-worker | 32 * * * * | local | 2026-04-02T02:32:00+00:00 | 51/100 | active |
| 401e59cc | forge-worker | 37 * * * * | local | 2026-04-02T02:37:00+00:00 | 52/100 | active |
| 4bdcef11 | jax-worker | 22 * * * * | local | 2026-04-02T02:22:00+00:00 | 51/100 | active |
| affd389a | rumi-worker | 27 * * * * | local | 2026-04-02T02:27:00+00:00 | 51/100 | active |
| af7f3c07 | moxie-daily-self-improvement | 0 20 * * * | local | 2026-04-02T20:00:00+00:00 | 2/100 | active |
| 91520aa6 | nova-worker | 47 * * * * | local | 2026-04-02T02:47:00+00:00 | 50/100 | active |
| 5b9c6eb7 | issues-rishi-watch | every 240m | local | 2026-04-02T04:41:20+00:00 | 13/200 | active |
| 3e93c4f5 | luna-worker | 52 * * * * | local | 2026-04-02T02:52:00+00:00 | 52/100 | active |
| cf1a8f9e | pax-worker | 57 * * * * | local | 2026-04-02T02:57:00+00:00 | 50/100 | active |
| b0e9c513 | iris-weekly-formbeep-repo-copy-audit | 30 9 * * 1 | local | 2026-04-06T09:30:00+00:00 | 0/200 | active |
| 0ed491f6 | orion-worker | 2 * * * * | local | 2026-04-02T03:02:00+00:00 | 52/200 | active |
| 868bd30f | moxie-hq-autocommit-push | every 30m | local | 2026-04-02T01:19:58+00:00 | ∞ | active |
| 1c008e06 | moxie-orchestration-reconciler | 13 * * * * | local | 2026-04-02T03:13:00+00:00 | 42/100 | active |
| c342e174 | opencode-go-weekly-limit-reset-reminder | 26 13 * * 1 | local | 2026-04-06T13:26:00+00:00 | ∞ | active |
| 7af300e6 | cmo-delegation-queue-runner | */15 * * * * | local | 2026-04-02T01:30:00+00:00 | ∞ | active |

**Retired/Removed jobs** (no longer in live registry):
- `97eacc1cb3fa` codex-online-check — one-shot job, completed
- `6b5fe0d2220c` cmo-dispatch-orchestrator — removed from registry
- `415e88f0` wp-plugin-rishi-reminder — removed from registry  
- `904c65910bfe` moxie-forward-reports-to-telegram — removed from registry
   251|   227|
   252|   228|---
   253|   229|
   254|   230|## Completed Deliverables
   255|   231|| Date | Employee | File | Status |
   256|   232||------|----------|------|--------|
   257|   233|| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
   258|   234|| 2026-03-31 | Mira | /root/moxie/products/formbeep/traffic-vs-keywords.md | COMPLETED |
   259|   235|| 2026-03-31 | Orion | /root/moxie/products/formbeep/outbound/outbound-pack.md | COMPLETED |
   260|   236|| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
   261|   237|| 2026-03-31 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED |
   262|   238|| 2026-04-01 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED — Monthly competitor scan (WPForms WA live, Getform WA+SMS roadmap, 4 new entrants) |
   263|   239|| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
   264|   240|| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
   265|   241|| 2026-03-31 | Ember | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md | COMPLETED |
   266|   242|| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-post-comment-scripts.md | COMPLETED |
   267|   243|| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-manual-posting-plan-gst-nonus-v1.md | COMPLETED |
   268||| 2026-04-02 | Ember | /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md | COMPLETED — Full subreddit rules table (28 subs) + activity log + quick-ref + posting guardrails |
   269|   244|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
   270|   245|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions-p1.md | COMPLETED (P1 submission pack ready; execution awaits credentials) |
   271|   246|| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
   272|   247|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
   273|   248|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
   274|   249|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
   275|   250|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |
   276|   251||| 2026-03-31 | Luna | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md | COMPLETED |
   277|   252||| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md | COMPLETED
   278|   253||| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/platform-partner-outreach.md | COMPLETED
   279|   254||| 2026-04-01 | Pax | /root/moxie/products/formbeep/partnerships/platform-applications-week3.md | COMPLETED
   280|||| 2026-04-02 | Luna | /root/moxie/products/formbeep/lifecycle/win-back-emails.md | COMPLETED — 3-email win-back sequence (Day 1/3/7) + pre-churn triggers + segmentation matrix + behavioral onboarding handoff
   281|   255|
   282|   256|---
   283|   257|
   284|## Rishi Action Items (Requires Human)
   285|1. WordPress plugin resubmission (founder-owned) — implement fixes + resubmit when you're ready (see /root/moxie/products/formbeep/wp-plugin-fixes.md)
   286|2. After approval: execute post-approval WP launch plan (I'll keep it ready on disk)
   287|3. Directory submissions — inbox confirmed as hello@formbeep.com; share any existing directory accounts (for Jax)
   288|4. **REWORK REQUESTED** Kiro blog posts (do not publish yet):
   289|   - Drafts:
   290|     - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md
   291|     - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md
   292|   - Required fixes:
   293|     - Make them longer / more rankable (~1200–1800 words)
   294|     - Correct: contact email = hello@formbeep.com
   295|     - Correct: free tier = 15 submissions/month
   296|     - Set slugs: whatsapp-without-zapier/ and formbeep-vs-zapier/
   297|     - Research Zapier→WhatsApp reality (out-of-the-box vs needs WhatsApp Business API provider like Twilio/360dialog/Meta Cloud API)
   298|     - Add a comparison table in the “vs Zapier” post
   299|     - Add `thumb_prompt:` frontmatter to each post (thumbnail generation prompt text)
   300|5. (Ops) If HQ pushes are needed: confirm MOXIE_GITHUB_WRITE_PAT in /opt/data/.env has write access to rishikeshsreehari/moxie
   301|   267|
   302|   268|---
   303|   269|
   304|   270|## Rubric & Scoring System (NEW — Auto-wired)
   305|   271|**Every completed task is automatically scored against the Employee Rubric.**
   306|   272|
   307|   273|### How it works:
   308|   274|1. Task completes → Employee updates orchestration.md
   309|   275|2. `task-scorer.py` auto-runs: scores 7 dimensions (1-5), weighted overall
   310|   276|3. Scorecard saved to: `/root/moxie_hq/cmo/scores/{employee}/{task_id}.md`
   311|   277|4. SOUL.md auto-updated with: Recent Scores table + Current Improvement Focus
   312|   278|5. "Dreaming" reflection triggered: employee reflects on what worked/didn't
   313|   279|
   314|   280|### Scoring Dimensions (weights):
   315|   281|- Output completeness: 20%
   316|   282|- Business impact: 25% (30% for Copy/Distribution/Paid)
   317|   283|- Accuracy & evidence: 15% (25% for Analytics)
   318|   284|- Speed/cycle time: 10%
   319|   285|- Autonomy & unblockability: 10% (15% for Distribution)
   320|   286|- Reusability/systemization: 10%
   321|   287|- Communication quality: 10%
   322|   288|
   323|   289|### Auto Pass/Fail Gates:
   324|   290|- FAIL: No output file written
   325|   291|- FAIL: Claims "working" without verification
   326|   292|- FAIL: Violates scope (pushes to product repo)
   327|   293|
   328|   294|### CMO Self-Scoring:
   329|   295|- Weekly self-assessment against CMO Orchestration Rubric
   330|   296|- Saved to: `/root/moxie_hq/cmo/scores/moxie/weekly-{date}.md`
   331|   297|- Dimensions: Throughput, Outcome progress, Signal quality, Token efficiency, Reliability, Modularity
   332|   298|
   333|   299|### Tools:
   334|   300|- `python3 /root/moxie_hq/cmo/tools/task-scorer.py <employee> <task_id> <output_file>`
   335|   301|- `python3 /root/moxie_hq/cmo/tools/token-optimizer.py [--apply]`
   336|   302|- `python3 /root/moxie_hq/cmo/tools/cmo-self-score.py`
   337|   303|
   338|   304|## Token Optimization Rules
   339|   305|- Hourly crons: **All workers currently scheduled** — monitor for idle
   340|   306|- Auto-pause threshold: 6+ hours idle (no tasks completed)
   341|   307|- Governance cron checks usage daily; pauses idle workers automatically
   342|   308|- If free model quota tight: stagger to 2 workers per hour max
   343|   309|- Worker SOULs are company-framed and must read product assignments from orchestration.md before each cycle
   344|   310|
   345|   311|## Codex Deep Audit (ONE-SHOT)
   346|   312|- Previous one-shot job `codex-5hr-resume-premium` (Cron ID: 1e17a419b9e4) is **no longer present** in the live cron registry (treat as completed/retired).
   347|   313|- Current premium “resume” job in the live registry: `codex-weekly-resume-premium` (Cron ID: ca6591a837b7) — schedule: once at 2026-04-06 17:30 (GST, +04:00)
   348|   314|- Expected audit output path (if/when run): /root/moxie/cmo/orchestration-audit.md
   349|   315|
   350|   316|## Product Assignments (Multi-product ready)
   351|   317|| Product | Status | Priority | Assigned Employees |
   352|   318||---------|--------|----------|-------------------|
   353|   319|| FormBeep | Active (Sprint 1) | P0 | All employees |
   354|   320|| Product 2 | Not yet launched | N/A | TBD |
   355|   321|| Product 3 | Not yet launched | N/A | TBD |
   356|   322|
   357|   323|**How this works:** When a second product is added, update this table. Workers read orchestration.md, see which products are active, and allocate their time accordingly. By default, all effort goes to the currently active product(s); FormBeep is just the current sprint.
   358|   324|
   359|   325|**Employee flexibility:** All employees are designed to be product-agnostic. Their SOUL files define their role (research, outreach, analytics, etc.) — not the product. The product assignments above determine where they focus their effort each cycle. Workers should read this table before each cycle to know which product(s) to work on.
   360|   326|