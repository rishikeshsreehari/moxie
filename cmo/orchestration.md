# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
# Last updated: 2026-03-31T07:04:49Z
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
| Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked “worker not configured” | Moxie | IN_PROGRESS | Fixed cron providers to OpenRouter where needed; unblocked queue rows from BLOCKED→QUEUED; verify next run produces outputs and governance promotes safely |
| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
---

## Employee State

### Vale — Competitor Intelligence Lead
- SOUL: /root/moxie/cmo/employees/vale-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: IN_PROGRESS
- Current task: Monthly competitor monitoring (pricing changes, new features, blog posts) — **IN_PROGRESS**
- Last output: /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
- Output (this task): /root/moxie/products/formbeep/competitor-monitoring.md
- Next task after completion: Quarterly competitor positioning refresh (pricing page screenshots + feature diff + “what changed”) 
- Blockers: Reddit founder profile analysis blocked by Reddit network policy in this environment (requires login/dev token)
- Competitor founder intel:
  - Beepmate: u/adambengur
  - Web2Phone: u/ConferenceOnly1415
  - Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n

### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: IN_PROGRESS
- Current task: Tally Forms growth teardown (channels, SEO/templates, PLG loops, distribution) + what we can copy for FormBeep
- Inputs: /root/moxie/products/formbeep/keyword-briefing.md + /root/moxie/products/formbeep/analytics-report.md
- Output: /root/moxie/products/formbeep/tally-growth-teardown.md
- Next task after completion: Keyword v2 expansion (top-50 prioritized with intent/difficulty)
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
- Status: IN_PROGRESS
- Current task: Reddit campaign launch plan (calendar + posting SOP + partnerships tie-in + ideal posting day/time based on active userbase)
- Next task after completion: Community posting schedule, partnership outreach list
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
- Status: IN_PROGRESS
- Current task: Traffic vs keyword opportunity map (use Umami + Astra keyword briefing)
- Last output: /root/moxie/products/formbeep/analytics-report.md
- Umami: cloud.umami.is, website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d
- Next task after completion: Set up weekly automated KPI report cron
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
- Current task: Competitor blog analysis + 30-day content calendar — **COMPLETED**
- Keyword seed: /root/moxie/products/formbeep/seo-keywords.md
- Next task after completion: Weekly content gap scan (what new topics emerged, what's trending)
- Blockers: None

---

## Active Crons (System-managed, DO NOT EDIT manually)
| Cron ID | Name | Schedule | Employee | Last Run | Status |
|---------|------|----------|----------|----------|--------|
| ae770f4f9ff8 | formbeep-hourly-heartbeat | every 60m | Moxie | See logs | OK |
| aba07be535ec | formbeep-daily-traffic-check | 0 10 * * * | Mira | Not yet fired | SCHED |
| 513b777e84ea | formbeep-search-check | 0 10 * * 1,4 | Astra/Mira | Not yet fired | SCHED |
| 753d42f32fbb | formbeep-weekly-growth-review | 0 11 * * 1 | Moxie/Mira | Not yet fired | SCHED |
| 1e17a419b9e4 | codex-5hr-resume-premium | 03:30 GST daily | Moxie | Pending | SCHED |
| ca6591a837b7 | codex-weekly-resume-premium | 2026-04-06 17:30 GST | Moxie | Pending | SCHED |
| f63bfbc548a6 | vale-competitor-deepdive | one-shot | Vale | Running | ACTIVE |
| c35598f90ddf | astra-wordpress-market | one-shot | Astra | Running | ACTIVE |
| 98f011592fdc | jax-saas-directory-list | one-shot | Jax | Pending | SCHED |
| a230996e123a | rumi-content-analysis | one-shot | Rumi | Pending | SCHED |
| e3d998d1f127 | mira-umami-audit | one-shot | Mira | Pending | SCHED |
| 069296011969 | ember-reddit-research | one-shot | Ember | Pending | SCHED |
| 97eacc1cb3fa | codex-online-check | every 30m x12 | Moxie | Pending | SCHED |

---

## Completed Deliverables
| Date | Employee | File | Status |
|------|----------|------|--------|
| 2026-03-31 | Mira | /root/moxie/products/formbeep/analytics-report.md | COMPLETED |
| 2026-03-31 | Vale | /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md | COMPLETED |
| 2026-03-31 | Astra | /root/moxie/products/formbeep/wordpress-market-analysis.md | COMPLETED |
| 2026-03-31 | Ember | /root/moxie/products/formbeep/reddit-strategy.md | COMPLETED |
| 2026-03-31 | Jax | /root/moxie/products/formbeep/directory-submissions.md | COMPLETED |
| 2026-03-31 | Rumi | /root/moxie/products/formbeep/content-calendar.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/landing-page-v1.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-whatsapp-without-zapier.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-post-formbeep-vs-zapier.md | COMPLETED |
| 2026-03-31 | Kiro | /root/moxie/products/formbeep/copy/blog-posts-v1.md | COMPLETED |

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
