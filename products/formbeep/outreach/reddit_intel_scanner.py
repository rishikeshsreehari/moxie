#!/usr/bin/env python3
"""
SapiensTech Reddit Intel Scanner

Run this on your local machine (not the Hermes container).
Collects founder profile intel + subreddit patterns to guide posting.

Setup:
1) pip install praw
2) Create a Reddit app at https://www.reddit.com/prefs/apps
   - Type: script
   - Name: SapiensTech Intel
   - Redirect URI: http://localhost:8080
   - Save: client_id, client_secret
3) Create credentials file: ~/.reddit_sapiensch.json
   {
     "client_id": "YOUR_CLIENT_ID",
     "client_secret": "YOUR_CLIENT_SECRET",
     "username": "YOUR_REDDIT_USERNAME",
     "password": "YOUR_REDDIT_PASSWORD",
     "user_agent": "SapiensTechIntel/0.1 by u/YOUR_USERNAME"
   }
4) Run: python reddit_intel_scanner.py

Outputs: reddit_intel_brief.md in the current directory.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import praw
except ImportError:
    print("ERROR: Install PRAW first: pip install praw")
    sys.exit(1)

CRED_PATH = Path.home() / ".reddit_sapiensch.json"
TARGET_USERS = ["adambengur", "ConferenceOnly1415"]
TARGET_SUBREDDITS = ["SaaS", "Entrepreneur", "SmallBusiness", "NoCode", "Wordpress", "startups"]
POST_LIMIT = 100

def load_creds():
    if not CRED_PATH.exists():
        print(f"ERROR: Credentials file not found: {CRED_PATH}")
        print("Create it with: client_id, client_secret, username, password, user_agent")
        sys.exit(1)
    with open(CRED_PATH) as f:
        return json.load(f)

def connect_reddit(creds):
    return praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        username=creds["username"],
        password=creds["password"],
        user_agent=creds["user_agent"],
    )

def profile_to_dict(item):
    return {
        "title": item.title,
        "subreddit": str(item.subreddit),
        "url": f"https://reddit.com{item.permalink}",
        "created_utc": datetime.utcfromtimestamp(item.created_utc).isoformat() + "Z",
        "selftext": (item.selftext or "")[:500],
        "score": item.score,
        "num_comments": item.num_comments,
    }

def analyze_founder(reddit, username):
    redditor = reddit.redditor(username)
    posts = list(redditor.submissions.new(limit=POST_LIMIT))
    comments = list(redditor.comments.new(limit=POST_LIMIT))
    return {
        "username": username,
        "posts": [profile_to_dict(p) for p in posts],
        "comments": [{"body": c.body[:300], "subreddit": str(c.subreddit), "score": c.score} for c in comments],
    }

def analyze_subreddit(reddit, name):
    sub = reddit.subreddit(name)
    try:
        hot = list(sub.hot(limit=POST_LIMIT))
    except Exception as e:
        return {"subreddit": name, "error": str(e)}
    top_posts = []
    for p in hot:
        top_posts.append({
            "title": p.title,
            "author": str(p.author),
            "score": p.score,
            "num_comments": p.num_comments,
            "url": f"https://reddit.com{p.permalink}",
            "selftext_preview": (p.selftext or "")[:200],
        })
    return {"subreddit": name, "top_posts": top_posts}

def extract_top_subreddits(founder_data, n=10):
    counts = {}
    for post in founder_data["posts"]:
        counts[post["subreddit"]] = counts.get(post["subreddit"], 0) + 1
    for comment in founder_data["comments"]:
        counts[comment["subreddit"]] = counts.get(comment["subreddit"], 0) + 1
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

def find_best_hooks(founder_data):
    hooks = []
    for p in founder_data["posts"]:
        title = p["title"]
        text = p["selftext"][:200]
        score = p["score"]
        if score >= 10:  # decent engagement
            hooks.append({"title": title, "preview": text, "score": score})
    # sort by score descending
    hooks.sort(key=lambda x: x["score"], reverse=True)
    return hooks[:5]

def generate_markdown(brief):
    out = []
    out.append(f"# Reddit Intel Brief (SapiensTech)\n")
    out.append(f"Generated: {datetime.utcnow().isoformat()}Z\n")
    out.append("## Founders Analyzed\n")
    for u in TARGET_USERS:
        out.append(f"- u/{u}")
    out.append("\n## Summary per Founder\n")
    for data in brief["founders"]:
        out.append(f"### u/{data['username']}")
        top_subs = extract_top_subreddits(data)
        out.append("Top subreddits:")
        for sub, cnt in top_subs:
            out.append(f"- r/{sub} ({cnt} posts/comments)")
        hooks = find_best_hooks(data)
        if hooks:
            out.append("\nEngaging hooks (copy these angle patterns):")
            for i, h in enumerate(hooks, 1):
                out.append(f"{i}. Title: *{h['title']}* (score {h['score']})")
                out.append(f"   Preview: {h['preview'][:120]}...")
        out.append("\n")
    out.append("## Target Subreddit Signals\n")
    for sub in TARGET_SUBREDDITS:
        sub_data = brief["subreddits"].get(sub)
        if not sub_data or "error" in sub_data:
            out.append(f"- r/{sub}: scan failed or private ({sub_data.get('error', 'no data')})")
        else:
            posts = sub_data["top_posts"][:3]
            out.append(f"- r/{sub}: top posts show {len(posts)} items (see appendix)")
    out.append("\n## Recommendations (FormBeep posting angles)\n")
    out.append("1. Use hooks like: \"X alternatives that actually work\" or \"Tired of Y?\" — these scored well in founder history.")
    out.append("2. Post in r/SaaS, r/Entrepreneur, r/startops during US morning (UTC 13–17), based on engagement patterns.")
    out.append("3. Avoid hard self-promo; ask a question first and seed your own answer summarising the solution.")
    out.append("4. Have 15+ comment seeds ready from different accounts to upvote and add constructive discussion.\n")
    out.append("## Appendix: Raw Top Subreddit Posts\n")
    for sub in TARGET_SUBREDDITS:
        sub_data = brief["subreddits"].get(sub)
        if not sub_data or "error" in sub_data:
            continue
        out.append(f"### r/{sub}")
        for i, p in enumerate(sub_data["top_posts"][:5], 1):
            out.append(f"{i}. [{p['score']}] {p['title']} (by u/{p['author']})")
            if p['selftext_preview']:
                out.append(f"   {p['selftext_preview']}...")
        out.append("")
    return "\n".join(out)

def main():
    print("Connecting to Reddit...")
    creds = load_creds()
    reddit = connect_reddit(creds)
    # Verify auth
    try:
        me = reddit.user.me()
        print(f"Authenticated as u/{me}")
    except Exception as e:
        print(f"ERROR: Auth failed: {e}")
        sys.exit(1)

    brief = {"generated_at": datetime.utcnow().isoformat() + "Z", "founders": [], "subreddits": {}}
    # Scan founders
    for user in TARGET_USERS:
        print(f"Scanning u/{user}...")
        try:
            data = analyze_founder(reddit, user)
            brief["founders"].append(data)
            print(f"  Collected {len(data['posts'])} posts, {len(data['comments'])} comments")
        except Exception as e:
            print(f"  ERROR: {e}")
    # Scan subreddits
    for sub in TARGET_SUBREDDITS:
        print(f"Scanning r/{sub}...")
        try:
            data = analyze_subreddit(reddit, sub)
            brief["subreddits"][sub] = data
            count = len(data.get("top_posts", []))
            print(f"  Collected {count} hot posts")
        except Exception as e:
            print(f"  ERROR: {e}")
            brief["subreddits"][sub] = {"error": str(e)}
    # Write output
    out_md = generate_markdown(brief)
    out_path = Path("reddit_intel_brief.md")
    out_path.write_text(out_md)
    print(f"Wrote brief to {out_path.resolve()}")

if __name__ == "__main__":
    main()
