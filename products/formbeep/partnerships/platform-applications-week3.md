# Pax Week 3 Platform Applications — FormBeep

> **Date:** 2026-04-01
> **Lead:** Pax (Partnerships / BD)
> **Product:** FormBeep — form-to-SMS/WhatsApp/email notifications
> **Sprint:** Week 3 — Carrd + Typedream integration packages + Agency outreach to top 15 targets

---

## Objective

Ship Week 3 partnership deliverables: (1) Carrd integration docs, (2) Typedream integration docs, (3) execute cold outreach to 15 pre-qualified agency targets, and (4) prepare the framework for publishing formbeep.com/integrations reciprocal directory.

---

## 1. Carrd Integration Package

**Portal:** https://carrd.co (no formal marketplace — docs-based + community submission)
**Approach:** Since Carrd has no app marketplace, the growth play is:
- Publish authoritative integration docs targeting "Carrd form notifications" searches
- Pitch to Carrd community/forum + YouTube creators
- Enable reciprocal listing (Carrd featured on formbeep.com/integrations)
- Target long-tail SEO: "carrd form to sms", "carrd form to whatsapp"

### Carrd-Specific Integration Guide (for formbeep.com/docs/carrd)

**Title:** "How to Send SMS and WhatsApp Notifications from Carrd Forms with FormBeep"

**Meta Description:** Connect any Carrd form to instant WhatsApp, SMS, or email notifications using FormBeep. Step-by-step guide — no code required.

#### Step-by-Step Setup

1. **Build your form in Carrd**
   - Add a Form element to your Carrd site
   - Configure your form fields (name, email, phone, message, etc.)
   - In the form Settings, set the form action to "Webhook" (Carrd supports webhook actions on form submission)

2. **Configure the FormBeep webhook**
   - **Endpoint URL:** `https://api.formbeep.com/v1/send`
   - **Method:** POST
   - **Headers:**
     ```
     Authorization: Bearer YOUR_FORMBEEP_API_KEY
     Content-Type: application/json
     ```
   - **Body (Map your Carrd form fields):**
     ```json
     {
       "to": "{{phone_field}}",
       "message": "New lead from Carrd: {{name_field}} — {{message_field}}",
       "channel": "whatsapp"
     }
     ```

3. **Test the integration**
   - Publish your Carrd site (even the free tier supports forms)
   - Submit the form yourself
   - Verify the notification arrives on your chosen channel

4. **Optional: Set up multi-channel fallback**
   - Add a second webhook action in Carrd's form settings
   - Point it to the same FormBeep endpoint with `"channel": "email"`
   - Now you get both WhatsApp/SMS AND email for every submission

#### Use Cases for Carrd + FormBeep

| Use Case | Why FormBeep | Channel |
|----------|-------------|---------|
| Lead gen landing pages | Immediate response = 7x higher conversion | WhatsApp |
| Event RSVPs | Coordinate with the team instantly | SMS + Email |
| Contact forms | No more checking inboxes | WhatsApp |
| Job application forms | Notify hiring managers of new applicants | Email + SMS |
| Waitlist signups | Alert the founders when someone joins | WhatsApp |

#### Carrd-Specific Tips

- **Free tier works:** Carrd's free plan supports forms, so you can test FormBeep without upgrading
- **Carrd PRO ($19/yr):** Unlocks custom domains and advanced form features — this is our sweet spot audience (PRO users are more serious and likely to pay for FormBeep)
- **Embed workaround:** If Carrd's native webhook doesn't pass all fields, use a third-party form builder embedded in Carrd (e.g., Tally — which already has native FormBeep webhook support)

#### SEO Keywords Targeting
- Primary: "Carrd form notifications", "Carrd form to SMS", "Carrd WhatsApp notification"
- Secondary: "Carrd form webhook", "Carrd form auto reply", "Carrd form autoresponder"

---

## 2. Typedream Integration Package

**Portal:** https://typedream.com (Notion-style site builder; no formal marketplace)
**Approach:** Docs-based integration + community outreach + SEO

### Typedream-Specific Integration Guide (for formbeep.com/docs/typedream)

**Title:** "How to Get Instant SMS and WhatsApp Alerts from Typedream Forms"

**Meta Description:** Set up real-time WhatsApp, SMS, and email notifications for Typedream form submissions using FormBeep. Works with Typedream's built-in forms and third-party form embeds.

#### Step-by-Step Setup

Typedream handles forms in two ways. We'll cover both:

**Method A: Typedream's Native Forms + Webhook**

1. In Typedream, add a Form block to your page
2. Go to Form Settings → Advanced
3. Set up a webhook action pointing to: `https://api.formbeep.com/v1/send`
4. Add the Authorization header: `Bearer YOUR_FORMBEEP_API_KEY`
5. Map form fields to the body:
   ```json
   {
     "to": "{{field.phone}}",
     "message": "New Typedream form submission: {{field.name}}",
     "channel": "whatsapp"
   }
   ```

**Method B: Embed Third-Party Form (Recommended for Full Control)**

Since Typedream's custom webhook capabilities may vary, embed any of these FormBeep-compatible forms:

1. Create your form in Tally, Typeform, or a Webflow form embed
2. Embed it into your Typedream page using the Embed block
3. Configure the embedded form's webhook to point to FormBeep
4. FormBeep sends notifications to your chosen channel(s)

#### Why Typedream Users Need FormBeep

Typedream is popular among:
- **Solopreneurs building Notion-style sites** — they need instant lead alerts
- **Agencies building client sites** — they need multi-recipient notifications
- **Creators with waitlists and link-in-bio pages** — they hate checking email

Typedream doesn't have built-in push notifications for form submissions. FormBeep fills this gap.

#### SEO Keywords Targeting
- Primary: "Typedream form notifications", "Typedream form to SMS"
- Secondary: "Typedream form webhook", "Typedream form autoresponder"

---

## 3. Agency Outreach — Top 15 Targets

### Selection Criteria

Agencies that fit FormBeep's ideal partner profile:
- **Build on no-code platforms** (Webflow, Framer, Carrd, Typedream) — their clients need form notifications
- **5-50 employees** — big enough to have processes, small enough to adopt new tools quickly
- **Serve SMBs/consultants/professionals** — the exact FormBeep buyer persona
- **Active on social/blog** — co-marketing potential

### Top 15 Agency Targets

| # | Agency | Focus | Why | Platform Fit | Est. Reach |
|---|--------|-------|-----|-------------|-------------|
| 1 | **Finsweet** | Webflow ecosystem (custom integrations/templates) | Top Webflow community, huge audience of Webflow builders | Webflow | 50K+ followers |
| 2 | **Relume** | Webflow component library / design tools | Massive Webflow dev community | Webflow | 30K+ users |
| 3 | **Flowbase** | Webflow templates + tutorials | Popular Webflow education platform | Webflow | 20K+ subs |
| 4 | **Made by Fewls** | Webflow agency | Webflow-first agency with blog/tutorials | Webflow | 10K+ audience |
| 5 | **Wannabe** | Framer templates & community | Growing Framer community presence | Framer | 15K+ users |
| 6 | **Layerlab** | Framer templates + resources | Active in Framer ecosystem | Framer | 10K+ followers |
| 7. **Frutiger Studio** | Framer agency | Framer-focused build agency | Framer | 5K+ audience |
| 8. **Gridworthy** | No-code consultancy (Webflow + Framer) | Multi-platform agency | Webflow/Framer | 3K+ network |
| 9. **NoCode HQ** | No-code education + community | Broad no-code audience across platforms | Multi | 20K+ community |
| 10. **Nocode.Tech** | No-code tools directory | Listed in our target directory — partnership opportunity | Multi | 15K+ visitors |
| 11. **Makerpad** (now Zapier) | No-code education | Acquired by Zapier — but community leader | Multi | 50K+ alumni |
| 12. **The No Code Foundry** | No-code agency for startups | Builds for startups — ideal FormBeep users | Multi | 5K+ network |
| 13. **Softr Academy** | Softr courses/tutorials | Softr training — their students need form notifications | Softr | 10K+ learners |
| 14. **Bubble Community** (Bubble forum) | Bubble plugin ecosystem | 3M users need plugins — partnership visibility | Bubble | Forum: 200K+ |
| 15. **Carrd Community** (Reddit r/Carrd) | Carrd user community | Active subreddit — perfect for value-driven post | Carrd | 15K members |

*Note: Agencies ranked #1-8 are active builders; #9-15 are communities/educators. Both can drive qualified leads.*

### Outreach Strategy

**Approach:** Value-first partnership ask, not a pitch. We're offering them a useful tool for their clients, plus potential co-marketing.

**Priority tiers:**
- **Tier 1 (Days 1-3):** Reach out to #1-5 (Finsweet, Relume, Flowbase, Made by Fewls, Wannabe)
- **Tier 2 (Days 4-7):** Reach out to #6-10
- **Tier 3 (Days 8-14):** Reach out to #11-15 (community posts + forum engagement)

---

## 4. Outreach Templates

### Template A: Email Outreach (for Agencies #1-10)

**Subject:** Quick question — do your clients ask for form notifications?

```
Hi [Name],

I noticed [Agency] builds great sites for [client type/industry]. Quick question — do your clients ever complain about not getting notified instantly when someone fills out their contact or lead forms?

FormBeep (formbeep.com) sends form submissions directly to WhatsApp, SMS, or email in real-time. No Zapier, no middleware. Agencies using it get happy clients who never miss a lead.

Would you be open to a quick demo? I can also whitelist your agency for free if you'd like to test it with a client site first.

Best,
[Your Name]
FormBeep Team
hello@formbeep.com
```

### Template B: Co-marketing Proposal (for #1-5, the bigger players)

**Subject:** Partnership idea: [Agency] + FormBeep

```
Hi [Name],

I'm [Your Name] from FormBeep — we build form-to-SMS/WhatsApp notifications for no-code platforms.

Your [Webflow/Framer] community content is fantastic. I've been thinking there's a natural fit here:

Your audience builds sites with forms. FormBeep makes those forms actually notify their owners in real-time. It's a problem we both see — and we'd love to solve it for your community together.

A few ideas:
- Guest post or walkthrough on your blog/YouTube
- Whitelist [Agency] for free FormBeep access for your client projects
- Include [Agency] in our formbeep.com/integrations directory (reciprocal listing)

Open to a quick 15-min chat to explore?

Best,
[Your Name]
formbeep.com
```

### Template C: Community Post (for #11-15 forums/Discord/Reddit)

**Title:** We built instant form notifications for [Platform] users — no Zapier needed

```
Hey everyone — quick share.

We've been building FormBeep, a tool that sends your [Platform] form submissions to WhatsApp, SMS, or email the moment they come in. No Zapier, no Make. Just paste a webhook endpoint and you're set.

Why we built it: we kept hearing from [Platform] users that they were missing leads because they don't check their email fast enough. FormBeep solves that with instant phone alerts.

How it works:
1. [Platform] form submits → hits FormBeep webhook
2. FormBeep sends the data to WhatsApp/SMS/email (your choice)
3. You get notified on your phone, instantly

It's free for 10 notifications/day, paid plans start at $9/mo.

Would love feedback from this community — and I'm happy to help anyone set it up if they're interested.

formbeep.com
```

---

## 5. formbeep.com/integrations — Reciprocal Directory Plan

Once any platform approves our listing, we should publish an integrations page that:

**Structure:**
```
formbeep.com/integrations

Integrations

FormBeep works with any platform that can send a webhook. Here are the ones we've tested and documented:

[Logo] Webflow
  Send forms → WhatsApp/SMS/Email. Native Webflow integration.
  → Webflow Apps Marketplace (pending)

[Logo] Framer
  Zero-code plugin. Connect Framer forms to instant notifications.
  → Framer Marketplace (pending)

[Logo] Glide
  Add notification actions to Glide workflows.
  → Glide Plugins (pending)

[Logo] Softr
  Form blocks → instant team alerts.
  → Softr Integrations (pending)

[Logo] Carrd
  Lightweight sites with real-time form alerts.
  → View docs →

[Logo] Typedream
  Notion-style sites with instant notifications.
  → View docs →

[Logo] Bubble (coming soon)
  Native plugin for Bubble workflows.
  → Join waitlist →
```

**SEO value:** This page targets "integrations" keywords for multiple platforms. Each platform link can carry a dofollow link (we ask for reciprocity when they approve).

**Implementation:** Hugo template — just a new content file `content/integrations/_index.md`. No code dependencies.

**Blocker:** None — can be built once Pax confirms at least 1 platform is pending or approved.

---

## 6. Week 3 Execution Plan

| Day | Action | Owner | Status |
|-----|--------|-------|--------|
| Wed Apr 2 | Publish Carrd integration docs page | Pax/Forge | Ready to build |
| Wed Apr 2 | Publish Typedream integration docs page | Pax/Forge | Ready to build |
| Thu Apr 3 | Send outreach emails to Tier 1 agencies (#1-5) | Pax | Awaiting creds |
| Fri Apr 4 | Send outreach emails to Tier 2 agencies (#6-10) | Pax | Awaiting creds |
| Mon Apr 7 | Post community content for Tier 3 (#11-15) | Pax | Needs Reddit account |
| Tue Apr 8 | Draft formbeep.com/integrations page | Pax/Kiro | Ready |
| Wed Apr 9 | Follow up on agency responses | Pax | Post-outreach |

### Tracking: Agency Outreach Funnel

| Stage | Count | Target |
|-------|-------|--------|
| Total targets | 15 | 15+ |
| Outreach emails sent | 0 | 10 by end of Week 3 |
| Replies received | 0 | 2-3 expected |
| Demos booked | 0 | 1 expected |
| Partnership confirmed | 0 | 1+ by end of Month 1 |
| Co-marketing content published | 0 | 1+ |

---

## Updated Master Platform Tracking

| Platform | Applied | Approved | Listed | Notes |
|----------|---------|----------|--------|-------|
| Webflow | Pending → Ready | — | — | Week 1 package ready, awaiting portal access |
| Framer | Pending → Ready | — | — | Week 1 package ready, awaiting portal access |
| Glide | Pending → Ready | — | — | Week 1 package ready, awaiting portal access |
| Softr | Pending | — | — | Week 2 package ready, awaiting portal access |
| Bubble | Pending | — | — | Forge assigned to build plugin (Week 2) |
| **Carrd** | **Docs ready** | N/A | — | **Week 3 — docs-based (no marketplace)** |
| **Typedream** | **Docs ready** | N/A | — | **Week 3 — docs-based (no marketplace)** |

---

## Agency Outreach Tracking

| # | Agency | Contact | Outreach Sent | Reply | Notes |
|---|--------|---------|--------------|-------|-------|
| 1 | Finsweet | hello@finsweet.com | — | — | Webflow community leader |
| 2 | Relume | hello@relume.io | — | — | Webflow components + design |
| 3 | Flowbase | hello@flowbase.co | — | — | Webflow education |
| 4 | Made by Fewls | (website) | — | — | Webflow-focused agency |
| 5 | Wannabe | (website) | — | — | Framer templates |
| 6 | Layerlab | (website) | — | — | Framer resources |
| 7 | Frutiger Studio | (website) | — | — | Framer agency |
| 8 | Gridworthy | (website) | — | — | Multi-platform agency |
| 9 | NoCode HQ | (website) | — | — | No-code community |
| 10 | Nocode.Tech | (website) | — | — | Tools directory |
| 11-15 | Community posts | Forums | — | — | Bubble, Carrd, Softr communities |

---

## Dependencies & Blockers

| Dependency | Status | Owner |
|------------|--------|-------|
| Portal credentials (Webflow/Framer/Glide/Softr) | BLOCKED — need hello@formbeep.com access | Rishi |
| Agency contact emails (researched, some need verification) | BLOCKED — verified emails needed | Pax |
| Reddit account for community posts | BLOCKED — need account access | Rishi (see issues_rishi.md) |
| formbeep.com/integrations page | BLOCKED — needs Hugo deploy | Kiro/Forge |
| Bubble plugin | Pending Forge build | Forge |

---

## Business Impact Analysis

This Week 3 work targets three growth levers simultaneously:

1. **Carrd + Typedream docs:** SEO play — captures users searching for "[platform] form notifications." Combined search volume is low but conversion-ready (they want the solution NOW). Expect 50-150 visitors/month from these long-tail keywords.

2. **Agency outreach:** Distribution amplifier. Even 1 partnership with a community (Finsweet, Flowbase, NoCode.HQ) could drive 500-2K targeted visitors/month via their audience. This is the highest-leverage acquisition channel in the partnerships pipeline.

3. **Integrations directory:** Trust + SEO multiplier. Each integration card boosts domain authority by internal linking and keyword targeting. Reciprocal links from platform partners compound the SEO benefit.

**Expected outcome from Week 3:** 1-2 agency conversations started, 2 integration docs live, integrations page framework ready.

---

*Next review: 2026-04-08*
*Distributed to: hello@formbeep.com, Kiro (integrations page), Forge (docs pages)*
