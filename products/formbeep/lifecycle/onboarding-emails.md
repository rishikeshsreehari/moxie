# FormBeep Lifecycle Onboarding + Activation Emails

---

## 1. ICP + Job-to-be-Done

### Primary ICPs
1. **Lead-gen agencies** — Managing 5–30 client sites. Every missed inquiry = lost revenue or an angry client. They already use WhatsApp for client comms.
2. **SMB owners** (clinics, consultants, home services) — One person wears all hats. The website form is their #1 lead source but their inbox is a graveyard.
3. **Freelance devs / builders** — Deliver client sites and want a clean, low-maintenance handoff. "Set once and forget" is the standard.

### Job-to-be-Done
> "When a prospect fills out a form on my site, I want to know **instantly** — not hours later when I finally check email — so I can respond while the lead is still warm and win the job."

### Activation definition
A user is **activated** when they:
- Connect their first form/integration
- Send at least one test submission
- Receive their first real alert (WhatsApp, email, or SMS)

**Target: Day 1 activation rate > 60%**

---

## 2. Lifecycle Stages Overview

| Stage | Timing | Trigger | Goal |
|-------|--------|---------|------|
| Welcome | Day 0 (immediate on signup) | User creates account | Confirm signup, set expectation, drive to "Connect your first form" |
| Activation prompt | Day 1 (24h after signup) | No test submission OR no form connected | Remove friction — show exactly how to connect in 3 minutes |
| Feature discovery | Day 3 | User activated but no production form live | Show real use cases, nudge to go live |
| Social proof / use case | Day 7 | User has not sent a production alert yet | Build trust with customer story + one specific use case |
| Upgrade nudge | Day 14 | User on free tier, active usage | Explain paid value, offer upgrade path |
| Winback | Day 30 | User inactive for 7+ days | Re-engage with a quick win or gather feedback on why they left |

---

## 3. Email Copy

### Email 1 — Welcome (Day 0)

**Subject:** Never miss a lead again 📬

**From:** Moxie <hello@formbeep.com>

```
Hey {{ first_name }},

Welcome to FormBeep. You just eliminated the one thing that kills most leads: **waiting too long to respond.**

Here's what to do next — it takes 3 minutes:

1. Pick your form platform (Webflow, WordPress, Framer, or custom HTML)
2. Follow the {{ integration_type }} guide → [Setup Guide Link]
3. Send a test submission — you'll get an alert in seconds

That's it. Once your first alert arrives, you're set.

Quick links:
- Setup docs → [Docs Link]
- Need help? Reply to this email

— Team FormBeep
```

**Trigger:** Account created
**CTA:** "Set up your first form"
**Metric:** Open rate, click rate → integration page

---

### Email 2 — Activation Prompt (Day 1)

**Subject:** Did you connect your form yet?

**From:** Moxie <hello@formbeep.com>

```
Hey {{ first_name }},

Just checking in — did you connect your form yet?

Most users are up and running in under 3 minutes. Here's the fastest path:

{{#if integration_selected}}
You picked {{ integration_type }}. Here's the step-by-step:
→ [Quick Start for {{ integration_type }}]
{{else}}
Pick your platform and we'll walk you through it:
→ [Choose your platform]
{{/if}}

Three things you'll get:
✓ Instant WhatsApp, email, or SMS alerts for every submission
✓ No Zapier or complex workflows
✓ A test mode so you can verify before going live

Still stuck? Just reply to this email — we're here to help.

— Team FormBeep
```

**Trigger:** 24 hours since signup AND (no form connected OR no test submission)
**CTA:** "Finish setup — takes 3 min"
**Metric:** Activation rate after this email (target: 40% of recipients activate within 24h)

---

### Email 3 — Feature Discovery (Day 3)

**Subject:** What to do when a lead submits your form

**From:** Moxie <hello@formbeep.com>

```
Hey {{ first_name }},

Now that FormBeep is connected, here's a tip most people don't know:

**Lead response time matters more than your follow-up script.**

Studies show the odds of qualifying a lead drop 80% after just 5 minutes. With FormBeep, you're notified the second someone submits — so you can strike while they're still thinking about you.

Things you can do right now:
• Add a second alert channel (WhatsApp + email = double coverage)
• Share the alert number with your sales rep or client
• Set up a custom message format so alerts show exactly what you need

→ [Manage your alerts]

Questions? Hit reply.

— Team FormBeep
```

**Trigger:** 3 days since signup AND (user has connected a form OR completed activation)
**CTA:** "Manage your alert settings"
**Metric:** Feature adoption rate (add second channel, customize message)

---

### Email 4 — Social Proof / Use Case (Day 7)

**Subject:** How agencies never miss a client lead

**From:** Moxie <hello@formbeep.com>

```
Hey {{ first_name }},

A lead-gen agency we work with manages 12 client sites. Before FormBeep:

- Lead inquiries landed in 12 different inboxes
- Response time: hours (sometimes days)
- Lost contracts because they were "too slow to quote"

After switching to FormBeep:

- Each client gets their own WhatsApp alert
- Response time: under 5 minutes
- Zero missed inquiries in 3 months

The setup for all 12 sites took about 40 minutes total.

If you run multiple sites or manage forms for clients, this is the highest-ROI 40 minutes you'll spend this quarter.

→ [Add another site]

— Team FormBeep
```

**Trigger:** 7 days since signup AND no production alert sent (or low usage: < 5 alerts)
**CTA:** "Add another site / scale up"
**Metric:** Multi-site adoption, production alert volume increase

---

### Email 5 — Upgrade Nudge (Day 14)

**Subject:** You're on the free tier — here's what you're missing

**From:** Moxie <hello@formbeep.com>

```
Hey {{ first_name }},

You've been using FormBeep's free tier — great start!

If you're getting value from instant alerts, here's what you unlock when you upgrade:

- **More alerts per month** — never hit a cap when a campaign takes off
- **Multiple websites** — connect all your client sites under one account
- **Priority delivery** — your alerts skip the queue during peak hours
- **Email + WhatsApp + SMS** — triple-channel redundancy so nothing slips through

It costs less than a single missed lead.

→ [See pricing](https://formbeep.com/pricing)

Need a custom plan for your agency? Just reply to this email.

— Team FormBeep
```

**Trigger:** 14 days since signup, still on free tier, active user (at least 1 alert sent)
**CTA:** "Upgrade to Pro"
**Metric:** Free-to-paid conversion rate (target: 5–10% of free users by Day 30)

---

### Email 6 — Winback / Churn Prevention (Day 30)

**Subject:** Still using FormBeep?

**From:** Moxie <hello@formbeep.com>

```
Hey {{ first_name }},

We noticed it's been a while since your last form alert.

If something didn't work as expected, we'd love to know — reply to this email and we'll fix it.

If you just haven't had a chance to finish setup, it still takes only 3 minutes:
→ [Pick up where you left off]

And if FormBeep isn't the right fit right now — that's okay too. We'll keep your account ready if you need it later.

Either way, thanks for trying FormBeep.

— Team FormBeep
```

**Trigger:** 30 days since signup AND inactive for 7+ days (no alerts in last 7 days)
**CTA:** "Resume setup" or "Reply with feedback"
**Metric:** Winback rate, feedback responses

---

## 4. Trigger Definitions + Required Events

To power this lifecycle system, the product needs to emit these events:

| Event | When fired | Data captured |
|-------|------------|---------------|
| `account.created` | User signs up | user_id, email, signup_source, plan |
| `integration.connected` | User connects a form platform | user_id, platform_type |
| `test_submission.sent` | User sends a test form | user_id, delivery_channel |
| `alert.delivered` | Real alert delivered | user_id, delivery_channel, alert_count (total) |
| `user.inactive.7d` | No alerts in 7 days | user_id, last_active_date, total_alerts |
| `plan.changed` | User upgrades/downgrades | user_id, old_plan, new_plan |

### Integration notes
- If using a service like Postmark, SendGrid, or Resend: map events → user properties → trigger automated sends
- For bootstrap phase: run a daily cron query → manually sends via API — works without a full automation stack
- Minimum viable: a script that runs once/day, checks user signup dates + activity, and fires the right email

---

## 5. What to Measure

### Core KPIs

| Metric | Target (30-day sprint) | How to calculate |
|--------|------------------------|-------------------|
| **Day 1 activation rate** | >60% | Users who connected a form + sent a test within 24h ÷ total signups |
| **Day 7 activation rate** | >75% | Users with at least 1 production alert in 7 days ÷ total signups |
| **Free → paid conversion** | 5–10% | Upgraded users ÷ total free tier signups |
| **Churn (30-day)** | <15% | Inactive users at Day 30 ÷ Day 0 cohort |
| **Email open rate** | >40% | Tracked via ESP |
| **CTA click rate** | >15% | Clicks ÷ opens |

### Reporting cadence
- Daily: activation rate (day 0 cohort vs current)
- Weekly: full funnel (signup → connect → test → first alert → upgrade)
- Monthly: cohort retention analysis

---

## 6. In-App Messaging Plan

Even before a full ESP is connected, you can run lifecycle through **in-app banners + the setup wizard**:

| Screen | Message | Goal |
|--------|---------|------|
| Post-signup dashboard (no form connected) | "Connect your first form — takes 3 minutes" with platform picker | Drive activation |
| After first connection | "Send a test alert to verify everything works" | Confirm delivery |
| After first alert | "Add a second channel for redundancy" | Feature adoption |
| Free tier user approaching limits | "You've sent X alerts. Upgrade to never hit a cap" | Upgrade |

---

## 7. Simple Segmentation + Messaging Matrix

| Segment | Definition | Messaging focus |
|---------|-----------|-----------------|
| **New signup** | < 24 hours old | Setup guide, reduce friction |
| **Activated user** | Connected + tested | Advanced features, multiple platforms |
| **Multi-site user** | 2+ platforms connected | Plan upgrade, agency features |
| **Stalled user** | No action in 3–7 days | Re-engage, offer help |
| **At-risk user** | No action in 14+ days | Winback, feedback request |
| **Paid user** | On Pro plan | Retention, referrals, NPS |
---

## 8. Bootstrap Implementation (No ESP Required)

**Phase 1 (Week 1): Manual + Script-based**
- Run a daily Python script that queries FormBeep's user table
- Match users to lifecycle stage based on signup date + activity
- Send emails via SMTP (SendGrid free tier / Resend) using templates above
- Log all sends for tracking

**Phase 2 (Month 2): Automated with customer.io / SendGrid Journeys**
- Map events → email automation platform
- Set up the 6-email flow with real-time triggers
- Add A/B testing for subject lines

**Phase 3 (Quarter 2): Full lifecycle CRM**
- Add in-app messages, push notifications
- Behavioral triggers (e.g., user viewing pricing page but not upgrading)
- Automated winback with discount codes

---

*Version: 1.0 | Created by Luna (Lifecycle/CRM Lead) | Date: 2026-03-31*
