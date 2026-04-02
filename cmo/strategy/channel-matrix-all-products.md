# Platform × Product Posting Matrix

**Owner:** Rumi · **Last updated:** 2026-04-02T03:00Z · **Used by:** All employees executing posts

One operational reference for every channel we post on, per product. Every cell answers: frequency, best time (UTC + geo), days to avoid, blockers, scheduling allowed?, and the minimum execution packet.

---

## 0) ICP Geo Reference

| Geo | Offset | Peak Local | Peak UTC |
|-----|--------|-----------|----------|
| UAE/GST | +4 | 10–12 & 18–21 | 06–08 & 14–17 |
| Saudi (AST) | +3 | 09–11 & 19–22 | 06–08 & 16–19 |
| WEU (CET) | +1 | 09–11 & 13–15 | 08–10 & 12–14 |
| UK (GMT/BST) | +0/+1 | 09–11 & 13–15 | 09–11 & 13–15 |
| MY/SG | +8 | 09–11 & 17–20 | 01–03 & 09–12 |
| Australia (AEST) | +10 | 08–10 & 17–20 | 22–00 & 07–10 |
| NZ (NZST) | +12 | 09–11 & 17–20 | 21–23 & 05–08 |
| US (ET) | -5 | 09–11 & 14–16 | 14–16 & 19–21 |
| EU (CET) | +1 | 09–11 & 14–16 | 08–10 & 13–15 |

**Composite posting windows:**
- **Primary (WEU + UAE + SG overlap):** 07:00–09:00 UTC
- **Secondary (WEU + US overlap):** 14:00–16:00 UTC
- **AU/NZ only:** 22:00–00:00 UTC (when AU/NZ push is active)

---

## 1) X / Twitter

| Dimension | FormBeep | StackStats | HQ (BiP / Brand) |
|-----------|----------|------------|------------------|
| Frequency | 1–2 posts/day | 3–4 posts/week | 3–5 posts/week |
| Best windows (UTC) | 07–09 (WEU/UAE); 14–16 (US/WEU) | 14–16 (US/EU Substack writers); 08–10 (EU morning) | 12–14 & 14–16 (max geo overlap) |
| Best days | Mon–Thu; Fri OK for light content | Tue–Thu; avoid Mon | Tue–Thu for signal; BiP any day |
| Days to avoid | Sun; Sat (mixed) | Sat–Sun | Sun |
| Scheduling | YES (native or free tools) | YES | YES |
| Blockers | None — account active | X handle needed | Founder account @rishikeshshari |
| Min execution packet | Copy (≤260) + UTM'd link + 2–3 hashtags + geo note | Copy + demo link + UTM'd CTA + audience note | Hook (1 line) + body (1–2 lines) + proof element + CTA/question + product tags |

**Content pillars:** WhatsApp form alerts; "no Zapier" angle; lead-response-time tips / Substack analytics; cohort analysis; Build-in-public metrics; revenue transparency.

---

## 2) Reddit

| Dimension | FormBeep | StackStats |
|-----------|----------|------------|
| Frequency | 1 post/week/sub max; 3–5 comments/week | 1 post/month; 2–3 comments/month |
| Best windows (UTC) | 14–17 (US morning); 08–10 (WEU morning); 01–03 (MY/SG morning) | 14–16 (US); 08–10 (EU) |
| Best days | Mon–Thu; weekends OK for r/SideProject r/vibecoding r/buildinpublic | Tue–Thu only |
| Days to avoid | Fri after 18:00 UTC; sub-specific promo-ban days; Sun | Sat–Sun; Mon |
| Scheduling | **NO** — manual only for personal accounts | **NO** — same constraint |
| Blockers | **CREDENTIALS BLOCKED** — u/rishikeshshari login needed; see issues_rishi.md. No API access (network blocked). | Same; also needs validated subreddit list for analytics niche |
| Min execution packet | 1) Target subreddit 2) Rule check 3) 14d history check 4) Title 5) Body (value-first) 6) Link (if allowed) 7) Flair 8) Log to tracker | 1) Target subreddit 2) Rule check 3) Thread URL + context 4) Value-first response 5) No product push unless asked |

**Target subreddits (FormBeep):** r/SaaS · r/webdev · r/smallbusiness · r/microsaas · r/SideProject · r/buildinpublic · r/vibecoding · r/indiehackers · r/GrowthHacking · r/WhatsappBusinessAPI · r/EntrepreneurRideAlong · r/roastmystartup (feedback only)

**Target subreddits (StackStats):** r/analytics · r/Substack · r/newsletters · r/SaaS · r/Blogging (comments)

**Full subreddit rules table + activity log:** `products/formbeep/outreach/reddit-posting-tracker.md`

**Reddit guardrails:** 1-in-3 comment ratio; 7d cooldown same sub; no cross-post spam within 48h; title variance; log immediately.

---

## 3) IndieHackers (forum + subreddit)

| Dimension | FormBeep | StackStats |
|-----------|----------|------------|
| Frequency | 1 post/month + 2–3 comments/month | 1 post/quarter + 1–2 comments/month |
| Best windows (UTC) | 14–16 (IH US-heavy, peaks ET 9–11am) | 14–16 (same) |
| Best days | Tue–Thu | Tue–Wed |
| Days to avoid | Weekends; Mon | Mon; Fri–Sun |
| Scheduling | Forum: YES (schedule). Subreddit: NO (manual). | Same |
| Blockers | IH forum account (founder-owned) | Same |
| Min execution packet | Post: Title + narrative body + natural product link + tags + scheduled time. Comments: Thread URL + summary + genuine reply | Same structure, analytics angle |

---

## 4) SaaS Directories

| Dimension | FormBeep | StackStats |
|-----------|----------|------------|
| Frequency | 1–2 submissions/week (active); then 1/month | 2–4 total (one-time launch) |
| Best windows | 08–16 UTC Tue–Thu (US/WEU business hours) | Same |
| Days to avoid | Fri PM through Sun (approval queues stall) | None critical (async) |
| Scheduling | **NO** — requires form fill + account creation + email verify | Same |
| Blockers | **ACTIVE BLOCKER** — directory account credentials needed. Many directories have 7–30 day age gates. Email verify: hello@formbeep.com. See issues_rishi.md. | None expected; simpler submissions |
| Min execution packet | 1) Directory name + URL 2) Account status 3) Tagline + description + features 4) Category/tags 5) Submission URL 6) "Verified on" timestamp 7) Log to directory-submissions-log.md | Same (lighter copy) |

**Priority directories (FormBeep):** SaaSHub · ProductHunt (launch) · BetaList · AlternativeTo · ToolFinder · StartupStash · 1000Tools · Microwire. **Defer:** G2/Capterra (need reviews first).

**Priority directories (StackStats):** ProductHunt (launch) · AlternativeTo · SaaSHub · ToolFinder · G2.

---

## 5) Forums & Communities (Non-Reddit)

| Platform | FormBeep | StackStats | Frequency | Best UTC | Schedule? | Blockers |
|----------|----------|------------|-----------|----------|-----------|----------|
| Hacker News | ❌ | ⚠️ Show HN only | Show HN once per major release | 11–13 UTC Tue–Thu | NO | — |
| ProductHunt discussions | ✅ Comments on hunts | — | 5–10/week | 08:00 UTC (PH launch) | NO | PH account |
| Webflow/Framer forums | ✅ Integration showcases | ❌ | 1/month | 14–16 | NO | Forum account |
| Dev.to / Hashnode | ✅ Blog cross-posts | ✅ Blog cross-posts | 1 post/2 weeks | 08–10 | YES | Account needed |
| LinkedIn | ⚠️ Personal profile only | ⚠️ Personal only | 1 post/week (founder) | 07–09 or 12–13 | YES (LI native) | Founder account |
| WhatsApp/FB Groups | ✅ WA business groups | ❌ | 2–3 comments/week | Varies | NO | Group membership |
| StackOverflow | ⚠️ Answer WA/Form API Qs | ❌ | As questions arise | — | NO | SO account |

---

## 6) Channel Priority Matrix

| Channel | FormBeep | StackStats | Rationale |
|---------|----------|------------|-----------|
| X/Twitter | **P1** | **P1** | Fastest feedback loop; builds founder audience |
| Reddit | **P1** | P3 | ICP communities; 30–40% referral traffic potential |
| SaaS Directories | **P1** | P2 | Evergreen SEO + passive signups |
| IndieHackers | P2 | P2 | Social proof; lower volume |
| Dev.to/Hashnode | P2 | P2 | Free cross-post SEO |
| Hacker News | P3 | P2 (launch only) | High spike / high risk |
| ProductHunt | P1 (launch) | P1 (launch) | Plan carefully, one shot per product |
| Forums/Community | P2 | P3 | High-intent answers |
| LinkedIn | P3 | P3 | Requires founder time |

---

## 7) Universal Days/Times to Avoid

| What to avoid | Why | Channels |
|--------------|-----|----------|
| Sunday all day | Lowest B2B engagement everywhere | X, Reddit, IH, LI |
| Fri 18:00 UTC → Sat 12:00 UTC | Dead zone for WEU + UAE + US simultaneously | X, Reddit, IH |
| Mon 06:00–09:00 UTC | Email catch-up time; low engagement | Reddit, IH, X |
| 22:00–06:00 UTC | No major ICP geo active | All (unless AU/NZ push) |
| Regional holidays (US, UAE, Hari Raya MY/SG) | Regional audiences absent | All |

---

## 8) Execution Packet Templates

### X/Twitter:
```
Product: [FormBeep/StackStats/HQ] | Type: [promo/value/BiP/engagement]
Hook: [1 line] | Body: [1–2 lines]
CTA: [UTM'd URL] | Hashtags: [2–3] | Geo: [Primary/Secondary/US]
Schedule: [YYYY-MM-DD HH:MM UTC] | Status: [draft/scheduled/posted]
```

### Reddit:
```
Sub: [r/name] | Rules OK: [Y/N] | 14d Posted: [Y/N]
Type: [post/comment] | Title/Thread: [...]
Body: [value-first] | Link: [URL if allowed] | Log: [Y/N]
```

### Directory:
```
Directory: [name+URL] | Account: [created/age/verified]
Tagline: [≤100] | Description: [250–500] | Category: [...]
Submitted: [YYYY-MM-DD] | Follow-up: [X days]
```

---

## 9) Weekly Posting Cadence (Starter Template)

| Day | Channel | Product | Content Type |
|-----|---------|---------|-------------|
| Mon | X | FormBeep | WhatsApp vs email stat |
| Mon | X | HQ | Weekly metrics (BiP) |
| Tue | X | FormBeep | Integration spotlight |
| Tue | Reddit | FormBeep | Value post r/SaaS or r/microsaas |
| Wed | X | StackStats | Substack growth tip |
| Wed | IndieHackers | HQ | BiP lesson |
| Thu | X | FormBeep | "No Zapier" angle |
| Thu | Reddit | StackStats | Analytics comment (if relevant) |
| Fri | X | HQ | Weekly shipping recap |
| Sat | X | FormBeep | Light: build-in-public fun |
| Sun | — | — | **NO POSTING** |

Adjust after 2 weeks based on engagement data.

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-04-02 | v1 — full matrix: all channels, both products, geo windows, execution packets, priority, routing cadence, blockers, guardrails | Rumi |
