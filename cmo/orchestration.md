# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
# Last updated: 2026-03-31T08:00:00Z
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
| WordPress plugin pending review changes | Forge + Rishi | BLOCKED | Forge audit complete; Rishi to apply suggested changes + resubmit (see /root/moxie/products/formbeep/wp-plugin-fixes.md) |
| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked "worker not configured" | Moxie | RESOLVED | Fixed cron providers to OpenRouter where needed; all workers producing outputs; Pax first task COMPLETED |
| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
---

## Employee State

### Vale — Competitor Intelligence Lead
- SOUL: /root/moxie/cmo/employees/vale-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Monthly competitor monitoring — **COMPLETED** (2026-03-31)
- Last output: /root/moxie/products/formbeep/competitor-monitoring.md
- Next task after completion: Quarterly competitor positioning refresh (pricing page screenshots + feature diff + "what changed")
- Blockers: Reddit founder profile analysis blocked (requires login/dev token — logged in issues_rishi.md)
- Competitor founder intel:
  - Beepmate: u/adambengur
  - Web2Phone: u/ConferenceOnly1415
  - Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n
### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: SMS demand + keyword analysis — **COMPLETED** (2026-03-31)
- Last output: /root/moxie/products/formbeep/sms-keyword-analysis.md
- Next task after completion: All Astra sprint tasks COMPLETED — awaiting new assignments
- Blockers: None

### Kiro — Conversion Copy Lead
- SOUL: /root/moxie/cmo/employees/kiro-soul.md
- Output dir: /root/moxie/products/formbeep/copy/
- Status: COMPLETED
- Current task: 2 blog posts from Astra's keyword list — **COMPLETED**
- Last output: /root/moxie/products/formbeep/copy/blog-posts-v1.md
- Next task after completion: Draft 2–3 platform “money pages” (WordPress form → WhatsApp, Webflow form → WhatsApp, Framer form notifications) and one comparison page (FormBeep vs Web2Phone)
- Blockers: None

### Ember — Outreach & Distribution Lead
- SOUL: /root/moxie/cmo/employees/ember-soul.md
- Output dir: /root/moxie/products/formbeep/outreach/
- Status: COMPLETED
- Current task: Reddit campaign launch plan (calendar + posting SOP + partnerships tie-in + ideal posting day/time based on active userbase) — **COMPLETED**
- Last output: /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md
- Next task after completion: Begin Week 1 posting (Post A on Tue 14:00 UTC r/smallbusiness/Entrepreneur, Post B on Wed 14:00 UTC r/WordPress) + daily comment seeding. Ember should also check for any new Ember assignments in dispatch-queue.
- Blockers: None

### Forge — Product/Codebase Inspector
- SOUL: /root/moxie/cmo/employees/forge-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Technical SEO audit (page speed, structured data, meta tags) — **COMPLETED**
- Last output: /root/moxie/products/formbeep/technical-seo-audit.md
- Next task: (if approved) implement SEO fixes in Hugo templates: image optimization pipeline + taxonomy noindex + keywords delimiter
- Blockers: None for audit. WP plugin still awaiting Rishi to implement/apply suggested changes + resubmit on WP.org (see /root/moxie/products/formbeep/wp-plugin-fixes.md)

### Mira — Analytics & Reporting Lead
- SOUL: /root/moxie/cmo/employees/mira-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Traffic vs keyword opportunity map (use Umami + Astra keyword briefing) — **COMPLETED** (2026-03-31)
- Last output: /root/moxie/products/formbeep/traffic-vs-keywords.md
- Umami: cloud.umami.is, website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d
- Next task after completion: Improve KPI reporting outputs (no new cron jobs without approval)
- Blockers: None
- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv

### Nova — Paid Acquisition Lead
- SOUL: /root/moxie/cmo/employees/nova-soul.md
- Output dir: /root/moxie/cmo/sops/
- Status: COMPLETED
- Current task: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence) — **COMPLETED**
- Last output: /root/moxie/cmo/sops/paid-ads-sop.md
- Next task after completion: Formalize campaign naming + UTM taxonomy in configs/templates + ship first tracked campaign for FormBeep (Google Search BOF)
- Blockers: None

### Jax — SaaS Growth Operations Lead
- SOUL: /root/moxie/cmo/employees/jax-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: 40+ SaaS directory master list — **COMPLETED**
- Last output: /root/moxie/products/formbeep/directory-submissions.md
- Next task after completion: Prepare P1 directory submission assets (logos, banners, screenshots, copy) from the GitHub repo, then begin submissions (ProductHunt, AlternativeTo, BetaList, SaaSHub)
- Blockers: None
- If directory submissions need founder credentials/email verification: note in this file and flag for Rishi

### Rumi — Blog & Content Analyst
- SOUL: /root/moxie/cmo/employees/rumi-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Bi-weekly content gap scan + trending topic check — **COMPLETED** (2026-03-31)
- Last output: /root/moxie/products/formbeep/content-gap-scan.md
- Keyword seed: /root/moxie/products/formbeep/seo-keywords.md
- Next task after completion: Next bi-weekly scan (2026-04-10). Priority backlog: 4 P0/P1 topics flagged for Kiro drafts.
- Blockers: None

### Pax — Partnerships / BD Lead
- SOUL: /root/moxie/cmo/employees/pax-soul.md
- Output dir: /root/moxie/products/formbeep/partnerships/
- Status: COMPLETED
- Current task: Partnership target list (agencies + no-code builders + form tools) + 3 outreach templates — **COMPLETED** (2026-03-31)
- Last output: /root/moxie/products/formbeep/partnerships/targets-and-outreach.md
- Next task after completion: Begin P0 outreach (spread over 2 weeks), apply to platform partner programs (Webflow, Framer, Glide, Softr), build Bubble plugin
- Blockers: None

---

## Active Crons (Source of truth: `hermes cron list`)

**Editing rule:** do not edit jobs via this table. Update jobs using `hermes cron edit <cron_id> ...` and then reconcile this table to match.

| Cron ID | Name | Schedule | Deliver | Next run (UTC) | State | Last status |
|---|---|---|---|---|---|---|
| 7067633e99b9 | astra-worker | 17 * * * * | local | 2026-03-31 08:17:00Z | scheduled | ok |
| 52af5ec91c81 | codex-dashboard-update-checkin | every 720m | telegram:6699776435 | 2026-03-31 14:37:27.851179Z | scheduled | ok |
| ca6591a837b7 | codex-weekly-resume-premium | once at 2026-04-06 17:30 | local | 2026-04-06 17:30:00+04:00 | scheduled | — |
| eb803b7d69a3 | ember-worker | 32 * * * * | local | 2026-03-31 08:32:00Z | scheduled | ok |
| 401e59cc06f5 | forge-worker | 37 * * * * | local | 2026-03-31 08:37:00Z | scheduled | ok |
| aba07be535ec | formbeep-daily-traffic-check | 0 10 * * * | local | 2026-03-31 10:00:00Z | scheduled | — |
| 6effbb323126 | formbeep-daily-user-count-checkin | every 1440m | telegram:6699776435 | 2026-03-31 14:05:28.074031Z | scheduled | — |
| ae770f4f9ff8 | formbeep-hourly-heartbeat | 6 * * * * | telegram:6699776435 | 2026-03-31 08:06:00Z | scheduled | ok |
| 513b777e84ea | formbeep-search-check | 0 10 * * 1,4 | local | 2026-04-02 10:00:00Z | scheduled | — |
| 753d42f32fbb | formbeep-weekly-growth-review | 0 11 * * 1 | local | 2026-04-06 11:00:00Z | scheduled | — |
| b0e9c5135620 | iris-weekly-formbeep-repo-copy-audit | 30 9 * * 1 | local | 2026-04-06 09:30:00Z | scheduled | — |
| 5b9c6eb70662 | issues-rishi-watch | every 240m | telegram:6699776435 | 2026-03-31 07:59:37.636307Z | scheduled | ok |
| 4bdcef11fcc7 | jax-worker | 22 * * * * | local | 2026-03-31 08:22:00Z | scheduled | ok |
| 3171d2c2d4b2 | kiro-worker | 42 * * * * | local | 2026-03-31 08:42:00Z | scheduled | ok |
| 3e93c4f54be5 | luna-worker | 52 * * * * | local | 2026-03-31 07:52:00Z | scheduled | ok |
| 647387aeef66 | mira-daily-kpi | 0 10 * * * | local | 2026-03-31 10:00:00Z | scheduled | ok |
| 2553a6832a11 | moxie-daily-governance | 0 * * * * | telegram:6699776435 | 2026-03-31 08:00:00Z | scheduled | ok |
| af7f3c07b24b | moxie-daily-self-improvement | 0 20 * * * | telegram | 2026-03-31 20:00:00Z | scheduled | — |
| 868bd30fe7c1 | moxie-hq-autocommit-push | every 30m | local | 2026-03-31 08:15:47.101299Z | scheduled | ok |
| b0492991a3cd | moxie-memory-skill-audit | every 720m | local | 2026-03-31 19:14:06.559706Z | scheduled | — |
| 1c008e06fe40 | moxie-orchestration-reconciler | 13 * * * * | local | 2026-03-31 08:13:00Z | scheduled | — |
| 91520aa6ca57 | nova-worker | 47 * * * * | local | 2026-03-31 07:47:00Z | scheduled | ok |
| 0ed491f66432 | orion-worker | 2 * * * * | local | 2026-03-31 08:02:00Z | scheduled | ok |
| cf1a8f9eec33 | pax-worker | 57 * * * * | local | 2026-03-31 07:57:00Z | scheduled | ok |
| affd389a7783 | rumi-worker | 27 * * * * | local | 2026-03-31 08:27:00Z | scheduled | ok |
| a468835d1396 | vale-monthly-competitor-scan | 0 10 1 * * | local | 2026-04-01 10:00:00Z | scheduled | — |
| 8bcfe505aba3 | vale-worker | 12 * * * * | local | 2026-03-31 08:12:00Z | scheduled | ok |
| 0526cbc1e1b5 | weekly-free-models-reminder | 0 17 * * 2 | telegram:6699776435 | 2026-03-31 17:00:00Z | scheduled | — |
| 415e88f05397 | wp-plugin-rishi-reminder | every 240m | telegram:6699776435 | 2026-03-31 10:49:47.952239Z | scheduled | ok |

---

## Completed Deliverables
| Date | Employee | File | Status |
|------|----------|------|--------|
| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
| 2026-03-31 | Mira | /root/moxie/products/formbeep/traffic-vs-keywords.md | COMPLETED |
| 2026-03-31 | Orion | /root/moxie/products/formbeep/outbound/outbound-pack.md | COMPLETED |
| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
| 2026-03-31 | Vale | /root/moxie/products/formbeep/competitor-monitoring.md | COMPLETED |
| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
| 2026-03-31 | Ember | /root/moxie/products/formbeep/outreach/reddit-campaign-plan.md | COMPLETED |
| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |
| 2026-03-31 | Luna | /root/moxie/products/formbeep/lifecycle/onboarding-emails.md | COMPLETED |
| 2026-03-31 | Pax | /root/moxie/products/formbeep/partnerships/targets-and-outreach.md | COMPLETED |

---

## Rishi Action Items (Requires Human)
1. WordPress plugin resubmission — apply Forge’s fix list and resubmit (see /root/moxie/products/formbeep/wp-plugin-fixes.md)
2. Review/approve Forge’s WP plugin patch notes/package when ready
3. Directory submissions — inbox confirmed as hello@formbeep.com; share any existing directory accounts (for Jax)
4. Review/approve Kiro’s 2 blog drafts for publishing: /root/moxie/products/formbeep/copy/blog-posts-v1.md
5. (Ops) If HQ pushes are needed: confirm MOXIE_GITHUB_WRITE_PAT in /opt/data/.env has write access to rishikeshsreehari/moxie

---

## Note it down and see if it's unnecessary:
- Hourly crons may burn too many free model tokens. Plan to reduce to every 2h or 4h if quota gets tight. Governance cron will check token usage and adjust if needed.
- If workers report "no pending tasks" for 3+ consecutive cycles, pause their cron to save tokens.
- Monitor daily token usage across all workers. If we hit free model limits, stagger workers so only 2 fire per hour.
- Worker SOULs are company-framed and must read product assignments from orchestration.md before each cycle.

## Codex Deep Audit (ONE-SHOT)
- Cron ID: 1e17a419b9e4 (codex-5hr-resume-premium)
- Fires: once at 2026-03-31 03:30 GST
- This is a ONE-TIME task. It does NOT repeat. After firing, the system continues with the hourly worker schedule below.
- Audit output: /root/moxie/cmo/orchestration-audit.md

## Product Assignments (Multi-product ready)
| Product | Status | Priority | Assigned Employees |
|---------|--------|----------|-------------------|
| FormBeep | Active (Sprint 1) | P0 | All employees |
| Product 2 | Not yet launched | N/A | TBD |
| Product 3 | Not yet launched | N/A | TBD |

**How this works:** When a second product is added, update this table. Workers read orchestration.md, see which products are active, and allocate their time accordingly. By default, all effort goes to the currently active product(s); FormBeep is just the current sprint.

**Employee flexibility:** All employees are designed to be product-agnostic. Their SOUL files define their role (research, outreach, analytics, etc.) — not the product. The product assignments above determine where they focus their effort each cycle. Workers should read this table before each cycle to know which product(s) to work on.
