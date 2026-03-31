# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
# Last updated: 2026-03-31T00:17:40Z
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
| WordPress plugin pending review changes | Forge + Rishi | BLOCKED | Needs code review + Rishi action |
| Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
| Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
---

## Employee State

### Vale — Competitor Intelligence Lead
- SOUL: /root/moxie/cmo/employees/vale-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Beepmate + Web2Phone deep-dive — **COMPLETED**
- Last output: /root/moxie/products/formbeep/beepmate-web2phone-deepdive.md
- Next task after completion: Monthly competitor monitoring cron (pricing changes, new features, blog posts)
- Blockers: Reddit founder profile analysis blocked by Reddit network policy in this environment (requires login/dev token)
- Competitor founder intel:
  - Beepmate: u/adambengur
  - Web2Phone: u/ConferenceOnly1415
  - Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n

### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RETRY(1/3) (no deliverable file found)
- Current task: WordPress form-notification plugin market analysis
- Seed keyword file: /root/moxie/products/formbeep/seo-keywords.md
- Last output: **MISSING expected file** (/root/moxie/products/formbeep/wordpress-market-analysis.md) → RETRY(1/3)
- Next task after completion: Keyword v2 expansion (top-50 prioritized with intent/difficulty)
- Blockers: None

### Kiro — Conversion Copy Lead
- SOUL: /root/moxie/cmo/employees/kiro-soul.md
- Output dir: /root/moxie/products/formbeep/copy/
- Status: READY (dependency satisfied: Vale intel completed)
- Next task: Landing page copy (headline, features, pricing, FAQ), 2 blog posts from Astra's keyword list
- Blockers: None

### Ember — Outreach & Distribution Lead
- SOUL: /root/moxie/cmo/employees/ember-soul.md
- Output dir: /root/moxie/products/formbeep/outreach/
- Status: RETRY(1/3) (expected output missing)
- Current task: Reddit landscape research + 3 post drafts (expected output missing: /root/moxie/products/formbeep/reddit-strategy.md)
- Next task after completion: Community posting schedule, partnership outreach list
- Blockers: Partial (can start Reddit work, full campaign needs Vale's intel)

### Forge — Product/Codebase Inspector
- SOUL: /root/moxie/cmo/employees/forge-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: READY (Codex premium available)
- Current task: WordPress plugin code review for directory resubmission
- WP plugin location: TBD (needs discovery in /root/moxie/formbeep/)
- Next task: Technical SEO audit, integration health checks
- Blockers: Rishi review still required; Codex blocker cleared

### Mira — Analytics & Reporting Lead
- SOUL: /root/moxie/cmo/employees/mira-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: COMPLETED
- Current task: Umami traffic audit + funnel analysis — **COMPLETED**
- Umami: cloud.umami.is, website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d
- Analytics report: /root/moxie/products/formbeep/analytics-report.md
- Next task after completion: Set up weekly automated KPI report cron
- Blockers: Umami may require login for API access
- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv

### Nova — Paid Acquisition Lead
- SOUL: /root/moxie/cmo/employees/nova-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: IN_PROGRESS
- Current task: FormBeep paid acquisition plan + tracking + 3 starter campaigns (Google, Meta, Reddit)
- Next task after completion: Cross-product ads SOP (naming, UTMs, conversion taxonomy, reporting cadence)
- Blockers: None

### Jax — SaaS Growth Operations Lead
- SOUL: /root/moxie/cmo/employees/jax-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RETRY(1/3) (expected output missing)
- Current task: 40+ SaaS directory master list (expected output missing: /root/moxie/products/formbeep/directory-submissions.md)
- Next task after completion: Begin P1 directory submissions (ProductHunt, AlternativeTo, BetaList, SaaSHub)
- Blockers: None
- If directory submissions need founder credentials/email verification: note in this file and flag for Rishi

### Rumi — Blog & Content Analyst
- SOUL: /root/moxie/cmo/employees/rumi-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RETRY(1/3) (expected output missing)
- Current task: Competitor blog analysis + 30-day content calendar (expected output missing: /root/moxie/products/formbeep/content-calendar.md)
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
| 2026-03-31 | Astra/Ember/Jax/Rumi | Expected outputs missing | RETRY(1/3) |

---

## Rishi Action Items (Requires Human)
1. Fix Telegram bot token: Run `docker exec hermes-moxie sed -i 's|^TELEGRAM_BOT_TOKEN=.*|TEL...64|' /opt/data/.env` then restart gateway
2. Update GitHub write PAT in /opt/data/.env (MOXIE_GITHUB_WRITE_PAT needs write access to rishikeshsreehari/moxie)
3. Review WordPress plugin code changes from Forge when ready
4. Approve content calendar from Rumi before Kiro starts writing
5. Provide Jax with any directory account credentials needed (email-based signups)

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
