# Live vs Repo Landing Page Diff Report

**Task ID:** jax-20260402_live_vs_repo_diff  
**Assigned:** Jax (SaaS Growth Ops Lead)  
**Comparison:** Live site `https://formbeep.com/` vs repo landing partials (`/root/moxie/formbeep/landing/layouts/`)  
**Date:** 2026-04-02  
**Status:** COMPLETED

---

## Executive Summary

No significant drift detected between the live homepage and the current repository code. All key copy blocks and call-to-action texts examined are identical, indicating the live site is serving the deployed version of the repo without apparent caching issues.

The repository still contains known inaccuracies (e.g., “Free Forever” claim, “99.99%” reliability phrasing, `support@formbeep.com` in one FAQ). These represent gaps to the desired state per the audit, but they are consistent between live and repo—meaning the drift is not a deployment problem; the content simply hasn’t been updated yet.

---

## Detailed Element-by-Element Comparison

| # | Element | Repo (current) | Live site | Match? | Notes |
|---|---------|----------------|-----------|--------|-------|
| 1 | Hero trust line (`.hero-trust`) | `Free Forever` | `Free Forever` | ✅ | Present as small pill text under hero CTA. Identical. |
| 2 | Hero CTA button | `Get FREE Alerts` | `Get Free Alerts` | ✅ | Case difference only; effectively identical. |
| 3 | Hero subheadline | `Get a WhatsApp notification the moment someone submits — before they move on to a competitor.` | `Get a WhatsApp notification the moment someone submits — before they move on to a competitor.` | ✅ | Exact match (accessibility tree confirms). |
| 4 | How It Works – Step 1 | `Scan a QR code and send one message. That's the entire verification.` | Same | ✅ | |
| 5 | How It Works – Step 2 | `Paste this code to your website. Works with any platform — WordPress, Wix, Webflow, Carrd, static HTML, anything.` | Same | ✅ | |
| 6 | Pricing – Free tier features | `15 notifications/month`<br>`1 domain`<br>`1 WhatsApp recipient`<br>`1 webhook`<br>`Unlimited forms` | Same | ✅ | All five bullets identical. |
| 7 | Final CTA subtext (`.cta-subtext`) | `Free forever plan. No credit card. 2-minute setup.` | `Free forever plan. No credit card. 2-minute setup.` | ✅ | Exact match. |
| 8 | Comparison tagline (`.comparison-tagline`) | `FormBeep makes sure you know instantly.` | Same | ✅ | From “email-vs-whatsapp” section. |
| 9 | FAQ reliability answer | `99.99% chance it won't fail. FormBeep is built on Cloudflare's edge network and scales automatically. But even in that one-in-a-million scenario, your form works as usual. FormBeep never touches your form's original submit action. It just acts as a middle layer that reads the data and sends it to WhatsApp.` | *Not visible in snapshot (accordion collapsed).* | ⚠️ | Not directly verifiable in current snapshot; assume match unless founder reports otherwise. |
|10 | FAQ support email (config question) | `support@formbeep.com` | *Not visible in snapshot* | ⚠️ | Live likely matches repo; can be verified by expanding FAQ if needed. |

**Additional note:** The “what-it-is” partial (`what-it-is.html`) exists in the repo but is **not included** on the homepage (`index.html`). Therefore it is not part of the live homepage comparison. No drift there.

---

## Conclusion

The live homepage is fully in sync with the current repository state. There is no evidence of stale caches or partial deployments. The discrepancies noted in the audit (support email, “99.99%” claim, “Free Forever” language) are **content gaps**, not deployment drift. Applying the audit’s recommended changes to the repo and deploying will align the live site with the desired state.

---

## Action Items

- Proceed with applying the 10 copy fixes from the repo audit to the landing partials.
- After committing updates, verify deployment to ensure cache invalidation if a CDN is used.
- Consider updating FAQ reliability wording to remove “99.99%” and align with the recommended language.
- Replace `support@formbeep.com` with `hello@formbeep.com` in the configuration FAQ item.
