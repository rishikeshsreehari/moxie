# Paid Ads SOP (Cross-Product) — SapiensTech

Owner: Nova (Paid Acquisition Lead)

This SOP standardizes **naming**, **UTMs**, **conversion taxonomy**, and **reporting cadence** across all SapiensTech products so we can:
- compare CAC/ROAS across products and channels
- avoid “tracking drift” when multiple people launch ads
- debug attribution quickly
- ship campaigns faster with reusable templates

---

## 0) The 4 rules (non-negotiable)

1) **No campaign launches without UTMs + conversion goals set** (even if goals are “soft”).
2) **One objective per campaign.** Separate prospecting vs retargeting vs brand.
3) **One landing page per intent.** Don’t send cold traffic to a generic homepage.
4) **Report weekly using the same scorecard.** If it’s not in the scorecard, it didn’t happen.

---

## 1) Naming Convention (accounts → campaigns → ad sets → ads)

### 1.1 Product codes

Use short codes (stable; never rename once shipped):
- `FB` = FormBeep
- `ST` = SapiensTech brand / cross-product / hiring / announcements

If a new product ships, create a 2–3 letter code.

### 1.2 Channel codes

- `GG` = Google Ads (Search/Performance Max)
- `MB` = Meta (FB/IG)
- `RD` = Reddit
- `LI` = LinkedIn (optional)
- `YT` = YouTube (optional)

### 1.3 Funnel / intent codes

- `BOF` = bottom-of-funnel (high intent keyword / competitor / “buy”)
- `MOF` = mid-funnel (solution aware)
- `TOF` = top-of-funnel (problem aware)
- `RT` = retargeting
- `BR` = brand defense

### 1.4 Creative / offer codes

- `HP` = homepage / general
- `LP` = dedicated landing page
- `CMP` = comparison page
- `TMP` = template page

Offer angle (examples; add as needed):
- `WA` = WhatsApp
- `SMS` = SMS
- `EM` = Email
- `ZAP0` = “No Zapier” angle
- `FAST` = speed/instant alert
- `AGY` = agency angle

### 1.5 Full campaign naming template

**Campaign name format:**

`{PROD}-{CH}-{GEO}-{FUNNEL}-{NET}-{OFFER}-{AUD}-{YYMMDD}-v{N}`

Where:
- `GEO`: `US`, `UK`, `CA`, `AU`, `ROW`, or `EN` (English-speaking bundle)
- `NET`: `SRCH` (search), `DSP` (display), `SOC` (social), `VID` (video)
- `AUD`: `KW` (keywords), `LAL` (lookalike), `INT` (interests), `RMK` (remarketing), `CMPTR` (competitor)
- `YYMMDD`: first launch date (never changes)
- `vN`: increment only when structure materially changes

**Example:**
- `FB-GG-US-BOF-SRCH-WA-KW-260331-v1`
- `FB-MB-EN-TOF-SOC-FAST-INT-260331-v1`
- `FB-RD-US-MOF-SOC-ZAP0-INT-260331-v1`

### 1.6 Ad set / ad group naming

**Ad group format (Search):**
`{THEME}-{MATCH}-{LP}`

- `THEME`: `whatsapp-form`, `contact-form`, `zapier-alt`, `sms-form`
- `MATCH`: `E` (exact), `P` (phrase), `B` (broad)
- `LP`: `LP1`, `LP2` etc.

**Example:** `whatsapp-form-E-LP1`

**Ad set format (Meta/Reddit):**
`{AUDSEG}-{PLACEMENT}-{LP}`

- `AUDSEG`: `agency`, `smallbiz`, `webflow`, `wordpress`, `framer`, `leadgen`
- `PLACEMENT`: `auto` or `feed` or `stories`

---

## 2) UTM Taxonomy (required)

### 2.1 Parameter standard

Always include:
- `utm_source` (platform)
- `utm_medium` (paid type)
- `utm_campaign` (campaign name)
- `utm_content` (creative identifier)
- `utm_term` (keyword, audience, or targeting descriptor)

Optional:
- `utm_id` (stable campaign ID if platform supports)

### 2.2 Allowed values

- `utm_source`: `google`, `meta`, `reddit`, `linkedin`, `youtube`
- `utm_medium`: `cpc`, `paid_social`, `display`, `video`

### 2.3 Mapping rules by platform

**Google Ads (Search):**
- `utm_source=google`
- `utm_medium=cpc`
- `utm_campaign={campaign.name}`
- `utm_term={keyword}` (use `{keyword}` ValueTrack)
- `utm_content={creative}` (or `{adgroupid}_{creative}`)

**Meta:**
- `utm_source=meta`
- `utm_medium=paid_social`
- `utm_campaign={campaign.name}`
- `utm_content={ad.name}` (or `{adset.name}__{ad.name}`)
- `utm_term={audience}` (short descriptor)

**Reddit:**
- `utm_source=reddit`
- `utm_medium=paid_social`
- `utm_campaign={campaign.name}`
- `utm_content={ad.name}`
- `utm_term={subreddit_or_interest}`

### 2.4 UTM examples

`https://formbeep.com/whatsapp-form-notifications/?utm_source=google&utm_medium=cpc&utm_campaign=FB-GG-US-BOF-SRCH-WA-KW-260331-v1&utm_term={keyword}&utm_content={creative}`

---

## 3) Conversion Taxonomy (cross-product standard)

### 3.1 Event naming

Use lowercase snake_case for events. Every product should map to this funnel:

**Acquisition / intent (soft):**
- `view_pricing`
- `view_signup`
- `click_signup`

**Activation (core):**
- `signup_start`
- `signup_complete`
- `onboarding_complete` (or equivalent)
- `integration_connected` (generic)
- `first_value` (the moment user gets the core outcome)

**Revenue:**
- `upgrade_start`
- `purchase_complete`

**Retention proxy (optional):**
- `active_day_7`
- `active_day_30`

### 3.2 Product-specific mapping (example: FormBeep)

For FormBeep, define `first_value` as:
- user successfully receives at least one real notification to WhatsApp/SMS/email

Suggested additional events:
- `create_endpoint`
- `send_test_notification`
- `add_destination_whatsapp`
- `add_destination_sms`

### 3.3 Primary conversion per channel

- Google Search (BOF): optimize for `signup_complete` (or `purchase_complete` if volume allows)
- Meta/Reddit (TOF/MOF): optimize for `signup_complete` initially; use `view_pricing` as secondary

---

## 4) Tracking + QA Checklist (before launch)

### 4.1 Pre-launch checklist (10 minutes)

- [ ] Landing page loads in <3s on mobile (rough check)
- [ ] UTM parameters present on final URL (spot check)
- [ ] `signup_start` fires when signup begins
- [ ] `signup_complete` fires at successful account creation
- [ ] Internal dashboard (or Umami/GA4) shows UTM values for a test click
- [ ] A “conversion receipt” screenshot saved in notes (timestamp + UTM)

### 4.2 Post-launch (first 24h)

- [ ] Spend is pacing (no runaway budgets)
- [ ] Search terms / placements checked for obvious junk
- [ ] At least 1 tracked `signup_start` event from ads (or we debug immediately)

---

## 5) Campaign Structures (starter templates)

### 5.1 Google Search (BOF) — template

**Campaign:** `FB-GG-US-BOF-SRCH-WA-KW-YYMMDD-v1`

Ad groups (separate):
- `whatsapp-form-E-LP1`
- `contact-form-whatsapp-P-LP1`
- `form-to-whatsapp-E-LP1`
- `zapier-whatsapp-form-P-CMP1`

Negative keywords (starter):
- free, whatsapp api pricing (if mismatch), jobs, meaning, definition, download

Landing pages:
- LP1: “WhatsApp form notifications” (core)
- CMP1: “FormBeep vs Zapier” (comparison)

Offers:
- “Instant alerts”
- “No Zapier required”
- “Works with Webflow / WP / Framer” (only if true)

### 5.2 Meta (TOF/MOF) — template

**Campaign:** `FB-MB-EN-MOF-SOC-FAST-INT-YYMMDD-v1`

Ad sets:
- `agency-auto-LP1`
- `smallbiz-auto-LP1`
- `webflow-auto-LP_webflow`

Creatives (minimum viable):
- 2 static image variants
- 1 short video (optional)

### 5.3 Reddit (MOF) — template

**Campaign:** `FB-RD-US-MOF-SOC-ZAP0-INT-YYMMDD-v1`

Targeting:
- interests: web design, freelancing, small business
- (optionally) subreddit targeting once we have validated lists

Creative:
- headline is the offer; body is 1–2 lines + clear CTA

---

## 6) Reporting Cadence (scorecard)

### 6.1 Daily (first 7 days of a new campaign)

- Spend
- Clicks / CTR
- CPC
- `signup_start`
- `signup_complete`
- Cost per signup
- Notes: what changed today (1 line)

### 6.2 Weekly (every Monday)

**Weekly scorecard (per product + channel):**
- Spend
- Signups (complete)
- CAC (cost per signup)
- Activation rate (`first_value / signup_complete`)
- Pay conversion (`purchase_complete / signup_complete`) if available
- Best ad (by CAC)
- Worst placement / keyword (by spend with no outcomes)
- Next week actions (max 3)

### 6.3 Decision thresholds

- If a campaign spends **$50+ with 0 signup_starts** → tracking/LP mismatch; pause + debug
- If a campaign spends **$100+ with 0 signup_completes** (and clicks are real) → offer/LP mismatch; iterate
- If CAC < target and activation is healthy → scale budget 20–30% every 48h

(Define CAC target per product; default early-stage target: “get any signups cheaply” + learn.)

---

## 7) Creative + Landing Page iteration loop

Iteration order (fastest to slowest):
1) headline + primary CTA
2) landing page hero (promise + proof)
3) ad creative angle
4) audience/keyword expansion
5) pricing tests

Always log changes:
- date
- what changed
- hypothesis
- result 48h later

---

## 8) Templates (copy/paste)

### 8.1 UTM builder snippet

`utm_source={source}&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}`

### 8.2 Weekly scorecard table

| Product | Channel | Spend | Clicks | CPC | Signup Start | Signup Complete | CAC | First Value | Activation % | Notes | Next actions |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

---

## 9) Implementation notes (where this plugs in)

- Ads should always point to a URL that captures UTMs and persists them through signup.
- If Umami is used per product, ensure UTM params are captured in Umami and are queryable.
- If GA4 is used, mirror the same UTMs; do not invent a second naming scheme.

---

## Change Log

- 2026-03-31: v1 created (naming + UTM + conversions + reporting cadence + starter structures)
