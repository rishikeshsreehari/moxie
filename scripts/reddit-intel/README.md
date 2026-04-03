# Reddit intel scanner (browser automation, no API)

Current version: **v2026-04-01-v3**

This script gathers comprehensive Reddit intel for FormBeep and the SapiensTech portfolio.

**What it collects:**
- For each founder/user (adambengur, ConferenceOnly1415, rishikeshshari):
  - Recent posts (title, subreddit, score, comment count) and top subreddit aggregates.
  - Recent comments (subreddit, score, snippet) and top subreddit aggregates by comment count.
  - For the most-commented posts (top 6): the post's selftext snippet + top 5 replies with sentiment scores.
- For keywords (beepmate, web2phone, formbeep, zapier, typeform, tally, twilio, "sms notifications", "whatsapp without zapier"):
  - Top threads sorted by comment count.
  - For the top 6 threads per keyword: post selftext snippet + top 3 replies with sentiment.
  - Aggregate table by subreddit: total threads, total comments, average sentiment.
- Collection summary counts at the top.

**Output:** `reddit_intel_brief_browser.md`

**How it works:**
- Uses Playwright to drive Chromium against old.reddit.com (stable HTML).
- If login is required, pauses for manual login; saves session state for later runs.
- Respectful pacing to reduce rate-limit / captcha risk.

## Install

```bash
python3 -m pip install -r requirements.txt
playwright install chromium
```

## Run

Interactive (recommended first run to login and save session state):

```bash
python3 reddit_intel_scanner_browser.py
```

### Campaign preflight (per-subreddit: your history, competitor history, top posts of week, rules)

```bash
python3 reddit_campaign_preflight.py \
  --subreddits microsaas buildinpublic \
  --me rishikeshshari \
  --competitors adambengur ConferenceOnly1415 \
  --out reddit_campaign_preflight.md \
  --headed
```

- Output: `reddit_campaign_preflight.md`
- This is the required input for Ember before writing the paste-ready execution packet.

Simple single command (handles login automatically):

```bash
python3 reddit_intel_scanner_browser.py --auto
```

- First run: opens Chromium, you log in, session saved to `reddit_storage_state.json`
- Subsequent runs: detects saved session, runs headless automatically

Background/headless (after you already have `reddit_storage_state.json` saved):

```bash
python3 reddit_intel_scanner_browser.py --auto > run.log 2>&1 &
```

Note: even headless runs still spawn a Chromium process; you just don’t need to keep a visible window open.

## Configuration

Edit the script to adjust:
- `FOUNDERS` – Reddit usernames to analyze.
- `KEYWORDS` – terms to search.
- `MAX_*` limits (keep conservative).
- `TOP_THREADS_DETAILS_PER_SOURCE` – how many threads to fetch full details for.
- `HEADLESS` – set `True` to run without a visible browser window.

## Output structure

- **Collection Summary** – total posts, comments, keyword threads.
- **Founder + Your Activity** – per user:
  - Top subreddits (posts & comments tables)
  - Top comments by score (with snippets & links)
  - Most commented posts with OP excerpt & sample replies (with sentiment)
- **Keyword Attention & Sentiment**:
  - Subreddit aggregate table (threads/comments/avg sentiment)
  - Per-keyword thread list with details (OP excerpt + sample replies)

Use the excerpts and reply samples to craft posting angles, seed comments, and understand community tone.

## Notes

- Sentiment is a heuristic (VADER compound). Always verify top threads manually.
- Delete `reddit_storage_state.json` to force re-login.
- Do not hammer Reddit; the defaults are intentionally conservative.
