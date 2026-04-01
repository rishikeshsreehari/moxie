#!/usr/bin/env python3
"""StackStats daily Umami puller.

Writes a small JSON + Markdown summary for yesterday and last 7 days.

Requirements:
- env UMAMI_CLOUD_API_KEY (x-umami-api-key)

Notes:
- Purchases are on Gumroad; this script only monitors traffic. Click events will be added later.
"""

import json
import os
import time
import urllib.request
from datetime import datetime, timedelta, timezone

UMAMI_API_KEY = os.getenv("UMAMI_CLOUD_API_KEY") or os.getenv("UMAMI_API_KEY")
WEBSITE_ID = "52a19925-9bf4-4efe-9a42-ecc2a7f08d81"
BASE = "https://cloud.umami.is/api"

OUT_JSON = "/root/moxie/products/stackstats/analytics/umami-daily.json"
OUT_MD = "/root/moxie/products/stackstats/analytics/umami-daily.md"


def _get(path: str):
    if not UMAMI_API_KEY:
        raise SystemExit("Missing UMAMI_CLOUD_API_KEY env var")
    req = urllib.request.Request(BASE + path)
    req.add_header("x-umami-api-key", UMAMI_API_KEY)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    now = datetime.now(timezone.utc)
    end = int(now.timestamp() * 1000)
    start_7d = int((now - timedelta(days=7)).timestamp() * 1000)
    start_1d = int((now - timedelta(days=1)).timestamp() * 1000)

    # Basic stats
    stats_7d = _get(f"/websites/{WEBSITE_ID}/stats?startAt={start_7d}&endAt={end}")
    stats_1d = _get(f"/websites/{WEBSITE_ID}/stats?startAt={start_1d}&endAt={end}")

    # Top referrers (7d)
    ref_7d = _get(f"/websites/{WEBSITE_ID}/metrics?type=referrer&startAt={start_7d}&endAt={end}")

    payload = {
        "generated_at": now.isoformat(),
        "range": {"start_7d": start_7d, "start_1d": start_1d, "end": end},
        "stats_7d": stats_7d,
        "stats_1d": stats_1d,
        "referrers_7d": ref_7d[:10],
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    def _md_stats(title, s):
        return (
            f"## {title}\n"
            f"- pageviews: {s.get('pageviews', {}).get('value')}\n"
            f"- visitors: {s.get('visitors', {}).get('value')}\n"
            f"- visits: {s.get('visits', {}).get('value')}\n"
            f"- bounces: {s.get('bounces', {}).get('value')}\n"
            f"- totaltime: {s.get('totaltime', {}).get('value')}\n"
        )

    lines = [
        "# StackStats — Umami daily\n",
        f"Generated: {now.isoformat()}\n",
        _md_stats("Last 24h", stats_1d),
        _md_stats("Last 7d", stats_7d),
        "## Top referrers (7d)\n",
    ]

    for r in ref_7d[:10]:
        lines.append(f"- {r.get('x')}: {r.get('y')}\n")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("OK")


if __name__ == "__main__":
    main()
