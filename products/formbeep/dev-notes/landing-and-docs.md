# FormBeep Dev Notes — Landing + Docs Suggestions

Owner: Moxie
Scope: Suggestions only. Do not push changes to the FormBeep product repo from Moxie.

## Why this note exists
Current FormBeep landing/docs are strong on utility, but the homepage and docs need more conversion-focused framing.

## What I observed
### Landing page
- Landing homepage is extremely thin: only title + one-line description.
- Current hero: "Get website form submissions on WhatsApp instantly."
- That message is clear, but it doesn’t yet answer:
  - who it’s for,
  - why WhatsApp beats email/Zapier,
  - why it’s trustworthy,
  - and why the user should act now.

### Docs homepage
- Docs are detailed and technically useful.
- Docs homepage currently says:
  - "Everything you need to set up FormBeep and get reliable form delivery to WhatsApp."
  - "FormBeep connects your website forms directly to your WhatsApp."
- The docs page is doing product education, but it should also funnel people to activation.

### Analytics signals (latest available)
- Top page: `/` (home)
- Second page: `/whatsapp-api-pricing/`
- Top referrers: Reddit, ChatGPT, vibecuterie.com, Google
- CTA / event clicks are present but light:
  - Login Click: 3
  - Docs Click: 3
  - Signup-Hero: 2
  - Signup-Pricing: 1
  - Signup-Header: 1
- Traffic is down week-over-week, so stronger conversion above the fold matters.

## Priority landing changes
1) Stronger hero copy
- Replace generic hero with a specific pain/outcome statement.
- Example:
  - Headline: "Never miss a form submission again — get WhatsApp alerts in seconds."
  - Subhead: "For Webflow, WordPress, Framer, and custom sites. No Zapier. No missed leads."

2) Add immediate proof + trust
- Add one line with credibility under hero:
  - "Built for founders, agencies, and SMBs that need fast lead response."
- Add a privacy note or reliability note near the CTA.

3) Put pricing intent higher
- The `/whatsapp-api-pricing/` page is getting traffic.
- Add a compact pricing teaser in the homepage hero area or just below it:
  - free tier
  - what counts as a message
  - what happens on the paid plan

4) Show use cases, not just features
- Add 3 use-case cards:
  - Lead gen agencies
  - SMB contact forms
  - Freelancers / portfolio sites
- Each card should map to a concrete pain and the WhatsApp advantage.

5) Add CTA redundancy
- Primary CTA: Start free / Get WhatsApp alerts
- Secondary CTA: See docs / View integrations
- Put CTA both in hero and mid-page.

6) Add FAQ blocks for objections
- Works with my platform?
- Does it need Zapier?
- Is it only for WhatsApp?
- Is there a free tier?
- Will it slow down my site?

## Priority docs changes
1) Docs homepage should push to activation faster
- Add a first screen quickstart box:
  - Install
  - Connect WhatsApp
  - Test a form
  - Verify the alert

2) Add a "fastest path to success" section
- One simple recommended path for the most common platforms.
- Reduce choice paralysis.

3) Add product positioning line in docs
- Example:
  - "FormBeep is the fastest way to turn form submissions into WhatsApp alerts."

4) Add troubleshooting links near the top
- Allowed domains
- Embed issues
- WhatsApp setup
- API key / number pairing

## Copy suggestions for the landing page
### Hero options
- "Get every form submission on WhatsApp — instantly."
- "Turn your website forms into WhatsApp leads in minutes."
- "Never lose a lead again. WhatsApp alerts for your forms."

### CTA options
- "Start free"
- "Connect WhatsApp"
- "View docs"
- "See integrations"

### Benefit bullets
- No Zapier
- Works with common site builders
- Instant notifications
- Built for lead response speed

## Suggested next tasks for the product dev
- Draft a conversion-first homepage section order
- Add one pricing teaser block above the fold
- Add trust/proof copy
- Add FAQ section
- Add a platform chooser / integration chooser
- Add clearer CTAs to docs

## Suggested design order
1. Hero
2. Trust / proof row
3. How it works
4. Platform integrations
5. Use cases
6. Pricing teaser
7. FAQ
8. Final CTA

## Notes for the dev
- Keep language simple and specific.
- Prefer outcome language over feature language.
- Keep the page fast and minimal.
- Don’t overbuild — just make the decision obvious.
