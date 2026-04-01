# Reddit access: what works + API details (FormBeep)

## TL;DR
- From *this* Hermes environment, requests to reddit.com return **HTTP 403: Blocked** (verified).
- That means: even read-only scraping via `.json` endpoints will not work here.
- You (Rishi) can still post manually using the content packs already on disk.
- If you want automated scanning (founder profiles, subreddit intel), run it from a network/machine that can reach Reddit and use OAuth.

## Content you can post manually (already prepared)
- /root/moxie_hq/products/formbeep/outreach/reddit-week1-execution-pack.md
- /root/moxie_hq/products/formbeep/outreach/reddit-campaign-plan.md
- /root/moxie_hq/products/formbeep/reddit-strategy.md
- /root/moxie_hq/products/formbeep/community-posting-plan.md

## Option A: Official Reddit API (OAuth) — recommended for scanning
1) Create a Reddit dev app
- Go to: https://www.reddit.com/prefs/apps
- Click: “create app”
- Type: **script** (for personal use) or **web app** (for user-facing OAuth)
- Note your:
  - client_id (the short string under the app name)
  - client_secret
  - redirect_uri (if web app)

2) Get an access token (script app)
Request:
POST https://www.reddit.com/api/v1/access_token
Basic auth: client_id:client_secret
Body (x-www-form-urlencoded):
- grant_type=password
- username=<your_reddit_username>
- password=<your_reddit_password>

3) Call the API
Use the returned bearer token:
GET https://oauth.reddit.com/user/<username>/submitted
Headers:
- Authorization: Bearer <token>
- User-Agent: <descriptive UA like "FormBeepIntel/0.1 by u/<username>">

Notes:
- Don’t share passwords in automation if you can avoid it; a “web app” flow with refresh tokens is cleaner.
- Reddit is strict about User-Agent; always set one.

## Option B: Logged-in session (cookies)
- Export cookies from a logged-in browser session and use them in a script.
- Works for some private/edge cases but is more brittle than OAuth.

## What I can do next once you confirm where you’ll run the scan
- Provide a ready-to-run Python script (PRAW-based) that:
  - pulls a founder profile history
  - extracts top subreddits + post types
  - outputs a 1-page “angles + hooks” brief

(But it must run from a machine/network that isn’t 403-blocked from reddit.com.)
