# Reddit Intel Scanner — Browser Automation (no API)

Uses Playwright to automate a real browser session and scrape Reddit HTML directly. No Reddit app credentials needed. Works without API approval.

## Prerequisites

- Python 3.8+
- pip

## Setup

```bash
cd /root/moxie_hq/products/formbeep/outreach
pip install playwright
playwright install chromium
```

## Run

```bash
python reddit_intel_scanner_browser.py
```

The script will:
1. Open a Chromium browser window (visible or headless).
2. Visit Reddit’s homepage; if a login wall appears, it pauses so you can log in manually. After logging in, press Enter in the terminal to continue.
3. Scrape:
   - For each founder username: collects up to 50 recent posts with titles, subreddit, and URLs.
   - For each target subreddit: collects up to 50 hot posts with titles and scores.
4. Outputs `reddit_intel_brief_browser.md` with:
   - Founder top subreddits (by post count)
   - High-engagement post titles (copy hooks)
   - Target subreddit signals
   - Raw appendix of top posts

## Notes

- This respects Reddit’s website pacing; it includes waits to avoid hammering the site.
- If you are rate-limited or see CAPTCHAs, run the script fewer times and from your normal IP (not a server data center).
- The script does not automate posting — it is for intel only. Use the existing content packs to post manually.
- To make headless (no browser window): change `headless=False` to `headless=True` in the script after verifying it works interactively.

## Files

- `reddit_intel_scanner_browser.py` — main script
- `reddit_intel_brief_browser.md` — generated output

Keep the output private to SapiensTech.
