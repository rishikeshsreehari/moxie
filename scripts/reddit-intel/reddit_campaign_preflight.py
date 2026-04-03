#!/usr/bin/env python3
"""Reddit campaign preflight intel (browser automation, no API)

Purpose (Rishi requirement): for each target subreddit, gather FOUR things BEFORE drafting/posting:
  1) What ME (u/<me>) has posted/commented in that subreddit recently
  2) What 2 competitors have posted/commented in that subreddit recently
  3) Top performing posts of the week in that subreddit
  4) The subreddit rules

This uses Playwright against old.reddit.com / www.reddit.com and works without Reddit API.
It is read-only and does NOT post.

Run (from this folder):
  python3 -m pip install -r requirements.txt
  playwright install chromium

  python3 reddit_campaign_preflight.py \
    --subreddits microsaas buildinpublic \
    --me rishikeshshari \
    --competitors adambengur ConferenceOnly1415 \
    --out reddit_campaign_preflight.md

Notes:
- First run may require manual login; we reuse reddit_storage_state.json if present.
- If Reddit shows a bot wall/captcha, run with --headed and complete the challenge.
"""

from __future__ import annotations

import argparse
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
STORAGE_STATE = HERE / "reddit_storage_state.json"

OLD = "https://old.reddit.com"
NEW = "https://www.reddit.com"


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def _md(s: str) -> str:
    # minimal markdown escaping for pipes
    return (s or "").replace("|", "\\|")


def _now_utc() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")


@dataclass
class PostRow:
    title: str
    subreddit: str
    score: str
    comments: str
    url: str


@dataclass
class CommentRow:
    subreddit: str
    score: str
    snippet: str
    url: str


def ensure_login(page, headed: bool):
    # We don't force login; we just make sure pages load. If user is logged out,
    # the script still often works. If a wall shows up, we pause in headed mode.
    page.goto(f"{OLD}/", wait_until="domcontentloaded")
    time.sleep(1.2)
    html = page.content().lower()
    if "log in" in html and "sign up" in html and headed:
        # Not necessarily blocked, but give a quick chance to login.
        # User can just close the login modal and continue.
        pass


def parse_listing_posts(page) -> List[PostRow]:
    rows: List[PostRow] = []
    # old reddit listing items
    items = page.locator("div.thing")
    n = items.count()
    for i in range(min(n, 50)):
        it = items.nth(i)
        try:
            title = _clean(it.locator("a.title").first.inner_text(timeout=2000))
        except Exception:
            continue
        sub = _clean(it.get_attribute("data-subreddit") or "")
        score = _clean(it.locator("div.score.unvoted").first.inner_text(timeout=2000))
        if not score or score == "•":
            score = _clean(it.locator("div.score").first.inner_text(timeout=2000))
        try:
            comments = _clean(it.locator("a.comments").first.inner_text(timeout=2000))
        except Exception:
            comments = ""
        try:
            href = it.locator("a.comments").first.get_attribute("href")
        except Exception:
            href = None
        if href and href.startswith("/"):
            url = f"https://reddit.com{href}"
        elif href:
            url = href
        else:
            # fallback to title link
            tl = it.locator("a.title").first.get_attribute("href")
            url = tl if tl and tl.startswith("http") else f"https://reddit.com{tl or ''}"
        rows.append(PostRow(title=title, subreddit=sub, score=score, comments=comments, url=url))
    return rows


def parse_listing_comments(page) -> List[CommentRow]:
    rows: List[CommentRow] = []
    items = page.locator("div.thing")
    n = items.count()
    for i in range(min(n, 80)):
        it = items.nth(i)
        sub = _clean(it.get_attribute("data-subreddit") or "")
        try:
            score = _clean(it.locator("span.score").first.inner_text(timeout=2000))
        except Exception:
            score = ""
        try:
            snippet = _clean(it.locator("div.md").first.inner_text(timeout=2000))[:240]
        except Exception:
            snippet = ""
        try:
            href = it.locator("a.bylink").first.get_attribute("href")
        except Exception:
            href = None
        if href and href.startswith("/"):
            url = f"https://reddit.com{href}"
        else:
            url = href or ""
        if sub:
            rows.append(CommentRow(subreddit=sub, score=score, snippet=snippet, url=url))
    return rows


def _next_button_href(page) -> Optional[str]:
    """Return the old.reddit next-page URL if present."""
    try:
        href = page.locator("span.next-button a").first.get_attribute("href", timeout=1500)
        if href:
            return href
    except Exception:
        return None
    return None


def subreddit_author_posts(page, subreddit: str, username: str, limit_pages: int = 2) -> List[PostRow]:
    """Fetch recent posts by author within a subreddit using subreddit search.

    Aligns with the requirement: check activity *in that subreddit*, not just profiles.
    Reddit search is imperfect but catches older posts when profile paging fails.
    """
    rows: List[PostRow] = []
    q = f"author%3A{username}"
    url = f"{OLD}/r/{subreddit}/search?q={q}&restrict_sr=on&sort=new&t=all"
    for _ in range(limit_pages):
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(1.3)
        for r in parse_listing_posts(page):
            # search results often omit data-subreddit; force it
            rows.append(PostRow(title=r.title, subreddit=subreddit, score=r.score, comments=r.comments, url=r.url))
        if len(rows) >= 12:
            break
        nxt = _next_button_href(page)
        if not nxt:
            break
        url = nxt
    return rows[:12]


def user_activity_in_sub(page, username: str, subreddit: str, limit_pages: int = 4) -> Dict[str, List]:
    """Activity for a user within a specific subreddit.

    Posts: subreddit-scoped search (author:<user> within r/<sub>) + fallback profile scan.
    Comments: profile scan filtered by subreddit.

    Fix: old paging logic used a blank `after=` token and re-read page 1.
    """
    sub_l = subreddit.lower()

    # 1) Posts: subreddit-scoped search (matches requirement)
    posts: List[PostRow] = subreddit_author_posts(page, subreddit, username, limit_pages=2)

    # 1b) Fallback: profile scan for posts, filtered by subreddit
    if len(posts) < 6:
        url = f"{OLD}/user/{username}/submitted/?sort=new"
        for _ in range(limit_pages):
            page.goto(url, wait_until="domcontentloaded")
            time.sleep(1.2)
            for row in parse_listing_posts(page):
                if row.subreddit and row.subreddit.lower() == sub_l:
                    posts.append(row)
            if len(posts) >= 12:
                break
            nxt = _next_button_href(page)
            if not nxt:
                break
            url = nxt

    # 2) Comments: profile scan (Reddit doesn't reliably provide comment search)
    comments: List[CommentRow] = []
    url = f"{OLD}/user/{username}/comments/?sort=new"
    for _ in range(limit_pages):
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(1.2)
        for row in parse_listing_comments(page):
            if row.subreddit and row.subreddit.lower() == sub_l:
                comments.append(row)
        if len(comments) >= 12:
            break
        nxt = _next_button_href(page)
        if not nxt:
            break
        url = nxt

    # Dedup posts by URL (search + profile may overlap)
    seen = set()
    dedup_posts: List[PostRow] = []
    for p in posts:
        if p.url and p.url not in seen:
            seen.add(p.url)
            dedup_posts.append(p)

    return {"posts": dedup_posts[:12], "comments": comments[:12]}


def top_posts_week(page, subreddit: str) -> List[PostRow]:
    # old reddit top page supports t=week
    url = f"{OLD}/r/{subreddit}/top/?t=week"
    page.goto(url, wait_until="domcontentloaded")
    time.sleep(1.5)
    rows = parse_listing_posts(page)
    # Some items may have empty data-subreddit; set it.
    fixed = []
    for r in rows[:12]:
        fixed.append(PostRow(title=r.title, subreddit=subreddit, score=r.score, comments=r.comments, url=r.url))
    return fixed


def subreddit_rules(page, subreddit: str) -> List[str]:
    # rules are more reliable on new reddit route
    url = f"{NEW}/r/{subreddit}/about/rules"
    page.goto(url, wait_until="domcontentloaded")
    time.sleep(1.8)

    # Try multiple selectors (Reddit changes markup)
    rules: List[str] = []

    # Attempt: headings + adjacent text
    candidates = page.locator("h3")
    for i in range(min(candidates.count(), 30)):
        h = _clean(candidates.nth(i).inner_text(timeout=1000))
        if not h:
            continue
        # heuristically select rule-looking headers
        if re.search(r"rule", h, re.I) or re.match(r"^\d+\.", h):
            rules.append(h)

    # Fallback: old reddit sidebar rules text
    if not rules:
        page.goto(f"{OLD}/r/{subreddit}/about/rules", wait_until="domcontentloaded")
        time.sleep(1.4)
        text = _clean(page.inner_text("body")[:5000])
        # naive split
        for m in re.finditer(r"Rule\s*\d+[:\-]\s*([^\.]{5,120})", text, re.I):
            rules.append(m.group(1))

    # Dedup
    seen = set()
    out = []
    for r in rules:
        r = _clean(r)
        if r and r not in seen:
            seen.add(r)
            out.append(r)
    return out[:20]


def render_md(subreddits: List[str], me: str, competitors: List[str], data: dict) -> str:
    lines = []
    lines.append(f"# Reddit Campaign Preflight (generated {_now_utc()})")
    lines.append("")
    lines.append(f"Me: u/{me}")
    if competitors:
        lines.append("Competitors: " + ", ".join([f"u/{c}" for c in competitors]))
    else:
        lines.append("Competitors: (none provided)")
    lines.append("")

    for s in subreddits:
        lines.append("---")
        lines.append("")
        lines.append(f"## r/{s}")
        lines.append("")

        # Rules
        lines.append("### Rules")
        rules = data[s]["rules"]
        if rules:
            for r in rules:
                lines.append(f"- {_md(r)}")
        else:
            lines.append("- (could not fetch rules reliably; open /about/rules manually)")
        lines.append("")

        # Top posts
        lines.append("### Top posts (week)")
        tops = data[s]["top_week"]
        if tops:
            for i, p in enumerate(tops, 1):
                lines.append(f"{i}. ({_md(p.score)} / {_md(p.comments)}) {_md(p.title)[:160]} — {p.url}")
        else:
            lines.append("- (no top posts found)")
        lines.append("")

        # Me activity
        lines.append(f"### My recent activity in r/{s} (u/{me})")
        mine = data[s]["me"]
        if not mine["posts"] and not mine["comments"]:
            lines.append("- None found in scan window.")
        else:
            if mine["posts"]:
                lines.append("Posts:")
                for p in mine["posts"]:
                    lines.append(f"- ({_md(p.score)} / {_md(p.comments)}) {_md(p.title)[:160]} — {p.url}")
            if mine["comments"]:
                lines.append("Comments:")
                for c in mine["comments"]:
                    lines.append(f"- ({_md(c.score)}) {_md(c.snippet)} — {c.url}")
        lines.append("")

        # Competitors activity
        lines.append(f"### Competitor activity in r/{s}")
        for comp in competitors:
            lines.append(f"#### u/{comp}")
            d = data[s]["competitors"].get(comp)
            if not d or (not d["posts"] and not d["comments"]):
                lines.append("- None found in scan window.")
            else:
                if d["posts"]:
                    lines.append("Posts:")
                    for p in d["posts"]:
                        lines.append(f"- ({_md(p.score)} / {_md(p.comments)}) {_md(p.title)[:160]} — {p.url}")
                if d["comments"]:
                    lines.append("Comments:")
                    for c in d["comments"]:
                        lines.append(f"- ({_md(c.score)}) {_md(c.snippet)} — {c.url}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Interpretation notes")
    lines.append("- If you posted recently in a subreddit: do comments instead of a new post.")
    lines.append("- If rules prohibit promo/links: keep it discussion-only; no product link.")
    lines.append("- Use top posts for format/tone; avoid copying competitor angles.")
    lines.append("")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subreddits", nargs="+", required=True)
    ap.add_argument("--me", required=True)
    ap.add_argument("--competitors", nargs="*", default=[], help="Optional list of competitor usernames to scan within each subreddit")
    ap.add_argument("--out", default="reddit_campaign_preflight.md")
    ap.add_argument("--headed", action="store_true", help="Run with visible browser")
    args = ap.parse_args()

    out_path = Path(args.out)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headed)
        context = browser.new_context(storage_state=str(STORAGE_STATE) if STORAGE_STATE.exists() else None)
        page = context.new_page()

        ensure_login(page, headed=args.headed)

        all_data = {}
        for s in args.subreddits:
            all_data[s] = {"rules": [], "top_week": [], "me": None, "competitors": {}}
            all_data[s]["rules"] = subreddit_rules(page, s)
            all_data[s]["top_week"] = top_posts_week(page, s)
            all_data[s]["me"] = user_activity_in_sub(page, args.me, s)
            for c in args.competitors:
                all_data[s]["competitors"][c] = user_activity_in_sub(page, c, s)

        # Save storage state for next time
        try:
            context.storage_state(path=str(STORAGE_STATE))
        except Exception:
            pass

        md = render_md(args.subreddits, args.me, args.competitors, all_data)
        out_path.write_text(md, encoding="utf-8")
        print(f"OK: wrote {out_path.resolve()}")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
