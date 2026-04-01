#!/usr/bin/env python3
"""
SapiensTech Reddit Intel Scanner — Browser Automation (no API)

This script uses Playwright to automate a real browser session.
It scrapes Reddit HTML directly (no API, no app credentials needed).
Works even if Reddit API approvals are closed.

Setup:
1) Install dependencies: pip install playwright
2) Install browsers: playwright install chromium
3) Run: python reddit_intel_scanner_browser.py

Outputs: reddit_intel_brief_browser.md

Note:
- This accesses Reddit via the public website, so it obeys rate limits and ToS.
- Do not run aggressive parallel scrapes; the defaults are conservative.
- If Reddit shows a login wall, the script will pause for manual login.
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: Install Playwright first: pip install playwright")
    print("Then run: playwright install chromium")
    sys.exit(1)

# Configuration
TARGET_USERS = ["adambengur", "ConferenceOnly1415"]
TARGET_SUBREDDITS = ["SaaS", "Entrepreneur", "SmallBusiness", "NoCode", "Wordpress", "startups"]
MAX_POSTS_PER_USER = 50
MAX_POSTS_PER_SUBREDDIT = 50
OUTPUT_FILE = Path("reddit_intel_brief_browser.md")
WAIT_AFTER_NAV = 3  # seconds to wait for content to load

def safe_text(elem):
    try:
        return elem.inner_text().strip()
    except Exception:
        return ""

def scrape_user_profile(page, username):
    url = f"https://www.reddit.com/user/{username}"
    print(f"Scraping {url}")
    page.goto(url, timeout=60000)
    time.sleep(WAIT_AFTER_NAV)
    # Scroll a bit to trigger lazy loading
    for _ in range(2):
        page.mouse.wheel(0, 1500)
        time.sleep(1.5)

    posts = []
    # Select post links from the feed
    anchors = page.query_selector_all("a[data-click-id='body']")
    for a in anchors[:MAX_POSTS_PER_USER]:
        try:
            href = a.get_attribute("href")
            if not href or "/comments/" not in href:
                continue
            # Get parent post container details by navigating or using DOM; easier: collect titles from the feed
            title_elem = a.evaluate_handle("el => el.closest('div[data-testid=\"post-container\"]')?.querySelector('h3')?.innerText")
            title = title_elem.json_value() if title_elem else a.inner_text().strip()
            subreddit_elem = a.evaluate_handle("el => el.closest('div[data-testid=\"post-container\"]')?.querySelector('a[data-click-id=\"subreddit\"]')?.innerText")
            subreddit = subreddit_elem.json_value() if subreddit_elem else ""
            posts.append({
                "title": title,
                "subreddit": subreddit,
                "url": f"https://www.reddit.com{href}" if href.startswith("/") else href,
            })
        except Exception as e:
            continue
    return {"username": username, "posts": posts}

def scrape_subreddit(page, name):
    url = f"https://www.reddit.com/r/{name}"
    print(f"Scraping {url}")
    page.goto(url, timeout=60000)
    time.sleep(WAIT_AFTER_NAV)
    for _ in range(2):
        page.mouse.wheel(0, 1500)
        time.sleep(1.5)

    top_posts = []
    anchors = page.query_selector_all("a[data-click-id='body']")
    for a in anchors[:MAX_POSTS_PER_SUBREDDIT]:
        try:
            href = a.get_attribute("href")
            if not href or "/comments/" not in href:
                continue
            title_elem = a.evaluate_handle("el => el.closest('div[data-testid=\"post-container\"]')?.querySelector('h3')?.innerText")
            title = title_elem.json_value() if title_elem else a.inner_text().strip()
            score_elem = a.evaluate_handle("el => el.closest('div[data-testid=\"post-container\"]')?.querySelector('div[data-click-id=\"score\"]')?.innerText")
            score_text = score_elem.json_value() if score_elem else ""
            top_posts.append({
                "title": title,
                "url": f"https://www.reddit.com{href}" if href.startswith("/") else href,
                "score_text": score_text,
            })
        except Exception:
            continue
    return {"subreddit": name, "top_posts": top_posts}

def extract_top_subreddits(founder_data):
    counts = {}
    for p in founder_data.get("posts", []):
        sub = p.get("subreddit", "").strip()
        if sub:
            counts[sub] = counts.get(sub, 0) + 1
    sorted_subs = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:10]
    return sorted_subs

def generate_markdown(brief):
    out = []
    out.append(f"# Reddit Intel Brief (Browser Scrape)\n")
    out.append(f"Generated: {datetime.utcnow().isoformat()}Z\n")
    out.append("## Founders Analyzed\n")
    for u in TARGET_USERS:
        out.append(f"- u/{u}")
    out.append("\n## Summary per Founder\n")
    for data in brief["founders"]:
        out.append(f"### u/{data['username']}")
        top_subs = extract_top_subreddits(data)
        if top_subs:
            out.append("Top subreddits:")
            for sub, cnt in top_subs:
                out.append(f"- r/{sub} ({cnt} posts)")
        else:
            out.append("No subreddit data collected.")
        out.append("\n")
    out.append("## Target Subreddit Signals\n")
    for sub in TARGET_SUBREDDITS:
        sub_data = brief["subreddits"].get(sub)
        if not sub_data or "error" in sub_data:
            out.append(f"- r/{sub}: scan failed or private")
        else:
            count = len(sub_data.get("top_posts", []))
            out.append(f"- r/{sub}: collected {count} top posts (see appendix)")
    out.append("\n## Recommendations\n")
    out.append("1. Prioritize subreddits where founders are most active.")
    out.append("2. Match posting style to top-performing posts in each sub.")
    out.append("3. Mix self-contained value posts with community questions.")
    out.append("4. Prepare 15+ comment seeds to engage early.\n")
    out.append("## Appendix: Raw Top Posts by Subreddit\n")
    for sub in TARGET_SUBREDDITS:
        sub_data = brief["subreddits"].get(sub)
        if not sub_data or "error" in sub_data:
            continue
        out.append(f"### r/{sub}")
        for i, p in enumerate(sub_data.get("top_posts", [])[:10], 1):
            out.append(f"{i}. {p['title']} (score: {p.get('score_text','?')})")
            out.append(f"   {p['url']}")
        out.append("")
    return "\n".join(out)

def main():
    print("Starting browser-based Reddit intel scan...")
    brief = {"generated_at": datetime.utcnow().isoformat() + "Z", "founders": [], "subreddits": {}}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for headless
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
        )
        page = context.new_page()
        # Check if login is forced
        try:
            page.goto("https://www.reddit.com", timeout=30000)
            time.sleep(2)
            if "login" in page.url.lower():
                print("\n=== Reddit is asking to log in ===")
                print("Please log in manually in the browser window that just opened.")
                print("After logging in, press Enter in this terminal to continue...")
                input()
        except Exception as e:
            print(f"Warning: initial page check failed: {e}")
        # Scan founders
        for user in TARGET_USERS:
            try:
                data = scrape_user_profile(page, user)
                brief["founders"].append(data)
                print(f"  Collected {len(data['posts'])} posts from u/{user}")
            except Exception as e:
                print(f"  ERROR scanning {user}: {e}")
                brief["founders"].append({"username": user, "error": str(e), "posts": []})
        # Scan subreddits
        for sub in TARGET_SUBREDDITS:
            try:
                data = scrape_subreddit(page, sub)
                brief["subreddits"][sub] = data
                print(f"  Collected {len(data.get('top_posts', []))} posts from r/{sub}")
            except Exception as e:
                print(f"  ERROR scanning r/{sub}: {e}")
                brief["subreddits"][sub] = {"error": str(e)}
        browser.close()
    # Write output
    out_md = generate_markdown(brief)
    OUTPUT_FILE.write_text(out_md)
    print(f"\nWrote intel brief to {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    main()
