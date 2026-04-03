#!/usr/bin/env python3
"""FormBeep Reddit Campaign Intel (laptop-run)

Goal (per Rishi): before drafting any Reddit execution packet, gather FOUR things for each target subreddit:
  1) What *you* (u/<me>) have posted/commented in that subreddit recently
  2) What our 2 competitors have posted/commented in that subreddit recently
  3) Top performing posts of the week in that subreddit
  4) Subreddit rules

This script is read-only. It does NOT post.

DEPRECATED: Reddit API/PRAW path is no longer the recommended approach.
Use the browser-automation scripts in the main repo instead:
  /root/moxie_hq/scripts/reddit-intel/reddit_campaign_preflight.py
  /root/moxie_hq/scripts/reddit-intel/reddit_intel_scanner_browser.py

Prereqs (browser automation):
  python3 -m pip install -r /root/moxie_hq/scripts/reddit-intel/requirements.txt
  playwright install chromium

Example:
  python3 reddit_campaign_intel.py \
    --subreddits microsaas buildinpublic \
    --me rishikeshshari \
    --competitors adambengur ConferenceOnly1415 \
    --out reddit_campaign_intel.md

Outputs a markdown report you can paste into the execution packet.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    import praw
except ImportError:
    print("ERROR: PRAW not installed. Run: python3 -m pip install --upgrade praw")
    sys.exit(1)

DEFAULT_CRED_PATH = Path.home() / ".reddit_sapiensch.json"


def _utc(ts: float) -> str:
    return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")


def load_creds(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Credentials file not found: {path}")
    return json.loads(path.read_text())


def connect_reddit(creds: dict):
    return praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        username=creds["username"],
        password=creds["password"],
        user_agent=creds["user_agent"],
    )


def md_escape(s: str) -> str:
    return (s or "").replace("\n", " ").strip()


def item_url(item) -> str:
    return f"https://reddit.com{item.permalink}"


def get_rules(sub) -> list[dict]:
    rules_out = []
    try:
        for r in sub.rules:
            rules_out.append({
                "short_name": getattr(r, "short_name", ""),
                "description": getattr(r, "description", ""),
                "kind": getattr(r, "kind", ""),
            })
    except Exception as e:
        rules_out.append({"short_name": "ERROR", "description": str(e), "kind": ""})
    return rules_out


def recent_user_activity_in_sub(reddit, username: str, subreddit: str, limit: int = 200, keep: int = 7) -> dict:
    u = reddit.redditor(username)

    posts = []
    for p in u.submissions.new(limit=limit):
        if str(p.subreddit).lower() == subreddit.lower():
            posts.append({
                "date": _utc(p.created_utc),
                "title": p.title,
                "score": p.score,
                "comments": p.num_comments,
                "url": item_url(p),
            })
        if len(posts) >= keep:
            break

    comments = []
    for c in u.comments.new(limit=limit):
        if str(c.subreddit).lower() == subreddit.lower():
            comments.append({
                "date": _utc(c.created_utc),
                "score": c.score,
                "body": c.body[:240],
                "url": item_url(c),
            })
        if len(comments) >= keep:
            break

    return {"username": username, "posts": posts, "comments": comments}


def top_posts_week(sub, limit: int = 12) -> list[dict]:
    out = []
    try:
        for p in sub.top(time_filter="week", limit=limit):
            out.append({
                "title": p.title,
                "author": str(p.author),
                "score": p.score,
                "comments": p.num_comments,
                "date": _utc(p.created_utc),
                "url": item_url(p),
            })
    except Exception as e:
        out.append({"title": f"ERROR: {e}", "author": "", "score": 0, "comments": 0, "date": "", "url": ""})
    return out


def render_report(reddit, subreddits: list[str], me: str, competitors: list[str]) -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")
    lines = []
    lines.append(f"# Reddit Campaign Intel (generated {now})")
    lines.append("")
    lines.append(f"Me: u/{me}")
    lines.append("Competitors: " + ", ".join([f"u/{c}" for c in competitors]))
    lines.append("")

    for s in subreddits:
        sub = reddit.subreddit(s)
        lines.append("---")
        lines.append("")
        lines.append(f"## r/{s}")
        lines.append("")

        # 4) Rules
        lines.append("### Rules")
        rules = get_rules(sub)
        for r in rules:
            name = md_escape(r.get("short_name", ""))
            desc = md_escape(r.get("description", ""))
            if name == "ERROR":
                lines.append(f"- ERROR fetching rules: {desc}")
            else:
                lines.append(f"- {name}: {desc}")
        lines.append("")

        # 3) Top posts of the week
        lines.append("### Top posts (week)")
        tops = top_posts_week(sub)
        for i, p in enumerate(tops, 1):
            title = md_escape(p["title"])[:140]
            lines.append(f"{i}. ({p['score']}↑ / {p['comments']}c) {title} — u/{p['author']} — {p['date']} — {p['url']}")
        lines.append("")

        # 1) Me activity
        lines.append(f"### My recent activity in r/{s} (u/{me})")
        mine = recent_user_activity_in_sub(reddit, me, s)
        if not mine["posts"] and not mine["comments"]:
            lines.append("- No recent posts/comments found in this subreddit within scan limits.")
        else:
            if mine["posts"]:
                lines.append("Posts:")
                for p in mine["posts"]:
                    lines.append(f"- ({p['date']}) ({p['score']}↑ / {p['comments']}c) {md_escape(p['title'])[:140]} — {p['url']}")
            if mine["comments"]:
                lines.append("Comments:")
                for c in mine["comments"]:
                    lines.append(f"- ({c['date']}) ({c['score']}↑) {md_escape(c['body'])} — {c['url']}")
        lines.append("")

        # 2) Competitors activity
        lines.append(f"### Competitor activity in r/{s}")
        for comp in competitors:
            data = recent_user_activity_in_sub(reddit, comp, s)
            lines.append(f"#### u/{comp}")
            if not data["posts"] and not data["comments"]:
                lines.append("- No recent posts/comments found in this subreddit within scan limits.")
            else:
                if data["posts"]:
                    lines.append("Posts:")
                    for p in data["posts"]:
                        lines.append(f"- ({p['date']}) ({p['score']}↑ / {p['comments']}c) {md_escape(p['title'])[:140]} — {p['url']}")
                if data["comments"]:
                    lines.append("Comments:")
                    for c in data["comments"]:
                        lines.append(f"- ({c['date']}) ({c['score']}↑) {md_escape(c['body'])} — {c['url']}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## How to use this")
    lines.append("- If rules forbid promo/links: switch to pure discussion post + no link (or comment-only).")
    lines.append("- If you posted recently in this sub: avoid posting again; do comments instead.")
    lines.append("- Reuse hooks from top posts (format + tone), not the exact content.")
    lines.append("- Use competitor activity to avoid copying their angle; differentiate.")
    lines.append("")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cred", default=str(DEFAULT_CRED_PATH), help="Path to ~/.reddit_sapiensch.json")
    ap.add_argument("--subreddits", nargs="+", required=True, help="List of subreddit names (no r/ prefix)")
    ap.add_argument("--me", required=True, help="Your Reddit username")
    ap.add_argument("--competitors", nargs="+", required=True, help="Competitor Reddit usernames")
    ap.add_argument("--out", default="reddit_campaign_intel.md", help="Output markdown path")
    args = ap.parse_args()

    cred_path = Path(args.cred).expanduser()
    out_path = Path(args.out)

    creds = load_creds(cred_path)
    reddit = connect_reddit(creds)

    md = render_report(reddit, args.subreddits, args.me, args.competitors)
    out_path.write_text(md)
    print(f"OK: wrote {out_path.resolve()}")


if __name__ == "__main__":
    main()
