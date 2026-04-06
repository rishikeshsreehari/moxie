# Landing Page Truth Snapshots — FormBeep + StackStats

Generated: 2026-04-06

Rules: Do not invent numbers. Live site content is authoritative for copy/pricing/claims. Repo docs are used only for comparison and internal truth-layer constraints.

---

## FormBeep — https://formbeep.com/ (LIVE scrape)

### Current headline + CTA (above the fold)
- H1: “Contact Form to WhatsApp™ Notifications”
- Tagline line (hero): “Never Miss a Lead Again Instant Alerts from your Forms”
- Subhead: “Get a WhatsApp notification the moment someone submits — before they move on to a competitor.”
- Primary CTA button: “Get FREE Alerts” (links to https://accounts.formbeep.com/sign-up)
- Header CTA: “Get Started Free” (same destination)
- Trust microcopy near hero: “Free Forever”, “No Credit Card”, “2min Setup”

### Pricing (as displayed on live landing)
“Simple Pricing” section includes these tiers:
- Free — $0 /month
  - 15 notifications/month
  - 1 domain
  - 1 WhatsApp recipient
  - 1 webhook
  - Unlimited forms
- Starter — $4.99 /month
  - 200 notifications/month
  - 2 domains
  - 2 WhatsApp recipients
  - 2 webhooks
  - Unlimited forms
- Pro (Most Popular) — $24.99 /month
  - 1,500 notifications/month
  - 5 domains
  - 3 WhatsApp recipients
  - 5 webhooks
  - Unlimited forms
- Business — $49.99 /month
  - 3,000 notifications/month
  - 10 domains
  - 10 WhatsApp recipients
  - 10 webhooks
  - Unlimited forms
- Agency — $99 /month
  - 7,000 notifications/month
  - Unlimited domains
  - Unlimited recipients
  - Unlimited webhooks
  - Unlimited forms

### Claims list (explicit, live-page visible)
Primary product claims:
- “Get a WhatsApp notification the moment someone submits”
- “Works with any existing form”
- “Go live in 2 minutes”
- “Add one line of code” (script embed)
- “Works with any platform — WordPress, Wix, Webflow, Carrd, static HTML, anything.”
- “99.9% uptime powered by Cloudflare”
- “Works With Every Website”
- “Your form notifications should be seen, not buried.” (positioning)

Other notable on-page assertions:
- “78% of customers buy from the first business to respond.*” with citation label “* Lead Connect Survey”

### Trust / credibility elements (live)
- Uptime claim: “99.9% uptime powered by Cloudflare”
- Testimonial-style line: “Tiny tool, real impact. Exactly what small teams need to stay on top of every lead.”
  - Attribution shown: “dadomo UG — developer of Software Licensing System” (with link to tebani.com)
- Founder story block (“Why” section): founder quote and “Rishi Founder, FormBeep” + link “Read the full story →” (blog post)
- “Featured on” with a visible Frazier badge linking to fazier.com launch page
- Docs link in nav and in “Installation guide” link: https://docs.formbeep.com
- Contact in pricing section: hello@formbeep.com

### Repo docs comparison (truth-layer constraints)
Repo sources checked:
- /root/moxie_hq/products/formbeep/status.md
- /root/moxie_hq/products/formbeep/copy/landing-page-v1.md
- /root/moxie_hq/products/formbeep/dev-notes/live-site-snapshot.md

Key diffs / alignment:
- Repo status warns: “Do NOT claim ‘free forever’ unless pricing page explicitly says so.” Live landing DOES say “Free Forever” and shows a Free plan. So the claim is currently safe (as long as it stays on the landing/pricing section).
- Repo positioning draft (landing-page-v1.md) includes “email or SMS” options. Live landing is WhatsApp-only in its visible value prop and claims (no SMS/email claims above).
- Repo traction truth: Paying customers = 1 (founder-confirmed). Live landing does not state customer counts.

### Founder Questions (unknowns to confirm)
(Do not infer; answer explicitly.)
1) Revenue: What is current MRR and total revenue to date for FormBeep (including any annual prepay)?
2) Traffic: What are sessions/pageviews to https://formbeep.com over last 7/30 days (source: Umami/GA)?
3) Conversion: Landing → signup conversion rate last 7/30 days; and signup → activated (first successful notification) conversion.
4) ICP: Which segment is converting best today (agencies vs SMBs vs freelancers), and what geos are actually showing demand vs the “founder-noted” geo list in status.md?
5) Channel mix: Top 3 acquisition channels currently driving signups (SEO, directories, PH, paid, referrals, etc.).

---

## StackStats — https://stackstats.app/ (LIVE scrape)

### Current headline + CTA (above the fold)
- Above-hero labels: “100% local”, “No cloud”, “No subscription”
- H1: “Better analytics for your Substack™”
- Subhead line: “Connect once. See everything.”
- Supporting copy: “Who’s actually reading. Who stopped. Which posts drive real subscribers.”
- Primary CTA: “Download StackStats →” (scrolls to pricing)
- Secondary CTA: “Live demo →” (https://demo.stackstats.app)
- Microcopy under CTAs: “No account · No internet · Works on Mac & Windows”

### Pricing (as displayed on live landing)
“One payment. Yours forever.”
- 1-Year — $39
  - Full analytics
  - Works fully offline
  - Optional AI via Ollama or BYOK
  - Mac & Windows Apps
  - 1 device
  - 1 year of updates & support
  - App yours forever
  - Note: “Perpetual license — app keeps working after year 1. Renew for $29/yr or don’t. Your call.”
  - CTA: “Get 1-year license →” (Gumroad link)
- Lifetime — shows “$129 $79” (discounted display)
  - Everything in 1-Year
  - Up to 3 devices
  - Every future update, forever
  - Lifetime priority support
  - Never pay again
  - CTA: “Get lifetime license →” (Gumroad link)
- Guarantee/trust near pricing: “14-day refund · Secure checkout via Gumroad”
- Additional CTA near pricing: “Not sure yet? Try the live demo — no sign-up needed →”

### Claims list (explicit, live-page visible)
Core positioning claims:
- “100% local / No cloud / No subscription”
- “No account · No internet · Works on Mac & Windows”
- “Everything Substack™ doesn’t show you.”
- “Install StackStats. Connect your Substack. Done.”
- “Auto-Sync pulls all your data in one click. No CSVs, no manual exports.”
- “All computed locally. All actionable.”

Specific insight claims shown in “What writers find in their first 5 minutes” section:
- “~30% of your list may have stopped reading.”
- “Your biggest fans.” (scoring readers by opens, clicks, comments, shares)
- “Your best day and hour to post.” (computed from your post history + sample-size warnings)

AI-related claims (optional add-on):
- “All analytics work without AI.”
- Local AI option: “Run Ollama locally” (no API key, no internet, no cost)
- BYOK: “Claude, GPT-4, Gemini, Groq, OpenRouter, or any OpenAI-compatible endpoint. Prompts go straight from your device to the provider.”

### Trust / credibility elements (live)
- Product Hunt badge link: “StackStats on Product Hunt”
- Founder credibility blockquote: “Built by a Substack writer, for himself.”
  - Includes link to founder newsletter (“10+1 Things” on Substack) and statement: “around 3,000 subscribers” (founder-claimed on page)
  - Links to founder X/Twitter handle
- Changelog section with recent versions/dates (e.g., v1.5.x entries shown)
- Footer “Featured on …” links:
  - Twelve Tools
  - Wired Business
  - SaasDB
- Refund + payment trust: “14-day refund · Secure checkout via Gumroad”
- Legal/trademark: “Not affiliated with Substack™ Inc.”

### Repo docs comparison (truth-layer constraints)
Repo sources checked:
- /root/moxie_hq/products/stackstats/status.md
- /root/moxie_hq/cmo/deliverables/2026-04-06_stackstats_landing_copy_patch.txt
- /root/moxie_hq/cmo/deliverables/stackstats_reddit_packet_next.md

Alignment:
- Pricing matches repo status.md exactly: 1-year $39; lifetime $79; renew updates $29/yr.
- Repo traction truth matches internal docs: 5 sales, $237.17 revenue (not stated on landing page).

Notable differences:
- Repo “landing copy patch” proposes a different headline/angle (“See what’s happening in your Substack in 5 minutes a week”) and mentions “paid conversion” explicitly; live landing currently leads with offline/local/no-subscription and “first 5 minutes” insights.

### Founder Questions (unknowns to confirm)
(Do not infer; answer explicitly.)
1) Traffic: Sessions and unique visitors for stackstats.app and demo.stackstats.app (last 7/30 days).
2) Conversion: Landing → Gumroad checkout start → purchase conversion rates; and demo → purchase conversion.
3) ICP: Which Substack cohort is buying (free-only writers vs paid newsletters; subscriber-range bands)?
4) Primary acquisition channels: what’s driving the 5 sales so far (Product Hunt, X, Reddit, SEO, word-of-mouth)?
5) Retention/renewal expectation: Any early signals on renew intent or support load (since updates renew at $29/yr)?

---

## Quick cross-product notes (truth-layer safe)
- FormBeep is subscription (monthly tiers) + free plan; StackStats explicitly positions as no subscription and fully local.
- Both lean on speed/time-to-value (“2 minutes” vs “first 5 minutes”).
- Both include founder-story credibility blocks.

