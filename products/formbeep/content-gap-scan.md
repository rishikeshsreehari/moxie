# FormBeep — Content Gap Scan (Rumi, Bi-weekly)

**Scan date:** 2026-03-31 (Friday)
**Type:** Content gap analysis + trending topic check
**Based on:** Astra's keyword research, Vale's competitor monitoring, Kiro's blog drafts, existing content calendar

---

## 1) New Gaps Identified This Cycle

### HIGH — Urgent gaps (ship within 7 days)

**G1. "BeepMate Enterprise / Agency Plan" comparison page**
- **Why now:** Vale confirmed BeepMate launched a $29/mo Enterprise tier with Smart Routing and AI reply-drafting beta. No FormBeep content addresses this tier.
- **Content need:** A comparison/angle piece: "FormBeep vs BeepMate Enterprise: Why Teams Need SMS Fallback, Not Just AI Reply Drafts" — positions FormBeep's multi-channel reliability against BeepMate's AI-only features.
- **Est. effort:** 1 blog post (1,200 words) + 1 comparison landing page
- **Keywords to target:** `email to whatsapp agency`, `whatsapp notification for teams`, `beepmate enterprise`

**G2. "Web2Phone Account-Wide Pool" — migration/opportunity angle**
- **Why now:** Web2Phone restructured from per-form to account-wide quotas (500–10,000 WA/month). This is a feature upgrade that makes them harder to displace with simple blog posts.
- **Content need:** Angle piece highlighting what account-wide pools *don't* solve: no SMS fallback, no multi-channel routing, no per-form rules, no retry visibility. This makes the "upgrade" the right entry point for migration content.
- **Content need 2:** A "Switching from Web2Phone → FormBeep" migration guide (setup steps, what carries over, what gets better).
- **Keywords to target:** `web2phone alternative`, `web2phone vs formbeep`, `whatsapp form notification without zapier`

**G3. Integration pages — BeepMate is outranking us pre-launch**
- **Why now:** BeepMate launched `/guides` with WordPress→WhatsApp, Framer→WhatsApp, Shopify→WhatsApp, Gmail→WhatsApp pages. These will start capturing long-tail SEO intent *today*.
- **Content need:** Mirror BeepMate's guide structure but add SMS + multi-channel differentiation on every page. Minimum: 4 integration pages matching BeepMate's current guides.
- **Priority pages:** `/wordpress-form-sms-whatsapp`, `/framer-form-sms-whatsapp`, `/shopify-form-sms-whatsapp`, `/webform-to-sms-guide`

### MEDIUM — Ship within 14 days

**G4. "AI in Form Notifications" — positioning page**
- **Why now:** BeepMate (AI reply-drafting) + Web2Phone (AI Triage) have introduced AI features. The market is setting AI as table-stakes.
- **Content need:** A thought-leadership piece: "Why AI Reply-Drafting Is the Wrong Priority for Lead Notifications" — argue that *speed* and *multi-channel reliability* matter more than AI-generated responses when seconds count. FormBeep can then announce its own AI features as additive, not core value.
- **Keywords to target:** `AI form notifications`, `automated form response`, `AI for lead notifications`

**G5. "FormBeep vs Make / n8n" comparison pages**
- **Why now:** Nova's paid acquisition plan covers these as channels, but no content pages exist. Astra identified these in keyword research.
- **Content need:** Two comparison pages (800–1,000 words each) with honest use-case recommendations and FormBeep as the simpler/cleaner option for form-specific alerts.
- **Keywords:** `Make alternative form notifications`, `n8n form SMS webhook alternative`

### LOW — Nice to include in content calendar updates

**G6. "Basin uptime 99.95%" → "FormBeep reliability" post**
- **Why now:** Basin raised SLA to 99.95%. Developer-first audience notices these signals. A transparent reliability page would build credibility.
- **Content need:** Status page + reliability blog post (retry logic, uptime monitoring, what happens when SMS fails).

---

## 2) Trending Topics & Emerging Angles

### Trending in the Form/SaaS notification space

| Trend / Signal | Relevance to FormBeep | Action |
|---|---|---|
| **AI reply-drafting** (WhatsApp) | High — BeepMate beta. We need a positioning response ASAP. | Ship G4. Monitor BeepMate beta launch date. |
| **AI Triage/Tagging** (form submissions) | Medium — Web2Phone launched it. Nice-to-have but not urgent. | Note for product roadmap. Blog can cover it (G4). |
| **Smart Routing** (conditional delivery) | High — BeepMate just shipped it. Routing is now an expectation. | Update landing pages to include routing in differentiators. |
| **Account-wide quota pools** | Medium — removes per-form friction for competitors. | Use migration content (G2) as counter-angle. |
| **"Without Zapier" search intent** | High — confirmed by Astra's keyword data: weak SERPs, low competition. | Already in content calendar (Day 11, calendar confirms). Ship fast. |
| **Speed-to-lead data** | High — growing body of research showing <5 min response time increases conversion 10x. | Build a data-driven blog post citing third-party studies. |

### Google Trends / Search pattern shifts (inferred from Astra's SERP + keyword data)

- **Platform-specific queries** (WordPress/Webflow/form builders) are the *strongest* and most actionable intent. ~60–70% of total searchable demand in this space.
- **"No-code" and simple-setup modifiers** rising — users increasingly search "without [tool]" and "no code" as they want to avoid complex automation stacks.
- **SMS vs WhatsApp** — US market skews heavily to SMS. FormBeep is the only competitor offering both. This should be front-and-center on all content.

---

## 3) Content Calendar Updates (Recommended)

Based on this scan, the existing 30-day calendar (from `content-calendar.md`) is well-structured but needs the following insertions:

| Priority | Change | Insert After |
|---|---|---|
| 🔴 P0 | Add "BeepMate Enterprise comparison" blog post | After Day 4 (Formspree comparison) |
| 🔴 P0 | Add "Switching from Web2Phone" migration guide | After Day 8 (FormBeep vs Web2Phone) |
| 🔴 P1 | Accelerate integration guide pages (4 BeepMate mirrors) | Create as Day 3.5, 5.5, 9.5, 12.5 |
| 🟡 P2 | Add "AI Reply-Drafting Is Wrong Priority" post | After Day 12 (no-Zapier post) |
| 🟡 P2 | Add FormBeep vs Make comparison page | Replace Day 23 or add as Day 23.5 |
| 🟢 P3 | Add reliability/status page content | Can be combined with Day 20 (spam/security post) |

### Revised 30-day priority order (top 4 must ship first):
1. `/wordpress-form-sms-whatsapp` integration page (highest-volume WP keyword)
2. "Switching from Web2Phone → FormBeep" migration guide
3. "FormBeep vs BeepMate Enterprise" comparison
4. "AI in Notifications" positioning post

---

## 4) Gaps in Current Assets

We've shipped these deliverables but have gaps:

| Asset | Status | Missing Content |
|---|---|---|
| content-calendar.md | COMPLETED | 30-day plan exists; needs updates above |
| blog-posts-v1.md | COMPLETED (2 posts) | Only covers Zapier angles. Missing BeepMate/Web2Phone/AI topics. |
| landing-page-v1.md | COMPLETED | Covers basics. Does not address new BeepMate Enterprise tier. |
| seo-keywords.md | Exists | Needs updated priority based on this scan |
| No content on | — | Migration guides, BeepMate/Enterprise comparison, AI positioning, integration guides |

---

## 5) Recommended Next Blog Topics (Ready for Kiro to Draft)

1. **"Why AI Reply-Drafting Won't Save Your Lead Response Time"** — positioning piece against BeepMate's AI focus; 1,200 words
2. **"Switching from Web2Phone to FormBeep: A Complete Migration Guide"** — practical how-to; 1,500 words  
3. **"FormBeep vs BeepMate Enterprise: Multi-Channel Lead Alerts That Actually Scale"** — comparison; 1,000 words
4. **"Best Form Notification Setup for Agencies in 2026"** — targets agency decision-makers; 1,200 words
5. **"Why Basin's 99.95% SLA Matters for Your Lead Pipeline"** — trust/reliability piece; 800 words

---

## 6) Content Production Bottleneck Warning

Current shipped blog content: **2 posts** (both Zapier-oriented).
Competitor monitoring identified **5 new content needs** this cycle.
Content calendar targets **~30 posts in 30 days** — this is 1 per day.

**Recommendation for Moxie:** With the current free-model setup, Kiro can produce 2–3 drafts per run. Prioritize the 4 P0/P1 topics above; defer the rest. If Codex premium time is available, batch 3+ posts in a single session.

---

*This scan was performed by Rumi (Blog & Content Analyst) on 2026-03-31. Next scan: bi-weekly Friday (2026-04-10).*
