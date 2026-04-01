     1|# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
     2|# Last updated: 2026-04-01T20:00:00Z
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
    16|#
    17|# DELEGATION SYSTEM (HQ, product-agnostic):
    18|# - "Do not run tooling during live chat; queue work orders instead." Append to: /root/moxie_hq/cmo/delegation-queue.md
    19|# - During ops cycle (or by the orchestration reconciler when appropriate), run:
    20|#     python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py
    21|#     python3 /root/moxie_hq/cmo/scripts/process_artifacts.py
    22|# - These processors ONLY edit HQ files under /root/moxie_hq/cmo and do not require new cron scheduling.
    23|
    24|---
    25|
    26|## Mission
    27|- Company: Sapiens Technology LLC (SapiensTech)
    28|- Goal: grow a portfolio of indie products to consistent revenue via repeatable acquisition + conversion systems
    29|
    30|## Active Product (current sprint)
    31|- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
    32|- Target: English-speaking SMBs, agencies, freelance devs
    33|- 30-day goals: 10 paid users, $100 MRR, more organic traffic
    34|- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
    35|- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory
    36|
    37|---
    38|
    39|## Known Blockers
    40|| Blocker | Owner | Status | Action Needed |
    41||---------|-------|--------|---------------|
    42|| Codex 5-hour limit hit | System | RESOLVED | Premium window available now (reset completed) |
    43|| WordPress plugin resubmission (WP.org) | Rishi | BLOCKED (Founder-owned) | Do not touch/iterate in automation. Rishi will implement + resubmit. After approval, execute post-approval launch plan. |
    44|| Directory submissions (P1) require founder credentials/verification | Jax + Rishi | BLOCKED | Provide any existing directory accounts / inbox verification access for hello@formbeep.com (see issues_rishi.md) |
    45|| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
    46|| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked "worker not configured" | Moxie | RESOLVED | Fixed cron providers to OpenRouter where needed; all workers producing outputs; Pax first task COMPLETED |
    47|| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
    48|| Hermes config backup | Moxie | COMPLETED | Config backed up to /root/moxie_hq/infrastructure/hermes/ |
    49|---
    50|
    51|## Employee State

NOTE: All employees are SapiensTech (HQ) employees (role-based, product-agnostic). The current sprint focus is FormBeep, so most tasks route there, but no one is “hired for a product”.
    52|
    53|### Vale — Competitor Intelligence Lead
    54|- SOUL: /root/moxie/cmo/employees/vale-soul.md
    55|- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: (FormBeep) Reddit intel analysis → positioning + subreddit playbook — **COMPLETED** (2026-04-01T16:30Z)
- Last output: /root/moxie/products/formbeep/pricing-war-room-april-2026.md
- Source intel artifact: /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md (generated 2026-04-01)
- Blockers: None for analysis. Note: Reddit execution still needs credentials (see issues_rishi.md)
- Founder activity (from new intel): Beepmate u/adambengur (2 posts, 25 comments) and Web2Phone u/ConferenceOnly1415 (25 posts, 25 comments)
- Key April findings: WPForms native WA (Mar 5), Getform WA live + SMS Q2 roadmap, WANotifier commerce integrations, 4 new direct competitors detected (FormToWA, SendForm.io, PingForms, NotifyStack)
- Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n, FormToWA, SendForm.io, PingForms, NotifyStack
- Idle-cycle deliverable: /root/moxie/products/formbeep/pricing-war-room-april-2026.md — Pricing decision analysis ($4 vs $4.99), feature gap matrix, recommend hold price + lean into SMS moat
### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: SERP demand probe + keyword roadmap (US + overall FormBeep) — **COMPLETED** (2026-04-02T07:00Z)
- Task details: (1) US SMS demand keywords, (2) overall FormBeep keyword expansion, (3) DataForSEO credits/$ estimate. MUST ask Rishi approval before any paid API calls beyond the 1 already-run test. Creds policy: /root/moxie_hq/cmo/resources/credentials/dataforseo.md
- Last output: /root/moxie/products/formbeep/seo/us-sms-serp-demand-brief.md
- Previous output: /root/moxie/products/formbeep/sms-keyword-analysis.md
- Blockers: DataForSEO validation (50-query plan, $0.10) pending Rishi approval
    72|
### Kiro — Conversion Copy Lead
- SOUL: /root/moxie/cmo/employees/kiro-soul.md
- Output dir: /root/moxie/products/formbeep/copy/
- Status: QUEUED
- Current task: REWORK 2 blog posts per founder feedback (length + factual fixes + Zapier/WhatsApp research + comparison table + thumbnail prompts) — **QUEUED** (2026-04-01T21:35Z)
- Last output (rejected drafts; do not publish as-is):
  - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md
  - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md
- Rework requirements (must address all):
  - Expand each post to ~1200–1800 words with additional subheads + examples
  - Fix: support email = hello@formbeep.com
  - Fix: free tier = 15 submissions/month
  - Add frontmatter: slug = whatsapp-without-zapier / formbeep-vs-zapier
  - Research: Zapier→WhatsApp “out-of-the-box” reality (WhatsApp Business API; Twilio vs 360dialog vs Meta Cloud API) and reflect accurately
  - Add a comparison table in the vs post
  - Add frontmatter: thumb_prompt (text prompt for thumbnail generation)
- Blockers: None
    84|
    85|### Ember — Outreach & Distribution Lead
    86|- SOUL: /root/moxie/cmo/employees/ember-soul.md
    87|- Output dir: /root/moxie/products/formbeep/outreach/
    88|- Status: COMPLETED (execution blocked on creds)
    89|- Current task: Manual Reddit posting plan (Non-US/GST focus) + subreddit rules checklist + posting windows + verification steps — **COMPLETED** (2026-04-01T17:32Z)
- Last output: /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md (2026-04-02 — full rules table + activity log + quick-ref)
- Previous outputs: reddit-manual-posting-plan-gst-nonus-v1.md (2026-04-01), reddit-post-comment-scripts.md (2026-04-01), reddit-campaign-plan.md (2026-03-31), reddit-strategy.md (2026-03-31)
    92|- Completed deliverables: reddit-strategy.md, reddit-campaign-plan.md, reddit-post-comment-scripts.md, manual-posting-plan-gst-nonus-v1.md
    93|- Next task after completion: Execute Week 1 posting — **BLOCKED** on Reddit account credentials (see issues_rishi.md)
    94|- Blockers: Reddit account credentials required for all posting execution (see issues_rishi.md)
    95|
### Forge — Product/Codebase Inspector
- SOUL: /root/moxie/cmo/employees/forge-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: QUEUED
- Current task: 1) GSC indexing report delivered. 2) Rishi approved and applied patches. 3) Next: Validate GSC indexing post-SEO-fixes (3 days after sitemap resubmit) — **QUEUED** (2026-04-04T12:00Z)
- Last output: /root/moxie/products/formbeep/analytics/gsc-indexing-report.md (delivered 2026-04-01)
- Previous task: Technical SEO audit — **COMPLETED**
- Next task after completion: Monitor Index Coverage for taxonomy page removal; measure impression changes for blog pages
- Blockers: None
   105|
   106|### Mira — Analytics & Reporting Lead
   107|- SOUL: /root/moxie/cmo/employees/mira-soul.md
   108|- Output dir: /root/moxie/products/formbeep/
   109|- Status: COMPLETED
   110|- Current task: Traffic vs keyword opportunity map (use Umami + Astra keyword briefing) — **COMPLETED** (2026-03-31)
   111|- Last output: /root/moxie/products/formbeep/traffic-vs-keywords.md
   112|- Umami: cloud.umami.is, website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d
   113|- Next task after completion: Improve KPI reporting outputs (no new cron jobs without approval)
   114|- Blockers: None
   115|- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv
   116|
   117|### Nova — Paid Acquisition Lead
   118|- SOUL: /root/moxie/cmo/employees/nova-soul.md
   119|- Output dir: /root/moxie/cmo/sops/
   120|- Status: COMPLETED
   121|- Current task: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) — **COMPLETED**
   122|- Last output: /root/moxie/cmo/sops/paid-ads-sop.md
   123|- Next task after completion: Formalize campaign naming + UTM taxonomy in configs/templates + ship first tracked campaign for FormBeep (Google Search BOF)
   124|- Blockers: None
   125|
### Jax — SaaS Growth Operations Lead
- SOUL: /root/moxie/cmo/employees/jax-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Daily directory 2-pick + maintenance — **COMPLETED** (2026-04-03)
- Last output: /root/moxie/products/formbeep/distribution/directory-submissions-log.md & /root/moxie/products/formbeep/distribution/directory-submissions-today-pick.md
- Next task after completion: Pick #1: BetaList (DR 66), Pick #2: AlternativeTo (DR 91). Awaiting Rishi execution. 4 directories remain (PH deferred, Capterra/G2/GetApp/AppSumo).
- Blockers: Execution still requires Rishi to submit via the "today-pick" bundles. No new credentials needed for these two picks (form-based).
   134|
   135|### Rumi — Blog & Content Analyst
   136|- SOUL: /root/moxie/cmo/employees/rumi-soul.md
   137|- Output dir: /root/moxie/products/formbeep/
   138|- Status: COMPLETED
   139|- Current task: Bi-weekly content gap scan + trending topic check — **COMPLETED** (2026-03-31)
   140|- Last output: /root/moxie/products/formbeep/content-gap-scan.md
   141|- Keyword seed: /root/moxie/products/formbeep/seo-keywords.md
   142|- Next task after completion: Next bi-weekly scan (2026-04-10). Priority backlog: 4 P0/P1 topics flagged for Kiro drafts.
   143|- Blockers: None
   144|
   145|### Pax — Partnerships / BD Lead
   146|- SOUL: /root/moxie/cmo/employees/pax-soul.md
   147|- Output dir: /root/moxie/products/formbeep/partnerships/
   148|- Status: COMPLETED
   149|- Current task: Week 3 submissions (Carrd + Typedream integration packages + agency outreach to top 15 targets) — **COMPLETED**
   150|- Last output: /root/moxie/products/formbeep/partnerships/platform-applications-week3.md
   151|- Next task after completion: Send agency outreach emails once verified contact info obtained; publish formbeep.com/integrations reciprocal directory; follow up on Week 1-2 platform application reviews
   152|- Blockers: Portal credentials (Webflow/Framer/Glide/Softr), Reddit account for community posts, verified agency email contacts, hello@formbeep.com access for sending
   153|
### Luna — Lifecycle / CRM Lead
|- SOUL: /root/moxie/cmo/employees/luna-soul.md
|- Output dir: /root/moxie/products/formbeep/lifecycle/
|- Status: COMPLETED
|- Current task: Win-back email sequence for churned users — **COMPLETED** (2026-04-02T08:52Z)
|- Last output: /root/moxie/products/formbeep/lifecycle/win-back-emails.md
|- Previous output: /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
|- Next task after completion: Continue lifecycle optimization (retention triggers, segmentation)
|- Blockers: None
   162|
### Orion — Outbound Lead (Cold Email)
|- SOUL: /root/moxie/cmo/employees/orion-soul.md
|- Output dir: /root/moxie/products/formbeep/outbound/
|- Status: COMPLETED
|- Current task: Prospect list refresh from competitor intel — **COMPLETED** (2026-04-02T08:15Z)
|- Last output: /root/moxie/products/formbeep/outbound/prospect-refresh.md
|- Previous output: /root/moxie/products/formbeep/outbound/outbound-pack.md
|- Next task after completion: Continue outbound optimization (subject tests, sequence refinement)
|- Blockers: Sending infrastructure (email warmup/domain setup) required for actual outreach execution
   171|
   172|### Iris — Repo Copy Auditor
   173|- SOUL: /root/moxie/cmo/employees/iris-soul.md
   174|- Output dir: /root/moxie_hq/products/formbeep/dev-notes/
   175|- Status: IDLE
   176|- Current task: Weekly FormBeep repo copy audit — runs every Monday 09:30 UTC
   177|- Last output: N/A (first run scheduled 2026-04-06)
   178|- Next task after completion: Weekly copy/UX audit of landing + docs content
   179|- Blockers: None
   180|
   181|---
   182|
   183|## Active Crons (Source of truth: `hermes cron list`)
   184|
   185|**Editing rule:** do not edit jobs via this table. Update jobs using `hermes cron edit <cron_id> ...` and then reconcile this table to match.
   186|
Last verified: 2026-04-01T21:13:00Z

|||| Cron ID | Name | Schedule | Deliver | Next run (UTC) | Repeats | State ||
||||---|---|---|---|---|---|---||
|||| 6effbb32 | formbeep-daily-user-count-checkin | every 1440m | local | 2026-04-02T14:06:30+00:00 | ∞ | active ||
|||| aba07be5 | formbeep-daily-traffic-check | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | ∞ | active ||
|||| 513b777e | formbeep-search-check | 0 10 * * 1,4 | local | 2026-04-02T10:00:00+00:00 | ∞ | active ||
|||| 753d42f3 | formbeep-weekly-growth-review | 0 11 * * 1 | local | 2026-04-06T11:00:00+00:00 | ∞ | active ||
|||| ae770f4f | formbeep-hourly-heartbeat | 6 * * * * | local | 2026-04-01T22:06:00+00:00 | ∞ | active ||
|||| 52af5ec9 | codex-dashboard-update-checkin | every 720m | local | 2026-04-02T02:38:58+00:00 | ∞ | active ||
|||| b0492991 | moxie-memory-skill-audit | every 720m | local | 2026-04-02T07:30:09+00:00 | ∞ | active ||
|||| ca6591a8 | codex-weekly-resume-premium | once at 2026-04-06 17:30 | local | 2026-04-06T17:30:00+04:00 | 0/1 | active ||
|||| 0526cbc1 | weekly-free-models-reminder | 0 17 * * 2 | local | 2026-04-07T17:00:00+00:00 | ∞ | active ||
|| 647387ae | mira-daily-kpi | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | 9/100 | active |
|| a468835d | vale-monthly-competitor-scan | 0 10 1 * * | local | 2026-05-01T10:00:00+00:00 | 1/100 | active |
|| 2553a683 | moxie-daily-governance | 0 * * * * | local | 2026-04-01T22:00:00+00:00 | 46/100 | active |
|| 8bcfe505 | vale-worker | 12 * * * * | local | 2026-04-01T22:12:00+00:00 | 48/100 | active |
|| 7067633e | astra-worker | 17 * * * * | local | 2026-04-01T21:17:00+00:00 | 47/100 | active |
|| 3171d2c2 | kiro-worker | 42 * * * * | local | 2026-04-01T21:42:00+00:00 | 46/100 | active |
|| eb803b7d | ember-worker | 32 * * * * | local | 2026-04-01T21:32:00+00:00 | 46/100 | active |
|| 401e59cc | forge-worker | 37 * * * * | local | 2026-04-01T21:37:00+00:00 | 47/100 | active |
|| 4bdcef11 | jax-worker | 22 * * * * | local | 2026-04-01T21:22:00+00:00 | 46/100 | active |
|| affd389a | rumi-worker | 27 * * * * | local | 2026-04-01T21:27:00+00:00 | 46/100 | active |
|| af7f3c07 | moxie-daily-self-improvement | 0 20 * * * | local | 2026-04-02T20:00:00+00:00 | 2/100 | active |
|| 91520aa6 | nova-worker | 47 * * * * | local | 2026-04-01T21:47:00+00:00 | 45/100 | active |
|| 5b9c6eb7 | issues-rishi-watch | every 240m | local | 2026-04-02T00:26:57+00:00 | 12/200 | active |
|| 3e93c4f5 | luna-worker | 52 * * * * | local | 2026-04-01T21:52:00+00:00 | 47/100 | active |
|| cf1a8f9e | pax-worker | 57 * * * * | local | 2026-04-01T21:57:00+00:00 | 45/100 | active |
|| b0e9c513 | iris-weekly-formbeep-repo-copy-audit | 30 9 * * 1 | local | 2026-04-06T09:30:00+00:00 | 0/200 | active |
|| 0ed491f6 | orion-worker | 2 * * * * | local | 2026-04-01T22:02:00+00:00 | 47/200 | active |
|| 868bd30f | moxie-hq-autocommit-push | every 30m | local | 2026-04-01T21:27:13+00:00 | ∞ | active |
|| 1c008e06 | moxie-orchestration-reconciler | 13 * * * * | local | 2026-04-01T22:13:00+00:00 | 37/100 | active |
|||| c342e174 | opencode-go-weekly-limit-reset-reminder | 26 13 * * 1 | local | 2026-04-06T13:26:00+00:00 | ∞ | active ||
|||| 7af300e6 | cmo-delegation-queue-runner | */15 * * * * | local | 2026-04-01T21:15:00+00:00 | ∞ | active ||
   221|
   222|**Retired/Removed jobs** (no longer in live registry):
   223|- `97eacc1cb3fa` codex-online-check — one-shot job, completed
   224|- `6b5fe0d2220c` cmo-dispatch-orchestrator — removed from registry
   225|- `415e88f0` wp-plugin-rishi-reminder — removed from registry  
   226|- `904c65910bfe` moxie-forward-reports-to-telegram — removed from registry
   227|
   228|---
   229|
   230|## Completed Deliverables
   231|| Date | Employee | File | Status |
   232||------|----------|------|--------|
   233|| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
   234|| 2026-03-31 | Mira | /root/moxie/products/formbeep/traffic-vs-keywords.md | COMPLETED |
   235|| 2026-03-31 | Orion | /root/moxie/products/formbeep/outbound/outbound-pack.md | COMPLETED |
   236|| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
   237|| 2026-03-31 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED |
   238|| 2026-04-01 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED — Monthly competitor scan (WPForms WA live, Getform WA+SMS roadmap, 4 new entrants) |
   239|| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
   240|| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
   241|| 2026-03-31 | Ember | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md | COMPLETED |
   242|| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-post-comment-scripts.md | COMPLETED |
   243|| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-manual-posting-plan-gst-nonus-v1.md | COMPLETED |
|| 2026-04-02 | Ember | /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md | COMPLETED — Full subreddit rules table (28 subs) + activity log + quick-ref + posting guardrails |
   244|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
   245|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions-p1.md | COMPLETED (P1 submission pack ready; execution awaits credentials) |
   246|| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
   247|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
   248|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
   249|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
   250|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |
   251||| 2026-03-31 | Luna | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md | COMPLETED |
   252||| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md | COMPLETED
   253||| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/platform-partner-outreach.md | COMPLETED
   254||| 2026-04-01 | Pax | /root/moxie/products/formbeep/partnerships/platform-applications-week3.md | COMPLETED
||| 2026-04-02 | Luna | /root/moxie/products/formbeep/lifecycle/win-back-emails.md | COMPLETED — 3-email win-back sequence (Day 1/3/7) + pre-churn triggers + segmentation matrix + behavioral onboarding handoff
   255|
   256|---
   257|
## Rishi Action Items (Requires Human)
1. WordPress plugin resubmission (founder-owned) — implement fixes + resubmit when you're ready (see /root/moxie/products/formbeep/wp-plugin-fixes.md)
2. After approval: execute post-approval WP launch plan (I'll keep it ready on disk)
3. Directory submissions — inbox confirmed as hello@formbeep.com; share any existing directory accounts (for Jax)
4. **REWORK REQUESTED** Kiro blog posts (do not publish yet):
   - Drafts:
     - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md
     - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md
   - Required fixes:
     - Make them longer / more rankable (~1200–1800 words)
     - Correct: contact email = hello@formbeep.com
     - Correct: free tier = 15 submissions/month
     - Set slugs: whatsapp-without-zapier/ and formbeep-vs-zapier/
     - Research Zapier→WhatsApp reality (out-of-the-box vs needs WhatsApp Business API provider like Twilio/360dialog/Meta Cloud API)
     - Add a comparison table in the “vs Zapier” post
     - Add `thumb_prompt:` frontmatter to each post (thumbnail generation prompt text)
5. (Ops) If HQ pushes are needed: confirm MOXIE_GITHUB_WRITE_PAT in /opt/data/.env has write access to rishikeshsreehari/moxie
   267|
   268|---
   269|
   270|## Rubric & Scoring System (NEW — Auto-wired)
   271|**Every completed task is automatically scored against the Employee Rubric.**
   272|
   273|### How it works:
   274|1. Task completes → Employee updates orchestration.md
   275|2. `task-scorer.py` auto-runs: scores 7 dimensions (1-5), weighted overall
   276|3. Scorecard saved to: `/root/moxie_hq/cmo/scores/{employee}/{task_id}.md`
   277|4. SOUL.md auto-updated with: Recent Scores table + Current Improvement Focus
   278|5. "Dreaming" reflection triggered: employee reflects on what worked/didn't
   279|
   280|### Scoring Dimensions (weights):
   281|- Output completeness: 20%
   282|- Business impact: 25% (30% for Copy/Distribution/Paid)
   283|- Accuracy & evidence: 15% (25% for Analytics)
   284|- Speed/cycle time: 10%
   285|- Autonomy & unblockability: 10% (15% for Distribution)
   286|- Reusability/systemization: 10%
   287|- Communication quality: 10%
   288|
   289|### Auto Pass/Fail Gates:
   290|- FAIL: No output file written
   291|- FAIL: Claims "working" without verification
   292|- FAIL: Violates scope (pushes to product repo)
   293|
   294|### CMO Self-Scoring:
   295|- Weekly self-assessment against CMO Orchestration Rubric
   296|- Saved to: `/root/moxie_hq/cmo/scores/moxie/weekly-{date}.md`
   297|- Dimensions: Throughput, Outcome progress, Signal quality, Token efficiency, Reliability, Modularity
   298|
   299|### Tools:
   300|- `python3 /root/moxie_hq/cmo/tools/task-scorer.py <employee> <task_id> <output_file>`
   301|- `python3 /root/moxie_hq/cmo/tools/token-optimizer.py [--apply]`
   302|- `python3 /root/moxie_hq/cmo/tools/cmo-self-score.py`
   303|
   304|## Token Optimization Rules
   305|- Hourly crons: **All workers currently scheduled** — monitor for idle
   306|- Auto-pause threshold: 6+ hours idle (no tasks completed)
   307|- Governance cron checks usage daily; pauses idle workers automatically
   308|- If free model quota tight: stagger to 2 workers per hour max
   309|- Worker SOULs are company-framed and must read product assignments from orchestration.md before each cycle
   310|
   311|## Codex Deep Audit (ONE-SHOT)
   312|- Previous one-shot job `codex-5hr-resume-premium` (Cron ID: 1e17a419b9e4) is **no longer present** in the live cron registry (treat as completed/retired).
   313|- Current premium “resume” job in the live registry: `codex-weekly-resume-premium` (Cron ID: ca6591a837b7) — schedule: once at 2026-04-06 17:30 (GST, +04:00)
   314|- Expected audit output path (if/when run): /root/moxie/cmo/orchestration-audit.md
   315|
   316|## Product Assignments (Multi-product ready)
   317|| Product | Status | Priority | Assigned Employees |
   318||---------|--------|----------|-------------------|
   319|| FormBeep | Active (Sprint 1) | P0 | All employees |
   320|| Product 2 | Not yet launched | N/A | TBD |
   321|| Product 3 | Not yet launched | N/A | TBD |
   322|
   323|**How this works:** When a second product is added, update this table. Workers read orchestration.md, see which products are active, and allocate their time accordingly. By default, all effort goes to the currently active product(s); FormBeep is just the current sprint.
   324|
   325|**Employee flexibility:** All employees are designed to be product-agnostic. Their SOUL files define their role (research, outreach, analytics, etc.) — not the product. The product assignments above determine where they focus their effort each cycle. Workers should read this table before each cycle to know which product(s) to work on.
   326|