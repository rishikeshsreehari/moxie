# Moxie Team -- Sapiens Technology LLC Growth Org Chart

Last updated: 2026-03-31

## Leadership
| Name | Role | Reports To |
|------|------|------------|
| Moxie | CMO / growth lead (orchestrator, strategy, Rishi comms) | Rishi |

## Active Team

### Vale -- Competitor Intelligence Lead
**Scope:**
- Deep-dive on direct competitors (Beepmate, Web2Phone)
- Pricing teardowns, feature comparison matrices
- Founder profiling (Reddit, IndieHackers, LinkedIn)
- Identifying exploitable weaknesses
- Track new market entrants monthly
- Map competitor keyword targeting

**Current Task:** Beepmate + Web2Phone deep-dive
**Founder Intel:** Beepmate=u/adambengur, Web2Phone=u/ConferenceOnly1415
**Status:** Dispatched (cron: vale-competitor-deepdive)

### Astra -- Growth Research Lead
**Scope:**
- Keyword research and SERP analysis
- SEO content planning and topic clusters
- Market sizing and audience segmentation
- WordPress plugin directory research
- Traffic source analysis
- Search volume research

**Current Task:** WP form-notification plugin market analysis
**Status:** Dispatched (cron: astra-wordpress-market)

### Kiro -- Conversion Copy Lead
**Scope:**
- Landing page copy (headline, features, pricing page)
- Blog post writing (2-3/week targeting low-competition keywords)
- Email sequences (onboarding, drip campaigns)
- Ad copy (Reddit, Google)
- A/B test hypothesis generation

**Current Task:** None -- awaiting competitor intel
**Status:** BLOCKED (waiting on Vale)

### Ember -- Outreach & Distribution Lead
**Scope:**
- Reddit engagement strategy (posting, commenting, community presence)
- SaaS directory submissions (ProductHunt, AlternativeTo, G2, Capterra, BetaList)
- Integration marketplace submissions (Webflow, Framer, WordPress plugin directory)
- Cold outreach targets (agencies, SMBs, freelancer communities)
- Partnership prospecting

**Current Task:** None yet
**Status:** BLOCKED (waiting on Vale + Astra intel)

### Forge -- Product/Codebase Inspector
**Scope:**
- WordPress plugin code audit and fix recommendations
- Integration health checks (Webflow page, Framer plugin)
- Technical SEO audit (page speed, structured data, broken links)
- Product change log tracking
- Code review for resubmissions

**Current Task:** WP plugin code review for WordPress directory resubmission
**Status:** BLOCKED (waiting for Codex premium quota)

### Mira -- Analytics & Reporting Lead
**Scope:**
- Daily traffic and usage tracking
- Conversion rate monitoring
- Analytics dashboard maintenance
- Cron health reporting
- Weekly growth review compilation
- Codex usage tracking
- **Umami dashboard analysis** -- top pages, traffic sources, time-on-page, bounce rates
- **Funnel tracking** -- visits → signup → connect WhatsApp → first submission → paid
- **Blog traffic analysis** -- which posts/pages drive the most visits, what topics to double-down on

**Current Task:** Daily/weekly traffic/search crons active + Umami dashboard audit queued
**Status:** ACTIVE (crons running)
**Note:** Umami website ID: 750e37be-3e04-4672-abe8-a2983afb9a4d (cloud.umami.is)

### Jax -- SaaS Growth Operations Lead
**Scope:**
- Submit FormBeep to 40+ SaaS directories (ProductHunt, AppSumo, BetaList, AlternativeTo, GetApp, etc.)
- Directory listing optimization (descriptions, screenshots, categories)
- Review generation campaigns
- Competitor backlink gap analysis
- Track submission status and follow-ups
- Affiliate program setup

**Current Task:** Building master directory submission list (40+ sites)
**Status:** Dispatched (cron: jax-saas-directory-list)

---

## Task Cascade (Once Intel Arrives)

1. Vale delivers competitor deep-dive
2. Kiro writes landing page copy using competitor gaps
3. Ember begins outreach + directory submissions
4. Jax handles 40+ directory submissions
5. Forge audits WP plugin code for resubmission
6. Astra feeds Kiro long-tail keyword targets for blog posts
7. Mira tracks all metrics and reports weekly

## Blockers
- Telegram bot token truncated -- all cron delivery to Telegram fails (Rishi to fix on host)
- Codex 5-hour limit hit -- Forge and Kiro premium tasks wait until 3:26 AM GST
- WP plugin resubmission -- Rishi needs to review and apply code changes
- GitHub write PAT broken -- commits not pushing to origin (known issue)
