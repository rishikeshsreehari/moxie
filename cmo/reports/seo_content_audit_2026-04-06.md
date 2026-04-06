# SEO + Content Audit — FormBeep + StackStats
Date: 2026-04-06
Repo: /root/moxie_hq (plus product site workspaces referenced below)

This report audits (1) current indexable pages / IA, (2) whether a blog exists, (3) missing “foundational” SEO/conversion pages, (4) technical SEO basics (sitemap/robots/metadata), and (5) a prioritized content backlog (10 posts each).

Evidence sources used
- FormBeep marketing site (Hugo): /root/moxie/formbeep/landing (content/, layouts/, static/)
- FormBeep GSC export (top pages last 28d): /root/moxie_hq/products/formbeep/analytics/inputs/gsc_pages_last28d.csv
- FormBeep technical SEO audit notes: /root/moxie_hq/products/formbeep/technical-seo-audit.md

- StackStats “live site snapshot” (copy + pages observed): /root/moxie/products/stackstats/dev-notes/live-site-snapshot.md
- StackStats GSC export (top pages last 28d): /root/moxie/products/stackstats/analytics/inputs/gsc_pages_last28d.csv
- StackStats canonical facts (stack + claims constraints): /root/moxie/products/stackstats/briefings/canonical-facts.md
- StackStats SEO outlines (planned pages): /root/moxie/products/stackstats/seo/page-outlines.md


========================
FORMBEEP (formbeep.com)
========================

1) Current pages (observed)

A) From Hugo content tree (/root/moxie/formbeep/landing/content)
Core + legal
- / (content/_index.md)
- /privacy/ (content/privacy.md)
- /terms/ (content/terms.md)
- /whatsapp-api-pricing/ (content/whatsapp-api-pricing.md)

Integrations
- /integrations/ (content/integrations/_index.md)
- /integrations/webflow/ (content/integrations/webflow/index.md)
- /integrations/framer/ (content/integrations/framer/index.md)

Tools (TOFU SEO / link magnets)
- /tools/ (content/tools/_index.md)
- /tools/whatsapp-business-bio-generator/
- /tools/whatsapp-chat-button-generator/
- /tools/whatsapp-link-generator/
- /tools/whatsapp-message-formatter/
- /tools/whatsapp-qr-code-generator/
- /tools/whatsapp-contact-form-generator/

Blog
- /blog/ (content/blog/_index.md)
- /blog/building-formbeep-weekend/
- /blog/whatsapp-business-api-explained/
- /blog/why-you-are-missing-leads/
- /blog/why-formbeep/
- /blog/whatsapp-leads-private-number/
- /blog/whatsapp-form-notifications/
- /blog/webflow-whatsapp-notifications/
- /blog/framer-whatsapp-notifications/
- /blog/framer-whatsapp-without-zapier/

B) From GSC pages export (last 28d)
(/root/moxie_hq/products/formbeep/analytics/inputs/gsc_pages_last28d.csv)
- / and hash anchors (#how-it-works, #pricing)
- /blog and /blog/ (both present)
- Individual posts (multiple)
- /integrations/framer/ and /integrations/webflow/
- /terms and /terms/ (both present)
- Tools pages (multiple)
- /whatsapp-api-pricing/ (dominant impressions: 2047)

Takeaway: IA exists and is fairly broad (home + blog + integrations + tools). Blog exists and is already indexed.


2) Blog status
- Blog exists (content/blog/*) with at least 9 published posts (page bundles).
- Blog appears to be indexing (GSC shows impressions on multiple posts).
- Primary SEO risk called out in the existing technical audit: large images in blog bundles causing performance / CWV risk.


3) Missing or weak “foundational” pages (SEO + conversion)

P0 missing/weak (affects conversions + rankings)
- Dedicated Pricing page (/pricing/): currently traffic is going to /whatsapp-api-pricing/. That page is a “WhatsApp API pricing explainer”, not a product pricing page.
  Recommendation: keep /whatsapp-api-pricing/ as SEO asset, but add /pricing/ as the canonical product pricing page and cross-link them.
- “How it works” page (/how-it-works/) separate from homepage anchors: anchors show up in GSC, but anchors aren’t real pages; a dedicated page can rank and be linked.
- “Alternatives/Comparisons” hub: e.g. /alternatives/ or /compare/ for high-intent searchers.

P1 missing (SEO breadth + trust)
- /about/ (founder story, why trust, uptime/reliability claims)
- /contact/ or /support/ (clear support contact; also helps trust/EEAT)
- /security/ (even a short page: data handling, retention, encryption posture; aligns with FAQ claim in JSON-LD about deletion)
- /status/ link (if a status page exists) or uptime page
- More integration pages for the builders mentioned in marketing claims (Wix, Squarespace, Shopify, Carrd, Ghost, etc.). Currently only Webflow + Framer are present in the Hugo content tree.


4) Technical SEO basics (sitemap/robots/metadata)

What exists (confirmed in repo)
- robots.txt exists: /root/moxie/formbeep/landing/static/robots.txt
  - Includes Sitemap: https://formbeep.com/sitemap.xml
  - Disallows /categories/ and /tags/
  - Allows /llms.txt
- Sitemap template exists: /root/moxie/formbeep/landing/layouts/sitemap.xml
- Metadata implementation exists: /root/moxie/formbeep/landing/layouts/partials/head.html
  - <title>, meta description
  - canonical tag
  - robots meta tag (based on .Params.noindex)
  - OpenGraph + Twitter tags
  - JSON-LD structured data (Organization, WebSite, SoftwareApplication, plus FAQPage + Product on home)

Known issues / risks (from technical-seo-audit.md + code)
P0
- Performance risk: multi‑MB PNGs in blog posts; img shortcode lacks lazy-loading + explicit dimensions.
  (See: /root/moxie_hq/products/formbeep/technical-seo-audit.md)

P1
- Taxonomy pages: robots.txt disallows /categories/ and /tags/ but sitemap template ranges over .Data.Pages, which can include taxonomy/term pages if enabled.
  Fix: exclude taxonomy/term kinds from sitemap and/or disable taxonomy output.
- meta keywords rendering: head.html prints .Params.keywords directly; if keywords are an array, it can render as [a,b,c]. Clean by delimiting.

P1 / hygiene
- Trailing slash duplicates in GSC (/terms and /terms/, /blog and /blog/). Ensure 301 + consistent canonicals.


5) Recommended actions (prioritized)

P0 (this week)
1) Fix blog image weight + lazy loading (WebP/AVIF + resize, add loading="lazy" decoding="async"; add width/height).
2) Ensure taxonomy pages are noindex + excluded from sitemap (or disable taxonomies entirely).
3) Address trailing-slash duplication with redirects/canonicalization.
4) Build /pricing/ page and link it prominently from home; keep /whatsapp-api-pricing/ as SEO explainer but convert it with clear FormBeep CTA.

P1 (next)
5) Add /how-it-works/ page (indexable) and point homepage anchors to that page.
6) Add /compare/ pages (Zapier, Make, Twilio DIY; plus “WhatsApp notifications vs email”).
7) Expand integrations pages: WordPress (CF7/WPForms), Wix, Squarespace, Shopify, Carrd, Tally, Typeform.
8) Add /security/ + /support/ pages (trust).


6) Content backlog (10 posts) — FormBeep
Goal: convert existing impressions (esp. /whatsapp-api-pricing/) into a topical cluster: “form notifications → WhatsApp/SMS, no Zapier, specific builders”.

1) “WhatsApp Form Notifications: The Complete Setup Guide (No Zapier)”
   - Intent: how-to / high TOFU; internal links to /integrations/* and signup.
2) “Webflow Form to WhatsApp: 3 Ways (and the fastest one)”
3) “Framer Form Notifications to WhatsApp: Step-by-step (2026)”
4) “WordPress Contact Form 7 SMS Notifications (without Twilio code)”
5) “WPForms SMS Notifications: Setup + routing to multiple recipients”
6) “Carrd Contact Form Notifications: WhatsApp alerts in minutes”
7) “Tally Forms WhatsApp Notifications: How to get instant alerts”
8) “Zapier vs FormBeep for lead alerts: cost, reliability, and setup time”
9) “Email vs WhatsApp vs SMS for lead alerts: response-time math + when to use each”
10) “How to stop losing leads: 9 reasons form submissions don’t get answered (with fixes)”


========================
STACKSTATS (stackstats.app)
========================

1) Current pages (observed)

A) From live-site snapshot + tracking inventory
(/root/moxie/products/stackstats/dev-notes/live-site-snapshot.md and tracking-implementation-notes.md)
- / (landing)
- /license
- /changelog
- /instructions (referenced in outreach intel elsewhere)
- demo.stackstats.app (interactive demo)
- buy.stackstats.app (Gumroad checkout domain)

B) From GSC pages export (last 28d)
(/root/moxie/products/stackstats/analytics/inputs/gsc_pages_last28d.csv)
- https://stackstats.app/
- https://demo.stackstats.app/
- /changelog and /changelog/
- /license and /license/
- /manage-license and /manage-license/
- /privacy and /privacy/
- /terms and /terms/

Takeaway: StackStats has core legal/support-ish pages already (privacy/terms, license, manage-license, changelog). No blog is visible in current indexed pages.


2) Blog status
- No blog detected in the indexed page list (last 28d) and not referenced in live snapshot.
- Current content strategy is “SEO landing pages” (6 outlines) rather than ongoing blog.

Recommendation: ship the 6 SEO pages first (they are designed as evergreen landing/guide pages), then add a lightweight blog only if you can maintain it.


3) Missing or weak “foundational” pages (SEO + conversion)

P0 missing/weak
- Download/install pages for OS-specific intent (if not already present):
  - /download (or /download/mac, /download/windows)
  This captures high-intent queries and clarifies onboarding.
- “What is StackStats / how it works” page separate from home; useful for linking from Reddit/X.

P1 missing
- /faq/ page (indexable) with schema; addresses: offline/local, Substack connection, refunds, licensing, BYOK/Ollama.
- /examples/ or /teardowns/ (indexable): link the “example teardown” promised in landing copy patch.
- If you want topical authority: /guides/ (but only if you’ll ship at least 6-10 pieces).


4) Technical SEO basics (sitemap/robots/metadata)

What we can confirm from this workspace
- We do NOT have the StackStats marketing site source code in /root/moxie_hq.
- However, canonical facts state marketing site stack is Hugo (so sitemap/robots are typically straightforward).

What should be verified in the StackStats marketing repo / deployment
P0 verification checklist
- robots.txt exists and points to sitemap.xml
- sitemap.xml exists and includes only indexable pages (avoid tag/category bloat)
- canonical tags present and consistent with trailing slash policy
- title/meta descriptions present on: /, /license, /changelog, /privacy, /terms, planned SEO pages
- OpenGraph/Twitter cards configured (for Reddit/X sharing)
- Schema: Organization + SoftwareApplication; add FAQ schema on /faq or on SEO pages with FAQs

Observed hygiene issue from GSC export
- Trailing slash duplicates appear (/changelog vs /changelog/, /license vs /license/). Ensure redirects/canonicalization.


5) Recommended actions (prioritized)

P0 (this week)
1) Ship SEO Pages 1–3 from page-outlines.md (they’re the highest-intent, lowest-competition cluster).
2) Fix trailing slash duplication with redirects/canonicals.
3) Add CTA click tracking + UTMs as per tracking-implementation-notes.md (not strictly SEO, but required to measure content ROI).

P1 (next)
4) Add /download and /how-it-works/ pages; keep them extremely simple and link them from onboarding.
5) Add /examples/teardown page and use it as a “linkable asset” from social + SEO pages.
6) Add /faq with FAQ schema.


6) Content backlog (10 posts) — StackStats
Goal: build a topic cluster around “Substack analytics beyond basics” and “local/offline analytics”, aligned to the 6 planned SEO pages.

1) “Substack Analytics Explained: What Substack shows vs what it hides”
2) “Cohort retention for newsletters: how to measure (and what to do with it)”
3) “Why your Substack open rate dropped: 12 causes + diagnostics checklist”
4) “Inactive subscribers: how to find ‘at-risk’ readers before they churn”
5) “Best time to post on Substack: how to compute it (and why it changes)”
6) “Newsletter growth sources: how to track which referrals convert best”
7) “Substack vs beehiiv analytics: what each platform gets right (and what’s missing)”
8) “Local-first analytics: what ‘runs fully offline’ means for privacy + reliability”
9) “BYOK vs local Ollama for newsletter insights: when to use each”
10) “Weekly analytics routine for Substack writers (5 minutes/week)”


========================
Cross-product notes (shared wins)
========================

P0
- Canonicalization: both products show trailing-slash duplicate URLs in GSC exports. Resolve with consistent redirects + canonical tags.
- Build “indexable” pages instead of relying on homepage anchors for key sections.

P1
- Internal linking: ensure new SEO pages link to (a) demo/pricing, (b) 1–2 adjacent articles, (c) the most relevant integration/setup doc.
- Add/standardize OG images per page for better social distribution performance.
