# Social / Distribution Audit (X, IndieHackers, Reddit)
Generated: 2026-04-06
Scope: audit existing in-repo artifacts for X/Twitter, IndieHackers, and Reddit distribution; identify what exists vs missing; propose a founder-executable Reddit plan for Tue–Fri.

Constraints / notes
- Reddit browsing from this server is blocked (no interactive session/token assumed). This audit does NOT claim current subreddit-specific rules/viral patterns.
- Where “intel refresh” is needed, this report provides a founder-executable laptop command using the existing Playwright-based scripts in-repo.


## 1) X (Twitter) — what exists

A) Strategy + tone
- /root/moxie_hq/cmo/strategy/founder-voice-x-indiehackers.md
  - Founder-voice pillars, Golden Rule (WHERE/WHY/HOW/WHEN/WHY-NOW), and an IndieHackers adaptation section.
- /root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md
  - “Founder tone fingerprint” + reply-guy workflow + large template library.
  - Notes that engagement metrics weren’t present in corpus; recommends rerun with X export.

B) Calendar + paste-ready copy
- /root/moxie_hq/cmo/content/calendar/x-7day-plan.md
  - 7-day schedule (2026-04-03 → 2026-04-09) with posting times + reply blocks.
- /root/moxie_hq/cmo/content/packs/x-day1-7.md
  - Paste-ready daily posts (Day 1–7) aligned to the calendar.
- /root/moxie_hq/cmo/content/packs/reply-guy-7day.md
  - 7-day “10 replies/day” packet with lane rotation.
- /root/moxie_hq/cmo/strategy/x-thread-moxie-ai-cmo-origin.md
  - Paste-ready thread draft: “I built an AI CMO” story.

C) Analytics / reporting
- /root/moxie_hq/cmo/reports/x-last30-analytics-summary-2026-04-02.md
  - Foundational metrics snapshot + interpretation + requested input (X export).

D) Tooling
- /root/moxie_hq/cmo/scripts/x_founder_tone_audit.py
  - Intended to ingest tweets.js/tweets.csv and generate tone + reply packet.
  - ISSUE FOUND: file currently appears syntactically broken at line ~209: `tokens_all=***` (invalid Python). This script will not run until fixed (should be `tokens_all=[]`).


## 2) X (Twitter) — what’s missing / gaps

Missing or weak links in the execution chain
1) “Source of truth” logging file for actual X posts
- x-7day-plan.md references: /root/moxie_hq/cmo/content/logs/x-post-outcomes.md
- That file was not found during this audit.
  - Impact: no consistent loop for “post URL → impressions/profile visits/replies → what to do next”.

2) A longer-horizon calendar
- There is a strong 7-day pack/calendar, but not a rolling 30-day calendar tied to product priorities.

3) X export ingestion is blocked by broken script
- x_founder_tone_audit.py needs a quick fix, otherwise any “what worked” scoring remains manual.

4) Product-specific X plan is explicitly marked “do not execute”
- /root/moxie_hq/products/formbeep/outreach/x-content-plan-14d.md is a draft framework only.


## 3) IndieHackers — what exists

1) Strategy guidance (but not a paste-ready post)
- /root/moxie_hq/cmo/strategy/founder-voice-x-indiehackers.md
  - Contains an IndieHackers post shape (title + body outline) but not the full paste-ready draft.

2) Evidence of at least one prior IndieHackers post/mention
- /root/moxie_hq/products/formbeep/distribution/existing-listings.md
  - Lists an Indie Hackers URL:
    https://www.indiehackers.com/post/from-building-client-websites-to-getting-my-first-micro-saas-live-in-a-weekend-ee1bcef569
  - Note: not verified in this environment (server browsing constraints), but it’s a concrete artifact reference.


## 4) IndieHackers — what’s missing / gaps

1) Paste-ready IndieHackers long post + follow-ups
- Needed: 1 long post (story + receipts + 2 specific questions) + 2 follow-up comments/posts.
- Needed: a “comment plan” (where to comment 2–4x/month) to build reputation before/after posting.

2) Asset bundle / receipts
- The IH format rewards screenshots/snippets (artifacts shipped, dashboards, failures + fix).
- We have the underlying material, but no assembled “IH proof pack” (2–4 screenshots + 1 excerpt block) with a checklist.


## 5) Reddit — what exists

A) Strategy + SOPs
- /root/moxie_hq/products/formbeep/outreach/reddit-campaign-plan.md
  - 4-week sprint plan, KPIs, posting calendar, posting SOP, anti-spam guardrails.
- /root/moxie_hq/products/formbeep/outreach/reddit-manual-posting-plan-gst-nonus-v1.md
  - GST timezone guidance + per-subreddit checklist approach.
- /root/moxie_hq/cmo/resources/distribution/reddit-submarket-map.md
  - Submarket selection rules + “viral pattern capture” template.

B) Execution packs (paste-ready)
- /root/moxie_hq/products/formbeep/outreach/reddit-week1-execution-pack.md
  - Full Week 1 posts + comment seeding schedule.
- /root/moxie_hq/products/formbeep/outreach/reddit_execution_packet_2026-04-03.md
  - A specific execution packet with “truth layer” notes and a post+comment plan.
- /root/moxie_hq/products/formbeep/outreach/reddit-post-comment-scripts.md
  - Multiple paste-ready post scripts for different subreddits + contextual comment blocks.

C) Tracking / history
- /root/moxie_hq/products/formbeep/outreach/reddit-posting-tracker.md
  - Subreddit rules/history table + activity log + guardrails.

D) Intel tooling (in-repo)
- /root/moxie_hq/scripts/reddit-intel/reddit_intel_scanner_browser.py
  - Playwright browser automation to collect founder + keyword intel.
- /root/moxie_hq/scripts/reddit-intel/reddit_campaign_preflight.py
  - Preflight for chosen subreddits: your history, competitor history, rules snippets, top posts.
- /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md
  - Example output brief (generated 2026-04-01).

E) Weekly cadence plan
- /root/moxie_hq/products/formbeep/outreach/reddit-weekly-plan-tuewedthu.md
- /root/moxie_hq/products/formbeep/outreach/reddit-weekly-plan-2026-04-07.md
  - Already proposes Tue–Thu actions; does not include Fri.


## 6) Reddit — what’s missing / gaps

1) Single “next 4 days” packet that a founder can execute without cross-referencing 6 docs
- Assets exist, but they’re fragmented (plan vs scripts vs trackers vs weekly plan).

2) Live rule verification + “viral pattern capture” isn’t consistently enforced
- There is a template for it, but execution depends on running the preflight script and then manually checking rules.

3) One authoritative “truth layer” per product for Reddit claims
- Some packets include truth-layer notes (e.g., “1 paying customer”), but it’s not centralized.


## 7) Recommended immediate fixes (highest leverage)

1) Fix x_founder_tone_audit.py so tone analysis can be rerun with X exports.
- 2-minute patch: replace `tokens_all=***` with `tokens_all=[]`.

2) Add a simple X post outcome log file (if missing)
- Create: /root/moxie_hq/cmo/content/logs/x-post-outcomes.md
- Format: date | post_url | impressions | profile_visits | replies | notes | next tweak.

3) Produce paste-ready IndieHackers post + receipts pack
- Deliverable: one long post draft + 2 follow-up comments, plus 3–5 “proof snippets” ready to paste.

4) Execute a focused Tue–Fri Reddit plan (1 post/day) with strict guardrails
- See deliverable created: /root/moxie_hq/cmo/deliverables/reddit_plan_next4days.md


## 8) Founder-executable Reddit intel refresh (laptop)

Why: subreddit rules change; also we should avoid repeating competitor angles and avoid posting where you recently posted.

Run on laptop (requires GUI + Reddit login once; saves session state):

  cd /root/moxie_hq/scripts/reddit-intel
  python3 -m pip install -r requirements.txt
  playwright install chromium

  # Preflight for the exact subs you plan to post in Tue–Fri
  python3 reddit_campaign_preflight.py \
    --subreddits buildinpublic WordPress SaaS SideProject \
    --me rishikeshshari \
    --competitors adambengur ConferenceOnly1415 \
    --out reddit_campaign_preflight.md \
    --headed

  # Optional broader intel (founder history + keyword threads)
  python3 reddit_intel_scanner_browser.py

Output files:
- /root/moxie_hq/scripts/reddit-intel/reddit_campaign_preflight.md
- /root/moxie_hq/scripts/reddit-intel/reddit_intel_brief_browser.md
