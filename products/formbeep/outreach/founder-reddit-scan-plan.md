# Founder Reddit Scan — Beepmate + Web2Phone (Plan + Inputs Needed)

Goal: extract what worked for the founders on Reddit so we can post with a similar angle in the same communities.

Founders to analyze
- Beepmate: u/adambengur
- Web2Phone: u/ConferenceOnly1415

What we want to output
1) Subreddit list (ranked): where they posted/commented and got traction
2) Winning angles: the story frames / pain points / hooks / formats that got upvotes + comments
3) Posting style: frequency, comment strategy, links vs no-links, self-promo patterns
4) “Do-not-copy” notes: anything that would be spammy or violates community rules
5) Our copycat plan: 5–10 post templates + 20 comment templates tailored to the same subs

Current blocker
Reddit is blocking access from this environment with “blocked by network policy” (both new Reddit and old.reddit.com).

Inputs needed to proceed
Option A (preferred): Reddit API dev app token
- Create a Reddit app and provide:
  - client_id
  - client_secret
  - username/password OR refresh_token
  - a unique user-agent string (required)

Option B: Logged-in session
- Provide a cookie export or a way to run with authenticated session.

Once unblocked
- Vale will run the scan, then write:
  - /root/moxie_hq/products/formbeep/outreach/founder-reddit-scan.md
