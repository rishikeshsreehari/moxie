#!/usr/bin/env python3
import json
import os
import time
from datetime import datetime, timezone

import requests

SITE_ID = "750e37be-3e04-4672-abe8-a2983afb9a4d"
BASE = "https://api.umami.is/v1"
OUT_JSON = "/root/moxie/products/formbeep/umami-full-data.json"
OUT_MD = "/root/moxie/products/formbeep/analytics-report.md"


def load_key() -> str:
    with open("/opt/data/.env", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("UMAMI_API_KEY="):
                return line.strip().split("=", 1)[1]
    raise RuntimeError("UMAMI_API_KEY not found in /opt/data/.env")


def get(path: str, headers: dict):
    resp = requests.get(f"{BASE}{path}", headers=headers, timeout=20)
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:500]}")
    return resp.json()


def pct_change(now: float, prev: float):
    if prev in (0, None):
        return None
    return (now - prev) / prev * 100


def fmt_pct(v):
    return "N/A" if v is None else f"{v:+.1f}%"


def main():
    key = load_key()
    headers = {"x-umami-api-key": key}

    now = int(time.time()) * 1000
    d7 = now - 7 * 86400000
    d14 = now - 14 * 86400000
    d30 = now - 30 * 86400000
    prior7_start = d14 - 7 * 86400000

    data = {
        "stats_7d": get(f"/websites/{SITE_ID}/stats?startAt={d7}&endAt={now}", headers),
        "stats_30d": get(f"/websites/{SITE_ID}/stats?startAt={d30}&endAt={now}", headers),
        "stats_prior_7d": get(f"/websites/{SITE_ID}/stats?startAt={prior7_start}&endAt={d14}", headers),
        "pageviews_7d_daily": get(f"/websites/{SITE_ID}/pageviews?startAt={d7}&endAt={now}&unit=day&timezone=UTC", headers),
        "pageviews_7d_hourly": get(f"/websites/{SITE_ID}/pageviews?startAt={d7}&endAt={now}&unit=hour&timezone=UTC", headers),
        "metrics_url": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=url&limit=10", headers),
        "metrics_referrer": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=referrer&limit=10", headers),
        "metrics_country": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=country&limit=10", headers),
        "metrics_region": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=region&limit=10", headers),
        "metrics_city": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=city&limit=10", headers),
        "metrics_browser": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=browser&limit=5", headers),
        "metrics_os": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=os&limit=5", headers),
        "metrics_device": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=device&limit=5", headers),
        "metrics_screen": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=screen&limit=5", headers),
        "metrics_language": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=language&limit=10", headers),
        "metrics_title": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=title&limit=10", headers),
        "metrics_event": get(f"/websites/{SITE_ID}/metrics?startAt={d7}&endAt={now}&type=event&limit=10", headers),
        "active": get(f"/websites/{SITE_ID}/active", headers),
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    s7 = data["stats_7d"]
    sp = data["stats_prior_7d"]
    pv_daily = data["pageviews_7d_daily"].get("pageviews", [])
    top_day = max(pv_daily, key=lambda x: x["y"]) if pv_daily else {"x": "N/A", "y": 0}

    report = []
    report.append("# FormBeep Analytics Report")
    report.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    report.append("")
    report.append("## Executive summary")
    report.append(f"- Pageviews: {s7['pageviews']} vs {sp['pageviews']} ({fmt_pct(pct_change(s7['pageviews'], sp['pageviews']))})")
    report.append(f"- Visitors: {s7['visitors']} vs {sp['visitors']} ({fmt_pct(pct_change(s7['visitors'], sp['visitors']))})")
    report.append(f"- Visits: {s7['visits']} vs {sp['visits']} ({fmt_pct(pct_change(s7['visits'], sp['visits']))})")
    report.append(f"- Bounce rate proxy: {s7['bounces']}/{s7['visits']} visits")
    report.append("")
    report.append("## Top pages")
    for item in data["metrics_url"]:
        report.append(f"- {item['x']}: {item['y']}")
    report.append("")
    report.append("## Top referrers")
    for item in data["metrics_referrer"]:
        report.append(f"- {item['x']}: {item['y']}")
    report.append("")
    report.append("## Countries")
    for item in data["metrics_country"]:
        report.append(f"- {item['x']}: {item['y']}")
    report.append("")
    report.append("## Events")
    for item in data["metrics_event"]:
        report.append(f"- {item['x']}: {item['y']}")
    report.append("")
    report.append("## Hourly peak")
    report.append(f"- Peak day: {top_day['x'][:10]} with {top_day['y']} pageviews")
    report.append("")
    report.append("## Raw data files")
    report.append(f"- JSON: {OUT_JSON}")
    report.append(f"- Markdown: {OUT_MD}")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")

    print("OK: Umami pull complete")
    print(f"Pageviews={s7['pageviews']} Visitors={s7['visitors']} Visits={s7['visits']}")
    print(f"Peak day={top_day['x'][:10]} views={top_day['y']}")
    print(f"Report written to {OUT_MD}")


if __name__ == "__main__":
    main()
