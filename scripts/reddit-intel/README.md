# Reddit intel scanner (browser automation, no API)

This script answers the exact questions you asked:
- What did each founder actually post, in which subreddits?
- Where did they get the most attention (comments)?
- How did people respond (sample comments) and what's the *rough* sentiment?
- Where do "beepmate" / "web2phone" get attention (which communities) and what's the general sentiment?

It uses Playwright to drive a real Chromium browser and scrapes **old.reddit.com** (HTML). No Reddit API app / approvals required.

## Install

```bash
python3 -m pip install -r requirements.txt
playwright install chromium
```

## Run

```bash
python3 reddit_intel_scanner_browser.py
```

First run:
- A Chromium window opens.
- If Reddit asks you to log in, log in manually.
- The script saves `reddit_storage_state.json` so next runs usually don't require login.

## Output

- `reddit_intel_brief_browser.md` — the brief
- `reddit_storage_state.json` — saved browser session (delete to force re-login)

## Tuning

Open `reddit_intel_scanner_browser.py` and adjust:
- `FOUNDERS`
- `KEYWORDS`
- `MAX_*` limits (keep conservative)
- `HEADLESS`

## Notes

- Sentiment is a heuristic (VADER compound score). Use it as a directional signal; always click into top threads for a human read.
- Script is intentionally conservative to reduce rate-limit / captcha risk.
