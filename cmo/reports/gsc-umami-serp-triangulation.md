# GSC vs Umami vs SERP triangulation (FormBeep)

Owner: CMO / Growth Ops
Generated: 2026-04-06
Scope: FormBeep SEO landing pages + measurement plan using existing research.

Key constraint (truth layer)
- FormBeep canonical facts explicitly say NOT to claim SMS or email notifications as shipped yet.
  Source: /root/moxie_hq/products/formbeep/briefings/canonical-facts.md ("NOT implemented (claims to avoid): SMS notifications, Email notifications").
- Therefore: SMS-keyword pages can still be used as top-of-funnel education / "SMS coming soon" capture, but must NOT promise FormBeep sends SMS today.

Sources used (no new live SERP querying done in this task)
- GSC vs Umami study receipt: /root/moxie_hq/products/formbeep/analytics/gsc-vs-umami-study.md
- SERP research (DataForSEO live snapshots executed previously):
  - /root/moxie_hq/products/formbeep/seo/serp-opportunity-brief.md (24 queries; India WhatsApp + US SMS)
  - /root/moxie_hq/products/formbeep/seo/us-sms-serp-demand-brief.md (50 queries; US)
  - /root/moxie_hq/products/formbeep/seo/dataforseo-test-20260401T184621Z.md (1 query test: "form to sms")
- Page outlines / briefs:
  - /root/moxie_hq/products/formbeep/seo/page-outlines.md
  - /root/moxie_hq/products/formbeep/seo/page-briefs/form-notifications-without-zapier.md
  - /root/moxie_hq/products/formbeep/seo/page-briefs/framer-form-whatsapp.md
- Instrumentation notes:
  - /root/moxie_hq/products/formbeep/dev-notes/tracking-implementation-notes.md
- Canonical facts (truth-layer):
  - /root/moxie_hq/products/formbeep/briefings/canonical-facts.md

---

## 1) The triangulation model (what each system is for)

We want one measurement story per page/keyword that answers:
A) Are we being shown in search? (demand + indexing)
B) Are we being clicked? (snippet/position fit)
C) Are those clicks doing the right thing on-site? (intent match + conversion)
D) Are we actually winning/losing the SERP vs competitors? (rank + features)

Use each tool for what it measures best:

1) Google Search Console (GSC) = “search reality”
- Best for: impressions, clicks, CTR, average position by query and page.
- GSC is the only first-party data source for Google search demand and page/query pairing.

2) Umami = “site behavior + CTA interaction”
- Best for: landing page sessions/pageviews, CTA clicks, micro-funnel steps (scroll, pricing views), referrers (when not blocked).
- Umami cannot reliably tell you what query the user searched; it can show referrer/source and what they did once on your site.

3) SERP snapshot (DataForSEO) = “competitive context”
- Best for: who ranks top 10, SERP features (AI Overview, PAA, video), and whether a keyword is dominated by forums, docs, competitors, etc.
- Snapshot-based: it is time-specific. It must be re-run periodically to remain truthful.

Operationally:
- SERP tells you the battlefield (what page format to build and what you’re up against).
- GSC tells you whether Google is actually testing you for the keyword.
- Umami tells you whether your page converts once it gets traffic.

---

## 2) What data is actually reliable (and what is not)

Reliable (high confidence)
1) GSC impressions/clicks/CTR/avg position
- If the property is verified and the URL is canonical, GSC numbers are the correct “Google-side” truth.
- Caveats: delayed reporting; sampled/rounded at low volume; average position is a mean across many auctions.

2) DataForSEO SERP results (as-of timestamp)
- The SERP briefs are based on paid “live” SERP pulls (documented costs and endpoints).
- Reliable as a snapshot for: top ranking domains, SERP feature prevalence, and qualitative patterns.
- Caveats: not continuous; location/device dependent.

Conditionally reliable (requires verification)
3) Umami totals and funnels
- Canonical facts say Umami script is installed and some events exist.
  Source: canonical-facts.md + tracking-implementation-notes.md.
- However, the existing GSC vs Umami study notes:
  - Umami export is not checked into the analytics inputs folder.
  - The study’s Umami API output shown is effectively zeroed and only mentions “2 daily records”.
  Source: /products/formbeep/analytics/gsc-vs-umami-study.md.
- Interpretation: Umami is probably implemented on the marketing site, but we currently do not have a verified, reproducible Umami data pull in-repo. Treat Umami numbers as “directional” until we capture the API pull/export as evidence.

Not reliable / do not use as primary KPI
4) “SERP wins” inferred from a single day’s GSC position
- GSC can show average position improving without actually owning top 3 (because of long-tail mixing).
- Use DataForSEO (or repeated manual checks) for rank confirmation on head terms.

---

## 3) The 10-page keyword plan (with validation metric per page)

Measurement principle per page
- SERP validation = do we appear competitively for the intended keyword?
- GSC validation = is Google giving the page impressions for the intended query cluster?
- Umami validation = does the page produce meaningful intent signals (CTA clicks) and downstream conversions?

Primary conversion event definition (current)
- On-site: Umami events already tracked for signup CTAs (Signup - Header/Hero/Pricing/Final CTA).
  Source: tracking-implementation-notes.md.
- Cross-domain issue: actual signup completion happens at accounts.formbeep.com, which may not be tracked by the same Umami property.
  So: treat “Signup CTA click” as the consistent conversion proxy unless/until cross-domain signup completion is instrumented.

Table legend
- SERP metric = run DataForSEO “live advanced” weekly (safe proxy) OR use GSC avg position if SERP pull not available.
- GSC metric = page+query metrics (last 28d) and trend (WoW or MoM).
- Umami metric = page sessions + CTA click-through rate (CTR-to-signup-click).

### Plan: 10 keywords/pages

1) Page: /whatsapp-form-notification
- Primary keyword: whatsapp form notification
- Intent: informational → transactional
- SERP context: WhatsApp cluster competitive/fragmented; dedicated competitor WhatsForm appears frequently.
  Source: serp-opportunity-brief.md.
- Validation metrics:
  - SERP: DataForSEO rank <= 20 for primary keyword (US+India locations) and improved by >= 5 positions over 30 days.
  - GSC: impressions for query contains “whatsapp form notification” rising MoM; CTR >= site median for non-branded queries.
  - Umami: >= 200 organic landing sessions/month to this URL AND Signup CTA click rate (any Signup - *) >= 3%.

2) Page: /form-notifications-without-zapier
- Primary keyword: form notifications without zapier
- Intent: transactional (switch/cost)
- SERP context: anti-Zapier intent exists; Zapier often ranks even for “alternative” terms.
  Source: us-sms-serp-demand-brief.md + whatsapp-nozapier-opportunity-brief.md.
- Validation metrics:
  - SERP: presence in top 20 for keyword; page contains AI Overview-friendly definition block (verify via SERP snapshot features).
  - GSC: clicks for queries containing “without zapier” or “zapier alternative” to this page (query filter) > 0 and increasing.
  - Umami: Pricing CTA clicks (Signup - Pricing) attributable to this page >= 25/month OR >= 4% of sessions.

3) Page: /framer-form-whatsapp
- Primary keyword: framer form whatsapp
- Intent: transactional (platform-specific)
- SERP context: noted as underserved / weak competition in the US SERP demand brief.
  Source: us-sms-serp-demand-brief.md (platform-specific tier).
- Validation metrics:
  - SERP: rank <= 10 for “framer form whatsapp” (US, en, desktop) in weekly DataForSEO run.
  - GSC: impressions for queries containing “framer” + “whatsapp” mapping to this URL increasing WoW after publish.
  - Umami: Docs Click (if linking to docs) + Signup clicks combined >= 5% of page sessions.

4) Page: /webflow-form-whatsapp-without-zapier
- Primary keyword: webflow whatsapp form without zapier
- Intent: transactional (platform-specific + no-Zapier)
- SERP context: Webflow community/forum results often rank; opportunity to outrank with a definitive guide.
  Source: us-sms-serp-demand-brief.md (webflow form terms) + whatsapp-nozapier-opportunity-brief.md.
- Validation metrics:
  - SERP: rank <= 20 for the exact keyword variant or close variants (“webflow form whatsapp”, “webflow whatsapp notifications”).
  - GSC: page starts receiving impressions for “webflow” queries within 14 days of indexing.
  - Umami: Footer - Integrations (if added) + Signup clicks from this page >= 3% of sessions.

5) Page: /google-forms-to-whatsapp-without-zapier
- Primary keyword: google forms to whatsapp without zapier
- Intent: informational → transactional
- SERP context: Google forms terms are high demand; competitor WhatsForm ranks for “google forms to whatsapp” in the US brief.
  Source: us-sms-serp-demand-brief.md.
- Validation metrics:
  - SERP: rank <= 20 for keyword family (“google forms to whatsapp”, “google form whatsapp notification”, “without zapier”).
  - GSC: impressions for “google forms” + “whatsapp” queries to this page; avg position improves over first 60 days.
  - Umami: Scroll depth proxy (if implemented) 50% scroll rate >= 35% AND Signup clicks >= 2%.

6) Page: /wordpress-form-whatsapp-notification
- Primary keyword: wordpress form whatsapp notification
- Intent: transactional
- SERP context: WordPress plugin directory and WPForms content rank; opportunity via “solution + comparison” content.
  Source: serp-opportunity-brief.md + page-outlines.md.
- Validation metrics:
  - SERP: rank <= 20 for keyword; WordPress geo variations (US/IN) tracked.
  - GSC: CTR for this page >= 1.5% once impressions > 200/28d.
  - Umami: Signup - Header clicks from this page >= 10/month (platform pages should drive decisive clicks).

7) Page: /contact-form-whatsapp-notification
- Primary keyword: contact form whatsapp notification
- Intent: transactional (generic, high fit)
- SERP context: appears in WhatsApp cluster list.
  Source: serp-opportunity-brief.md.
- Validation metrics:
  - SERP: rank <= 20; confirm SERP dominated by how-tos/tools (snapshot) and tune content format accordingly.
  - GSC: impressions for “contact form” + “whatsapp” rise; page captures long-tail variants.
  - Umami: Hero CTA click rate >= 3.5% (generic pages should have high CTA intent).

8) Page: /html-form-whatsapp-integration-no-code
- Primary keyword: html form whatsapp integration no code
- Intent: transactional (DIY builder / developer-lite)
- SERP context: long-tail “send form data to whatsapp” developer intent exists.
  Source: serp-opportunity-brief.md + whatsapp-nozapier-opportunity-brief.md.
- Validation metrics:
  - SERP: rank <= 20 for at least one of the phrase variants (“html form whatsapp”, “send form data to whatsapp”).
  - GSC: query coverage breadth: >= 20 distinct queries landing on the page in 28d (signals long-tail capture).
  - Umami: Docs Click rate >= 2% (developer-ish readers should click docs) OR Signup clicks >= 1.5%.

9) Page: /booking-form-whatsapp-notification
- Primary keyword: booking form whatsapp notification
- Intent: transactional (use-case)
- SERP context: use-case cluster explicitly recommended for expansion; competitor templates suggest demand.
  Source: whatsapp-nozapier-opportunity-brief.md.
- Validation metrics:
  - SERP: rank <= 20 for “booking form whatsapp” variants.
  - GSC: impressions become non-zero within 30 days post-index (use-case pages are slower; threshold is “it’s showing”).
  - Umami: conversion proxy = Signup clicks >= 1% AND at least 1 assisted conversion path (page -> /pricing click or /integrations click) per week.

10) Page: /whatsapp-lead-notification
- Primary keyword: whatsapp lead notification
- Intent: transactional (sales/CRM use case)
- SERP context: listed in WhatsApp cluster; YouTube + Zapier often present.
  Source: serp-opportunity-brief.md.
- Validation metrics:
  - SERP: rank <= 20; if video results dominate, add a short embedded walkthrough and measure engagement.
  - GSC: CTR improvement test: rewrite title/meta until CTR > page median at similar position.
  - Umami: Demo interaction event (Demo - View Details Click) >= 2% of page sessions AND Signup clicks >= 2%.

Notes on SMS keywords/pages (gated)
- The SERP research shows a large SMS whitespace ("no dedicated tool ranks"), but canonical facts say SMS is not shipped.
- Recommendation: do NOT publish "FormBeep SMS" pages until SMS is real.
- Safe interim play: publish “How to…” SMS pages that do not claim FormBeep sends SMS; instead:
  - provide a neutral guide (Twilio/Zapier/ClickSend) + capture email for updates, OR
  - reframe to WhatsApp as faster alternative for WhatsApp-heavy geos.

---

## 4) How we will validate SERP without claiming live queries

We have two safe options:

Option A (preferred): scheduled DataForSEO “live advanced” runs
- Weekly run (same endpoint used in existing briefs): serp/google/organic/live/advanced
- Track the 10 primary keywords in 2 locations:
  - US (2840) and India (2356)
- Store JSON outputs in-repo with timestamped filenames.
- Metric to compute: rank position for our URL, plus SERP features present.

Option B: use GSC average position as a rank proxy
- If DataForSEO is paused, monitor:
  - avg position trend for the page’s primary query cluster
  - impression growth
- Limitation: average position is not a strict “rank” and can mask volatility.

---

## 5) Instrumentation checklist (make triangulation possible)

A) GSC instrumentation (search-side)
- [ ] Confirm property verification and API access actually works in this environment.
      Note: gsc-quick-audit.md is currently placeholder.
- [ ] Ensure sitemap submitted and clean; coverage/indexing issues resolved.
- [ ] Standardize canonical URLs and prevent duplicates (aliases, trailing slash, etc.).
- [ ] Add FAQ/HowTo schema where appropriate (align with high AI Overview + PAA prevalence).
- [ ] For each of the 10 pages, create a “primary query cluster” definition (regex list) for consistent reporting.

B) Umami instrumentation (site-side)
- [ ] Verify Umami script is actually present on production pages (canonical facts say yes).
      Script snippet: https://cloud.umami.is/script.js with website_id 750e37be-...
- [ ] Ensure each page has at least one tracked conversion proxy:
  - Signup - Header
  - Signup - Hero
  - Signup - Pricing
  - Signup - Final CTA
  Source: tracking-implementation-notes.md.
- [ ] Implement UTM preservation to accounts.formbeep.com (recommended Option A JS in tracking notes).
- [ ] Add footer tracking (Integrations/Blog/Roadmap/Tools) so we can measure assisted conversions.
- [ ] Add scroll depth tracking and demo interaction tracking where relevant.
- [ ] Create Umami goals/dashboards for:
  - page -> signup click rate
  - page -> docs click rate
  - page -> pricing click rate

C) Cross-domain conversion measurement (important gap)
- [ ] Decide the “true conversion” source of truth:
  - If accounts.formbeep.com can run Umami: add a second Umami property there or share the same one (privacy/ops decision).
  - If not: add server-side signup attribution logging (store utm_* and landing path at signup time).
- [ ] Minimum viable: capture a “signup completed” event keyed by a click-id passed from marketing site.

D) Evidence capture / governance (fix the current reliability gap)
- [ ] Store Umami API pull output (JSON/CSV) in /products/formbeep/analytics/inputs/ with a meta.json receipt.
      The current GSC vs Umami study explicitly notes missing Umami exports.
- [ ] Store GSC exports used for reporting alongside the report (already present for last 28d CSVs).
- [ ] For SERP, store DataForSEO JSON outputs with timestamps.

---

## 6) Minimal reporting template (weekly)

For each of the 10 pages, report a single line with 3 numbers:
- SERP: rank (US + IN) [from DataForSEO weekly run]
- GSC: impressions/clicks/CTR for primary query cluster (last 7d vs prior 7d)
- Umami: organic sessions + signup click rate (last 7d)

This prevents “dashboard soup” and forces alignment across systems.

---

## Appendix: StackStats (how triangulation would work there)

Current StackStats truth layer (no claims beyond shipped)
- StackStats traction and pricing are documented in /root/moxie_hq/products/stackstats/status.md.

If/when StackStats adds SEO pages:
- SERP: use DataForSEO snapshots for target queries (Substack analytics, subscriber analytics, etc.).
- GSC: track impressions/clicks for those query clusters.
- On-site analytics: measure demo activation (already referenced in existing content packs) plus signup/checkout conversion.

