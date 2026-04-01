# FormBeep Pricing War Room — April 2026
**Owner: Vale (Competitor Intelligence) | Date: 2026-04-01**
**Trigger: BeepMate dropped to $4/mo; FormBeep at $4.99/mo — under price pressure**

---

## 1) Direct Competitor Pricing Teardown

### BeepMate (beepmate.io) — THE NEW BASELINE
| Tier | Price | Daily Limit | Key Features |
|------|-------|-------------|-------------|
| Free | $0 | 20/day | Basic WA notifications |
| **VIP** | **$4/mo** | 200/day | WA + groups, AI summarize, AI filter |
| PRO | $9/mo | 800/day | All VIP + regex filters (coming) |
| Enterprise | Custom | Unlimited | Self-hosted, company domain/number |

**Weaknesses:**
- **No SMS channel** — WhatsApp only. All eggs in Meta's basket. If Meta bans/limits WA BAPI, BeepMate has nothing.
- **Enterprise tier is just "Contact Us"** — no price anchoring, no self-serve path for large accounts.
- **AI features are basic** — email summarization/filtering are commodity AI (GPT-4 class). Not defensible.
- **$4 pricing is likely a land grab** — they've restructured pricing 2-3x, suggesting uncertainty about optimal price. May rise again.
- **Self-hosted mentioned only at Enterprise** — power users who want control can't self-host at any consumer tier.

**Strengths:**
- Cheapest paid entry point ($4/mo vs FormBeep $4.99)
- AI features create perceived value even at lowest tier
- SEO content pages (WP→WA, Framer→WA) are working for discoverability

### Web2Phone (web2phone.co.uk)
| Tier | Price | Monthly Limit |
|------|-------|---------------|
| Free | £0 | 10 WA notifications/month |
| Starter | £9/mo (~$11) | Basic |
| Pro | £19/mo (~$24) | More |
| Business | £39/mo (~$48) | Max |

**Weaknesses:**
- **Priced 2-3x higher than FormBeep** — not competing on price. Premium positioning but no premium justification.
- **UK-only pricing (£)** — alienates international SMB market.
- **WP-plugin only** — limited platform reach compared to FormBeep's API + integrations approach.
- **Cloudflare-heavy site** — feels corporate, not indie-friendly.

### WPForms (wpforms.com)
- WhatsApp notifications went live March 5, 2026
- **Pricing: $49.50/yr Basic, $199.50/yr Plus, $399.50/yr Pro — all include WA**
- **Not a direct competitor** — WPForms is a full form builder ($200-400/yr), WA is just a feature
- **Threat**: If someone already pays for WPForms, they won't buy FormBeep separately for notifications
- **Opportunity**: WPForms users who want SMS (not just WA) still need FormBeep; WPForms doesn't do SMS

### Formspree (formspree.io)
| Tier | Price | Submissions | WA | SMS |
|------|-------|-------------|----|-----|
| Free | $0 | 50/mo | ❌ | ✅ (paid addon) |
| Gold | $10/mo | 1,000 | ❌ | ✅ |
| Platinum | $50/mo | 10,000 | ❌ | ✅ |
| Enterprise | Custom | Unlimited | ❌ | ✅ |

**Weaknesses:**
- **No WhatsApp at all** — their biggest blind spot vs FormBeep
- **$10/mo entry** — 2.5x BeepMate's price
- **APIv2 deprecation (Q3 2026)** — creates migration anxiety but they're too expensive to be the natural alternative

---

## 2) Indirect/Partial Competitors

| Tool | Price | Channel | Relevance to FormBeep |
|------|-------|---------|----------------------|
| Getform | $10-25/mo | SMS (Q2 target) | Becomes direct competitor IF they ship dual-channel |
| Basin | $5-20/mo | Email/webhooks only | No WA, no SMS — not a notification competitor |
| WANotifier | $25+/mo | WhatsApp only | Commerce-focused, not form-focused. Different user. |
| Zapier | $20+/mo | Multi-channel via zaps | Expensive, complex. Good for existing Zapier users. |
| Make/n8n | $8-16/mo | Multi-channel via workflows | Self-host n8n ($0) is the real threat for devs. |

---

## 3) Feature Gap Analysis: What Each Has That FormBeep Doesn't

| Feature | BeepMate | Web2Phone | n8n (free) | FormBeep |
|---------|----------|-----------|------------|----------|
| WhatsApp notifications | ✅ | ✅ | ✅ (build it) | ✅ |
| SMS notifications | ❌ | ❌ | ✅ (build it) | ✅ (differentiator) |
| AI email filtering | ✅ | ❌ | ❌ (build it) | ❌ |
| AI email summarization | ✅ | ❌ | ❌ (build it) | ❌ |
| Regex routing | coming | ❌ | ✅ (build it) | ❌ |
| Group messaging | ✅ ($4) | limited | ✅ (build it) | ❓ |
| Self-hosted option | Enterprise only | ❌ | ✅ (free) | ❓ |
| Multi-platform (WP/Webflow/Framer) | Guides only (WA) | WP only | API-based | ✅ (native integrations) |
| Platform-agnostic API | ❌ | ❌ | ❌ | ✅ |

**FormBeep's unique advantages (no one else has both):**
1. **SMS as first-class channel** — BeepMate, Web2Phone, WPForms none do SMS natively
2. **Platform-agnostic API** — not tied to WordPress like Web2Phone
3. **Integrations (Webflow/Framer/WP)** — native, not just guide pages

---

## 4) Pricing Decision Matrix

### Option A: Drop to $4/mo (match BeepMate)
- **Pros**: Price parity removes #1 objection, simplifies comparison
- **Cons**: Lose $11.99/year per customer; sets ceiling at $4; race to bottom
- **Math**: 10 users × $4/mo = $40/mo (vs $49.90 at current). Need 12.5 users to hit same $50/mo.

### Option B: Hold $4.99 (current)
- **Pros**: Higher revenue per user; can justify with SMS dual-channel
- **Cons**: $0.99/month price delta gives prospects a reason to choose BeepMate
- **Counter**: Lead messaging on "the only tool with SMS + WhatsApp in one place" — not a price play

### Option C: Create $3.99 Starter tier + $9.99 Pro tier
- **Pros**: Undercut BeepMate at entry; capture agency at $9.99 (no one targets this)
- **Cons**: Two tiers to manage; $3.99 still loses money per customer
- **Math**: Need to predict split % between tiers

### Option D: $4.99/mo — add an AI feature ASAP
- **Pros**: Neutralizes BeepMate's AI advantage; keeps price premium justified
- **Cons**: Requires engineering effort (even basic AI auto-acknowledge templates)
- **Counter**: "AI-powered form responses" can be simple templates (no LLM cost per notification)

---

## 5) Recommendation

**Hold $4.99/mo. Do NOT drop price.** Here's why:

1. **$0.99/month is not a rational switching cost** — if someone has evaluated both tools and the form→notification works, nobody chooses based on $12/year. The buyer who cares that much about $0.99 has a $0 LTV.
2. **SMS is the moat.** BeepMate is WA-only. FormBeep is dual-channel. Lead with that in all copy. "WhatsApp AND SMS. Because one channel is never enough."
3. **BeepMate's pricing instability is a weakness** — "We've restructured 3x" is not what you tell enterprise buyers. FormBeep's stable pricing is a feature.
4. **The agency gap is real money** — BeepMate removed their $19/mo tier. FormBeep should plan a $14.99/mo "Agency" tier (20 sites, shared inbox, branded notifications). This is the highest-margin segment.

**One immediate action:** Add AI-powered auto-acknowledgment emails as a feature (no LLM cost — template-based with smart variable substitution). This neutralizes BeepMate's "AI" marketing without engineering risk. Ship this to homepage and pricing page within 2 weeks.

---

## 6) Watch Items for Next Scan

- [ ] BeepMate pricing restructuring #3 (likely to happen — they're still finding their price)
- [ ] Getform SMS routing launch (Q2 2026) — becomes dual-channel competitor
- [ ] n8n WhatsApp + SMS templates — open-source alternative for developers
- [ ] Formspree API v2 sunset fallout (Q3 2026) — potential user migration target
- [ ] Any BeepMate AI feature expansion beyond email summarization
- [ ] Web2Phone release post-v3.2.1 (last confirmed Mar 12, 2026)

---

*Saved: 2026-04-01T19:12Z | Vale, Competitor Intelligence Lead*
