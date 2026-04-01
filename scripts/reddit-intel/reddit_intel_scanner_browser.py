#!/usr/bin/env python3
"""
SapiensTech Reddit Intel Scanner — Browser Automation (no API)

Version: 2026-04-01-v3
  - Adds: founder comments + thread details (selftext + top replies) with sentiment
  - Adds: your profile (rishikeshshari)
  - Adds: expanded keyword set (formbeep, competitors, key phrases)
  - Adds: collection summary + richer markdown brief
  - Details: old.reddit.com scraping, VADER sentiment, Playwright storage state

What it does (high level):
- Scrapes founder + your own activity (posts + comments) from the web UI (old.reddit.com).
- For each founder post, opens the thread and samples top-level comments,
  returning both sentiment (VADER) and actual comment excerpts.
- Lists founder comments by subreddit and score.
- Searches Reddit web UI for keyword mentions (beepmate/web2phone/formbeep + competitors)
  and summarizes which communities respond most + overall sentiment.
- Includes post selftext snippets and sampled comments for high-attention threads.
- Generates a rich markdown brief with actionable intel.

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
import random

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

FOUNDERS = ["adambengur", "ConferenceOnly1415", "rishikeshshari"]

# Communities we also sample for context (not necessarily where founders posted)
TARGET_SUBREDDITS = ["SaaS", "Entrepreneur", "SmallBusiness", "NoCode", "Wordpress", "startups"]

# Query-driven search (NOT single-word browsing).
# We focus on: forms → whatsapp/sms notifications, and competitor/alternative phrasing.
# These queries are used for global search AND per-subreddit restricted search.
SEARCH_QUERIES = [
    # Brand + direct competitors
    "formbeep",
    "formbeep.com",
    "beepmate",
    "beepmate.io",
    "web2phone",

    # Core pain / use-cases (forms → WhatsApp/SMS)
    "contact form whatsapp",
    "wordpress form whatsapp",
    "tally whatsapp",
    "typeform whatsapp",
    "google forms whatsapp",
    "form submission whatsapp notification",
    "form submission sms notification",
    "sms notifications for website",

    # Zapier alternative framing
    "zapier whatsapp",
    "zapier alternative whatsapp",
    "whatsapp without zapier",

    # Messaging infra in-context (avoid single-term like 'twilio')
    "twilio sms notifications",
    "twilio alternative sms",
    "whatsapp webhook",
]

# Back-compat alias (used in output headings)
KEYWORDS = SEARCH_QUERIES

MAX_FOUNDER_POSTS = 40
MAX_FOUNDER_COMMENTS = 60
MAX_THREAD_COMMENTS_TO_SAMPLE = 25
MAX_KEYWORD_RESULTS_PER_QUERY = 20
# Top threads (by comments) for which we fetch full details (selftext + comment excerpts)
TOP_THREADS_DETAILS_PER_SOURCE = 6

WAIT_AFTER_NAV = 2.5
SCROLL_PULSES = 2
SCROLL_PIXELS = 1400

HEADLESS = False

STORAGE_STATE_PATH = Path("reddit_storage_state.json")
OUTPUT_FILE = Path("reddit_intel_brief_browser.md")


# -------------------- UTIL --------------------

def _sleep(s: float) -> None:
    time.sleep(s)


def _sleep_jitter(base: float, extra_max: float = 0.8) -> None:
    """Randomized delay to reduce bot-like timing patterns."""
    mult = random.uniform(0.75, 1.55)
    extra = random.uniform(0.0, extra_max)
    time.sleep(base * mult + extra)


def _safe_text(el) -> str:
    try:
        return (el.inner_text() or "").strip()
    except Exception:
        return ""


def _parse_int_loose(s: str) -> Optional[int]:
    s = (s or "").strip().lower()
    if not s:
        return None
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
    snippet: str = ""  # comment snippet or selftext excerpt (when populated)


# -------------------- SCRAPERS (old.reddit.com) --------------------

def _goto(page, url: str) -> None:
    page.goto(url, timeout=60_000)
    _sleep_jitter(WAIT_AFTER_NAV)


def _scroll_some(page) -> None:
    for _ in range(SCROLL_PULSES):
        page.mouse.wheel(0, SCROLL_PIXELS)
        _sleep_jitter(1.0, extra_max=0.6)


def scrape_old_user_submitted(page, username: str, limit: int) -> List[ListingItem]:
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
                    snippet="",  # selftext fetched later
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


def scrape_thread_details(page, thread_url: str, comment_limit: int) -> Tuple[str, List[str]]:
    """
    Opens a thread page and returns:
      (selftext_snippet, [top_comment_texts...])
    """
    _goto(page, thread_url)
    # Get post selftext (old.reddit.com: div.usertext-body .md)
    selftext = ""
    try:
        selftext_el = page.query_selector("div.usertext-body .md")
        if selftext_el:
            selftext = _safe_text(selftext_el)[:500]
    except Exception:
        selftext = ""

    # Get top-level comments (div.comment div.entry div.md)
    comments: List[str] = []
    bodies = page.query_selector_all("div.comment div.entry div.md")
    for b in bodies:
        if len(comments) >= comment_limit:
            break
        txt = _safe_text(b)
        txt = re.sub(r"\s+", " ", txt).strip()
        if not txt or txt.lower() in ("[deleted]", "[removed]"):
            continue
        comments.append(txt[:800])
    return selftext, comments


def _parse_search_results(page, limit: int) -> List[ListingItem]:
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


def scrape_old_search(page, query: str, limit: int) -> List[ListingItem]:
    # Global search; sort by comments to find attention.
    from urllib.parse import quote_plus

    q = quote_plus(query)
    url = f"https://old.reddit.com/search?q={q}&sort=comments&t=all"
    print(f"Search (global): {query}")
    _goto(page, url)
    _scroll_some(page)
    return _parse_search_results(page, limit)


def scrape_old_search_in_subreddit(page, subreddit: str, query: str, limit: int) -> List[ListingItem]:
    # Restricted search inside a specific community.
    from urllib.parse import quote_plus

    q = quote_plus(query)
    url = f"https://old.reddit.com/r/{subreddit}/search?q={q}&restrict_sr=on&sort=comments&t=all"
    print(f"Search (r/{subreddit}): {query}")
    _goto(page, url)
    _scroll_some(page)
    return _parse_search_results(page, limit)


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
    founder_thread_details: Dict[str, Dict[str, Tuple[str, List[str]]]],  # username -> {url: (selftext, [comments])}
    founder_thread_sentiment: Dict[str, Dict[str, float]],
    keyword_results: Dict[str, List[ListingItem]],
    keyword_thread_details: Dict[str, Dict[str, Tuple[str, List[str]]]],  # keyword -> {url: (selftext, [comments])}
    keyword_thread_sentiment: Dict[str, Dict[str, float]],
) -> str:
    out: List[str] = []
    out.append("# Reddit Intel Brief (Browser Automation)")
    out.append(f"Generated: {_now_utc()} — scanner v2026-04-01-v3")
    out.append("")

    # Collection summary
    out.append("## Collection Summary")
    total_posts = sum(len(v) for v in founder_posts.values())
    total_comments = sum(len(v) for v in founder_comments.values())
    total_kw_threads = sum(len(v) for v in keyword_results.values())
    out.append(f"- Total founder posts collected: {total_posts}")
    out.append(f"- Total founder comments collected: {total_comments}")
    out.append(f"- Total keyword threads (all terms): {total_kw_threads}")
    out.append("")

    # Founder activity summary
    out.append("## Founder + Your Activity")
    for u in FOUNDERS:
        posts = founder_posts.get(u, [])
        comments = founder_comments.get(u, [])

        out.append("")
        out.append(f"### u/{u}")
        out.append(f"Collected: {len(posts)} posts, {len(comments)} comments")

        # Top subreddits for posts
        if posts:
            agg = agg_by_subreddit(posts)
            rows = [["subreddit", "posts", "avg comments", "avg score"]]
            for sub, a in sorted(agg.items(), key=lambda kv: kv[1]["count"], reverse=True)[:12]:
                avg_comments = (a["total_comments"] / a["with_comments"]) if a["with_comments"] else 0
                avg_score = (a["total_score"] / a["count"]) if a["count"] else 0
                rows.append([sub, str(a["count"]), f"{avg_comments:.1f}", f"{avg_score:.1f}"])
            out.append("\nTop subreddits by post count:")
            out.append(to_table(rows))

        # Top subreddits for comments
        if comments:
            agg_c = agg_by_subreddit(comments)
            rows_c = [["subreddit", "comments", "avg score"]]
            for sub, a in sorted(agg_c.items(), key=lambda kv: kv[1]["count"], reverse=True)[:12]:
                avg_score = (a["total_score"] / a["count"]) if a["count"] else 0
                rows_c.append([sub, str(a["count"]), f"{avg_score:.1f}"])
            out.append("\nTop subreddits by comment count:")
            out.append(to_table(rows_c))

        # Recent top comments by score
        if comments:
            top_comments = sorted(comments, key=lambda c: (c.score or 0), reverse=True)[:10]
            out.append("\nTop comments by score (sample):")
            for c in top_comments:
                out.append(f"- r/{c.subreddit} — score {c.score or 0}")
                out.append(f"  {c.url}")
                if c.snippet:
                    out.append(f"  > {c.snippet[:180]}...")
                out.append("")

        # Most-commented posts with details
        if posts:
            top_posts = sorted(posts, key=lambda p: (p.comments_count or 0), reverse=True)[:6]
            out.append("\nMost commented posts (with thread sentiment & top replies):")
            for p in top_posts:
                sent = founder_thread_sentiment.get(u, {}).get(p.url)
                sent_s = f"{sent:+.2f}" if sent is not None else "n/a"
                out.append(f"- [{p.comments_count or 0} comments | sent {sent_s}] r/{p.subreddit} — {p.title}")
                out.append(f"  {p.url}")
                details = founder_thread_details.get(u, {}).get(p.url)
                if details:
                    selftext, top_comms = details
                    if selftext:
                        out.append(f"  OP excerpt: {selftext[:200]}...")
                    if top_comms:
                        out.append("  Top replies (sample):")
                        for tcm in top_comms[:5]:
                            out.append(f"    - {tcm[:200]}...")
                out.append("")

    # Keyword attention + sentiment
    out.append("## Keyword Attention & Sentiment")
    out.append("(Threads sorted by comment count; samples show actual reply sentiment.)")

    # Aggregate by subreddit across keywords
    by_sub = defaultdict(lambda: {"threads": 0, "total_comments": 0, "sent_vals": []})
    for kw, entries in keyword_results.items():
        for item in entries:
            sub = item.subreddit or ""
            if not sub:
                continue
            by_sub[sub]["threads"] += 1
            by_sub[sub]["total_comments"] += int(item.comments_count or 0)
            sent = keyword_thread_sentiment.get(kw, {}).get(item.url)
            if sent is not None:
                by_sub[sub]["sent_vals"].append(sent)

    rows = [["subreddit", "threads", "total comments", "avg sentiment"]]
    for sub, a in sorted(by_sub.items(), key=lambda kv: kv[1]["total_comments"], reverse=True)[:20]:
        avg_sent = sum(a["sent_vals"]) / len(a["sent_vals"]) if a["sent_vals"] else 0.0
        rows.append([sub, str(a["threads"]), str(a["total_comments"]), f"{avg_sent:+.2f}"])
    out.append("\nSubreddit aggregates (all keywords):")
    out.append(to_table(rows))

    # Per-keyword thread details
    for kw in KEYWORDS:
        entries = keyword_results.get(kw, [])
        if not entries:
            continue
        out.append(f"\n### Keyword: \"{kw}\"")
        # sort by comments
        sorted_entries = sorted(entries, key=lambda e: (e.comments_count or 0), reverse=True)[:10]
        for item in sorted_entries:
            sent = keyword_thread_sentiment.get(kw, {}).get(item.url)
            sent_s = f"{sent:+.2f}" if sent is not None else "n/a"
            out.append(f"- [{item.comments_count or 0} comments | sent {sent_s}] r/{item.subreddit} — {item.title}")
            out.append(f"  {item.url}")
            details = keyword_thread_details.get(kw, {}).get(item.url)
            if details:
                selftext, top_comms = details
                if selftext:
                    out.append(f"  OP excerpt: {selftext[:200]}...")
                if top_comms:
                    out.append("  Top replies (sample):")
                    for tcm in top_comms[:3]:
                        out.append(f"    - {tcm[:200]}...")
            out.append("")

    out.append("")
    out.append("## How to use this intel")
    out.append("- Study founder posts and their thread replies to see what resonates and how to seed comments.")
    out.append("- Use the keyword samples to see where competitors are discussed and what sentiment exists; position FormBeep accordingly.")
    out.append("- Identify subreddits with high engagement on relevant keywords and plan manual posting using the content packs.")
    out.append("- Always sanity-check the top threads yourself; sentiment is a heuristic.")

    return "\n".join(out) + "\n"


# -------------------- MAIN --------------------

def ensure_logged_in(page) -> None:
    _goto(page, "https://old.reddit.com")
    if "login" in (page.url or "").lower():
        print("\n=== Reddit is asking to log in ===")
        print("Log in in the Chromium window that just opened.")
        print("Then return here and press Enter to continue...")
        input()


def main() -> None:
    print("=" * 60)
    print("Reddit Intel Scanner v2026-04-01-v3")
    print("Features: founder activity + thread sentiment; keywords expanded; selftext + reply samples")
    print("=" * 60)
    print("\nStarting scan...")

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

        try:
            context.storage_state(path=str(STORAGE_STATE_PATH))
        except Exception:
            pass

        # Data collection
        founder_posts: Dict[str, List[ListingItem]] = {}
        founder_comments: Dict[str, List[ListingItem]] = {}
        founder_thread_details: Dict[str, Dict[str, Tuple[str, List[str]]]] = defaultdict(dict)
        founder_thread_sentiment: Dict[str, Dict[str, float]] = defaultdict(dict)

        # Scan founders
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

            # For top posts by comment count, fetch thread details (selftext + top comments)
            top_posts = sorted(founder_posts[u], key=lambda p: (p.comments_count or 0), reverse=True)[:TOP_THREADS_DETAILS_PER_SOURCE]
            for post in top_posts:
                try:
                    selftext, top_comments = scrape_thread_details(page, post.url, MAX_THREAD_COMMENTS_TO_SAMPLE)
                    founder_thread_details[u][post.url] = (selftext, top_comments)
                    s = sentiment_score(analyzer, top_comments)
                    if s is not None:
                        founder_thread_sentiment[u][post.url] = s
                    print(f"    thread details: r/{post.subreddit} ({post.comments_count or 0} comments) -> {s if s is not None else 'n/a'}")
                except Exception as e:
                    print(f"    thread details failed: {post.url} ({e})")

        # Keyword scans
        keyword_results: Dict[str, List[ListingItem]] = {k: [] for k in KEYWORDS}
        keyword_thread_details: Dict[str, Dict[str, Tuple[str, List[str]]]] = {k: {} for k in KEYWORDS}
        keyword_thread_sentiment: Dict[str, Dict[str, float]] = {k: {} for k in KEYWORDS}

        for kw in KEYWORDS:
            # 1) Global query
            global_results = scrape_old_search(page, kw, MAX_KEYWORD_RESULTS_PER_QUERY)

            # 2) Restricted queries inside our target subs (keyword-based, not browsing)
            restricted_results: List[ListingItem] = []
            for sub in TARGET_SUBREDDITS:
                try:
                    restricted_results.extend(scrape_old_search_in_subreddit(page, sub, kw, limit=min(10, MAX_KEYWORD_RESULTS_PER_QUERY)))
                    _sleep_jitter(0.9, extra_max=0.8)
                except Exception as e:
                    print(f"    restricted search failed r/{sub}: {e}")

            # 3) Combine + de-dupe by URL
            combined_by_url: Dict[str, ListingItem] = {}
            for it in (global_results + restricted_results):
                if it.url not in combined_by_url:
                    combined_by_url[it.url] = it
            combined = list(combined_by_url.values())

            keyword_results[kw] = combined
            print(f"  query '{kw}': global={len(global_results)} restricted={len(restricted_results)} unique={len(combined)}")

            # Fetch details for top few threads (by comments) across combined set
            top_results = sorted(combined, key=lambda e: (e.comments_count or 0), reverse=True)[:TOP_THREADS_DETAILS_PER_SOURCE]
            for item in top_results:
                try:
                    _sleep_jitter(1.1, extra_max=1.0)
                    selftext, top_comments = scrape_thread_details(page, item.url, MAX_THREAD_COMMENTS_TO_SAMPLE)
                    keyword_thread_details[kw][item.url] = (selftext, top_comments)
                    s = sentiment_score(analyzer, top_comments)
                    if s is not None:
                        keyword_thread_sentiment[kw][item.url] = s
                    print(f"    thread details: r/{item.subreddit} ({item.comments_count or 0} comments) -> {s if s is not None else 'n/a'}")
                except Exception as e:
                    print(f"    thread details failed: {item.url} ({e})")

        browser.close()

    md = generate_markdown(
        founder_posts,
        founder_comments,
        founder_thread_details,
        founder_thread_sentiment,
        keyword_results,
        keyword_thread_details,
        keyword_thread_sentiment,
    )
    OUTPUT_FILE.write_text(md, encoding="utf-8")
    print(f"\nWrote brief: {OUTPUT_FILE.resolve()}")
    print(f"Saved session state: {STORAGE_STATE_PATH.resolve()} (delete this file to force re-login)")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Reddit intel scanner (browser automation; no API)")
    parser.add_argument("--headless", action="store_true", help="Run Chromium headless")
    parser.add_argument("--auto", action="store_true", help="Auto-select headless if session exists; else interactive (recommended)")
    args = parser.parse_args()

    # --auto overrides --headless and decides based on session file
    if args.auto:
        HEADLESS = STORAGE_STATE_PATH.exists()
        print(f"[auto] Session file {'found' if HEADLESS else 'not found'}; running {'headless' if HEADLESS else 'interactive (login required)'}")
    elif args.headless:
        HEADLESS = True

    main()
