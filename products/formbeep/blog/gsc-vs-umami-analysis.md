---
title: "GSC vs Umami: Why Your Numbers Don’t Match (and What to Do About It)"
description: "A practical, evidence-first guide to reconciling Google Search Console with Umami analytics—using FormBeep’s current instrumentation as an example."
date: 2026-04-06
draft: false
slug: "gsc-vs-umami-analysis"
tags: ["analytics", "gsc", "umami", "seo", "attribution"]
---

# GSC vs Umami: Why Your Numbers Don’t Match (and What to Do About It)

TL;DR
- Google Search Console (GSC) measures search visibility (impressions/clicks from Google Search). It is not a “pageviews” tool.
- Umami measures on-site traffic (pageviews/visitors) based on a tracking script and/or API data.
- It’s normal for the two to differ. It’s not normal for Umami to be consistently zero if you expect real visits.
- Use an evidence-first checklist: verify the tracking script, confirm site IDs/API parameters, then validate events and funnel steps.

## The problem (framing)
You open GSC and see impressions (maybe even clicks), but your analytics dashboard looks empty. Or you see traffic in analytics, but GSC looks flat.

This creates two common failure modes:
- You don’t trust your SEO results.
- You don’t trust your conversion tracking.

The fix is not “pick one tool” — it’s to understand what each tool is capable of measuring, and then build a simple reconciliation process.

## Who it’s for
- Founders who want a trustworthy view of early SEO traction.
- Marketers trying to connect search visibility → landing page visits → signups.
- Developers responsible for analytics instrumentation and debugging.

## What each tool actually measures
### Google Search Console (GSC)
GSC is Google’s view of how your site appears in Google Search.

Key points:
- Impressions can be non-zero even if clicks are near-zero.
- GSC does not record “pageviews”.
- GSC is delayed (not real-time).

### Umami
Umami is an on-site analytics tool. It typically depends on:
- A tracking script successfully loading in the browser.
- A pageview being sent from the client.

Important: analytics blockers, script loading errors, or misconfigured site IDs can reduce or eliminate recorded traffic.

## FormBeep case study (what we observed)
This post references internal source data captured in:
- /root/moxie_hq/products/formbeep/analytics/gsc-vs-umami-study.md (source data)

What that source data says (paraphrased, with caution):
- The Umami API pull returned stats with zeros for pageviews/visitors/visits.
- Only “2 daily records” of pageviews were noted.
- The source data explicitly warns that Umami exports are not checked into the repo and any Umami figures should be treated as unverified until an API pull/output is captured.

That combination (GSC exports exist + Umami appears empty) is a classic “instrumentation or query mismatch” scenario.

## Step-by-step: reconcile GSC and Umami
### Step 1: Check you’re comparing the same thing
Before debugging, align definitions:
- GSC impressions ≠ visits
- GSC clicks ≈ (some) visits, but not all visits
- Umami pageviews include non-Google traffic (direct, referrers, social)

If you have impressions but no clicks, it is perfectly normal for Umami to show very low traffic.

### Step 2: Verify your Umami site ID and API timestamp format
From the source data:
- Umami Cloud API expects timestamps in milliseconds.
- The site ID must match the tracked site.

Checklist:
- Confirm the Umami “website_id” is correct.
- If you query the API, confirm start/end timestamps are in milliseconds (not seconds).

[Screenshot placeholder] Umami settings showing website_id
[Screenshot placeholder] Example API request parameters (startAt/endAt)

### Step 3: Confirm the tracking script is loading on the real site
If Umami shows zeros, check whether the browser is actually sending events.

Checklist:
- Open the live site in an incognito window.
- Disable ad blockers for one test run.
- Use the browser Network tab:
  - Is the Umami script loaded?
  - Are pageview requests being sent?

[Screenshot placeholder] DevTools Network tab showing Umami requests

### Step 4: Watch out for the “early-stage reality”
If your site is brand new, these can be true simultaneously:
- GSC shows impressions.
- You have near-zero clicks.
- Umami shows near-zero pageviews.

That’s not a tracking bug — it’s just low traffic.

A simple sanity check:
- If you personally visit the site from a clean browser session, you should see at least one visit in Umami.
- If you never see your own test traffic, that’s a stronger signal of misconfiguration.

### Step 5: Validate event tracking separately from pageviews
If pageviews exist but conversion events are missing:
- Confirm the event names and triggers are correct.
- Confirm CTAs and buttons are not inside elements that prevent event capture.

For FormBeep specifically, internal notes indicate click events are tracked with a naming convention (example: “Signup - <Location>”).

[Screenshot placeholder] Umami Events dashboard showing CTA click events

### Step 6: Use a “funnel map” to connect SEO → visits → conversion
Once pageviews and events are confirmed, build a simple funnel:
- Landing page view
- CTA click (“Get FREE Alerts” / “Get Started Free”)
- Signup completed

In the source data, a recommended next step is:
- Run /root/moxie/cmo/scripts/validate_funnel_metrics.py to map GSC segments to Umami events (as noted in the study).

## Common reasons for mismatches (quick table)
| Symptom | Likely cause | What to do |
|---|---|---|
| GSC impressions exist, Umami is zero | Low clicks (normal) OR Umami misconfig | Check clicks first; then verify script and API timestamps |
| GSC clicks exist, Umami still zero | Tracking script blocked or missing | Confirm script loads; test without blockers |
| Umami traffic exists, GSC looks flat | Traffic not from Google Search | Check referrers; look at non-search channels |
| Umami shows traffic, but signups are “mystery” | Missing event tracking / broken signup measurement | Add/verify events and UTM hygiene |

## What to screenshot / assets to add
- [Screenshot placeholder] GSC Performance report (queries + pages)
- [Screenshot placeholder] Umami Stats view (pageviews/visitors)
- [Screenshot placeholder] Umami Events list (CTA clicks)
- [Screenshot placeholder] A short “definitions” diagram: Impressions → Clicks → Pageviews → Events

## Internal links
- /docs (setup and troubleshooting)
- /pricing (plan limits; free tier)
- /integrations (supported platforms)
- Related reading: /blog/seo-guide-formbeep (or wherever this post is published)

## CTA
If you’re getting SEO impressions, the next job is responding fast when clicks turn into form submissions.

FormBeep helps you respond in seconds by sending instant form alerts on WhatsApp (email/SMS planned) — no Zapier workflow required.

- Try it free (15 notifications/month): /signup
- Read the docs: /docs

---

Source data
- /root/moxie_hq/products/formbeep/analytics/gsc-vs-umami-study.md

Notes on claims
- This post intentionally avoids traffic numbers or conversion metrics. Early-stage analytics is noisy; verify your own instrumentation before drawing conclusions."