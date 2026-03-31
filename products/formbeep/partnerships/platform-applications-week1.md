# Pax Week 1 Platform Applications — FormBeep

> **Date:** 2026-04-01
> **Lead:** Pax (Partnerships / BD)
> **Product:** FormBeep — form-to-SMS/WhatsApp/email notifications
> **Status:** Execution plan + application materials ready

---

## Objective

Execute Week 1 platform partner applications (Webflow, Framer, Glide) following the approved P0 outreach plan. Each platform gets a complete application package ready for submission.

---

## 1. Webflow Apps Marketplace — Application Package

**Portal:** https://webflow.com/apps  
**Category:** Forms & CRM  
**Prerequisites met:** ✅ Webflow integration is live

### Application Details

| Field | Content |
|-------|---------|
| **App Name** | FormBeep |
| **Tagline** | Send form submissions to WhatsApp, SMS, and Email — no code needed |
| **Short Description** | FormBeep connects your Webflow forms to instant notifications via WhatsApp, SMS, and email. No middleware, no Zapier. Just paste your endpoint and get notified the moment someone submits. |
| **Full Description** | FormBeep is the fastest way to get notified when someone fills out your Webflow form. Instead of checking your inbox or setting up complex automations, FormBeep delivers form submissions directly to your phone via WhatsApp, SMS, or email.\n\n**Key Features:**\n- Instant WhatsApp notifications for new form submissions\n- SMS alerts — never miss a lead, even without internet\n- Email notifications as a fallback\n- Multi-channel routing: send to sales, support, or both\n- No middleware required — works directly with Webflow forms\n- No-code setup — paste the endpoint, configure channels, you're done\n\n**Perfect For:**\n- Agencies managing multiple client sites\n- Freelancers who can't afford to miss form submissions\n- Small businesses that need immediate lead response\n- Event registrations that need instant confirmation\n\n**How It Works:**\n1. Create your form in Webflow as usual\n2. Point your form action to your FormBeep endpoint\n3. Choose WhatsApp, SMS, email — or all three\n4. Get notified the instant someone submits\n\n**Integrations:** Webflow Forms\n**Support:** hello@formbeep.com\n**Docs:** formbeep.com/docs\n**Pricing:** Freemium — free tier available, paid plans from $9/mo |
| **Website URL** | https://formbeep.com |
| **Privacy Policy** | https://formbeep.com/privacy |
| **Terms of Service** | https://formbeep.com/terms |
| **Support Channel** | hello@formbeep.com |
| **Contact Email** | hello@formbeep.com |
| **Pricing Model** | Freemium |
| **Supported Regions** | Global (200+ countries for SMS/WhatsApp) |

### Assets to Prepare
- [ ] 5+ high-res screenshots of the FormBeep dashboard + Webflow integration setup
- [ ] App cover image (600×400px, Webflow Apps directory specification)
- [ ] Short demo video (30-60 seconds showing Webflow form → WhatsApp notification)
- [ ] Webflow-specific integration documentation page

### Submission Steps
1. Log into Webflow account → Marketplace → Submit App
2. Fill application form with details above
3. Upload screenshots + cover image
4. Submit and track review status (typically 5-7 business days)

---

## 2. Framer Marketplace — Application Package

**Portal:** https://www.framer.com/marketplace/  
**Category:** Utilities / Integrations  
**Prerequisites met:** ✅ Framer integration is live

### Application Details

| Field | Content |
|-------|---------|
| **Plugin Name** | FormBeep Notifications |
| **Tagline** | Never miss a form submission — get WhatsApp + SMS alerts instantly |
| **Short Description** | Connect any Framer form to FormBeep and receive instant WhatsApp, SMS, and email notifications when leads submit. Zero code, no Zapier dependency, works out of the box. |
| **Full Description** | Turn your Framer forms into instant lead-alert machines. FormBeep sends WhatsApp messages, SMS texts, and emails the moment someone submits a form on your Framer site.\n\n**Why FormBeep for Framer:**\n- Framer forms don't have built-in push notifications — FormBeep fills this critical gap\n- Zero code required — configure your endpoints, get alerts instantly\n- Multi-channel: WhatsApp for international, SMS for US, email as backup\n- Works with all Framer form blocks (contact, lead gen, waitlist)\n\n**Setup (30 seconds):**\n1. Install the FormBeep plugin in Framer\n2. Paste your FormBeep endpoint URL\n3. Select notification channels (WhatsApp, SMS, Email)\n4. That's it — your forms are now live-notified\n\n**Channels:**\n- 📱 WhatsApp Business API\n- 📲 SMS (global coverage)\n- ✉️ Email\n\n**Pricing:** Free tier included, paid plans start at $9/month for higher volumes\n**Support:** hello@formbeep.com |
| **Website URL** | https://formbeep.com |
| **Privacy Policy** | https://formbeep.com/privacy |
| **Support Email** | hello@formbeep.com |
| **Pricing** | Freemium |
| **Version** | 1.0.0 |

### Assets to Prepare
- [ ] Plugin icon (recommended: 128×128px PNG)
- [ ] 3+ screenshots showing Framer integration setup
- [ ] Demo GIF or short video: Framer form submission → WhatsApp notification received
- [ ] Framer-specific setup guide page

### Submission Steps
1. Go to framer.com/marketplace → Submit Plugin
2. Fill in plugin metadata
3. Upload plugin package (Framer plugin format)
4. Submit for review (typical timeline: 3-5 business days)

---

## 3. Glide Integrations — Application Package

**Portal:** https://www.glideapps.com/plugins  
**Category:** Communication / Notifications  
**Prerequisites:** FormBeep webhook API works with Glide's "Webhooks" action ✅

### Application Details

| Field | Content |
|-------|---------|
| **Integration Name** | FormBeep |
| **Tagline** | Instant WhatsApp + SMS alerts for Glide form submissions |
| **Description** | Add instant notifications to your Glide apps. When a user submits a form, adds a row, or triggers an action, FormBeep sends WhatsApp, SMS, or email notifications to whoever needs to know.\n\nNo Zapier. No Make. No middleware. Just a simple webhook from Glide to FormBeep, and you get notified instantly on the channel you choose.\n\n**Use Cases:**\n- New lead submission → WhatsApp your sales team\n- Order placement → SMS the kitchen/warehouse\n- Support ticket → Email the right department\n- Approval requests → WhatsApp the manager\n\n**Glide Setup:**\n1. Add a "Webhooks" action to your Glide workflow\n2. Point it to your FormBeep endpoint\n3. Map form fields to: phone, message, channel\n4. Fire — FormBeep handles the rest\n\n**Supported Channels:**\n📱 WhatsApp | 📲 SMS | ✉️ Email\n\n**Pricing:** Free tier (10 notifications/day), paid from $9/mo\n**Docs:** formbeep.com/docs/glide |
| **Website** | https://formbeep.com |
| **Documentation** | https://formbeep.com/docs/glide |
| **Support** | hello@formbeep.com |

### Glide-Specific Integration Guide (to publish)

**Title:** "How to Send FormBeep Notifications from Glide"  
**Content:**

1. In your Glide app editor, open the workflow for the action that triggers a notification
2. Add a new action → select "Webhooks" → "Send Webhook"
3. Configure the webhook:
   - **URL:** `https://api.formbeep.com/v1/send` (or your endpoint)
   - **Method:** POST
   - **Headers:** `Authorization: Bearer YOUR_API_KEY`, `Content-Type: application/json`
   - **Body:** `{ "to": "+1234567890", "message": "New order from [Customer Name]", "channel": "whatsapp" }`
4. Test the webhook — check that notification arrives on the chosen channel
5. Map dynamic fields (customer name, order total) from your Glide data

**Pro Tips:**
- Use conditional webhooks: only send WhatsApp for high-value orders (>= $100), email for others
- Set up separate webhooks for SMS (instant) + Email (receipt/detailed)
- Use FormBeep's multi-recipient feature to notify a team

### Submission Steps
1. Go to glideapps.com/plugins → Submit Integration
2. Fill in integration details + documentation link
3. Glide team reviews (timeline: 5-10 business days)

---

## 4. Bubble Plugin — Assignment for Forge

**Status:** Task to be assigned  
**Output path:** /root/moxie/products/formbeep/partnerships/bubble-plugin/

### Spec Summary
| Field | Value |
|-------|-------|
| **Plugin Name** | FormBeep Notifications |
| **Actions** | Send Alert, Check Status |
| **Inputs** | API Key, Phone, Message, Channel |
| **Output** | Bubble plugin file + installation guide |
| **Priority** | P2 (Week 2) |
| **Assigned to** | Forge (pending task creation) |

**Detailed plugin spec:** See /root/moxie/products/formbeep/partnerships/platform-partner-outreach.md (Bubble Plugin Task for Forge section)

---

## Application Checklist (Ready to Submit)

| Platform | Copy Ready | Screenshots Ready | Docs Ready | Status |
|----------|-----------|-------------------|------------|--------|
| Webflow | ✅ | 🟡 Need to capture | 🟡 Need to create | Application package prepared |
| Framer | ✅ | 🟡 Need to capture | 🟡 Need to create | Application package prepared |
| Glide | ✅ | ✅ (docs-based) | ✅ | Application package prepared |

**Note:** Actual submission requires accessing each platform's developer/partner portal with hello@formbeep.com credentials. Application materials are 100% copy-paste ready.

---

## Timeline Tracking

| Platform | Target Submit | Actual Submit | Review ETA | Status |
|----------|--------------|---------------|------------|--------|
| Webflow | Apr 1-2 | Pending creds | 5-7 days | Package ready |
| Framer | Apr 2-3 | Pending creds | 3-5 days | Package ready |
| Glide | Apr 3-4 | Pending creds | 5-10 days | Package ready |
| Bubble | Apr 7-9 | Forge to build | 10-14 days | Awaiting Forge |

---

## Dependencies for Execution

1. **Portal access credentials** for Webflow Apps, Framer Marketplace, Glide Plugins — need hello@formbeep.com login or existing accounts
2. **Screenshots/demo assets** — need live demo of each integration to capture
3. **Bubble plugin** — Forge must build the plugin first (Week 2)

---

## Updated Tracking Table

| Platform | Applied | Approved | Listed | Notes |
|----------|---------|----------|--------|-------|
| Webflow | Pending → Ready | — | — | Application package complete, awaiting portal access |
| Framer | Pending → Ready | — | — | Application package complete, awaiting portal access |
| Glide | Pending → Ready | — | — | Application package complete, awaiting portal access |
| Softr | Pending | — | — | Week 2 |
| Bubble | Pending | — | — | Week 2 — requires Forge build |

---

*Next review: 2026-04-07*
*Distributed to: hello@formbeep.com (pending submissions), Forge (Bubble plugin task)*
