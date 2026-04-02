#!/usr/bin/env python3
"""x_founder_tone_audit.py

Local-only script to:
- ingest X/Twitter exports (tweets.js / tweets.csv / generic CSV)
- compute a lightweight "founder tone" fingerprint
- identify what worked (when engagement metrics exist)
- generate a daily reply-guy packet framework (10 replies/day)

No external calls. Standard library only.

Usage examples:
  python3 cmo/scripts/x_founder_tone_audit.py --export tweets.js --out cmo/strategy/x-tone-and-reply-guy-kit.md
  python3 cmo/scripts/x_founder_tone_audit.py --export tweets.csv --out cmo/strategy/x-tone-and-reply-guy-kit.md
  python3 cmo/scripts/x_founder_tone_audit.py --fallback --out cmo/strategy/x-tone-and-reply-guy-kit.md
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import statistics
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional


@dataclass
class Post:
    text: str
    created_at: Optional[str] = None
    likes: Optional[int] = None
    replies: Optional[int] = None
    retweets: Optional[int] = None
    quotes: Optional[int] = None
    impressions: Optional[int] = None
    url: Optional[str] = None

    @property
    def engagement_score(self) -> Optional[float]:
        # Prefer impression-normalized when impressions exist; otherwise a simple weighted sum.
        if self.likes is None and self.replies is None and self.retweets is None and self.quotes is None:
            return None
        likes = self.likes or 0
        replies = self.replies or 0
        rts = self.retweets or 0
        quotes = self.quotes or 0
        raw = likes + 2 * replies + 3 * rts + 2 * quotes
        if self.impressions and self.impressions > 0:
            return raw / self.impressions
        return float(raw)


def _coerce_int(v: Any) -> Optional[int]:
    if v is None:
        return None
    if isinstance(v, int):
        return v
    s = str(v).strip()
    if s == "":
        return None
    try:
        return int(float(s))
    except Exception:
        return None


def load_from_tweets_js(path: Path) -> list[Post]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    # X exports typically look like: window.YTD.tweets.part0 = [ {...}, ... ];
    m = re.search(r"\[(.*)\]", raw, flags=re.S)
    if not m:
        raise ValueError("Could not locate JSON array in tweets.js")
    json_text = "[" + m.group(1) + "]"
    data = json.loads(json_text)

    posts: list[Post] = []
    for item in data:
        # Shape often: {"tweet": {"full_text": "...", "favorite_count": "0", ...}}
        tw = item.get("tweet") if isinstance(item, dict) else None
        if not isinstance(tw, dict):
            continue
        text = tw.get("full_text") or tw.get("text") or ""
        text = str(text).strip()
        if not text:
            continue
        posts.append(
            Post(
                text=text,
                created_at=tw.get("created_at"),
                likes=_coerce_int(tw.get("favorite_count")),
                replies=_coerce_int(tw.get("reply_count")),
                retweets=_coerce_int(tw.get("retweet_count")),
                quotes=_coerce_int(tw.get("quote_count")),
                impressions=_coerce_int(tw.get("impression_count")),
            )
        )
    return posts


def load_from_csv(path: Path) -> list[Post]:
    posts: list[Post] = []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row:
                continue
            # Attempt common column names.
            text = (
                row.get("full_text")
                or row.get("text")
                or row.get("tweet")
                or row.get("Tweet")
                or row.get("content")
                or ""
            )
            text = str(text).strip()
            if not text:
                continue

            posts.append(
                Post(
                    text=text,
                    created_at=row.get("created_at") or row.get("timestamp") or row.get("date"),
                    likes=_coerce_int(row.get("like_count") or row.get("likes") or row.get("favorite_count")),
                    replies=_coerce_int(row.get("reply_count") or row.get("replies")),
                    retweets=_coerce_int(row.get("retweet_count") or row.get("retweets")),
                    quotes=_coerce_int(row.get("quote_count") or row.get("quotes")),
                    impressions=_coerce_int(row.get("impression_count") or row.get("impressions")),
                    url=row.get("url") or row.get("link"),
                )
            )
    return posts


def load_fallback_corpus(repo_root: Path) -> list[Post]:
    """If no X export exists yet, use existing writing as a proxy corpus.

    This is imperfect, but it lets us bootstrap a first-pass tone fingerprint.
    """
    candidates = [
        repo_root / "products/formbeep/outreach/reddit-post-comment-scripts.md",
        repo_root / "products/formbeep/outreach/reddit-posting-tracker.md",
        repo_root / "products/formbeep/reddit/rishi-sentiment.md",
        repo_root / "cmo/strategy/channel-matrix-all-products.md",
    ]
    posts: list[Post] = []
    for p in candidates:
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        # Split into pseudo-post chunks
        chunks = [c.strip() for c in re.split(r"\n\n+|\n\s*-\s+", txt) if c.strip()]
        for c in chunks:
            # Filter out table rows and very short fragments
            if "|" in c and len(c) < 240:
                continue
            if len(c) < 80:
                continue
            posts.append(Post(text=c))
    return posts


def normalize_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"[@#]\w+", " ", s)
    s = re.sub(r"[^a-z0-9\s'\-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tokenize(s: str) -> list[str]:
    s = normalize_text(s)
    if not s:
        return []
    return [t for t in s.split(" ") if t]


def ngrams(tokens: list[str], n: int) -> Iterable[str]:
    if len(tokens) < n:
        return []
    return (" ".join(tokens[i : i + n]) for i in range(0, len(tokens) - n + 1))


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    values_sorted = sorted(values)
    k = (len(values_sorted) - 1) * p
    f = int(k)
    c = min(f + 1, len(values_sorted) - 1)
    if f == c:
        return values_sorted[f]
    d0 = values_sorted[f] * (c - k)
    d1 = values_sorted[c] * (k - f)
    return d0 + d1


def build_report(posts: list[Post], handle: Optional[str] = None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    lengths = [len(p.text) for p in posts]
    tokens_all = []
    for p in posts:
        tokens_all.extend(tokenize(p.text))

    # Hook signals
    q_rate = sum(1 for p in posts if "?" in p.text) / max(1, len(posts))
    num_rate = sum(1 for p in posts if re.search(r"\d", p.text)) / max(1, len(posts))
    i_rate = sum(1 for p in posts if re.search(r"\bI\b", p.text)) / max(1, len(posts))
    you_rate = sum(1 for p in posts if re.search(r"\byou\b", p.text, flags=re.I)) / max(1, len(posts))

    uni = Counter(tokens_all)
    bi = Counter()
    tri = Counter()
    for p in posts:
        t = tokenize(p.text)
        bi.update(ngrams(t, 2))
        tri.update(ngrams(t, 3))

    top_words = [w for (w, _) in uni.most_common(25) if w not in {"the", "and", "to", "a", "of", "in", "for", "on", "is", "it", "that", "with", "as", "this", "be", "are", "was", "i", "you", "we"}][:15]
    top_bi = [w for (w, _) in bi.most_common(15)][:10]
    top_tri = [w for (w, _) in tri.most_common(15)][:7]

    # Performance slice (if we have engagement)
    scored = [p for p in posts if p.engagement_score is not None]
    top_perf: list[Post] = []
    perf_notes = "Engagement metrics not present in corpus; rerun with X export to score what worked." 
    if scored:
        scored_sorted = sorted(scored, key=lambda p: p.engagement_score or 0.0, reverse=True)
        top_perf = scored_sorted[:10]
        perf_notes = "Top posts ranked by engagement_score (weighted; impression-normalized when available)."

    def fmt_post(p: Post, idx: int) -> str:
        score = p.engagement_score
        score_str = "n/a" if score is None else f"{score:.4f}" if p.impressions else f"{score:.0f}"
        snippet = p.text.strip().replace("\n", " ")
        snippet = re.sub(r"\s+", " ", snippet)
        if len(snippet) > 280:
            snippet = snippet[:277] + "..."
        return f"{idx}. (score={score_str}) {snippet}"

    avg_len = statistics.mean(lengths) if lengths else 0
    med_len = statistics.median(lengths) if lengths else 0

    p25 = percentile([float(x) for x in lengths], 0.25)
    p75 = percentile([float(x) for x in lengths], 0.75)

    # Heuristic fingerprint
    fingerprint = []
    if num_rate >= 0.35:
        fingerprint.append("metric-forward / specific numbers")
    if q_rate >= 0.25:
        fingerprint.append("curiosity + question-led")
    if you_rate >= 0.20:
        fingerprint.append("direct address (" + "you" + ")")
    if i_rate >= 0.10:
        fingerprint.append("first-person builder voice")
    if not fingerprint:
        fingerprint.append("neutral / informational")

    # Output as a single founder-ready kit
    lines: list[str] = []
    lines.append(f"# X Founder Tone + Reply-Guy Kit")
    lines.append("")
    lines.append(f"Generated: {now} (UTC)")
    if handle:
        lines.append(f"Handle: {handle}")
    lines.append("")

    lines.append("## 1) Inputs needed (so this becomes accurate)")
    lines.append("- Best: X export file (tweets.js or tweets.csv) with engagement fields (likes/replies/retweets/impressions).")
    lines.append("- If you don’t want to share export: at minimum confirm your handle + a CSV dump of last 90 days with text + likes/replies/retweets.")
    lines.append("")

    lines.append("## 2) What the script found (current corpus)")
    lines.append(f"Posts analyzed: {len(posts)}")
    if lengths:
        lines.append(f"Length (chars): avg={avg_len:.0f}, median={med_len:.0f}, p25={p25:.0f}, p75={p75:.0f}")
    lines.append(f"Hook signals: questions={q_rate:.0%}, numbers={num_rate:.0%}, first-person(I)={i_rate:.0%}, direct-you={you_rate:.0%}")
    lines.append(f"Heuristic tone fingerprint: {', '.join(fingerprint)}")
    lines.append("")

    lines.append("Top recurring words (rough): " + (", ".join(top_words) if top_words else "n/a"))
    lines.append("Top bigrams: " + (", ".join(top_bi) if top_bi else "n/a"))
    lines.append("Top trigrams: " + (", ".join(top_tri) if top_tri else "n/a"))
    lines.append("")

    lines.append("## 3) What worked (needs X export to be definitive)")
    lines.append(perf_notes)
    if top_perf:
        lines.append("")
        for i, p in enumerate(top_perf, start=1):
            lines.append(fmt_post(p, i))
    lines.append("")

    lines.append("## 4) Founder tone tweaks (practical, not cringe)")
    lines.append("Make posts and replies follow one of these three shapes:")
    lines.append("A) Observation → metric → lesson")
    lines.append("B) Mistake → what changed → result")
    lines.append("C) Tactic → who it’s for → exact steps")
    lines.append("")
    lines.append("Rules:")
    lines.append("- One concrete number per post when possible (time, $, %, count).")
    lines.append("- Keep sentences short (aim: 12–18 words).")
    lines.append("- Prefer ‘here’s exactly how’ over ‘excited to announce’.")
    lines.append("- If pitching FormBeep/StackStats: 80% value, 20% link. Links go in follow-up reply.")
    lines.append("")

    lines.append("## 5) Daily ‘reply guy’ workflow (10 replies/day)")
    lines.append("Goal: earn attention + DMs without selling. You’re borrowing distribution.")
    lines.append("")
    lines.append("Daily block (20–30 min):")
    lines.append("1) Pick 3 lanes (rotate): indie SaaS building, SEO/content, ops/analytics.")
    lines.append("2) Find 10 posts in-lane (mix: big accounts + mid-tail builders).")
    lines.append("3) Reply using templates below (2–4 lines).")
    lines.append("4) Log each reply (so we learn what converts).")
    lines.append("")

    lines.append("Reply log format (copy/paste into a note):")
    lines.append("- date | author | tweet_url | lane | reply_type | outcome (likes/replies/dm) | note")
    lines.append("")

    lines.append("## 6) Reply templates (choose based on the tweet)")
    templates = [
        "(Agree + add a missed edge case) ‘Yes — one edge case that bit me: ___. Fix: ___.’",
        "(Mini playbook) ‘If I had to do this today: 1) ___ 2) ___ 3) ___.’",
        "(Operator metric) ‘We saw ___ drop from ___ to ___. The lever was ___.’",
        "(Counterpoint politely) ‘Small disagree: ___ matters less than ___. Because ___.’",
        "(Question that upgrades the thread) ‘Curious: are you optimizing for ___ or ___? That changes the move.’",
        "(Example) ‘Concrete example: ___ (1 sentence). Result: ___.’",
        "(Tool-neutral stack) ‘The stack doesn’t matter; the sequence does: capture → qualify → notify → follow-up.’",
        "(Caution) ‘Watch out for ___ — it creates ___ failure mode.’",
        "(Checklist) ‘Quick checklist: [ ] ___ [ ] ___ [ ] ___.’",
        "(Offer) ‘If you want, I can share a template for ___ — no pitch.’",
    ]
    for i, t in enumerate(templates, start=1):
        lines.append(f"{i}. {t}")
    lines.append("")

    lines.append("## 7) Next step")
    lines.append("Once you drop the X export file, rerun:")
    lines.append("python3 cmo/scripts/x_founder_tone_audit.py --export /path/to/tweets.js --handle @YOURHANDLE --out cmo/strategy/x-tone-and-reply-guy-kit.md")
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", type=str, default=None, help="Path to tweets.js or tweets.csv")
    ap.add_argument("--fallback", action="store_true", help="Use repo corpus fallback (no X export)")
    ap.add_argument("--handle", type=str, default=None, help="X handle (e.g., @rishikeshshari)")
    ap.add_argument("--out", type=str, required=True, help="Output markdown path")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[2]  # /root/moxie_hq

    posts: list[Post] = []

    if args.export:
        p = Path(args.export).expanduser().resolve()
        if not p.exists():
            raise FileNotFoundError(f"Export file not found: {p}")
        if p.suffix.lower() == ".js":
            posts = load_from_tweets_js(p)
        elif p.suffix.lower() == ".csv":
            posts = load_from_csv(p)
        else:
            # try best-effort as text
            txt = p.read_text(encoding="utf-8", errors="ignore")
            posts = [Post(text=t.strip()) for t in txt.splitlines() if t.strip()]

    if (not posts) and args.fallback:
        posts = load_fallback_corpus(repo_root)

    if not posts:
        # still write a helpful stub
        posts = []

    report = build_report(posts, handle=args.handle)
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = (repo_root / out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

    print(f"Wrote: {out_path}")
    print(f"Posts analyzed: {len(posts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
