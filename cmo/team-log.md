# Moxie Team Roster

Last updated: 2026-03-31

## Leadership
- **Moxie** — CMO. Speaks directly with Rishi. Orchestrates team.

## Team
| Name | Role | Status | Current Task |
|------|------|--------|--------------|
| Astra | Growth Research Lead | Active | Keyword v2 deep-dive, SERP analysis |
| Vale | Competitor Intelligence Lead | Active | Beepmate & Web2Phone deep-dive (incl. founder Reddit research) |
| Kiro | Conversion Copy Lead | Idle | Awaiting competitor intel before drafting landing copy |
| Mira | Analytics & Reporting Lead | Active | Weekly traffic tracker cron running |
| Forge | Product/Codebase Inspector | Idle | Waiting for Codex to review WP plugin code |
| Ember | Outreach & Distribution Lead | Idle | Awaiting competitor intel before building target list |

## Pending Rishi Actions
1. Replace truncated Telegram bot token in `/opt/data/.env` (blocks all cron delivery)
2. Review & fix WordPress plugin code changes (Forge will assist once Codex is back)
3. Decide WP plugin review changes scope

## Task Log (reverse chronological)

### 2026-03-31
- **Vale** → Beepmate + Web2Phone deep competitive analysis (pricing, features, traffic, founder Reddit IDs, weaknesses, messaging). Status: *dispatched — cron running in 2min*. Founder Reddit usernames provided: Beepmate=u/adambengur, Web2Phone=u/ConferenceOnly1415
- **Astra** → WordPress market analysis + plugin directory research. Status: *dispatched — cron running in 5min*
- **Astra** → Keyword v2 expansion (top-50 prioritized). Status: *pending retry*
- **Mira** → Traffic/search daily check cron running. Status: *scheduled*
- **Forge** → WP plugin code review for resubmission. Status: *on hold — waiting for Rishi + Codex*
- **Kiro** → Landing page conversion copy. Status: *blocked — needs competitor intel first*
- **Ember** → Outreach target list (agencies, SMBs). Status: *blocked — needs positioning intel first*

### 2026-03-30
- **Moxie** → CMO HQ setup: heartbeat.md, recurring-crons.md, usage tracking, identity
- **Moxie** → Pushed 4 commits to moxie repo (competitor v1, keyword v1, cron setup, usage snapshot)
- **Moxie** → Set up 7 cron jobs (heartbeat, traffic/search, weekly review, Codex-resume, etc.)
- **Telegram** → Bot token broken (truncated). Discovered, waiting for Rishi to fix.
