# Pax Week 2 Platform Applications — FormBeep

> **Date:** 2026-03-31
> **Lead:** Pax (Partnerships / BD)
> **Product:** FormBeep — form-to-SMS/WhatsApp/email notifications
> **Sprint:** Week 2 — Softr integration + Week 1 follow-ups + Bubble plugin spec for Forge

---

## Objective

Execute Week 2 platform partner submissions (Softr), prepare follow-up materials for Week 1 applications (Webflow, Framer, Glide), and finalize the Bubble plugin task for Forge to build.

---

## 1. Softr Marketplace — Application Package

**Portal:** https://www.softr.io/integrations  
**Category:** Communication / Notifications  
**Prerequisites met:** ✅ FormBeep webhook API works with Softr forms via native webhook blocks

### Application Details

| Field | Content |
|-------|---------|
| **Integration Name** | FormBeep |
| **Tagline** | Real-time WhatsApp + SMS alerts for Softr form submissions |
| **Short Description** | Add instant SMS, WhatsApp, and email notifications to your Softr forms. When someone fills out your portal, application, or contact form — your team gets pinged immediately. No Zapier, no Make. |
| **Full Description** | Softr forms collect leads, applications, and support requests — but Softr doesn't push notifications when submissions arrive. FormBeep solves this.\n\nConnect any Softr form block to FormBeep and instantly route submissions to WhatsApp, SMS, or email. Perfect for:\n- Client portals where the team needs real-time visibility\n- Job application forms → SMS hiring managers\n- Event registration forms → WhatsApp organizers\n- Support/intake forms → route to the right department\n\n**How It Works:**\n1. In Softr Studio, add a Form block or use an existing one\n2. Add a "Webhook" action on form submit → point to your FormBeep endpoint\n3. Map fields: phone number, message content, channel (WhatsApp/SMS/Email)\n4. Test — notification arrives instantly on the chosen channel\n\n**Supported Channels:**\n📱 WhatsApp Business API | 📲 SMS (200+ countries) | ✉️ Email\n\n**Pricing:** Freemium — 10 free notifications/day, paid from $9/mo\n**Support:** hello@formbeep.com\n**Docs:** formbeep.com/docs/softr |
| **Website** | https://formbeep.com |
| **Documentation URL** | https://formbeep.com/docs/softr |
| **Support Email** | hello@formbeep.com |
| **Pricing Model** | Freemium |

### Softr-Specific Integration Guide (to publish at formbeep.com/docs/softr)

**Title:** "How to Add Instant Notifications to Softr Forms with FormBeep"

1. Open your Softr Studio project
2. Navigate to the page containing your form block
3. Click the form → go to Settings → "Actions after submission"
4. Add a "Webhook" action:
   - **Endpoint URL:** `https://api.formbeep.com/v1/send`
   - **Method:** POST
   - **Headers:** `Authorization: Bearer YOUR_API_KEY`, `Content-Type: application/json`
   - **Body (JSON):**
     ```json
     {
       "to": "{{field.phone_number}}",
       "message": "New submission from {{field.full_name}}: {{field.message}}",
       "channel": "whatsapp"
     }
     ```
5. Save and preview your app — submit a test response
6. Verify the notification arrives on the chosen channel
7. Duplicate the webhook to add email fallback alongside WhatsApp

**Pro Tips:**
- Conditional routing: use Softr's conditional actions to send WhatsApp for urgent/high-priority submissions, email for routine ones
- Multi-recipient: send to multiple team members by firing separate webhooks with different `to` values
- Use Softr's "Create Record" action + webhook together: store the submission AND notify the team simultaneously

### Asset Preparation Checklist
- [ ] Screenshots of Softr form block + webhook configuration
- [ ] Softr-specific logo/app icon if required by marketplace
- [ ] Live demo: Softr form submission → WhatsApp notification received

### Submission Steps
1. Contact Softr partnerships at partnerships@softr.io or use the integration request form at softr.io/integrations
2. Submit integration details + documentation link
3. Softr team reviews and may request a demo (prep a Loom video)
4. Expected timeline: 5-10 business days

### Follow-Up Plan (if no response in 7 days)
- Day 7: Email follow-up with Loom demo link
- Day 14: Try alternative contact via Softr community Slack/Discord
- Day 21: Last follow-up + offer to list Softr on formbeep.com/integrations reciprocally

---

## 2. Week 1 Application Follow-Up Kit

### Webflow Apps Marketplace

**Follow-up email (Day 5 after submission — send ~Apr 6):**

```
Subject: FormBeep App Submission — Follow-Up

Hi Webflow Apps team,

I submitted FormBeep to the Webflow Apps Marketplace on [submission date] under the Forms & CRM category.

FormBeep is a form-to-SMS/WhatsApp/email notification tool with a native Webflow integration. It's built specifically for the "missed lead" problem — agencies and SMBs using Webflow forms lose leads because they don't get notified in real-time.

Quick demo: https://[loom-demo-link]

Happy to provide any additional info or jump on a quick call if needed.

Thanks,
FormBeep Team
hello@formbeep.com
formbeep.com
```

**Status check:** If not yet submitted, the full application package is ready at `/root/moxie/products/formbeep/partnerships/platform-applications-week1.md`. Once Rishi provides portal credentials, we can submit same-day.

### Framer Marketplace

**Follow-up email (Day 4 after submission — send ~Apr 7):**

```
Subject: FormBeep Notifications Plugin — Submission Follow-Up

Hi Framer Marketplace team,

We submitted FormBeep Notifications to the Framer Marketplace on [submission date].

It's a zero-code plugin that connects Framer forms to instant WhatsApp, SMS, and email notifications — filling the notification gap that Framer users frequently request in the community.

App details: https://formbeep.com
Demo video: https://[loom-demo-link]

Let me know if you need anything else from our end.

Best,
FormBeep Team
hello@formbeep.com
```

**Status check:** Same as Webflow — full package ready, awaiting portal credentials.

### Glide Integrations

**Follow-up email (Day 5 after submission — send ~Apr 8):**

```
Subject: FormBeep Integration for Glide — Submission Follow-Up

Hi Glide team,

We submitted FormBeep as a Glide integration on [submission date].
It lets Glide app builders send WhatsApp, SMS, and email notifications from any workflow — no Zapier or Make required.

Integration docs: formbeep.com/docs/glide
Demo: https://[loom-demo-link]

Happy to provide a sandbox app for testing if that helps.

Thanks,
FormBeep Team
hello@formbeep.com
```

---

## 3. Bubble Plugin — Task Assignment for Forge

**Task:** Build a minimal Bubble plugin (API Connector pattern) wrapping FormBeep's REST API.

### Plugin Specification (Forge-Ready)

| Field | Value |
|-------|-------|
| **Plugin Name** | FormBeep Notifications |
| **Plugin ID** | `formbeep-notifications` |
| **Version** | 1.0.0 |
| **Publisher** | Sapiens Technology LLC |

### Bubble Actions

#### Action 1: `Send FormBeep Alert`
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | text | Yes | FormBeep API key |
| `phone` | text | Yes | Recipient phone number (E.164 format) |
| `message` | text | Yes | Message content |
| `channel` | dropdown | Yes | Options: `whatsapp`, `sms`, `email` |

**API Call (backend):**
```
POST https://api.formbeep.com/v1/send
Headers: Authorization: Bearer <api_key>, Content-Type: application/json
Body: { "to": "<phone>", "message": "<message>", "channel": "<channel>" }
```

**Response handling:** Return `message_id` (string) and `status` (string) to Bubble workflow.

#### Action 2: `Check FormBeep Delivery Status`
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | text | Yes | FormBeep API key |
| `message_id` | text | Yes | ID from Send Alert action |

**API Call (backend):**
```
GET https://api.formbeep.com/v1/status/<message_id>
Headers: Authorization: Bearer <api_key>
```

### Bubble Plugin Settings
| Setting | Type | Description |
|---------|------|-------------|
| `api_key` | text | User's FormBeep API key (saved once in plugin settings) |

### Deliverables Expected from Forge
- [ ] `plugin.json` — Bubble plugin manifest
- [ ] `actions.json` — Action definitions
- [ ] `shared.js` — Client-side code (if any)
- [ ] `servercode.js` — Server-side API call code
- [ ] `images/` — Plugin icon (recommended: 128×128px PNG with FormBeep branding)
- [ ] `README.md` — Installation guide + usage examples for Bubble users
- [ ] `demo-app-guide.md` — Step-by-step to build a test app in Bubble

### Output Path
`/root/moxie/products/formbeep/partnerships/bubble-plugin/`

### Priority Assignment
- **Assignee:** Forge
- **Priority:** P2
- **Estimated effort:** 2-4 hours (Bubble API Connector pattern is well-documented and straightforward)
- **Deadline:** End of Week 2 (by 2026-04-11)

---

## 4. Week 2 Tracking Update

| Platform | Target Submit | Actual Submit | Review ETA | Status |
|----------|--------------|---------------|------------|--------|
| Webflow | Apr 1-2 | Pending creds | 5-7 days | Package ready from Week 1, follow-up drafted |
| Framer | Apr 2-3 | Pending creds | 3-5 days | Package ready from Week 1, follow-up drafted |
| Glide | Apr 3-4 | Pending creds | 5-10 days | Package ready from Week 1, follow-up drafted |
| **Softr** | **Apr 7-9** | **Pending — this doc** | **5-10 days** | ✅ Application package ready |
| Bubble | Apr 7-11 | Forge to build | 10-14 days | ✅ Spec complete, assigned to Forge |

## Master Tracking Table

| Platform | Applied | Approved | Listed | Notes |
|----------|---------|----------|--------|-------|
| Webflow | Pending → Ready | — | — | Application package + follow-up email ready |
| Framer | Pending → Ready | — | — | Application package + follow-up email ready |
| Glide | Pending → Ready | — | — | Application package + follow-up email ready |
| **Softr** | **Pending** | — | — | ✅ Application package + integration docs ready |
| **Bubble** | **Pending** | — | — | ✅ Forge-ready spec complete |

---

## Dependencies & Blockers

| Dependency | Status | Owner |
|------------|--------|-------|
| Portal credentials (Webflow/Framer/Glide/Softr developer logins) | BLOCKED — need hello@formbeep.com access | Rishi |
| Screenshots + demo videos for listings | BLOCKED — need live demo access | Pax + Rishi |
| Bubble plugin build | Ready for Forge assignment | Forge |
| Forge task creation in orchestration.md | To be done by Moxie | Moxie |

---

## Next Actions (Week 3 Preview)

1. **Carrd integration** — create docs + submit to Carrd (P1)
2. **Typedream integration** — docs-only integration (P1)
3. **Agency outreach** — execute cold outreach to top 15 agency targets from target list
4. **Reciprocal listing** — publish formbeep.com/integrations featuring all approved platforms
5. **Bubble plugin review** — review Forge output and prepare Bubble marketplace submission

---

*Next review: 2026-04-07*
*Distributed to: hello@formbeep.com (pending submissions), Forge (Bubble plugin task)*
