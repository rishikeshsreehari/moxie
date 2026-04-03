# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
# Last updated: 2026-04-03T02:15:11Z
# 
# HOW THIS WORKS:
# Every cron job reads this file for context. When done, it updates relevant sections.
# Moxie (CMO) reviews this file and decides next actions.
# No manual prompt updates needed — agents read state from here.
# 
# SYSTEM IMPROVEMENTS (v2):
# - Atomic state updates: workers write to tmp files first, then rename
# - Retry logic: failed tasks get marked RETRY(1/3) before escalation
# - Task prioritization: P0 (blockers), P1 (revenue), P2 (growth), P3 (ops)
# - KPI tracking: every task completion updates KPI progress metrics
# - Cron collision mitigation: workers staggered across the hour (no longer all at :05)
# - Model stability: worker crons pinned to Codex-compatible models (avoid max_retries_exhausted from provider/model mismatch)
#
# DELEGATION SYSTEM (HQ, product-agnostic):
# - "Do not run tooling during live chat; queue work orders instead." Append to: /root/moxie_hq/cmo/delegation-queue.md
# - During ops cycle (or by the orchestration reconciler when appropriate), run:
#     python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py
#     python3 /root/moxie_hq/cmo/scripts/process_artifacts.py
# - These processors ONLY edit HQ files under /root/moxie_hq/cmo and do not require new cron scheduling.

---

## Mission
- Company: Sapiens Technology LLC (SapiensTech)
- Goal: grow a portfolio of indie products to consistent revenue via repeatable acquisition + conversion systems

## Active Product (current sprint)
- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
- Target: English-speaking SMBs, agencies, freelance devs
- 30-day goals: 10 paid users, $100 MRR, more organic traffic
- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory

---

## Known Blockers
| Blocker | Owner | Status | Action Needed |
|---------|-------|--------|---------------|
| Codex 5-hour limit hit | System | RESOLVED | Premium window available now (reset completed) |
| WordPress plugin resubmission (WP.org) | Rishi | BLOCKED (Founder-owned) | Do not touch/iterate in automation. Rishi will implement + resubmit. After approval, execute post-approval launch plan. |
| Directory submissions (P1) require founder credentials/verification | Jax + Rishi | BLOCKED | Provide any existing directory accounts / inbox verification access for hello@formbeep.com (see issues_rishi.md) |
| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked "worker not configured" | Moxie | RESOLVED | Fixed cron providers to OpenRouter where needed; all workers producing outputs; Pax first task COMPLETED |
| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
| Hermes config backup | Moxie | COMPLETED | Config backed up to /root/moxie_hq/infrastructure/hermes/ |
---

## Employee State

NOTE: All employees are SapiensTech (HQ) employees (role-based, product-agnostic). The current sprint focus is FormBeep, so most tasks route there, but no one is “hired for a product”.

### Vale — Competitor Intelligence Lead
- SOUL: /root/moxie/cmo/employees/vale-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: (StackStats) Reddit scanning plan — **COMPLETED** (2026-04-02T10:00Z)
- Last output: /root/moxie/products/stackstats/outreach/reddit-scan-plan.md
- Source intel artifact: /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md (generated 2026-04-01)
- Blockers: None for analysis. Note: Reddit execution still needs credentials (see issues_rishi.md)
- Founder activity (from new intel): Beepmate u/adambengur (2 posts, 25 comments) and Web2Phone u/ConferenceOnly1415 (25 posts, 25 comments)
- Key April findings: WPForms native WA (Mar 5), Getform WA live + SMS Q2 roadmap, WANotifier commerce integrations, 4 new direct competitors detected (FormToWA, SendForm.io, PingForms, NotifyStack)
- Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n, FormToWA, SendForm.io, PingForms, NotifyStack
- Idle-cycle deliverable: /root/moxie/products/formbeep/pricing-war-room-april-2026.md — Pricing decision analysis ($4 vs $4.99), feature gap matrix, recommend hold price + lean into SMS moat
### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: IDLE / COMPLETED
- Last completed task: (FormBeep) Run DataForSEO SERP sampling for keyword discovery — **COMPLETED** (2026-04-02T12:15Z)
- Output: /root/moxie/products/formbeep/seo/serp-opportunity-brief.md
- Previous: (StackStats) SERP brief — COMPLETED (2026-04-02T12:00Z)
- Previous: (FormBeep) SERP demand probe + keyword roadmap — COMPLETED (2026-04-02T07:00Z)
- Next task after completion: Ready for next assignment — SERP briefs shipped for both products; Rumi's 6-page outlines for both products are done
- Blockers: None
### Kiro — Conversion Copy Lead
|- SOUL: /root/moxie/cmo/employees/kiro-soul.md
|- Current output dir (sprint): /root/moxie/products/formbeep/copy/
|- Status: COMPLETED
|- Current task: REWORK 2 blog posts per founder feedback (length + factual fixes + Zapier/WhatsApp research + comparison table + thumbnail prompts) — **COMPLETED** (2026-04-01T22:45Z)
|- Last output:
  - /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md (~1,650 words, slug: whatsapp-without-zapier)
  - /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md (~1,720 words, slug: formbeep-vs-zapier)
|- Deliverables: Both posts expanded to target length, factual fixes applied (hello@formbeep.com, 15 submissions/month), frontmatter updated (slug + thumb_prompt), Zapier→WhatsApp API requirements research incorporated, comparison table added to vs post
|- Blockers: None

### Ember — Outreach & Distribution Lead
- SOUL: /root/moxie/cmo/employees/ember-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/outreach/
- Status: COMPLETED (execution blocked on creds)
- Current task: Manual Reddit posting plan (Non-US/GST focus) + subreddit rules checklist + posting windows + verification steps — **COMPLETED** (2026-04-01T17:32Z)
- Last output: /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md (2026-04-02 — full rules table + activity log + quick-ref)
- Previous outputs: reddit-manual-posting-plan-gst-nonus-v1.md (2026-04-01), reddit-post-comment-scripts.md (2026-04-01), reddit-campaign-plan.md (2026-03-31), reddit-strategy.md (2026-03-31)
- Completed deliverables: reddit-strategy.md, reddit-campaign-plan.md, reddit-post-comment-scripts.md, manual-posting-plan-gst-nonus-v1.md
- Next task after completion: Execute Week 1 posting — **BLOCKED** on Reddit account credentials (see issues_rishi.md)
- Blockers: Reddit account credentials required for all posting execution (see issues_rishi.md)

### Forge — Full Stack Engineer
- SOUL: /root/moxie/cmo/employees/forge-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: BLOCKED (GSC credentials required)
- Current task: Validate GSC indexing post-SEO-fixes — **BLOCKED** (reason: GSC credentials required)
- Task ID: gsc-validation-20260404
- Output path: /root/moxie/products/formbeep/analytics/gsc-post-seo-validation.md
- Last completed task: (FormBeep) Repo copy/UX audit — **COMPLETED** (2026-04-02T17:45Z)
- Last output: /root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md
- Blockers: GSC credentials required to access Index Coverage and impression data

### Mira — Analytics & Reporting Lead
- SOUL: /root/moxie/cmo/employees/mira-soul.md
- Current output dir (sprint): /root/moxie/products/stackstats/
- Status: IDLE (cron active; queued tasks pending)
- Previous task: (StackStats) Pull Umami Cloud analytics — REASSIGNED to Jax (see dispatch-queue.md) because deliverable was missing after promotion.
- Output path (still the same): /root/moxie/products/stackstats/analytics/umami-summary.md
- Next task: FormBeep monitoring scaffold + GSC vs Umami study (will remain blocked until GSC access is provided)
- Blockers: FormBeep GSC credentials required for GSC-based reporting
- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv

### Nova — Paid Acquisition Lead
- SOUL: /root/moxie/cmo/employees/nova-soul.md
- Current output dir (sprint): /root/moxie/cmo/sops/
- Status: COMPLETED
- Current task: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) — **COMPLETED**
- Last output: /root/moxie/cmo/sops/paid-ads-sop.md
- Next task after completion: Formalize campaign naming + UTM taxonomy in configs/templates + ship first tracked campaign for FormBeep (Google Search BOF)
- Blockers: None

### Jax — SaaS Growth Operations Lead
- SOUL: /root/moxie/cmo/employees/jax-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: COMPLETED (all P0 tasks done; awaiting next assignments)
- Current task: (StackStats) Live site snapshot (main + demo) — **COMPLETED** (2026-04-02T19:20:00Z)
- Task ID: jax-20260402_stackstats_snapshot
- Output path: /root/moxie/products/stackstats/dev-notes/live-site-snapshot.md
- Last completed task: (StackStats) Live site snapshot — COMPLETED (2026-04-02T19:20:00Z)
- Blockers: None
- Next queued tasks: None (awaiting new assignment)

### Rumi — Blog & Content Analyst
- SOUL: /root/moxie/cmo/employees/rumi-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: (HQ) X content OS (like Reddit tracker): build local script to infer founder tone from X export + analyze what worked; output a daily plan that includes 1 original post + "reply guy" mode (10 replies/day). — **COMPLETED** (2026-04-02T09:04Z)
- Task ID: rumi-20260402_083000-x1e9c
- Output path: /root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md
- Last completed task: (HQ) Platform×product posting matrix — **COMPLETED** (2026-04-02T03:15Z)
- Output: /root/moxie_hq/cmo/strategy/channel-matrix-all-products.md
- Previous completed task: (StackStats) 6 SEO landing page outlines — **COMPLETED** (2026-04-02T03:27Z)
- Output: /root/moxie/products/stackstats/seo/page-outlines.md
- Next task after completion: Await next assigned task
- Blockers: None

### Pax — Partnerships / BD Lead
- SOUL: /root/moxie/cmo/employees/pax-soul.md
- Current output dir (sprint): /root/moxie/products/formbeep/partnerships/
- Status: COMPLETED
- Current task: Week 3 submissions (Carrd + Typedream integration packages + agency outreach to top 15 targets) — **COMPLETED**
- Last output: /root/moxie/products/formbeep/partnerships/platform-applications-week3.md
- Next task after completion: Send agency outreach emails once verified contact info obtained; publish formbeep.com/integrations reciprocal directory; follow up on Week 1-2 platform application reviews
- Blockers: Portal credentials (Webflow/Framer/Glide/Softr), Reddit account for community posts, verified agency email contacts, hello@formbeep.com access for sending

### Luna — Lifecycle / CRM Lead
|- SOUL: /root/moxie/cmo/employees/luna-soul.md
|- Current output dir (sprint): /root/moxie/products/formbeep/lifecycle/
|- Status: COMPLETED
|- Current task: Win-back email sequence for churned users — **COMPLETED** (2026-04-02T08:52Z)
|- Last output: /root/moxie/products/formbeep/lifecycle/win-back-emails.md
|- Previous output: /root/moxie/products/formbeep/lifecycle/onboarding-emails.md
|- Next task after completion: Continue lifecycle optimization (retention triggers, segmentation)
|- Blockers: None

### Orion — Outbound Lead (Cold Email)
|- SOUL: /root/moxie/cmo/employees/orion-soul.md
|- Current output dir (sprint): /root/moxie/products/formbeep/outbound/
|- Status: COMPLETED
|- Current task: Prospect list refresh from competitor intel — **COMPLETED** (2026-04-02T08:15Z)
|- Last output: /root/moxie/products/formbeep/outbound/prospect-refresh.md
|- Previous output: /root/moxie/products/formbeep/outbound/outbound-pack.md
|- Next task after completion: Continue outbound optimization (subject tests, sequence refinement)
|- Blockers: Sending infrastructure (email warmup/domain setup) required for actual outreach execution

### Iris — Repo Copy Auditor
- SOUL: /root/moxie/cmo/employees/iris-soul.md
- Current output dir (sprint): /root/moxie_hq/products/formbeep/dev-notes/
- Status: IDLE (cron active; queued tasks pending)
- Previous task: (FormBeep) Repo copy audit — REASSIGNED to Forge (see dispatch-queue.md) because deliverable was missing after promotion.
- Output path (still the same): /root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md
- Next task: Weekly copy/UX audits once an Iris worker is configured (or continue routing via Forge)
- Blockers: None


### Moxie — CMO / Orchestrator
- SOUL: /root/moxie_hq/SOUL.md
- Current output dir (sprint): /root/moxie_hq/cmo/
- Status: IN_PROGRESS (self-review)
- Current task: Deep CMO self-review — **IN_PROGRESS** (task ID: moxie-20260402_002635-b85aa2; output: /root/moxie_hq/cmo/reports/moxie-self-score-2026-04-02.md)
- Previous: (FormBeep) Postmortem — **COMPLETED** (2026-04-02T15:33Z); (HQ) Create all-products Founder Voice / Build-in-Public strategy — **COMPLETED** (2026-04-02T11:00Z)
- Last output: /root/moxie_hq/cmo/postmortems/2026-04-01-formbeep-failures.md
- Next task: Create master SOP_INDEX.md — **QUEUED** (task ID: sop-index-soul-links-20260402)
- Blockers: None
---

### Forge — Full Stack Engineer (additional task)
- Current task: (*) Review analytics report and update growth metrics — **COMPLETED** (completed 2026-04-02T12:40Z)
- Output path: /root/moxie_hq/cmo/analytics/review-{artifact_relpath}.md
- Blockers: None
---

## Active Crons (Source of truth: `hermes cron list`)

**Editing rule:** do not edit jobs via this table. Update jobs using `hermes cron edit <cron_id> ...` and then reconcile this table to match.

Last verified: 2026-04-02T19:16:00Z

||| Cron ID | Name | Schedule | Deliver | Next run (UTC) | Repeats | State |||---|---|---|---|---|---|---|
|| 6effbb32 | formbeep-daily-user-count-checkin | every 1440m | local | 2026-04-02T14:06:30+00:00 | ∞ | active |
|| aba07be5 | formbeep-daily-traffic-check | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | ∞ | active |
|| 513b777e | formbeep-search-check | 0 10 * * 1,4 | local | 2026-04-02T10:00:00+00:00 | ∞ | active |
|| 753d42f3 | formbeep-weekly-growth-review | 0 11 * * 1 | local | 2026-04-06T11:00:00+00:00 | ∞ | active |
|| ae770f4f | formbeep-hourly-heartbeat | 6 * * * * | local | 2026-04-02T05:06:00+00:00 | ∞ | active |
|| 52af5ec9 | codex-dashboard-update-checkin | every 720m | local | 2026-04-02T14:43:36+00:00 | ∞ | active |
|| b0492991 | moxie-memory-skill-audit | every 720m | local | 2026-04-02T07:30:09+00:00 | ∞ | active |
|| ca6591a8 | codex-weekly-resume-premium | once at 2026-04-06 17:30 | local | 2026-04-06T17:30:00+04:00 | 0/1 | active |
|| 0526cbc1 | weekly-free-models-reminder | 0 17 * * 2 | local | 2026-04-07T17:00:00+00:00 | ∞ | active |
|| 647387ae | mira-daily-kpi | 0 10 * * * | local | 2026-04-02T10:00:00+00:00 | 10/100 | active |
|| a468835d | vale-monthly-competitor-scan | 0 10 1 * * | local | 2026-05-01T10:00:00+00:00 | 1/100 | active |
|| 2553a683 | moxie-daily-governance | 0 * * * * | local | 2026-04-02T11:00:00+00:00 | 61/100 | active |
|| 8bcfe505 | vale-worker | 12 * * * * | local | 2026-04-02T13:12:00+00:00 | 63/100 | active |
|| 7067633e | astra-worker | 17 * * * * | local | 2026-04-02T13:17:00+00:00 | 64/100 | active |
|| 3171d2c2 | kiro-worker | 42 * * * * | local | 2026-04-02T12:42:00+00:00 | 61/100 | active |
|| eb803b7d | ember-worker | 32 * * * * | local | 2026-04-02T13:32:00+00:00 | 61/100 | active |
|| 401e59cc | forge-worker | 37 * * * * | local | 2026-04-02T12:37:00+00:00 | 62/100 | active |
|| 4bdcef11 | jax-worker | 22 * * * * | local | 2026-04-02T13:22:00+00:00 | 61/100 | active |
|| affd389a | rumi-worker | 27 * * * * | local | 2026-04-02T12:27:00+00:00 | 62/100 | active |
|| af7f3c07 | moxie-daily-self-improvement | 0 20 * * * | local | 2026-04-02T20:00:00+00:00 | 2/100 | active |
|| 91520aa6 | nova-worker | 47 * * * * | local | 2026-04-02T13:47:00+00:00 | 60/100 | active |
|| 5b9c6eb7 | issues-rishi-watch | every 240m | local | 2026-04-02T12:46:52+00:00 | 15/200 | active |
|| 3e93c4f5 | luna-worker | 52 * * * * | local | 2026-04-02T13:52:00+00:00 | 62/100 | active |
|| cf1a8f9e | pax-worker | 57 * * * * | local | 2026-04-02T13:57:00+00:00 | 60/100 | active |
|| b0e9c513 | iris-weekly-formbeep-repo-copy-audit | 30 9 * * 1 | local | 2026-04-06T09:30:00+00:00 | 0/200 | active |
|| 0ed491f6 | orion-worker | 2 * * * * | local | 2026-04-02T13:02:00+00:00 | 62/200 | active |
|| 868bd30f | moxie-hq-autocommit-push | every 30m | local | 2026-04-02T10:42:51+00:00 | ∞ | active |
|| 1c008e06 | moxie-orchestration-reconciler | 13 * * * * | local | 2026-04-02T13:13:00+00:00 | 52/100 | active |
|| c342e174 | opencode-go-weekly-limit-reset-reminder | 26 13 * * 1 | local | 2026-04-06T13:26:00+00:00 | ∞ | active |
||| 7af300e6 | cmo-delegation-queue-runner | */15 * * * * | local | 2026-04-02T19:15:00+00:00 | ∞ | active |
|| 8c6364f4 | FormBeep SMS SEO reminder (2 weeks) | once at 2026-04-16 12:00 | origin (Telegram) | 2026-04-16T12:00:00+00:00 | 0/1 | active | ⚠️ One-shot reminder; delivers to Telegram (budget-sensitive)

**Retired/Removed jobs** (no longer in live registry):
- `01471699` cmo-deep-audit-5-4-2026-04-02 — one-shot deep audit job, completed/retired
- `97eacc1cb3fa` codex-online-check — one-shot job, completed
- `6b5fe0d2220c` cmo-dispatch-orchestrator — removed from registry
- `415e88f0` wp-plugin-rishi-reminder — removed from registry
- `904c65910bfe` moxie-forward-reports-to-telegram — removed from registry

---

## Completed Deliverables
| Date | Employee | File | Status |
|------|----------|------|--------|
| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
| 2026-03-31 | Mira | /root/moxie/products/formbeep/traffic-vs-keywords.md | COMPLETED |
| 2026-03-31 | Orion | /root/moxie/products/formbeep/outbound/outbound-pack.md | COMPLETED |
| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
| 2026-03-31 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED |
| 2026-04-01 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED — Monthly competitor scan (WPForms WA live, Getform WA+SMS roadmap, 4 new entrants) |
| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
| 2026-03-31 | Ember | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md | COMPLETED |
| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-post-comment-scripts.md | COMPLETED |
| 2026-04-01 | Ember | /root/moxie/products/formbeep/outreach/reddit-manual-posting-plan-gst-nonus-v1.md | COMPLETED |
|| 2026-04-02 | Ember | /root/moxie/products/formbeep/outreach/reddit-posting-tracker.md | COMPLETED — Full subreddit rules table (28 subs) + activity log + quick-ref + posting guardrails |
| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
|| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions-p1.md | COMPLETED (P1 submission pack ready; execution awaits credentials) |
|| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
|| 2026-04-02 | Rumi | /root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md | COMPLETED — fallback corpus tone fingerprint + daily reply-guy workflow + reply log format |
|| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |
|| 2026-03-31 | Luna | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md | COMPLETED |
|| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md | COMPLETED
|| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/platform-partner-outreach.md | COMPLETED
|| 2026-04-01 | Pax | /root/moxie/products/formbeep/partnerships/platform-applications-week3.md | COMPLETED
|||| 2026-04-02 | Luna | /root/moxie/products/formbeep/lifecycle/win-back-emails.md | COMPLETED — 3-email win-back sequence (Day 1/3/7) + pre-churn triggers + segmentation matrix + behavioral onboarding handoff
|| 2026-04-02 | Jax | /root/moxie/products/stackstats/analytics/umami-summary.md | COMPLETED — Tracking verified installed; API returns zero data (either no traffic or data access issue). Recommendations provided for founder verification.

---

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

---

## Rubric & Scoring System (NEW — Auto-wired)
**Every completed task is automatically scored against the Employee Rubric.**

### How it works:
1. Task completes → Employee updates orchestration.md
2. `task-scorer.py` auto-runs: scores 7 dimensions (1-5), weighted overall
3. Scorecard saved to: `/root/moxie_hq/cmo/scores/{employee}/{task_id}.md`
4. SOUL.md auto-updated with: Recent Scores table + Current Improvement Focus
5. "Dreaming" reflection triggered: employee reflects on what worked/didn't

### Scoring Dimensions (weights):
- Output completeness: 20%
- Business impact: 25% (30% for Copy/Distribution/Paid)
- Accuracy & evidence: 15% (25% for Analytics)
- Speed/cycle time: 10%
- Autonomy & unblockability: 10% (15% for Distribution)
- Reusability/systemization: 10%
- Communication quality: 10%

### Auto Pass/Fail Gates:
- FAIL: No output file written
- FAIL: Claims "working" without verification
- FAIL: Violates scope (pushes to product repo)

### CMO Self-Scoring:
- Weekly self-assessment against CMO Orchestration Rubric
- Saved to: `/root/moxie_hq/cmo/scores/moxie/weekly-{date}.md`
- Dimensions: Throughput, Outcome progress, Signal quality, Token efficiency, Reliability, Modularity

### Tools:
- `python3 /root/moxie_hq/cmo/tools/task-scorer.py <employee> <task_id> <output_file>`
- `python3 /root/moxie_hq/cmo/tools/token-optimizer.py [--apply]`
- `python3 /root/moxie_hq/cmo/tools/cmo-self-score.py`

## Token Optimization Rules
- Hourly crons: **All workers currently scheduled** — monitor for idle
- Auto-pause threshold: 6+ hours idle (no tasks completed)
- Governance cron checks usage daily; pauses idle workers automatically
- If free model quota tight: stagger to 2 workers per hour max
- Worker SOULs are company-framed and must read product assignments from orchestration.md before each cycle

## Codex Deep Audit (ONE-SHOT)
- Previous one-shot job `codex-5hr-resume-premium` (Cron ID: 1e17a419b9e4) is **no longer present** in the live cron registry (treat as completed/retired).
- Current premium “resume” job in the live registry: `codex-weekly-resume-premium` (Cron ID: ca6591a837b7) — schedule: once at 2026-04-06 17:30 (GST, +04:00)
- Expected audit output path (if/when run): /root/moxie/cmo/orchestration-audit.md

## Product Assignments (Multi-product ready)
| Product | Status | Priority | Assigned Employees |
|---------|--------|----------|-------------------|
| FormBeep | Active (Sprint 1) | P0 | All employees |
| Product 2 | Not yet launched | N/A | TBD |
| Product 3 | Not yet launched | N/A | TBD |

**How this works:** When a second product is added, update this table. Workers read orchestration.md, see which products are active, and allocate their time accordingly. By default, all effort goes to the currently active product(s); FormBeep is just the current sprint.

**Employee flexibility:** All employees are designed to be product-agnostic. Their SOUL files define their role (research, outreach, analytics, etc.) — not the product. The product assignments above determine where they focus their effort each cycle. Workers should read this table before each cycle to know which product(s) to work on.
