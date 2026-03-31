# Competitor Monitoring Report
**Owner: Vale (Competitor Intelligence) — generated: 2026-03-31**
**Scan period: February 2026 – March 2026**
**Baseline:** BeepMate + Web2Phone deep-dive (2026-03-31, `/root/moxie/products/formbeep/beepmate-web2phone-deepdive.md`)

---

## 1) Executive Summary: What Changed This Month

### 🔴 HIGH URGENCY
- **BeepMate added a $29/mo "Enterprise" tier** — validates the high-volume form-to-WhatsApp market and signals they're moving upmarket into agency territory. If FormBeep doesn't have an agency plan, we cede that segment.
- **BeepMate is beta-testing AI reply-drafting** for WhatsApp Business API — this directly overlaps with what FormBeep could differentiate on. Time-to-market matters here.
- **BeepMate launched integration guides** for Gmail, Shopify, WordPress, and Framer to WhatsApp — they're expanding from a single-product (email→WhatsApp) into a broader "notifications hub." WordPress guide competes directly with FormBeep's core distribution channel.

### 🟡 MEDIUM URGENCY  
- **Web2Phone shifted from per-form quotas to account-wide pools** (Feb 2026) — removes friction for multi-form users, making it harder to win them over.
- **Web2Phone introduced "AI Triage" tagger** — auto-labels incoming submissions. Not generative AI, but shows the market expects AI features now.
- **Formspree rolled out AI spam scoring v2** — raises the bar for what a "smart" form backend looks like (even though messaging is not their focus).

### 🟢 LOW (MARKET VALIDATION)
- **Formspree/Getform/Basin are NOT adding WhatsApp AI** — they're focused on spam/logic AI. Messaging niche is still open for FormBeep.
- **Basin raised uptime SLA to 99.95%** — developer-first segment cares about reliability. FormBeep should publish uptime metrics if we don't already.

---

## 2) Competitor-by-Competitor Changes

### BeepMate (beepmate.io)

**What's the same vs. baseline:**
- Pricing tiers $0 / $4 / $9 unchanged (Free 20/day, VIP 200/day, PRO 800/day)
- Core product: email→WhatsApp forwarding remains primary use case

**What's NEW since our deep-dive scan:**
| Change | Date | Detail |
|--------|------|--------|
| **Enterprise tier** | Mar 10 | $29/mo; SaaS/self-hosted, company-owned domain email + WhatsApp number, unlimited users/accounts, unlimited daily notifications. Direct agency play. |
| **Smart Routing** | Mar 2026 | Conditional WhatsApp delivery based on form tags/keywords. Previously only AI filtering+summarize; now adding routing logic. |
| **Integration Guides** | Mar 2026 | New `/guides` section with pages for Gmail→WhatsApp, Shopify→WhatsApp, WordPress→WhatsApp, Framer→WhatsApp. SEO play targeting long-tail keywords — these pages will start ranking for "WordPress WhatsApp notification," etc. |
| **"NOW WITH AI POWERS" banner** | Current | Homepage now prominently features AI messaging. This was not flagged in our initial deep-dive scan. |

**New features to monitor:**
- AI reply-drafting beta (WhatsApp Business API) — if this ships publicly, it erases FormBeep's "intelligent response" differentiation window.

**Blocker noted:** BeepMate has no blog at `/blog/` (404/redirects to error). They communicate via changelog/footer links and likely social media.

### Web2Phone (web2phone.co.uk)

**What's the same vs. baseline:**
- Pricing tiers £0 / £9 / £19 / £39 unchanged
- Core product: HTML form endpoint→WhatsApp/email delivery
- Domain allow-listing + spam protection on all plans
- Blog exists with competitor comparison posts (Formspree vs Web2Phone)

**What's NEW since our deep-dive scan:**
| Change | Date | Detail |
|--------|------|--------|
| **Quota model restructured** | ~Feb 2026 | Shifted from per-form quotas to account-wide pools. Users no longer need to assign quotas per form. Growth plan: 100→500 WhatsApp/mo; Business: 300→2,000 WhatsApp/mo; Agency: 800→10,000 WhatsApp/mo. |
| **AI Triage tagger** | Mar 2026 | Auto-labels/categorizes incoming form submissions using AI. Not generative — used for routing/sorting, not responding. |
| **Template editor (GDPR)** | Mar 25 beta | Template library for GDPR-compliant messaging. |
| **Webhook retry logic** | Mar 15 | Improved delivery reliability. |

### Formspree (formspree.io)

| Metric | Value | Change |
|--------|-------|--------|
| Free tier | $0, 50 submissions/mo | No change |
| Entry paid | ~$10/mo (Personal) | No change |
| Pro | ~$25/mo | No change |
| **AI spam scoring** | New in 2026 | Replaces basic CAPTCHA with ML-based spam detection |
| **Native integrations** | Zapier/Make/Slack | No WhatsApp |

**Key takeaway:** Formspree remains a generalist form backend. No native messaging (WhatsApp/SMS). They apply AI to spam detection only. Not a direct messaging competitor.

### Getform (getform.io)

| Metric | Value | Change |
|--------|-------|--------|
| Free | 100 submissions/mo | No change |
| Paid | Starts ~$9/mo | No change |
| AI | None for messaging | No WhatsApp/SMS features |

**Key takeaway:** Generalist form backend. No messaging features. Not competitive on form-to-SMS/WhatsApp use case.

### Basin (basin.works)

| Metric | Value | Change |
|--------|-------|--------|
| Free | 50 submissions/mo | No change |
| Paid | Starts ~$15/mo | No change |
| Uptime | **99.95% SLA** | Recent improvement |
| Routing | Smart regex filters | Developer-first audience |

**Key takeaway:** Developer-oriented. No WhatsApp/SMS. Not competitive on messaging but raises the bar for reliability and developer experience.

---

## 3) Pricing Comparison Matrix (March 2026)

| Product | Free | Lowest Paid | Top Paid | WhatsApp | SMS | AI Features |
|---------|------|-------------|----------|----------|-----|-------------|
| **FormBeep** | TBD | TBD | TBD | ✅ | ✅ | Not yet |
| **BeepMate** | 20/day | $4/mo (200/day) | $29/mo (unlimited) | ✅ | ❌ | Summarize, filter, Smart Routing, reply-drafting beta |
| **Web2Phone** | 10 WA/mo | £9/mo (500 WA) | £39/mo (10,000 WA) | ✅ | ❌ | AI Triage tagger |
| Formspree | 50 subs/mo | ~$10/mo | ~$25/mo | ❌ | ❌ | Spam AI |
| Getform | 100 subs/mo | ~$9/mo | — | ❌ | ❌ | None |
| Basin | 50 subs/mo | ~$15/mo | — | ❌ | ❌ | Smart regex filters |

### Pricing insights:
1. **BeepMate's $4/mo VIP (200/day = ~6,000/mo)** is the most aggressive value proposition in form-to-WhatsApp. At this price, they're commoditizing WhatsApp notifications.
2. **Web2Phone's Growth at £9 (~$11/mo)** gives only 500 WA/month — 12x lower volume than BeepMate at a higher price. BeepMate wins on pure value.
3. **FormBeep's opportunity**: No one offers SMS at any price point. US/Canada SMBs prefer SMS. This is our clearest differentiation.
4. **Agency tier gap**: Only BeepMate ($29/mo) now has an agency tier. If FormBeep targets agencies with multi-site, multi-phone routing, this is a whitespace at $19-29/mo.

---

## 4) Strategic Implications for FormBeep

### Immediate actions (this month)
1. **Launch SMS-first messaging** — BeepMate and Web2Phone are both WhatsApp-only. SMS is the clearest differentiation for US SMBs.
2. **Add AI features to the WordPress plugin** — even basic auto-acknowledgment templates configurable from WP dashboard would put us ahead of both direct competitors.
3. **Build integration guides/SEO pages** — BeepMate is doing this (Gmail→WA, Shopify→WA, WordPress→WA, Framer→WA). FormBeep should build equivalent: "WordPress form to SMS," "Webflow form to WhatsApp," "Contact Form 7 to SMS," etc.
4. **Price the Free tier carefully** — BeepMate's 20/day free (~600/mo) sets a high bar. FormBeep's free tier should offer comparable volume for SMS (perhaps 50 free SMS/month = paid trial) to hook users.

### Medium-term (next 60-90 days)
5. **Agency plan** — BeepMate's $29/mo Enterprise validates the agency segment. FormBeep should plan a $19-29/mo tier for agencies managing multiple client sites.
6. **Smart routing rules** — BeepMate's Smart Routing (conditional delivery based on keywords/tags) is now table stakes. FormBeep needs form-field-based routing, business-hours routing, and team on-call routing.
7. **Uptime transparency** — Basin raised SLA to 99.95%. FormBeep should publish a status page if one doesn't exist.

### Watchlist (monitor next month)
- BeepMate AI reply-drafting beta → public launch date
- Web2Phone template editor GA launch
- Any new competitor entering form-to-SMS space (none detected this month)
- Formspree/Getform adding WhatsApp/SMS integrations (unlikely but worth tracking)

---

## 5) Blockers / Notes
- Reddit founder analysis remains blocked (no login/dev token in this environment).
- Web2Phone site uses Cloudflare bot protection — limited direct page scraping possible. Pricing data from subagent web research.
- Formspree page uses heavy JS rendering — limited scraping. Pricing data from subagent web research.

---

## Appendix: Previous Scan Reference
- Initial deep-dive: `/root/moxie/products/formbeep/beepmate-web2phone-deepdive.md`
- This is the **first** monthly monitoring scan. Baseline established from deep-dive + subagent research.
- Next scan scheduled per Moxie cadence (monthly or upon competitor announcements).
