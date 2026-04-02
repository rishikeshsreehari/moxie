#!/usr/bin/env python3
"""
Reddit History Crosscheck for u/rishikeshshari

Given a list of subreddits, check whether the user has posted or commented in each
subreddit recently. Uses Reddit's public RSS feeds (no authentication required).

Output format: Plain text report
  Subreddit: r/example
  Status: ACTIVE (or NO_ACTIVITY)
  Last activity: 2026-04-01T12:34:56Z
  Recent URLs:
    - https://reddit.com/r/example/comments/...
    - ...

Usage:
  cat subreddits.txt | python3 reddit_history_check.py > report.txt
  python3 reddit_history_check.py --subreddits "askreddit,programming" > report.txt
"""

import argparse
import json
import sys
import time
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any, Optional
import re
import requests
import xml.etree.ElementTree as ET

USERNAME = "rishikeshshari"
REDDIT_RSS_COMMENTS = f"https://www.reddit.com/user/{USERNAME}/comments/.rss"
REDDIT_RSS_SUBMITTED = f"https://www.reddit.com/user/{USERNAME}/submitted/.rss"
USER_AGENT = "SapiensTech/1.0 (HQ internal ops script; contact: hello@formbeep.com)"
REQUEST_TIMEOUT = 15
RATE_LIMIT_DELAY = 1.0
MAX_DAYS_LOOKBACK = 180

NS = {"atom": "http://www.w3.org/2005/Atom", "reddit": "http://www.reddit.com/rss/1.0/mod/"}


def load_subreddits() -> List[str]:
    parser = argparse.ArgumentParser(description="Check Reddit posting history for specific subreddits")
    parser.add_argument("--subreddits", type=str, help="Comma-separated list of subreddit names", default=None)
    args = parser.parse_args()
    if args.subreddits:
        subs = [s.strip().replace("r/", "").replace("/", "") for s in args.subreddits.split(",") if s.strip()]
    else:
        subs = [line.strip().replace("r/", "").replace("/", "") for line in sys.stdin if line.strip()]
    seen = set()
    unique = []
    for sub in subs:
        sub_lower = sub.lower()
        if sub_lower and sub_lower not in seen:
            seen.add(sub_lower)
            unique.append(sub)
    return unique


def fetch_rss(url: str) -> Optional[ET.Element]:
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        if resp.status_code == 429:
            print(f"WARNING: Rate limited ({url}). Waiting...", file=sys.stderr)
            time.sleep(5)
            return None
        elif resp.status_code != 200:
            print(f"WARNING: HTTP {resp.status_code} from {url}", file=sys.stderr)
            return None
        # Parse XML
        return ET.fromstring(resp.content)
    except Exception as e:
        print(f"ERROR: Failed to fetch/parse {url}: {e}", file=sys.stderr)
        return None


def extract_entries(root: ET.Element) -> List[Dict[str, Any]]:
    entries = []
    for entry in root.findall(".//atom:entry", NS):
        # Extract subreddit from the 'reddit:subreddit' element or from the link
        sub_elem = entry.find("reddit:subreddit", NS)
        sub_name = sub_elem.text.lower() if sub_elem is not None else None

        # Published date
        published_elem = entry.find("atom:published", NS)
        published = published_elem.text if published_elem is not None else None
        # Convert to timestamp approx
        created_utc = None
        if published:
            try:
                dt = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
                created_utc = dt.timestamp()
            except ValueError:
                try:
                    dt = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                    created_utc = dt.timestamp()
                except ValueError:
                    created_utc = 0

        # Link (permalink)
        link_elem = entry.find("atom:link[@rel='alternate']", NS)
        if link_elem is None:
            link_elem = entry.find("atom:link", NS)
        url = link_elem.get("href") if link_elem is not None else ""

        # Title or body
        title_elem = entry.find("atom:title", NS)
        title = title_elem.text if title_elem is not None else ""
        content_elem = entry.find("atom:content", NS)
        body = content_elem.text if content_elem is not None else ""

        entries.append({
            "subreddit": sub_name,
            "created_utc": created_utc,
            "url": url,
            "title": title[:100] if title else "",
            "body": body[:100] if body else "",
            "kind": "comment" if "/comments/" in url and body else "post"
        })
    return entries


def build_activity_profile() -> Dict[str, List[Dict[str, Any]]]:
    """Fetch both RSS feeds and build subreddit->list index."""
    profile: Dict[str, List[Dict[str, Any]]] = {}

    for feed_name, url in [("comments", REDDIT_RSS_COMMENTS), ("submitted", REDDIT_RSS_SUBMITTED)]:
        print(f"Fetching {feed_name} RSS...", file=sys.stderr)
        root = fetch_rss(url)
        if root is None:
            continue

        entries = extract_entries(root)
        for entry in entries:
            sub = entry["subreddit"]
            if not sub:
                continue
            if sub not in profile:
                profile[sub] = []
            profile[sub].append(entry)

        time.sleep(RATE_LIMIT_DELAY)

    # Sort each subreddit's list by created_utc descending
    for sub in profile:
        profile[sub].sort(key=lambda x: x["created_utc"], reverse=True)
    return profile


def check_subreddits(subreddits: List[str], profile: Dict[str, List[Dict[str, Any]]]) -> str:
    lines = []
    lines.append(f"Reddit History Report for u/{USERNAME}")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"Checked subreddits: {len(subreddits)}")
    lines.append(f"Lookback period: RSS feed (all available)")
    lines.append("=" * 60)
    lines.append("")

    has_activity = 0
    no_activity = 0

    cutoff_time = (datetime.now(timezone.utc) - timedelta(days=MAX_DAYS_LOOKBACK)).timestamp()

    for sub in subreddits:
        sub_lower = sub.lower().replace("r/", "")
        lines.append(f"Subreddit: r/{sub_lower}")

        items = profile.get(sub_lower, [])

        # Filter to recent enough (RSS may include all history)
        recent = [it for it in items if it["created_utc"] >= cutoff_time]

        if not recent:
            lines.append("Status: NO_ACTIVITY")
            lines.append("")
            no_activity += 1
            continue

        latest = recent[0]
        latest_dt = datetime.fromtimestamp(latest["created_utc"], tz=timezone.utc)
        lines.append(f"Status: ACTIVE")
        lines.append(f"Last activity: {latest_dt.isoformat()}")
        lines.append("Recent URLs:")
        for item in recent[:5]:
            lines.append(f"  - {item['url']}")
            if item.get("title"):
                lines.append(f"    Title: {item['title']}")
            if item.get("body"):
                body = item['body'].replace('\n', ' ').strip()
                lines.append(f"    Comment: {body}...")
        lines.append("")
        has_activity += 1

    lines.append("=" * 60)
    lines.append(f"Summary: {has_activity} subreddits with activity, {no_activity} with no activity")

    return "\n".join(lines)


def main():
    subreddits = load_subreddits()
    if not subreddits:
        print("ERROR: No subreddits provided. Pass via --subreddits or pipe list via stdin.", file=sys.stderr)
        sys.exit(1)

    print(f"Checking {len(subreddits)} subreddits for u/{USERNAME}...", file=sys.stderr)
    profile = build_activity_profile()
    report = check_subreddits(subreddits, profile)
    print(report)


if __name__ == "__main__":
    main()
