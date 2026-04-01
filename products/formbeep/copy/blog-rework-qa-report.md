# Kiro Blog Post Rework — QA Gap Audit (Rumi)
# Date: 2026-04-02T01:00Z
# Auditor: Rumi
# Against: Dispatch queue line 9 + orchestration.md Kiro section

## Purpose
Audit the two rejected Kiro blog drafts against founder's rework checklist so Kiro can rework without guesswork.

---

## Post 1: blog-post-whatsapp-without-zapier.md
**Current length:** ~410 words (target: 1,200–1,800)
**Status:** Needs significant expansion (3×)

### Rework checklist

| # | Requirement | Status | Detail |
|---|------------|--------|--------|
| 1 | Length 1,200–1,800 words | ❌ FAIL | ~410 words — short by ~800 words. Needs 3–5 new subheads with examples. |
| 2 | Support email = hello@formbeep.com | ❌ FAIL | Line 99 says `support@formbeep.com` — must be `hello@formbeep.com` |
| 3 | Free tier = 15/month | ❌ FAIL | Line 93 says "Free for 50 submissions per month" — must be 15 |
| 4 | Frontmatter: slug | ❌ FAIL | No `slug:` key in frontmatter. Must add `slug: whatsapp-without-zapier` |
| 5 | Zapier→WhatsApp research | ❌ FAIL | Post says "Zapier to WhatsApp Business API" on line 34 with no depth. Must explain: Zapier does NOT offer out-of-the-box WhatsApp. Requires either (a) Twilio WhatsApp Templates (~$0.005/msg), (b) 360dialog (~€15/mo), or (c) Meta Cloud API direct. This is the core hook — currently too thin. |
| 6 | Comparison table in vs post | N/A | This is the "without Zapier" post, not the "vs" post. But could add a small decision table here too. |
| 7 | Frontmatter: thumb_prompt | ❌ FAIL | Missing entirely. Needs a text prompt for generating a thumbnail image. |

### Additional issues (not in spec, but should fix)
- Line 2: title mentions "Without Zapier" — good for SEO. But the body barely explains WHY Zapier is hard. The "Zapier to WhatsApp Business API" explanation (line 34) is one sentence. This is the money paragraph — needs 200–300 words explaining the Zapier↔WhatsApp gap.
- Lines 60–69: Setup steps are generic. Add a concrete example: "For a Webflow contact form, paste the script tag in Project Settings > Custom Code > Before </body>."
- Line 97: CTA link — verify `app.formbeep.com/sign-up` is live.
- Structure gap: Missing sections that would hit word-count: (a) "How Zapier + WhatsApp actually works under the hood" (b) "Step-by-step comparison side-by-side" (c) "Common failure modes: token expiry, template rejections" (d) "Real-world scenario / case study".

---

## Post 2: blog-post-formbeep-vs-zapier.md
**Current length:** ~505 words (target: 1,200–1,800)
**Status:** Needs significant expansion (2.5×)

### Rework checklist

| # | Requirement | Status | Detail |
|---|------------|--------|--------|
| 1 | Length 1,200–1,800 words | ❌ FAIL | ~505 words — short by ~700–1300 words. Needs 3–5 new subheads with examples. |
| 2 | Support email = hello@formbeep.com | ❌ FAIL | Line 84 says `support@formbeep.com` — must be `hello@formbeep.com` |
| 3 | Free tier = 15/month | ❌ FAIL | Line 78 says "Free for your first 50 submissions per month" — must be 15 |
| 4 | Frontmatter: slug | ❌ FAIL | No `slug:` key in frontmatter. Must add `slug: formbeep-vs-zapier` |
| 5 | Zapier→WhatsApp research | ❌ PASS (partial) | Line 12 mentions "Zapier hits the WhatsApp API" — but does not explain the WhatsApp Business API requirement. Needs the same depth as Post 1. |
| 6 | Comparison table | ❌ FAIL | Lines 59–62 have bullet-point recommendation. This is NOT a table. Needs a proper markdown comparison table with rows: Pricing, Setup Time, WhatsApp Support, Multi-step, Best For, Integration Count, Monitoring/Debugging, etc. |
| 7 | Frontmatter: thumb_prompt | ❌ FAIL | Missing entirely. Needs a text prompt for generating a thumbnail image. |

### Additional issues (not in spec, but should fix)
- Lines 52–56: Pricing section says "FormBeep is a flat $6/month" — this may conflict with pricing strategy. Confirm with Rishi before publishing. Do NOT repeat the free-tier number here incorrectly (see requirement #3).
- Line 2–3: Title is good for SEO. Description is thin.
- FAQ section is short. Could expand to 6–8 questions with more detailed answers.
- Missing: Real-world cost comparison (Zapier $20 vs FormBeep $6 × 12 months = $72 savings). Missing: Setup time comparison (Zapier: 30 min; FormBeep: 5 min).
- Structure gaps for word count: (a) Detailed feature comparison table (b) "When to graduate from FormBeep to Zapier" (c) "How agencies should structure their form notification stack" (d) Customer/reader scenario.

---

## Summary for Kiro (copy/paste into your rework ticket)

**Both posts have these common issues:**
1. Frontmatter: add `slug:` and `thumb_prompt:` to YAML frontmatter
2. Change ALL instances of `support@formbeep.com` → `hello@formbeep.com`
3. Change ALL instances of "50 submissions" → "15 submissions per month"
4. Expand both to 1,200–1,800 words each.

**Required additions for Post 1 (WhatsApp without Zapier):**
- 200–300 word section: explain that Zapier does NOT offer native WhatsApp; it requires a third-party WhatsApp Business API provider (Twilio, 360dialog, or Meta Cloud API), template approval from Meta, per-message pricing
- Real-world setup steps with platform-specific examples
- Common failure modes (token expiry, template rejections)

**Required additions for Post 2 (FormBeep vs Zapier):**
- Full markdown comparison table (minimum 6–8 rows, 4–5 columns)
- Cost comparison over 12 months (Zapier $20/mo × 12 vs FormBeep $6/mo × 12)
- Setup time comparison
- "When to use each" decision tree or scenario section
- Zapier→WhatsApp reality check (same as Post 1)

---

## Deliverable written to:
/root/moxie/products/formbeep/copy/blog-rework-qa-report.md
