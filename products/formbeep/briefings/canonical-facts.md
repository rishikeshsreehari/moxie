# FormBeep — Canonical Facts (source of truth)

Product: FormBeep
Website: https://formbeep.com
ICP: Website owners/agencies (agency-friendly) in WhatsApp‑heavy geos: India, Western Europe, Malaysia, Singapore, Australia, NZ, UAE, Saudi Arabia; US market for SMS angle (future).
Positioning: Instant WhatsApp notifications for form submissions; 2‑minute setup; no credit card required.

Pricing (live on site):
- Free: $0/month — 15 notifications, 1 domain, 1 recipient, 1 webhook, unlimited forms
- Starter: $4.99/month — 200 notifications, 2 domains, 2 recipients, 2 webhooks
- Pro: $24.99/month — 1,500 notifications, 5 domains, 3 recipients, 5 webhooks
- Business: $49.99/month — 3,000 notifications, 10 domains, 10 recipients, 10 webhooks
- Agency: $99/month — 7,000 notifications, unlimited domains/recipients/webhooks

Launch/traction:
- Launched: 2026-04-01 (approx)
- Paid customers: 1 (founder-confirmed)
- Revenue/MRR: do not state publicly unless founder provides current figures
- Inbox: hello@formbeep.com

Tech stack:
- Marketing site: Hugo
- Checkout/authentication: accounts.formbeep.com (own)
- Alerts: WhatsApp Business API (via provider)
- Analytics: Umami Cloud (website_id 750e37be-3e04-4672-abe8-a2983afb9a4d) + GSC

Tracking implementation:
- Umami script installed; pageview tracking active
- Click events tracked for: header "Get Started Free", hero "Get FREE Alerts", pricing CTAs, final CTA
- Event names follow `Signup - <Location>` convention

Integrations status:
- Webflow: documentation page exists; full app plugin required for marketplace — **DEFERRED**
- Framer: documentation page exists; full plugin required for marketplace — **DEFERRED** (prior rejection confirms)
- Glide: integration guide recommended (use Call API) — **BUILD NOW** (docs effort)
- Typedream: embed approach recommended — **BUILD NOW** (docs effort)

Marketplace submissions:
- None submitted yet; Webflow/Framer require full builds first.
- No formal marketplace for Glide/Typedream; use documentation/SEO play.

Directory submissions (current):
- SaaSHub, StartupBase, Uneed: submitted (pending)
- BetaList: failed (paid-only)
- AlternativeTo: failed (7-day account age gate)
- Fazier, Twelve Tools: recently submitted (pending)

Calls‑to‑action (live site):
- Primary: "Get FREE Alerts" (hero, pricing, final CTA)
- Secondary: "Get Started Free" (header nav), "Docs", "Login"
- Demo CTA: "View Details" (WhatsApp mockup)

Free tier claims:
- **MUST**: "15 submissions/month" (NOT "Free forever")
- **CAN include**: "No credit card", "2-minute setup", "Unlimited forms"

NOT implemented (claims to avoid):
- ❌ Email notifications
- ❌ SMS notifications (unless explicitly future-dated with disclaimer)
- ❌ "Unlimited" on free tier
- ❌ "One-click install" for Webflow/Framer
- ❌ "Official integration" badges
- ❌ Cloud sync / account features (applies to FormBeep, not StackStats)

Notes:
- GSC + Umami configured; tracking being enhanced (click events + UTM hygiene)
- Primary initial geo: India (WhatsApp penetration high)
- Always verify claims against live site snapshot before outreach.

