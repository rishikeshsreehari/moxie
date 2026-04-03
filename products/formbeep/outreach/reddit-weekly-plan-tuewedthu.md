# FormBeep — Reddit Weekly Plan (Tue/Wed/Thu cadence)

Last updated (UTC): 2026-04-03
Owner: Rishi (posting) / Moxie (ops)

Truth-layer (must match product status):
- Source of truth: /root/moxie_hq/products/formbeep/status.md
- Current paying customers: 1 (do not claim more)

Goal of this plan:
- Make Reddit sustainable and non-spammy.
- Concentrate posting on Tue/Wed/Thu (higher workweek intent) + use other days for replies + intel.

---

## Weekly cadence overview

- Monday: intel + drafting + queue selection (no posts)
- Tuesday: 1 primary action (post OR comment-sprint, depending on subreddit history)
- Wednesday: 1 primary action (post OR comment-sprint)
- Thursday: comment-sprint + partnership signal capture
- Friday–Sunday: replies only + log results (no new posts unless something is trending and rules allow)

Primary posting window (recommended):
- 14:00 UTC (≈ 18:00 GST) — consistent US/EU overlap

---

## Preflight (MANDATORY before any Tue/Wed/Thu action)

1) Run subreddit intel (laptop):
- Script: /root/moxie_hq/scripts/reddit-intel/reddit_campaign_preflight.py
- Command template:
  python3 reddit_campaign_preflight.py \
    --subreddits <sub1> <sub2> \
    --me rishikeshshari \
    --competitors adambengur ConferenceOnly1415 \
    --out reddit_campaign_preflight.md \
    --headed

2) Rules check (manual):
- https://www.reddit.com/r/<sub>/about/rules
- Confirm: link policy in post + comments, self-promo expectations, weekly promo threads.

3) Conflict check:
- If you posted in that subreddit in last 30–45 days: do comment-only (no new post).

---

## Week template (fill these in each Monday)

### Tuesday (Primary)
Pick ONE:
A) 1 post in a subreddit where you have low recent posting history.
B) Comment-sprint (2–3 high-value comments) in a subreddit where you posted recently.

### Wednesday (Primary)
Pick ONE:
A) 1 post (different subreddit than Tuesday)
B) Comment-sprint

### Thursday (Support)
- Comment-sprint (3 comments, spaced 30–60 min)
- Capture partnership leads (agencies, WP maintainers, Framer/Webflow builders)

---

## Suggested subreddit usage rules (simple)

- r/microsaas: comment-only most weeks (you already posted a launch last month; competitor is active there).
- r/buildinpublic: 1 post max per week, always with context + lessons + specific feedback request.

---

## Logging (required)
After each Tue/Wed/Thu action, append to your notes:
- URL
- subreddit
- upvotes/comments after 1h, 6h, 24h
- any DMs
- any product questions/objections (for landing page + FAQ)
