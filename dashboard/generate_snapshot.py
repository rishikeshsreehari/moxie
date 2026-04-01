#!/usr/bin/env python3
"""Generate dashboard/public_snapshot.json from HQ repo state.

This is designed for CI / Cloudflare Pages build steps.
It only emits aggregated + scrubbed data.

Inputs (repo-relative):
- cmo/exec-updates/last_snapshot.json (traffic summary + queue counts)
- cmo/dispatch-queue.md (running tasks)
- cmo/issues_rishi.md (open blockers)
- git log (recent commits)

Output:
- dashboard/public_snapshot.json

Usage:
  python3 dashboard/generate_snapshot.py
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TOKEN_RE = re.compile(r"\b([A-Za-z0-9_-]{20,})\b")
URL_RE = re.compile(r"https?://[^\s)\]]+")


def scrub(text: str) -> str:
    t = text
    t = EMAIL_RE.sub("[email]", t)
    # Avoid nuking normal words: only replace long token-ish blobs
    t = TOKEN_RE.sub("[token]", t)
    # Keep URL presence but remove specifics
    t = URL_RE.sub("[url]", t)
    # Remove overly specific paths
    t = t.replace("/root/", "/")
    return t.strip()


def safe_int_from_line(prefix: str, lines: list[str]) -> int | None:
    for ln in lines:
        if ln.startswith(prefix):
            m = re.search(r"(\d+)", ln)
            if m:
                return int(m.group(1))
    return None


def read_last_snapshot() -> dict[str, Any]:
    p = ROOT / "cmo" / "exec-updates" / "last_snapshot.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def parse_dispatch_queue_running() -> list[dict[str, str]]:
    p = ROOT / "cmo" / "dispatch-queue.md"
    if not p.exists():
        return []

    tasks: list[dict[str, str]] = []
    for raw in p.read_text(encoding="utf-8").splitlines():
        if "[IN_PROGRESS]" not in raw:
            continue
        # Format: [IN_PROGRESS][P1] Product|Employee|Task|Output|...
        parts = raw.split("|")
        if len(parts) < 3:
            continue
        left = parts[0]
        product = parts[0].split("]")[-1].strip() if "]" in parts[0] else ""
        employee = parts[1].strip()
        task = parts[2].strip()

        tasks.append({
            "role": scrub(employee),
            "status": "IN_PROGRESS",
            "text": scrub(task),
        })

    return tasks[:8]


def parse_issues_needs_rishi(max_items: int = 8) -> list[str]:
    p = ROOT / "cmo" / "issues_rishi.md"
    if not p.exists():
        return []

    lines = p.read_text(encoding="utf-8").splitlines()

    open_idx = None
    for i, ln in enumerate(lines):
        if ln.strip().lower() == "## open":
            open_idx = i
            break

    if open_idx is None:
        return []

    items: list[str] = []
    for ln in lines[open_idx + 1 :]:
        if ln.strip().startswith("## "):
            break
        if ln.strip().startswith("- [ ]"):
            # trim markdown checkbox
            txt = ln.strip()[5:].strip()
            # remove owner tail
            txt = re.sub(r"\s+—\s+Owner:.*$", "", txt)
            items.append(scrub(txt))

    return items[:max_items]


def git_recent(max_items: int = 8) -> list[dict[str, str]]:
    try:
        out = subprocess.check_output(
            ["git", "log", f"-n{max_items}", "--pretty=format:%h|%ad|%s", "--date=short"],
            cwd=str(ROOT),
            text=True,
        )
    except Exception:
        return []

    rows: list[dict[str, str]] = []
    for ln in out.splitlines():
        h, d, s = (ln.split("|", 2) + ["", "", ""])[:3]
        rows.append({"hash": h, "when": d, "subject": scrub(s)})
    return rows


def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    last = read_last_snapshot()
    analytics_lines = last.get("analytics_lines") or []

    pv = safe_int_from_line("- Pageviews:", analytics_lines)
    visitors = safe_int_from_line("- Visitors:", analytics_lines)

    # Signups: try to count hero/pricing/header lines as a heuristic
    signup = 0
    for ln in analytics_lines:
        if "Signup" in ln:
            m = re.search(r"(\d+)\s*$", ln)
            if m:
                signup += int(m.group(1))

    counts = last.get("counts") or {}

    running_tasks = parse_dispatch_queue_running()
    needs_rishi = parse_issues_needs_rishi()

    snapshot: dict[str, Any] = {
        "generated_at": now,
        "kpis": {
            "pageviews_7d": pv if pv is not None else 0,
            "visitors_7d": visitors if visitors is not None else 0,
            "signups_7d": signup,
            "paid_7d": 0,
            "mrr_usd": 0,
            "revenue_total_usd": 0,
        },
        "products": [
            {
                "name": "FormBeep",
                "status": "ACTIVE",
                "pageviews_7d": pv if pv is not None else 0,
                "signups_7d": signup,
            }
        ],
        "systems": {
            "queue": {
                "pending": int(counts.get("QUEUED", 0)),
                "in_progress": int(counts.get("IN_PROGRESS", 0)),
            },
            "cron": {
                # if you want: wire in a job count from orchestration later
                "active_jobs": 0,
            },
            "blockers": {
                "count": len(needs_rishi),
                "needs_rishi": needs_rishi,
            },
        },
        "running": {
            "count": len(running_tasks),
            "tasks": running_tasks,
            "highlights": [
                "Assessing competitor data: insights extracted",
                "US SERP analysis: in progress",
                "Directories: execution packs ready",
            ],
        },
        "team": [
            {"role": "Moxie", "status": "ACTIVE", "working_on": "Orchestration + growth decisions"},
        ],
        "github": {"recent": git_recent(8)},
        "console": [
            "[BOOT] Moxie HQ online",
            f"[SYNC] snapshot generated {now}",
            f"[QUEUE] in_progress={counts.get('IN_PROGRESS', 0)} queued={counts.get('QUEUED', 0)}",
            f"[BLOCK] needs_rishi={len(needs_rishi)}",
        ],
    }

    out_path = ROOT / "dashboard" / "public_snapshot.json"
    out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
