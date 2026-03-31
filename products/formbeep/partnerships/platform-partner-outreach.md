# Pax P0 Platform Partner Program Outreach — FormBeep

> **Date:** 2026-03-31
> **Lead:** Pax (Partnerships / BD)
> **Product:** FormBeep — form-to-SMS/WhatsApp/email notifications

---

## Objective

Get FormBeep listed/approved in platform partner directories and marketplaces to capture in-platform demand. Platform users searching for form notification solutions are high-intent leads — they already use the platform, they have forms, and they need what FormBeep does.

---

## P0 Platform Partner Programs (Apply This Week)

### 1. Webflow Experts / Apps Directory
- **Program:** Webflow Apps Marketplace
- **URL:** https://webflow.com/apps
- **Why:** We already have a Webflow integration. Users search the Webflow Apps directory for form solutions. FormBeep can be listed as a "Forms & CRM" category app.
- **Requirements:** Working Webflow integration, app listing page, privacy policy, support channel
- **Status:** ✅ Webflow integration complete — ready to apply
- **Action:** Submit app listing with screenshots, description, and integration demo
- **Listing Copy Draft:**
  - **Tagline:** "Send form submissions to WhatsApp, SMS, and Email — no code needed"
  - **Description:** "FormBeep connects your Webflow forms to instant notifications via WhatsApp, SMS, and email. No middleware, no Zapier. Just paste your endpoint and get notified the moment someone submits. Perfect for agencies, freelancers, and small businesses who can't afford to miss a lead."
  - **Category:** Forms & CRM
  - **Pricing:** Freemium (free tier + paid upgrades)

### 2. Framer Templates / Plugins Directory
- **Program:** Framer Marketplace
- **URL:** https://www.framer.com/marketplace/
- **Why:** FormBeep already has a Framer integration. Framer users actively browse the marketplace for utilities. Form submission → notifications is a top request in Framer community.
- **Requirements:** Working Framer integration, marketplace listing
- **Status:** ✅ Framer integration complete — ready to apply
- **Action:** Submit to Framer Marketplace with demo video + listing
- **Listing Copy Draft:**
  - **Tagline:** "Never miss a form submission — get WhatsApp + SMS alerts instantly"
  - **Description:** "Connect any Framer form to FormBeep and receive instant WhatsApp, SMS, and email notifications when leads submit. Zero code, no Zapier dependency, works out of the box."

### 3. Glide Apps Integrations
- **Program:** Glide Integrations / Glide Apps Marketplace
- **URL:** https://www.glideapps.com/plugins
- **Why:** Glide is a no-code app builder with heavy form/data-collection use cases. Glide users need push notifications for form submissions — FormBeep solves this natively.
- **Requirements:** Glide-compatible API/webhook endpoint, documentation
- **Status:** 🟡 No Glide-specific integration yet — but FormBeep's webhook API works with Glide's "Call an API" action
- **Action:** Create Glide-specific documentation + apply to Glide integrations directory
- **Approach:** Document how Glide users can use the "Webhooks" or "Call API" component to send form data to FormBeep, then receive SMS/WhatsApp alerts

### 4. Softr Integrations
- **Program:** Softr Integrations / Softr Marketplace
- **URL:** https://www.softr.io/integrations
- **Why:** Softr builds client portals and internal tools with forms. Users need real-time form submission alerts — a natural FormBeep use case.
- **Requirements:** Softr-compatible webhook setup
- **Status:** 🟡 No Softr-specific integration yet — but FormBeep's webhook API works
- **Action:** Create Softr-specific documentation page + apply to Softr integrations
- **Approach:** Document how Softr form blocks can trigger FormBeep webhooks for instant notifications

### 5. Bubble Plugin (Build)
- **Program:** Bubble Plugin Marketplace
- **URL:** https://bubble.io/plugins
- **Why:** Bubble is the largest no-code platform by users. A FormBeep Bubble plugin would expose FormBeep to thousands of Bubble app builders who need form→notification functionality.
- **Requirements:** Bubble plugin (JavaScript API connector), documentation, demo app
- **Status:** 🟡 Not yet built
- **Action:** Build a minimal Bubble plugin (API Connector wrapper for FormBeep endpoints) + submit to Bubble marketplace
- **Estimated Effort:** 1-2 days (Bubble's API Connector pattern is straightforward — wrapper around FormBeep REST API)
- **Plugin Scope:** 
  - Configure FormBeep API key in Bubble
  - Expose "Send Notification" action with fields: phone, message, channel (SMS/WhatsApp/email)
  - Expose "Check Status" action for delivery tracking
- **Note:** Requires developer to build. Log as a task for Forge.

---

## Outreach Timeline (2-Week Spread)

| Week | Platform | Action |
|------|----------|--------|
| Week 1 (Apr 1-4) | Webflow Apps | Submit listing, follow up on application |
| Week 1 (Apr 1-4) | Framer Marketplace | Submit listing, follow up on application |
| Week 1 (Apr 1-4) | Glide | Publish integration docs, submit to directory |
| Week 2 (Apr 7-11) | Softr | Publish integration docs, submit to directory |
| Week 2 (Apr 7-11) | Bubble | Build plugin (assign to Forge) + submit to marketplace |

---

## P1 Secondary Platforms (Future)

| Platform | Why | Effort |
|----------|-----|--------|
| Carrd | Lightweight sites with forms — need notification solution | Low (just docs) |
| Typedream | Notion-style site builder with forms | Low (just docs) |
| Dorik | AI website builder — growing fast | Low (just docs) |
| Notion (via API) | Notion forms → notifications is a hot use case | Medium (adapter needed) |
| WordPress (via plugin) | Once WP plugin approved, list in WP.org | Already in progress (Rishi-owned) |

---

## Partner Program Application Checklist

For each platform, prepare:
- [ ] Working integration (Webflow ✅, Framer ✅, Glide/Softr via webhook)
- [ ] Listing/description copy (drafted above)
- [ ] Screenshots or demo video
- [ ] Privacy policy link (formbeep.com/privacy)
- [ ] Support email: hello@formbeep.com
- [ ] Pricing page link
- [ ] API documentation link

---

## Bubble Plugin Task for Forge

**Assign to Forge:** Build a minimal Bubble plugin for FormBeep.

**Spec:**
- Plugin name: "FormBeep Notifications"
- Expose 2 Bubble actions:
  1. `Send FormBeep Alert` — inputs: API key, phone number, message, channel (SMS/WhatsApp/Email)
  2. `Check FormBeep Delivery Status` — inputs: API key, message ID
- Use Bubble's API Connector pattern
- Include setup instructions and a demo page
- Output: Bubble plugin file + installation guide at `/root/moxie/products/formbeep/partnerships/bubble-plugin/`

**Rationale:** Bubble has 3M+ users and an active plugin marketplace. A FormBeep plugin captures high-intent Bubble builders who search for "notification" or "SMS" plugins.

---

## Tracking

| Platform | Applied | Approved | Listed | Notes |
|----------|---------|----------|--------|-------|
| Webflow | Pending | — | — | Integration ready |
| Framer | Pending | — | — | Integration ready |
| Glide | Pending | — | — | Docs needed |
| Softr | Pending | — | — | Docs needed |
| Bubble | Pending | — | — | Plugin build needed |

---

*Next review: 2026-04-07*
