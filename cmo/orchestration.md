# Moxie CMO Orchestration State — FormBeep
# Last updated: 2026-03-31T00:32:00Z
# 
# HOW THIS WORKS:
# Every cron job reads this file for context. When done, it updates relevant sections.
# Moxie (CMO) reviews this file and decides next actions.
# No manual prompt updates needed — agents read state from here.

---

## Mission
- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
- Target: English-speaking SMBs, agencies, freelance devs
- 30-day goals: 10 paid users, $100 MRR, more organic traffic
- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory

---

## Known Blockers
| Blocker | Owner | Status | Action Needed |
|---------|-------|--------|---------------|
| Telegram bot token truncated in /opt/data/.env | Rishi | BLOCKED | Fix token on host: docker exec hermes-moxie sed -i 's|^TELEGRAM_BOT_TOKEN=.*|TELEGRAM_BOT_TOKEN=8365122447:AAE47_tmAgEovirMNwpJiBk4vsRbTMRr464|' /opt/data/.env |
| GitHub write PAT broken (403 on push) | Rishi | BLOCKED | Update MOXIE_GITHUB_WRITE_PAT in /opt/data/.env with write-access PAT |
| Codex 5-hour limit hit | System | WAITING | Resets at 3:26 AM GST (03:30 UAE time) daily |
| WordPress plugin pending review changes | Forge + Rishi | BLOCKED | Needs code review + Rishi action |
| Umami analytics — no one reviewing data | Mira | IDENTIFIED | Needs dashboard access/API key |

---

## Employee State

### Vale — Competitor Intelligence Lead
- SOUL: /root/moxie/cmo/employees/vale-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RUNNING
- Current task: Beepmate + Web2Phone deep-dive
- Last output: None yet
- Next task after completion: Monthly competitor monitoring cron (pricing changes, new features, blog posts)
- Blockers: None
- Competitor founder intel:
  - Beepmate: u/adambengur
  - Web2Phone: u/ConferenceOnly1415
  - Other competitors tracked: WPForms, Formspree, Getform, Basin, WANotifier, Zapier, Make, n8n

### Astra — Growth Research Lead
- SOUL: /root/moxie/cmo/employees/astra-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RUNNING
- Current task: WordPress form-notification plugin market analysis
- Seed keyword file: /root/moxie/products/formbeep/seo-keywords.md
- Last output: None yet
- Next task after completion: Keyword v2 expansion (top-50 prioritized with intent/difficulty)
- Blockers: None

### Kiro — Conversion Copy Lead
- SOUL: /root/moxie/cmo/employees/kiro-soul.md
- Output dir: /root/moxie/products/formbeep/copy/
- Status: BLOCKED
- Blocked on: Vale's competitor intel (needs positioning gaps to write differentiation copy)
- Next task: Landing page copy (headline, features, pricing, FAQ), 2 blog posts from Astra's keyword list
- Blockers: Vale's intel

### Ember — Outreach & Distribution Lead
- SOUL: /root/moxie/cmo/employees/ember-soul.md
- Output dir: /root/moxie/products/formbeep/outreach/
- Status: RUNNING
- Current task: Reddit landscape research + 3 post drafts
- Next task after completion: Community posting schedule, partnership outreach list
- Blockers: Partial (can start Reddit work, full campaign needs Vale's intel)

### Forge — Product/Codebase Inspector
- SOUL: /root/moxie/cmo/employees/forge-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: BLOCKED
- Current task: WordPress plugin code review for directory resubmission
- WP plugin location: TBD (needs discovery in /root/moxie/formbeep/)
- Next task: Technical SEO audit, integration health checks
- Blockers: Codex premium quota (needs 3:26 AM GST reset)

### Mira — Analytics & Reporting Lead
- SOUL: /root/moxie/cmo/employees/mira-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RUNNING
- Current task: Umami traffic audit + funnel analysis
- Umami: cloud.umami.is, website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d
- Analytics file: /root/moxie/products/formbeep/analytics.md
- Next task after completion: Set up weekly automated KPI report cron
- Blockers: Umami may require login for API access
- Codex tracking: /root/moxie/cmo/codex-usage.md + /root/moxie/cmo/codex-usage-tracker.csv

### Jax — SaaS Growth Operations Lead
- SOUL: /root/moxie/cmo/employees/jax-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RUNNING
- Current task: 40+ SaaS directory master list
- Next task after completion: Begin P1 directory submissions (ProductHunt, AlternativeTo, BetaList, SaaSHub)
- Blockers: None
- If directory submissions need founder credentials/email verification: note in this file and flag for Rishi

### Rumi — Blog & Content Analyst
- SOUL: /root/moxie/cmo/employees/rumi-soul.md
- Output dir: /root/moxie/products/formbeep/
- Status: RUNNING
- Current task: Competitor blog analysis + 30-day content calendar
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
| 2026-03-31 | Vale/Astra/Rumi/Ember/Mira/Jax | Pending — crons in progress | IN_PROGRESS |

---

## Rishi Action Items (Requires Human)
1. Fix Telegram bot token: Run `docker exec hermes-moxie sed -i 's|^TELEGRAM_BOT_TOKEN=.*|TELEGRAM_BOT_TOKEN=8365122447:AAE47_tmAgEovirMNwpJiBk4vsRbTMRr464|' /opt/data/.env` then restart gateway
2. Update GitHub write PAT in /opt/data/.env (MOXIE_GITHUB_WRITE_PAT needs write access to rishikeshsreehari/moxie)
3. Review WordPress plugin code changes from Forge when ready
4. Approve content calendar from Rumi before Kiro starts writing
5. Provide Jax with any directory account credentials needed (email-based signups)

---

## Notes
- All cron deliveries go to 'local' until Telegram is fixed
- Free model: qwen/qwen3-coder-480b-a35b:free (best available, rotates automatically)
- Codex resets daily at 03:30 GST (5-hour window) and weekly on April 6 at 17:30 GST
- Git commits use: Moxie <moxie@rishikeshs.com>
- Repo: /root/moxie_hq (symlinked from /root/moxie for cmo/ and products/)
- ALL employees MUST read KPIs at /root/moxie/cmo/kpis.md before executing tasks
