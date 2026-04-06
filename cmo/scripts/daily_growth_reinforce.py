#!/usr/bin/env python3
"""Daily growth reinforcement loop (Paperclip-lite).

Outputs:
- Updates /root/moxie_hq/cmo/reports/growth_log.md (append-only)
- Updates /root/moxie_hq/cmo/rishi_review.md (only if founder action required)

Alerting contract for cron:
- Print exactly '[SILENT]' if no founder action required and no noteworthy deltas
- Otherwise print a short changelog

This script is intentionally small and dependency-light.
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = Path("/root/moxie_hq")
CMO = BASE / "cmo"
LOG = CMO / "reports/growth_log.md"
REVIEW = CMO / "rishi_review.md"
ENV_PATH = Path("/opt/data/.env")
CACHE = Path("/opt/data/cache/daily_growth_state.json")
UMAMI_RAW = Path("/opt/data/cache/umami_pull_latest.json")

FORM = "750e37be-3e04-4672-abe8-a2983afb9a4d"
STACK = "52a19925-9bf4-4efe-9a42-ecc2a7f08d81"


def load_env():
    if not ENV_PATH.exists():
        return {}
    out = {}
    for line in ENV_PATH.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def umami_pull(site_id: str, days: int, key: str):
    base = "https://api.umami.is/v1"
    headers = {"Authorization": f"Bearer {key}"}

    now_s = int(time.time())
    now_ms = now_s * 1000
    start_ms = now_ms - days * 86400 * 1000

    r = requests.get(
        f"{base}/websites/{site_id}/stats",
        headers=headers,
        params={"startAt": start_ms, "endAt": now_ms},
        timeout=20,
    )
    r.raise_for_status()
    stats = r.json()

    def metrics(type_, metric, limit=10):
        rr = requests.get(
            f"{base}/websites/{site_id}/metrics",
            headers=headers,
            params={"startAt": start_ms, "endAt": now_ms, "type": type_, "metric": metric, "limit": limit},
            timeout=20,
        )
        rr.raise_for_status()
        return rr.json()

    return {
        "window_days": days,
        "unit": "ms",
        "stats": stats,
        "top_urls": metrics("url", "pageviews", 10),
        "top_referrers": metrics("referrer", "visitors", 10),
        "top_events": metrics("event", "count", 30),
    }


def load_state():
    if not CACHE.exists():
        return {}
    try:
        return json.loads(CACHE.read_text())
    except Exception:
        return {}


def save_state(state):
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(state, indent=2))


def append_log(md: str):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# Growth Log (daily)\n\n", encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(md)


def main():
    env = load_env()
    key = env.get("UMAMI_API_KEY")
    if not key:
        # This is ops, not founder-blocker.
        print("ERROR: UMAMI_API_KEY missing")
        return 1

    state = load_state()
    now = datetime.now(timezone.utc)

    data = {
        "generated_utc": now.isoformat(),
        "formbeep_7d": umami_pull(FORM, 7, key),
        "stackstats_7d": umami_pull(STACK, 7, key),
    }
    UMAMI_RAW.parent.mkdir(parents=True, exist_ok=True)
    UMAMI_RAW.write_text(json.dumps(data, ensure_ascii=False))

    # Compute simple deltas vs last run
    def kpi(block):
        s = block["stats"]
        return {
            "pageviews": s.get("pageviews", 0),
            "visitors": s.get("visitors", 0),
            "visits": s.get("visits", 0),
        }

    fb = kpi(data["formbeep_7d"])
    ss = kpi(data["stackstats_7d"])

    prev_fb = state.get("formbeep_7d")
    prev_ss = state.get("stackstats_7d")

    changed = False
    if prev_fb != fb or prev_ss != ss:
        changed = True

    # Append to growth log (always)
    append_log(
        "\n".join(
            [
                f"\n## {now.date().isoformat()} (UTC)\n",
                f"- FormBeep 7d: {fb}\n",
                f"- StackStats 7d: {ss}\n",
                "",
                "Next actions (auto):",
                "- If FormBeep visitors rising but no signups: add 1 stronger CTA + event tracking.",
                "- If StackStats visitors rising: run the teardown outbound tonight.",
                "",
            ]
        )
    )

    # Founder attention: only if issues_rishi has open items (notify_issues handles actual ping)
    issues_text = (CMO / "issues_rishi.md").read_text(encoding="utf-8", errors="replace")
    founder_blocked = "## Open" in issues_text and "(no open founder blockers)" not in issues_text.lower()

    # Save new state
    state["last_run_utc"] = now.isoformat()
    state["formbeep_7d"] = fb
    state["stackstats_7d"] = ss
    save_state(state)

    if founder_blocked:
        print("BLOCKED: founder blockers present (see cmo/issues_rishi.md)")
        return 2

    if not changed:
        print("[SILENT]")
        return 0

    print("OK: updated growth log + umami snapshot")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
