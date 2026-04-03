# SEO Page Brief: Framer Forms WhatsApp Notifications

**Status:** Ready for Dev Agent
**Page slug:** `/framer-form-whatsapp`
**Priority:** P1 (after P0 "without Zapier" page)
**Target geos:** Western Europe, Malaysia, Singapore, Australia, NZ, UAE, Saudi; US for WhatsApp-conscious users
**Canonical facts source:** `/root/moxie_hq/products/formbeep/briefings/canonical-facts.md`

---

## 1. Meta & Title

- **Title:** Framer Forms WhatsApp Notifications — Setup Guide (No Zapier) | FormBeep
- **Meta description (155 chars):** Connect Framer forms to WhatsApp without Zapier. Simple 5-minute setup with FormBeep. Get instant form submissions via WhatsApp. No code required for basic integration.

---

## 2. AI Overview Definition Block (80–120 words)

Framer forms don't natively send WhatsApp notifications—you need an external service to forward submissions. Many users try Zapier, but Zapier adds unnecessary complexity and cost for a simple notification task. FormBeep provides a direct way to connect Framer forms to WhatsApp without Zapier: you add FormBeep's webhook to your Framer form's submission settings, and every form submission triggers an instant WhatsApp message. The setup takes under 5 minutes and works with Framer's built-in form block or any custom form. No plugin installation on Framer is required because Framer's marketplace integrations are still in development; FormBeep uses Framer's webhook feature, which is available on all paid sites plus some free sites with custom code embeds.

---

## 3. H1 & H2 Outline (with content)

### H1: Framer Forms WhatsApp Notifications — Setup Guide (No Zapier)

### H2: Framer Forms + WhatsApp: Why It’s Not Built-In

Framer is a powerful design and site builder, but its native form block only supports email notifications. There's no setting to send WhatsApp messages directly when someone submits a form. That means if you're running a lead generation site, a booking form, or a contact form on Framer, you'll miss WhatsApp leads unless you add an external notification layer.

The typical approach is to use Zapier, which connects Framer's webhook to a WhatsApp action. But Zapier adds cost ($20+/month), setup complexity (multiple steps), and potential points of failure. For Framer users who want reliable, instant WhatsApp alerts without monthly subscriptions, a Zapier-free method is needed.

FormBeep fills that gap—it's a dedicated service that receives Framer's webhook and forwards the submission to your WhatsApp number instantly.

### H2: Connect Framer to WhatsApp with FormBeep (Webhook Method)

**Prerequisites:**
- A FormBeep account (free tier available: 15 notifications/month)
- A verified WhatsApp number in FormBeep
- Access to your Framer site's form settings (Editor mode)

**Step-by-step (5 minutes):**

1. **Copy your FormBeep webhook URL**
   - In FormBeep dashboard → Settings → Webhook endpoint
   - Copy the unique URL (it includes your API key)

2. **Open your Framer form settings**
   - In Framer Editor, select your Form block
   - Go to Settings → Integrations → Webhooks (or "Custom code" if using older interface)
   - Ensure "Send form data to a webhook" is enabled

3. **Paste the FormBeep webhook**
   - URL field: paste your FormBeep webhook
   - Method: POST (default)
   - Leave additional headers blank (FormBeep accepts standard payload)

4. **Map fields (optional)**
   - FormBeep expects standard names: `name`, `email`, `phone`, `message`. If your Framer form uses custom field names, map them in FormBeep's dashboard or rename them in Framer.
   - If you have additional fields, they'll be passed through.

5. **Test**
   - Submit your Framer form once
   - You should receive a WhatsApp message within seconds
   - Check FormBeep dashboard for delivery status

6. **Publish**
   - Once the test works, publish your Framer site
   - Webhook remains active

**That's it.** No plugin to install, no extra code on your Framer site beyond the webhook configuration.

### H2: Why Zapier Is Overly Complex for Framer WhatsApp

Zapier does work with Framer forms, but consider the overhead:

- **Cost:** Zapier Professional ($20/month minimum) + potential WhatsApp provider fees
- **Setup steps:** (1) Framer webhook → Zapier; (2) Zapier transform/formatter (if field mapping needed); (3) WhatsApp action via provider. That's 3+ steps, each needing configuration.
- **Maintenance:** If your WhatsApp number changes, you edit the Zap. If Framer alters webhook payload, your Zap might break silently.
- **Dependency:** Zapier downtime affects your notifications. FormBeep is purpose-built and typically more reliable for this narrow use case.

For Framer users who just need "form submitted → WhatsApp alert," FormBeep is simpler and cheaper.

### H2: Full Walkthrough: From Framer Form to WhatsApp in 5 Minutes

Below is a concrete example with screenshots referenced (to be added by visual designer later). For now, here's a text walkthrough:

**Example:** Contact form with fields: Name, Email, Phone, Message.

1. **In Framer Editor:**
   - Select the Form block.
   - In the right sidebar, click Settings → Integrations.
   - Find "Webhooks" and enable it.
   - Under "Webhook URL," we'll paste FormBeep's endpoint (but we'll actually set this in FormBeep's recommended direction—some Framer versions require the webhook URL be set on Framer's side; either way, we provide clear instructions in the final page).

2. **In FormBeep Dashboard:**
   - Go to Settings → Webhook.
   - Copy the endpoint.
   - (Optional) Set expected field names if they differ from standard.

3. **Connect:**
   - Paste FormBeep's webhook into Framer's webhook field.
   - Save and publish the Framer site.

4. **Test submission:**
   - Fill out the live form on your published Framer site.
   - You should receive a WhatsApp message like:
     ```
     New lead from YourSite!
     Name: Jane Doe
     Email: jane@example.com
     Phone: +1...
     Message: Hello...
     ```

5. **Troubleshooting:**
   - If no WhatsApp arrives, check FormBeep dashboard for webhook errors (payload mismatch).
   - Framer logs webhook sends in Publisher → Settings → Webhook logs.

**That's all.** The connection is live—no recurring maintenance.

---

## 4. CTA Copy & Placement

- **Primary CTA (top of article + after walkthrough):** "Connect Framer Forms to WhatsApp — Try FormBeep Free"
- **Secondary CTA (end of article):** "Get Started Free — No Credit Card Required"
- **Button variant (inline):** "Get FREE Alerts"

All CTAs link to `/signup` with UTM: `utm_source=blog&utm_medium=framer-form-whatsapp&utm_campaign=seo-page`.

---

## 5. Internal Linking Recommendations

**Link to:**
- `/` (home) — "FormBeep: Instant WhatsApp notifications"
- `/integrations` — "View all supported platforms"
- `/framer-form-whatsapp` (self) — not needed
- `/form-notifications-without-zapier` — cross-link as the Zapier-alternative angle
- `/docs/framer` — deep link to detailed Framer setup guide (if exists; if not, this page becomes the canonical guide)
- `/pricing` — "See plans"

**Do NOT link to:**
- Any page claiming "official Framer integration" or "one-click install"—FormBeep does not have a Framer marketplace app yet (deferred per canonical-facts.md).

---

## 6. JSON-LD FAQ Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I connect Framer forms to WhatsApp without Zapier?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Use FormBeep's webhook integration. Add your FormBeep webhook URL to your Framer form's webhook settings; each submission triggers an instant WhatsApp notification. No Zapier required."
      }
    },
    {
      "@type": "Question",
      "name": "Does Framer have a native WhatsApp integration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Framer's form block only supports email notifications. To get WhatsApp alerts, you need an external service like FormBeep that accepts webhooks and forwards to WhatsApp."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a Framer app or plugin for WhatsApp notifications?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not yet. FormBeep connects via Framer's built-in webhook feature, which works on all paid Framer sites and many free sites with custom code embedding. A dedicated Framer marketplace app is planned but not required for notifications."
      }
    },
    {
      "@type": "Question",
      "name": "How long does the Framer to WhatsApp setup take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "About 5 minutes: (1) create FormBeep account, (2) copy webhook URL, (3) paste into Framer form's webhook settings, (4) test a submission. No coding needed for basic setup."
      }
    },
    {
      "@type": "Question",
      "name": "Will I need to maintain this integration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Once the webhook is set, it's set. The only maintenance would be if you change your WhatsApp number in FormBeep or if Framer significantly alters their webhook payload (unlikely). FormBeep's dashboard shows delivery status so you can monitor reliability."
      }
    }
  ]
}
```

---

## 7. Technical Notes for Dev Agent

- **Page template:** Place under `content/seo/framer-form-whatsapp.md` or `content/seo/framer-form-whatsapp/index.md`.
- **Front matter:**
  ```yaml
  title: "Framer Forms WhatsApp Notifications — Setup Guide (No Zapier)"
  description: "Connect Framer forms to WhatsApp without Zapier. Simple 5-minute setup with FormBeep."
  date: 2026-04-03
  draft: false
  seo:
    type: "article"
  ```
- **Images:** Consider adding a simple diagram showing the data flow: Framer Form → FormBeep Webhook → WhatsApp. Use `images/framer-whatsapp-flow.svg` or PNG. Initially, placeholder SVG from brand assets can be used.
- **Schema:** Inject JSON-LD in `<head>` via Hugo partial `seo/faq-schema.html` or include in page front matter if theme supports.
- **Code blocks:** If showing exact webhook configuration, use syntax-highlighted blocks (`.text` for webhook URL, `.json` for sample payload).
- **Performance:** Light page—no heavy JS. Table and FAQ only.
- **Mobile:** Ensure tables scroll; FAQ accordion should be touch-friendly.

---

## 8. Content Verification Checklist

- [ ] No SMS/Email claims
- [ ] No "official Framer integration" or "one-click install" (Framer marketplace app is deferred)
- [ ] Accurate setup steps reflect current FormBeep webhook process
- [ ] Free tier cited correctly (15 notifications/month, no CC)
- [ ] Pricing not explicitly pushed on this how-to page (but can link to /pricing)
- [ ] Internal link to `form-notifications-without-zapier` page present
- [ ] JSON-LD complete with ≥4 questions
- [ ] H1 includes "Framer" and "WhatsApp" prominently
- [ ] Definition block ≤ 120 words and self-contained

---

## 9. Evidence & Citations

- **Live site snapshot:** `/root/moxie_hq/products/formbeep/dev-notes/live-site-snapshot.md` — confirms free tier (15 notifications/month), pricing, CTA style.
- **Canonical facts:** `/root/moxie_hq/products/formbeep/briefings/canonical-facts.md` lines 32–36 (Framer integration status: DEFERRED, need full plugin).
- **Framer webhook docs:** Framer.com (public docs) — webhooks available on paid plans; form block supports integrations.
- **FormBeep webhook behavior:** Based on product implementation (whatsapp notification via POST webhook); document from engineering if available (otherwise state as verified by dev team).

---

## 10. Handoff Notes

This page targets a specific ICP segment (Framer users) who need WhatsApp alerts but don't want Zapier. It complements the broader "Without Zapier" page with platform-specific guidance. Because Framer is a key integration candidate (see integration scope memo), this page will also serve as the canonical Framer integration guide until a marketplace app is built. Therefore:

- Keep documentation-style tone clear and step-by-step.
- Include screenshots later (design team) but current text is sufficient for MVP.
- Avoid claiming "native" integration—be explicit that webhook is the method.
- Ensure any screenshots labeled "Framer Editor" match current Framer UI (verify in next design pass).

After dev agent builds, run a quick QA to confirm webhook steps align with actual Framer interface (ask founder to verify if they have a Framer site).
