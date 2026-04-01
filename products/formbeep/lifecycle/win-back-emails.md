# FormBeep Win-Back Email Sequence — Churned Users

*Version: 1.0 | Created by Luna (Lifecycle/CRM Lead) | Date: 2026-04-02*

---

## 1. Churn Definition + User Segments

### What counts as churned?
- **Soft churn:** 14+ days with zero alerts + no login
- **Hard churn:** 30+ days inactive OR subscription cancelled

### Segmentation Matrix (Behavioral + Lifecycle Integration)

| Segment | Definition | Win-back Angle | Priority |
|---------|------------|----------------|----------|
| **Setup-abandoned** | Signed up, never connected a form | Remove friction, offer direct help | P0 — highest recovery potential |
| **Test-only** | Connected form, sent test, no production alerts | Trigger fear of missing real leads | P0 — very close to activation |
| **Light-user** | 1–10 alerts total, then stopped | Show usage patterns they're missing | P1 |
| **Heavy-churned** | Previously active (10+ alerts), now silent | Ask what broke, offer incentive | P1 — high LTV if recovered |
| **Cancelled-sub** | Explicitly cancelled paid plan | Competitive check or pricing objection | P2 |
| **Free-expired** | Hit free-tier limit, didn't upgrade | Re-offer free month or showcase ROI | P1 |

---

## 2. Win-Back Sequence (Day 1 / 3 / 7 Post-Churn Identification)

### Email 1 — Day 1: "Did we break something?"

**Subject (A/B variants):**
- A: "Did something go wrong, {{ first_name }}?"
- B: "We miss your form alerts"
- C: "Quick question about your FormBeep setup"

**From:** Luna <hello@formbeep.com>

```
Hey {{ first_name }},

I noticed your form alerts have gone quiet. No pressure — just checking in.

Did something not work as expected? A few things that commonly trip people up:

1. Your integration token expired (refresh it → [Account Settings])
2. The form URL changed after a site update (re-paste the snippet → [Docs])
3. You switched platforms and need a new integration

If it's something else entirely, just reply to this email. I read every response personally and can usually get things fixed within a few hours.

If you just took a break and plan to come back — your account is right where you left it. Nothing expired.

— Luna, Lifecycle @ FormBeep
```

**Trigger:** `user.inactive.14d` (soft churn identified) OR `subscription.cancelled`
**CTA variants by segment:**
- Setup-abandoned → "Finish setup — I'll walk you through it"
- Test-only → "Go live with your first real alert"
- Light-user/Cancelled → "Reply with what went wrong"
- Free-expired → "Claim your free month back"

**Metric:** Reply rate (primary), click rate to account setup

---

### Email 2 — Day 3: The Use-Case Reminder

**Subject:**
- "That one lead you missed last week"
- "3 minutes to never miss a lead again"

**From:** Luna <hello@formbeep.com>

```
Hey {{ first_name }},

Quick reality check: your website forms are still collecting submissions. The question is — are you getting them in time?

Here's what most people don't realize: a lead who hears back within 5 minutes is **9x more likely to convert** than one who waits 30 minutes.

If your alerts haven't been firing, every form submission this week went into the void.

The good news: fixing FormBeep takes 3 minutes:

→ [Reactivate your alerts now]{{#if integration_type}}
  (We already have your {{ integration_type }} setup saved){{/if}}

If you're wondering whether FormBeep is still worth it at $6/month — one saved lead more than covers a year.

— Luna, Lifecycle @ FormBeep

P.S. If you're using Zapier or Make for form alerts, we can show you a simpler setup that doesn't break when API keys expire.
```

**Trigger:** No response to Email 1, still inactive
**CTA:** "Reactivate your alerts"
**Metric:** Reactivation rate (alerts fired within 24h of this email)

---

### Email 3 — Day 7: Final Offer + Last Call

**Subject:**
- "Last chance — your FormBeep account"
- "One month on us? ☕"

**From:** Luna <hello@formbeep.com>

```
Hey {{ first_name }},

This will be the last email from me about this — I don't want to be that person.

Before I close your file: I'd like to offer you **one free month of FormBeep Pro**, no strings attached.

→ [Claim your free month]{{#if cancellation_reason}}
  (We've noted you left because {{ cancellation_reason }} — we've made improvements since then){{/if}}

Why am I doing this? Because I genuinely believe FormBeep is the fastest way to never miss a website lead. If after another month you still don't find value, I'll close the account myself and you'll never hear from us again.

Either way, if you have 30 seconds I'd love to know: what would make FormBeep must-have for you?

Reply to this email anytime.

— Luna, Lifecycle @ FormBeep
```

**Trigger:** No response to Email 2, still inactive
**CTA:** "Claim free month" (reduces friction to zero)
**Metric:** Redemption rate, final reply rate (feedback)

**After this email:** Mark user as `winback_exhausted`. No further outbound for 90 days.

---

## 3. Churn Prevention (Pre-Churn Trigger Emails)

*These fire BEFORE churn is confirmed — highest ROI for retention.*

### Pre-Churn: "Usage dropped" Alert

**Trigger:** User had 5+ alerts/month baseline, now <2 this week
**Timing:** Day 3 of reduced usage (before 14-day churn trigger)

**Subject:** "Are your alerts still working?"

```
Hey {{ first_name }},

I noticed your form alerts have been quiet this week. Normally you get ~{{ avg_weekly_alerts }} alerts.

Could be a seasonal dip. Could be a broken integration. Want me to check?

Reply with "check" and I'll run a quick diagnostic on your setup.

— Luna @ FormBeep
```

---

## 4. Re-Engagement Offers

| Segment | Offer | Cost | Recovery Rate (industry benchmark) |
|---------|-------|------|-----------------------------------|
| Setup-abandoned | Personal setup call (15-min WhatsApp) | Time only | 20–30% |
| Test-only | Free month of Pro | ~$0.50/user | 15–20% |
| Light-user | "Reactivate & get double alerts this month" | $0 marginal | 10–15% |
| Cancelled-sub | 50% off first month back | ~$3/user | 8–12% |
| Free-expired | Free month reset + 50 extra alerts | $0.50/user | 12–18% |

---

## 5. Integration with Onboarding (Behavioral Triggers)

The improvement focus from the onboarding email system: **integrate behavioral triggers**.

### Trigger Flow Map

```
signup → (Day 0–1 emails: Welcome + Activation)
  ↓ no activation
  → setup-abandoned segment → winback sequence begins Day 14
  ↓ activated (test sent)
  → Day 3/7 emails active
  ↓ no production alerts in 14d
  → test-only segment → winback begins (higher urgency angle)
  ↓ active production user
  → Day 14 upgrade email
  ↓ usage drops >50%
  → pre-churn email fires (before winback)
  ↓ 14 days inactive
  → soft churn → winback sequence Day 1
  ↓ 30 days inactive or cancelled
  → hard churn → final offer (Email 3 gets upgraded)
```

### Onboarding → Winback Signal Handoff

| Onboarding Event | Winback Implication |
|-----------------|---------------------|
| Integration never connected | Use Setup-abandoned winback track |
| Test sent, no production | Use Test-only track — higher urgency |
| Production alerts sent, then stopped | Use Light-user / Heavy-churned track |
| User viewed pricing but didn't upgrade | Use Free-expired with pricing objection angle |
| User replied to any onboarding email | Prioritize human response in winback |

---

## 6. Metrics & Success Criteria

| Metric | Target (30-day sprint) | How Measured |
|--------|------------------------|--------------|
| **Winback activation rate** | >15% of soft-churned users | Users who fire an alert after winback |
| **Winback paid recovery** | >5% of churned paid users | Resubscribe after winback |
| **Feedback response rate** | >8% of winback recipients | Replies to winback emails |
| **Email open rate (winback)** | >25% (lower than onboarding — expected) | ESP tracking |
| **Pre-churn save rate** | >20% of pre-churn flagged users | Alerts resume after pre-churn email |

---

## 7. Bootstrap Implementation

**Day 1 (no ESP):**
```python
# Run daily: check for users inactive 14+ days
# Query user table for: signup_date, last_active, alert_count, plan
# Segment → pick email template → send via SMTP/Resend
# Log send to lifecycle_sends table
```

**When ESP available:**
- Map `user.inactive.14d` event → Winback Email 1
- Wait 48h → no click → Winback Email 2
- Wait 96h → no click → Winback Email 3
- Add 90-day suppression after winback_exhausted

---

## 8. Suppression & Frequency Rules

| Rule | Detail |
|------|--------|
| Max winback emails per cycle | 3 (Day 1/3/7) |
| Cooldown after exhausted winback | 90 days |
| Never send if user has a pending support ticket | Suppress until resolved |
| Cancelled users | Can receive winback if cancellation <60 days ago |
| Paid churn vs free churn | Different offers, same cadence |
| Compliance | Always include unsubscribe link (required for CAN-SPAM/GDPR) |

---

*Luna — Lifecycle/CRM Lead | Sapiens Technology LLC*
*Win-back sequence v1.0 | Next iteration: A/B test results from first 30-day run*
