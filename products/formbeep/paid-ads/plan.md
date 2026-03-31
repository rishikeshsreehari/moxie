# FormBeep — Paid Acquisition Plan (Sprint 1)

Owner: Nova (Paid Acquisition)
Last updated: 2026-03-31

## Goal (7 days)
- Primary: **5 new free users** (signups) with clear learning on best channel + message.
- Secondary: Build a repeatable **tracking + campaign structure** so scaling is mechanical.

## Constraints / assumptions
- Early stage: optimize for **learning + signal quality**, not ROAS.
- Target buyer: English-speaking SMBs + agencies + freelance devs.
- Product: "form → WhatsApp/SMS/email notifications" (fast value, simple setup).

---

## 0) Measurement & tracking (do this before spending)

### A. UTM standard
Use the same UTM schema across all channels so Umami can segment cleanly.

**UTM template**
- utm_source: google | meta | reddit
- utm_medium: cpc
- utm_campaign: fb_<channel>_<objective>_<audience>_<offer>_<geo>_<yyyymmdd>
- utm_content: <creative_angle>_<format>_<v#>
- utm_term: <keyword> (Google only)

**Examples**
- Google Search: `utm_source=google&utm_medium=cpc&utm_campaign=fb_google_search_highintent_core_us_20260331&utm_term=contact+form+to+whatsapp&utm_content=whatsapp-notifications_text_v1`
- Meta: `utm_source=meta&utm_medium=cpc&utm_campaign=fb_meta_leads_no-code_us_20260331&utm_content=zapier-alternative_static_v1`
- Reddit: `utm_source=reddit&utm_medium=cpc&utm_campaign=fb_reddit_clicks_webflow_us_20260331&utm_content=form-to-whatsapp_text_v1`

### B. Landing pages (minimal set)
Run ads to **two** destinations max to keep learning clean:
1) Homepage (general): `/`  
2) High-intent page: `/whatsapp-api-pricing/` (already a top page)

If possible (nice-to-have), create a 1-page paid landing later:
- `/lp/form-to-whatsapp/` (copy: "Get WhatsApp notifications from your website forms in 5 minutes")

### C. Conversion events (what we can measure now)
Using Umami (already installed):
- **Primary proxy conversion:** `signup_click` (already tracked; total 4 so far)
- **Secondary:** `docs_click`, `login_click`

**Ideal (next iteration)**
- Track `signup_completed` (server-side or front-end event on success page)
- Track `activation` (first form connected / first notification sent)

### D. Success criteria (7-day)
- Baseline: low traffic, low signup clicks.
- Paid test success if we get:
  - ≥ 40–80 high-intent clicks total
  - CTR ≥ 3% (search) / ≥ 0.8% (meta) / ≥ 0.4% (reddit)
  - **Signup click rate** ≥ 3–6% on LP
  - At least **1–3 signups** (even if not all convert to paid yet)

---

## 1) Channel 1 — Google Search (highest intent)

### Objective
Capture people actively searching for "form → WhatsApp" / "WhatsApp form notifications".

### Campaign structure
**Campaign A: Search — High Intent Core (US/CA/UK/AU)**
- Bid strategy: Max Clicks (first 3–5 days) → then Max Conversions if conversion tracking is solid.
- Daily budget: **$10–$25/day**
- Locations: start **US** only (optional expand day 3)
- Ad schedule: all day

### Ad groups + starter keywords (phrase/exact)
**Ad group 1: Form to WhatsApp**
- "contact form to whatsapp"
- "form to whatsapp"
- "website form whatsapp notification"
- "whatsapp form notifications"
- "send form submission to whatsapp"

**Ad group 2: Webflow/Framer forms**
- "webflow form whatsapp"
- "webflow form notifications whatsapp"
- "framer form whatsapp"

**Ad group 3: Alternative/replace Zapier**
- "zapier whatsapp form"
- "send form to whatsapp without zapier"

### Negatives (starter)
- free download, apk, mod, hacked, jobs, careers, whatsapp business api documentation (if too broad), twilio api docs (unless targeting devs specifically)

### Ads (RSA copy angles)
**Angle 1: speed + simplicity**
- H1: WhatsApp Alerts for Form Submissions
- H2: Setup in 5 Minutes
- Desc: Get notified on WhatsApp when customers submit your forms. Works with Webflow + Framer. No Zapier required.

**Angle 2: agencies/devs**
- H1: Form → WhatsApp for Client Sites
- H2: Simple Integration
- Desc: Route leads to WhatsApp, SMS, and email. Great for agencies managing multiple sites.

### Extensions
- Sitelinks: Pricing, Integrations, Docs, Blog
- Callouts: No-code friendly, Fast setup, Webflow/Framer, Email + WhatsApp

### Landing suggestion
Send to `/whatsapp-api-pricing/` with UTMs.

---

## 2) Channel 2 — Meta (FB/IG) Prospecting (mid intent, bigger reach)

### Objective
Test hooks for SMB owners + agencies who want lead notifications and faster response times.

### Structure
**Campaign B: Meta — Leads/Traffic to site (US/CA/UK)**
- Daily budget: **$10–$20/day**
- Optimization: Link clicks initially; switch to conversions when `signup_completed` exists.

### Ad sets (2–3 only)
1) **No-code builders / SMB owners**
   - Interests: Webflow, Framer, Wix, Squarespace, small business, entrepreneurship
2) **Agencies / freelancers**
   - Interests: web design, digital marketing, freelancing, WordPress (optional), Webflow
3) **Retargeting** (if enough traffic)
   - Website visitors 30 days; exclude signups.

### Creative concepts (simple to ship)
- Static 1: "Don’t miss leads" (phone notification visual)
- Static 2: "Form → WhatsApp in minutes" (3-step graphic)
- Short video (optional): screen recording: connect integration + receive WhatsApp ping

### Primary copy angles
- Speed: "Respond to leads in minutes—get WhatsApp alerts instantly"
- Reliability: "Stop checking email—WhatsApp/SMS notifications for form submissions"
- Agency: "Set up WhatsApp lead alerts on client sites"

### Landing
Homepage `/` for broad; test `/whatsapp-api-pricing/` for higher intent.

---

## 3) Channel 3 — Reddit Ads (tight targeting, creative-first)

### Objective
Intercept audiences already discussing Webflow/Framer/WordPress forms and lead handling.

### Structure
**Campaign C: Reddit — Traffic**
- Daily budget: **$5–$15/day**
- Targeting: subreddits (start small)

### Subreddit targets (starter)
- r/webflow
- r/framer
- r/smallbusiness
- r/Entrepreneur
- r/WordPress (optional; until WP plugin is resubmitted)

### Creative (Reddit-native)
- Text ad format, straightforward:
  - Title: "Get WhatsApp alerts when someone submits your Webflow form"
  - Body: "FormBeep sends form submissions to WhatsApp/SMS/email so you respond faster. Setup takes ~5 minutes."
  - CTA: "Try free"

### Landing
Prefer `/integrations/framer/` for r/framer and `/integrations/webflow/` for r/webflow if these pages exist; otherwise `/whatsapp-api-pricing/`.

---

## 4) Budget + timeline (7-day sprint)

### Day 0 (today)
- Create UTM conventions; ensure all ad links include UTMs.
- Confirm Umami segments show UTM params.

### Days 1–2
- Launch **Google Search** only (fastest signal).
- Spend ~$10–$25/day.
- Goal: 15–30 clicks/day.

### Days 3–4
- Add Meta prospecting (small budget) + 1 retargeting ad set if feasible.
- Pause low CTR ads.

### Days 5–7
- Add Reddit ads if creative + targeting is ready.
- Consolidate learnings: winning keyword(s) + top message angle.

---

## 5) Reporting (daily 5-min dashboard)
Track per channel:
- Spend
- Impressions / CTR / CPC
- Landing page sessions (Umami filtered by utm_source)
- Signup clicks (per source)
- Notes: what changed

**Decision rules**
- If Google CTR < 3% on high intent → tighten keywords + rewrite RSAs.
- If signup-click rate < 2% → landing page mismatch; change destination or above-the-fold CTA.
- If CPC is high but signup clicks exist → keep; early stage learning is fine.

---

## 6) What I need from Rishi (not required to start planning)
- Confirm target geo focus for paid tests (US only vs US/CA/UK/AU).
- Confirm primary signup endpoint and whether a "signup success" page exists to track `signup_completed`.
