#!/usr/bin/env python3
"""\
SapiensTech Reddit Intel Scanner — Browser Automation (no API)

What it does (high level):
- Scrapes founder activity (posts + comments) from the web UI (old.reddit.com).
- For each founder post, optionally opens the thread and samples top-level comments,
  then estimates sentiment (VADER) + engagement (comment counts).
- Searches Reddit web UI for keyword mentions (beepmate/web2phone) and summarizes
  which communities respond most + overall sentiment.

Why old.reddit.com:
- More stable HTML + lighter JS than the new Reddit UI.

Setup (laptop):
  python3 -m pip install -r requirements.txt
  python3 reddit_intel_scanner_browser.py

First run:
- A Chromium window opens. If prompted, log in manually.
- The script saves a Playwright storage state file (reddit_storage_state.json)
  so future runs usually don't require login.

Output:
- reddit_intel_brief_browser.md

Notes:
- Keep limits conservative; don't hammer Reddit.
- This is for intel only; manual posting should be done separately.
"""

from __future__ import annotations

import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: Install Playwright first: python3 -m pip install playwright")
    print("Then install browser: playwright install chromium")
    sys.exit(1)

try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
except ImportError:
    print("ERROR: Install dependencies: python3 -m pip install -r requirements.txt")
    sys.exit(1)


# -------------------- CONFIG --------------------

FOUNDERS = ["adambengur", "ConferenceOnly1415"]

# Communities we *also* sample for context (not necessarily where founders posted)
TARGET_SUBREDDITS = ["SaaS", "Entrepreneur", "SmallBusiness", "NoCode", "Wordpress", "startups"]

# What to compare attention for
KEYWORDS = [
    "beepmate",
    "beepmate.io",
    "web2phone",
]

MAX_FOUNDER_POSTS = 40
MAX_FOUNDER_COMMENTS = 60
MAX_THREAD_COMMENTS_TO_SAMPLE = 25
MAX_KEYWORD_RESULTS_PER_QUERY = 20

WAIT_AFTER_NAV = 2.5
SCROLL_PULSES = 2
SCROLL_PIXELS = 1400

HEADLESS = False

STORAGE_STATE_PATH = Path("reddit_storage_state.json")
OUTPUT_FILE = Path("reddit_intel_brief_browser.md")


# -------------------- UTIL --------------------

def _sleep(s: float) -> None:
    time.sleep(s)


def _safe_text(el) -> str:
    try:
        return (el.inner_text() or "").strip()
    except Exception:
        return ""


def _parse_int_loose(s: str) -> Optional[int]:
    s = (s or "").strip().lower()
    if not s:
        return None
    # examples: "123 points", "1.2k points", "•", "comment"
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)(k|m)?", s)
    if not m:
        return None
    num = float(m.group(1))
    mult = m.group(2)
    if mult == "k":
        num *= 1000
    if mult == "m":
        num *= 1_000_000
    return int(num)


def _now_utc() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


@dataclass
class ListingItem:
    kind: str  # "post" | "comment" | "search_result"
    title: str
    url: str
    subreddit: str
    score: Optional[int] = None
    comments_count: Optional[int] = None
    author: Optional[str] = None
    snippet: str = ""  # comment snippet or selftext excerpt


# -------------------- SCRAPERS (old.reddit.com) --------------------

def _goto(page, url: str) -> None:
    page.goto(url, timeout=60_000)
    _sleep(WAIT_AFTER_NAV)


def _scroll_some(page) -> None:
    for _ in range(SCROLL_PULSES):
        page.mouse.wheel(0, SCROLL_PIXELS)
        _sleep(1.0)


def scrape_old_user_submitted(page, username: str, limit: int) -> List[ListingItem]:
    # Use /submitted/ which is stable
    url = f"https://old.reddit.com/user/{username}/submitted/"
    print(f"Scraping submissions: {url}")
    _goto(page, url)
    _scroll_some(page)

    items: List[ListingItem] = []
    things = page.query_selector_all("div.thing")
    for t in things:
        if len(items) >= limit:
            break
        try:
            subreddit = (t.get_attribute("data-subreddit") or "").strip()
            permalink = (t.get_attribute("data-permalink") or "").strip()
            if not permalink:
                continue
            title_el = t.query_selector("a.title")
            title = _safe_text(title_el)
            score_el = t.query_selector("div.score")
            score = _parse_int_loose(_safe_text(score_el))
            comments_el = t.query_selector("a.comments")
            comments_count = _parse_int_loose(_safe_text(comments_el))

            items.append(
                ListingItem(
                    kind="post",
                    title=title,
                    url=f"https://old.reddit.com{permalink}",
                    subreddit=subreddit,
                    score=score,
                    comments_count=comments_count,
                    author=username,
                )
            )
        except Exception:
            continue
    return items


def scrape_old_user_comments(page, username: str, limit: int) -> List[ListingItem]:
    url = f"https://old.reddit.com/user/{username}/comments/"
    print(f"Scraping comments: {url}")
    _goto(page, url)
    _scroll_some(page)

    items: List[ListingItem] = []
    things = page.query_selector_all("div.thing")
    for t in things:
        if len(items) >= limit:
            break
        try:
            subreddit_el = t.query_selector("a.subreddit")
            subreddit = _safe_text(subreddit_el).replace("r/", "").strip()
            permalink = (t.get_attribute("data-permalink") or "").strip()
            if not permalink:
                continue
            score_el = t.query_selector("span.score")
            score = _parse_int_loose(_safe_text(score_el))
            body_el = t.query_selector("div.md")
            snippet = _safe_text(body_el)
            title_el = t.query_selector("a.title")
            # comment pages include the post title
            title = _safe_text(title_el) or "(comment)"

            items.append(
                ListingItem(
                    kind="comment",
                    title=title,
                    url=f"https://old.reddit.com{permalink}",
                    subreddit=subreddit,
                    score=score,
                    author=username,
                    snippet=snippet[:400],
                )
            )
        except Exception:
            continue
    return items


def scrape_thread_top_comments(page, thread_url: str, limit: int) -> List[str]:
    # Collect a sample of top-level comments
    _goto(page, thread_url)
    _sleep(1.0)

    comments: List[str] = []
    # old reddit comment bodies are in div.comment div.md
    bodies = page.query_selector_all("div.comment div.entry div.md")
    for b in bodies:
        if len(comments) >= limit:
            break
        txt = _safe_text(b)
        txt = re.sub(r"\s+", " ", txt).strip()
        if not txt:
            continue
        # Skip deleted/removed
        if txt.lower() in ("[deleted]", "[removed]"):
            continue
        comments.append(txt[:800])
    return comments


def scrape_old_search(page, query: str, limit: int) -> List[ListingItem]:
    # Sort by comments to find where attention is highest
    url = f"https://old.reddit.com/search?q={query}&sort=comments&t=all"
    print(f"Search: {url}")
    _goto(page, url)
    _scroll_some(page)

    items: List[ListingItem] = []
    things = page.query_selector_all("div.thing")
    for t in things:
        if len(items) >= limit:
            break
        try:
            subreddit = (t.get_attribute("data-subreddit") or "").strip()
            permalink = (t.get_attribute("data-permalink") or "").strip()
            if not permalink:
                continue
            title_el = t.query_selector("a.title")
            title = _safe_text(title_el)
            score_el = t.query_selector("div.score")
            score = _parse_int_loose(_safe_text(score_el))
            comments_el = t.query_selector("a.comments")
            comments_count = _parse_int_loose(_safe_text(comments_el))

            items.append(
                ListingItem(
                    kind="search_result",
                    title=title,
                    url=f"https://old.reddit.com{permalink}",
                    subreddit=subreddit,
                    score=score,
                    comments_count=comments_count,
                )
            )
        except Exception:
            continue

    return items


# -------------------- ANALYSIS --------------------

def sentiment_score(analyzer: SentimentIntensityAnalyzer, texts: List[str]) -> Optional[float]:
    if not texts:
        return None
    vals = [analyzer.polarity_scores(t)["compound"] for t in texts if t]
    if not vals:
        return None
    return sum(vals) / len(vals)


def agg_by_subreddit(items: List[ListingItem]) -> Dict[str, Dict[str, Any]]:
    agg: Dict[str, Dict[str, Any]] = defaultdict(lambda: {"count": 0, "total_comments": 0, "total_score": 0, "with_comments": 0})
    for it in items:
        sub = (it.subreddit or "").strip()
        if not sub:
            continue
        a = agg[sub]
        a["count"] += 1
        if it.comments_count is not None:
            a["total_comments"] += it.comments_count
            a["with_comments"] += 1
        if it.score is not None:
            a["total_score"] += it.score
    return agg


def to_table(rows: List[List[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    out = []
    for ri, r in enumerate(rows):
        line = " | ".join(r[i].ljust(widths[i]) for i in range(len(r)))
        out.append(line)
        if ri == 0:
            out.append("-|-".join("-" * w for w in widths))
    return "\n".join(out)


def generate_markdown(
    founder_posts: Dict[str, List[ListingItem]],
    founder_comments: Dict[str, List[ListingItem]],
    founder_thread_sentiment: Dict[str, Dict[str, float]],
    keyword_results: Dict[str, List[Tuple[ListingItem, Optional[float]]]],
) -> str:
    out: List[str] = []
    out.append("# Reddit Intel Brief (Browser Automation)")
    out.append(f"Generated: {_now_utc()}")
    out.append("")

    # Founder summary
    out.append("## Founder activity summary")
    for u in FOUNDERS:
        posts = founder_posts.get(u, [])
        comments = founder_comments.get(u, [])

        out.append("")
        out.append(f"### u/{u}")
        out.append(f"Collected: {len(posts)} posts, {len(comments)} comments")

        # Top subs by post count + engagement
        agg = agg_by_subreddit(posts)
        rows = [["subreddit", "posts", "avg comments", "avg score"]]
        for sub, a in sorted(agg.items(), key=lambda kv: kv[1]["count"], reverse=True)[:12]:
            avg_comments = (a["total_comments"] / a["with_comments"]) if a["with_comments"] else 0
            avg_score = (a["total_score"] / a["count"]) if a["count"] else 0
            rows.append([sub, str(a["count"]), f"{avg_comments:.1f}", f"{avg_score:.1f}"])
        out.append("")
        out.append(to_table(rows))

        # Most-commented posts
        top_posts = sorted(posts, key=lambda p: (p.comments_count or 0), reverse=True)[:8]
        out.append("")
        out.append("Most commented posts (proxy for attention):")
        for p in top_posts:
            sent = founder_thread_sentiment.get(u, {}).get(p.url)
            sent_s = f"sent {sent:+.2f}" if sent is not None else "sent ?"
            out.append(f"- [{p.comments_count or 0} comments | {sent_s}] r/{p.subreddit} — {p.title}")
            out.append(f"  {p.url}")

    # Keyword attention summary
    out.append("")
    out.append("## Beepmate/Web2Phone attention + sentiment")
    out.append("(Based on keyword search results; sorted by comment count.)")

    # Aggregate by subreddit across keywords
    by_sub = defaultdict(lambda: {"threads": 0, "total_comments": 0, "sent_vals": []})
    for kw, entries in keyword_results.items():
        for item, sent in entries:
            sub = item.subreddit or ""
            if not sub:
                continue
            by_sub[sub]["threads"] += 1
            by_sub[sub]["total_comments"] += int(item.comments_count or 0)
            if sent is not None:
                by_sub[sub]["sent_vals"].append(sent)

    rows = [["subreddit", "threads", "total comments", "avg sentiment"]]
    for sub, a in sorted(by_sub.items(), key=lambda kv: kv[1]["total_comments"], reverse=True)[:20]:
        avg_sent = sum(a["sent_vals"]) / len(a["sent_vals"]) if a["sent_vals"] else 0.0
        rows.append([sub, str(a["threads"]), str(a["total_comments"]), f"{avg_sent:+.2f}"])
    out.append("")
    out.append(to_table(rows))

    out.append("")
    out.append("Top threads by keyword:")
    for kw, entries in keyword_results.items():
        out.append("")
        out.append(f"### Query: {kw}")
        for item, sent in sorted(entries, key=lambda t: (t[0].comments_count or 0), reverse=True)[:10]:
            sent_s = f"{sent:+.2f}" if sent is not None else "?"
            out.append(f"- [{item.comments_count or 0} comments | sent {sent_s}] r/{item.subreddit} — {item.title}")
            out.append(f"  {item.url}")

    out.append("")
    out.append("## Notes / how to use")
    out.append("- Use the founder 'most commented posts' list to copy the *style* (not the content).")
    out.append("- Use the keyword attention table to pick communities that discuss similar tools and react strongly (high comments).")
    out.append("- Sentiment is a rough heuristic (VADER compound score). Always sanity-check the top threads manually.")

    return "\n".join(out) + "\n"


# -------------------- MAIN --------------------

def ensure_logged_in(page) -> None:
    # If redirected to login, user must login once; we then persist state.
    _goto(page, "https://old.reddit.com")
    if "login" in (page.url or "").lower():
        print("\n=== Reddit is asking to log in ===")
        print("Log in in the Chromium window that just opened.")
        print("Then come back here and press Enter to continue...")
        input()


def main() -> None:
    print("Starting Reddit intel scan (browser automation, no API)...")

    analyzer = SentimentIntensityAnalyzer()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)

        if STORAGE_STATE_PATH.exists():
            context = browser.new_context(storage_state=str(STORAGE_STATE_PATH))
        else:
            context = browser.new_context()

        context.set_default_timeout(60_000)
        page = context.new_page()

        ensure_logged_in(page)

        # Persist session so next run doesn't require login
        try:
            context.storage_state(path=str(STORAGE_STATE_PATH))
        except Exception:
            pass

        founder_posts: Dict[str, List[ListingItem]] = {}
        founder_comments: Dict[str, List[ListingItem]] = {}
        founder_thread_sentiment: Dict[str, Dict[str, float]] = defaultdict(dict)

        # Founder scans
        for u in FOUNDERS:
            try:
                posts = scrape_old_user_submitted(page, u, MAX_FOUNDER_POSTS)
                founder_posts[u] = posts
                print(f"  u/{u}: posts={len(posts)}")
            except Exception as e:
                print(f"  ERROR scanning posts for u/{u}: {e}")
                founder_posts[u] = []

            try:
                comments = scrape_old_user_comments(page, u, MAX_FOUNDER_COMMENTS)
                founder_comments[u] = comments
                print(f"  u/{u}: comments={len(comments)}")
            except Exception as e:
                print(f"  ERROR scanning comments for u/{u}: {e}")
                founder_comments[u] = []

            # Per-thread sentiment sample for most-commented posts (limit to 6 to avoid overfetch)
            top_for_sent = sorted(founder_posts[u], key=lambda x: (x.comments_count or 0), reverse=True)[:6]
            for post in top_for_sent:
                try:
                    comm_texts = scrape_thread_top_comments(page, post.url, MAX_THREAD_COMMENTS_TO_SAMPLE)
                    s = sentiment_score(analyzer, comm_texts)
                    if s is not None:
                        founder_thread_sentiment[u][post.url] = s
                    print(f"    thread sentiment sampled: r/{post.subreddit} ({post.comments_count or 0} comments) -> {s if s is not None else 'n/a'}")
                except Exception as e:
                    print(f"    thread sentiment failed: {post.url} ({e})")

        # Keyword attention scans
        keyword_results: Dict[str, List[Tuple[ListingItem, Optional[float]]]] = {k: [] for k in KEYWORDS}
        for kw in KEYWORDS:
            q = kw
            results = scrape_old_search(page, q, MAX_KEYWORD_RESULTS_PER_QUERY)
            enriched: List[Tuple[ListingItem, Optional[float]]] = []
            # Only sample sentiment for the top few threads to avoid load
            for idx, item in enumerate(results):
                s: Optional[float] = None
                if idx < 6:
                    try:
                        comm_texts = scrape_thread_top_comments(page, item.url, MAX_THREAD_COMMENTS_TO_SAMPLE)
                        s = sentiment_score(analyzer, comm_texts)
                    except Exception:
                        s = None
                enriched.append((item, s))
            keyword_results[kw] = enriched
            print(f"  keyword '{kw}': threads={len(enriched)}")

        browser.close()

    md = generate_markdown(founder_posts, founder_comments, founder_thread_sentiment, keyword_results)
    OUTPUT_FILE.write_text(md, encoding="utf-8")
    print(f"\nWrote brief: {OUTPUT_FILE.resolve()}")
    print(f"Saved session state: {STORAGE_STATE_PATH.resolve()} (delete this file to force re-login)")


if __name__ == "__main__":
    main()
