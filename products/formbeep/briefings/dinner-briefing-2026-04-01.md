# FormBeep — Dinner briefing (CMO)
Date: 2026-04-01

You asked me to hold a tighter “briefing” for after dinner. This file is the snapshot.

---

## 1) What pages are driving traffic (Umami, last 30 days)
Top URLs by visitors/pageviews (Umami metrics url):
- / : 475
- /whatsapp-api-pricing/ : 56
- /blog/building-formbeep-weekend/ : 42
- /blog/webflow-whatsapp-notifications/ : 30
- /integrations/framer/ : 22
- /blog/ : 19
- /tools/whatsapp-link-generator/ : 12
- /blog/framer-whatsapp-notifications/ : 12
- /blog/why-you-are-missing-leads/ : 10
- /#pricing : 10

Immediate read:
- Homepage is still the main funnel entry.
- “WhatsApp API pricing” page is doing work (good SEO wedge).
- Blog posts are driving meaningful long-tail discovery already (small but real).

---

## 2) Landing → hero clicks (last 30 days, no Clarity)
Source file: /root/moxie/products/formbeep/analytics/landing-hero-funnel-30d.md

Baseline:
- Sitewide visitors: 659
- Landing visitors (‘/’): 475

Hero CTA (event):
- “Signup - Hero”: 14
- CTR vs landing visitors: 2.95%

Other CTA events (counts):
- Docs Click: 26
- Login Click: 13
- Signup - Header: 11
- Signup - Pricing: 3

Interpretation:
- Hero CTA is getting clicks, but docs is the #1 click. That usually means: people need more proof/clarity before signing up.

---

## 3) Employee rubric / evaluation metric — what’s happening
Status: rubric exists in orchestration documentation (scoring + scorecard paths), but I have NOT yet verified end-to-end that scorecards are being generated for recent tasks.

What we should verify next:
- Do we have any new files under: /root/moxie_hq/cmo/scores/** ?
- If not, we either (a) never wired task-scorer into completion, or (b) workers aren’t calling it.

Outcome:
- If rubric is not producing scorecards, we’ll either fix wiring or remove the rubric section (it becomes trust-breaking if it’s aspirational only).

---

## 4) US opportunity: SMS positioning (“Form → Phone”) 
Yes, it’s worth exploring even though we’re WhatsApp-first.

Why:
- US buyers are less WhatsApp-native; SMS is the “default urgent channel.”
- We already have SMS as a channel; this is a messaging + landing-page segmentation opportunity.

Risks / constraints:
- SMS in the US has compliance sensitivity (TCPA) if used to message leads. But we’re notifying the business owner/team about a submission (internal alert), which is typically safer. Still: wording must be careful.

Recommendation (low effort):
- Create a US-flavored landing variant (or page) that leads with SMS:
  - Title: “Get instant SMS alerts for every form submission.”
  - Subtitle: “No Zapier. Works with Webflow/WordPress/Framer.”
  - Keep WhatsApp as secondary (“Also supports WhatsApp”).
- Drive US traffic to that page via directories + content + future ads, then compare:
  - hero click rate
  - signup starts

---

## What I’ll bring you after dinner
- A short “so what” summary (3 bullets) + the single highest leverage change to the landing page based on the CTA distribution (docs-heavy).
