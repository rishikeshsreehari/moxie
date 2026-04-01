# Moxie CMO — KPI Progress Dashboard
# Last updated: 2026-04-01T20:00:00Z
# Automated updates via governance cron every 4h
# Workers update their own KPI sections when completing tasks

## Sprint Goal: 10 paid users, $100 MRR within 30 days (by 2026-04-30)
## Current Status: Day 2, Foundation built, awaiting execution blockers resolved

---

## Funnel Metrics (Live Tracking)
| Stage | Target/30d | Current | Progress | Source |
|-------|-----------|---------|----------|--------|
| Visitors | 3,800+ | 667 (last 30d, Umami) | 17.6% | Umami API snapshot |
| Signups | 130+ | 0 | 0% | FormBeep app |
| WhatsApp Connected | 100+ | 0 | 0% | FormBeep app |
| First Submission | 80+ | 0 | 0% | FormBeep app |
| Paid Users | 10 | 0 | 0% | Payment system |
| MRR | $100 | $0 | 0% | Payment system |

---

## Employee KPI Scorecard

### Vale — Competitor Intelligence Lead
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Competitor intel coverage | 2/2 in 48h | IN_PROGRESS | 0/2 done |
| Founder intel per competitor | Reddit IDs | FOUND | 2/2 (adambengur, ConferenceOnly1415) |
| Exploitable weaknesses found | 3+ per competitor | PENDING | 0/6 |
| Monthly scan (1st of month) | Next: 2026-04-01 | SCHEDULED | — |
| Pricing teardown completeness | All tiers mapped | IN_PROGRESS | 0/2 |

### Astra — Growth Research Lead  
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Keywords mapped to pages | 50+ in 7 days | IN_PROGRESS (seed done) | Partial |
| SERP top-5 analysis | All primary clusters | PENDING | 0/5 |
| WP plugin market analysis | Top 10 plugins with numbers | IN_PROGRESS | In progress |
| Content gap topics identified | 10+ nobody owns | PENDING | 0/10 |
| Search volume scored | All 50 keywords | PENDING | 0/50 |

### Kiro — Conversion Copy Lead
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Landing page conversion rate | 5% baseline | BLOCKED (needs Vale) | 0% |
| Blog output | 2-3 posts/week | BLOCKED (needs Astra+Rumi) | 0/week |
| CTA A/B variations | 2 in 14 days | BLOCKED | 0/2 |
| Draft velocity | <2h/post, <4h/page | N/A (blocked) | — |

### Ember — Outreach & Distribution Lead
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Reddit posts/week | 3-5 genuine | IN_PROGRESS (researching) | 0/3 |
| Community engagement | 10+ comments/week | PENDING | 0/10 |
| Referral traffic from Reddit | 50+ sessions/wk by Day 14 | NOT MEASURABLE yet | 0 |
| Partnership outreach | 5 convos/week | BLOCKED (needs Vale) | 0/5 |

### Forge — Product/Codebase Inspector
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| WP plugin approved | Published in 14 days | BLOCKED (Rishi + Codex) | 0% |
| Integration health | 0 broken | NOT CHECKED yet | Pending audit |
| Tech SEO issues fixed | All critical in 7 days | BLOCKED | Pending audit |
| Code review turnaround | <24h/issue | BLOCKED (Codex limit) | N/A |

### Mira — Analytics & Reporting Lead
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Umami data coverage | Sessions/pages/sources daily | COMPLETE | analytics-report.md + umami-full-data.json |
| Report accuracy | 0 guessed numbers | GREEN | 1 report delivered (2026-03-30) |
| Weekly KPI report | Mon 11:00 UTC | SCHEDULED | Next: 2026-04-06 |
| Funnel drop-off identified | Specific step in 7 days | BLOCKED (Umami access) | 0/1 |
| Blog performance tracking | Posts tracked within 48h | NO BLOG POSTS YET | N/A |

### Jax — SaaS Growth Operations Lead
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Directory submissions | 30+ in 14 days | IN_PROGRESS (list building) | 0/30 |
| Approval rate | 80%+ | N/A yet | No submissions |
| Directory referral traffic | 100+ sessions/month | NOT MEASURABLE | 0 |
| Competitor gap coverage | All B/W2P directories | PENDING | Research pending |

### Rumi — Blog & Content Analyst
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Content calendar | 30-day, 10+ posts in 7 days | IN_PROGRESS | 0/10 |
| Topic cluster depth | 5+ pillars, 5-10 articles each | PENDING | 0/5 |
| Competitor blog coverage | 100% in 7 days | IN_PROGRESS | Scanning |
| Quick wins identified | 3-5 in 30 days | PENDING | 0/5 |
| Backlink targets | 10 high-authority pages | PENDING | 0/10 |

### Moxie (CMO) Governance
| KPI | Target | Status | Score |
|-----|--------|--------|-------|
| Orchestrator uptime | 100% — no dead crons | GREEN | 16/16 active |
| Report quality | All actionable | GREEN | Day 1, clean |
| Blocker resolution time | <2h flag, <24h Rishi | YELLOW | Telegram: 2h+ pending |
| Dispatch latency | <4h from completion → next | GREEN | Workers fire every 4h |
| GitHub commits/day | 1-2 meaningful | GREEN | 10 commits today |

---

## Risk Heat Map
| Risk | Owner | Impact | Probability | Score | Mitigation |
|------|-------|--------|-------------|-------|------------|
| Telegram delivery failing | System | HIGH | 20% | MEDIUM | Monitor; reconcile conflicting state; verify next 3 deliveries |
| WP plugin blocked | Forge + Rishi | HIGH | 80% | HIGH | Rishi code review + Codex reset 03:26 GST |
| Umami data inaccessible | Mira | MEDIUM | 50% | MEDIUM | Fallback: manual weekly data entry |
| Workers stuck in loops | System | HIGH | 30% | MEDIUM | Self-termination after task complete |
| Free model quota exhaust | System | HIGH | 40% | MEDIUM | Rotate models, pause non-critical workers |

---

## Channel Revenue Contribution Tracking
| Channel | Target Paid | Pathway | Current Progress | Confidence |
|---------|------------|---------|------------------|------------|
| Organic SEO | 6 | 2000 visitors → 3% signup → 10% paid | Building foundations (Astra keywords) | MEDIUM |
| Reddit communities | 4 | 500 visitors → 5% signup → 15% paid | Ember researching, posting soon | HIGH (fast channel) |
| SaaS directories | 1 | 300 visitors → 2% signup → 10% paid | Jax building list, submissions pending | MEDIUM |
| WP plugin directory | 6 | 1000 visitors → 4% signup → 15% paid | BLOCKED — Rishi code review | HIGH if unblocked |
