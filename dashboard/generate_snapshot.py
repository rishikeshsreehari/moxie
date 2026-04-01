#!/usr/bin/env python3
"""Generate dashboard/public_snapshot.json from HQ repo state.

Public-facing dashboard snapshot generator.
- Emits aggregated + scrubbed fields only.
- Designed to make the dashboard feel live (work + blockers + commits).

Inputs (repo-relative):
- cmo/exec-updates/last_snapshot.json (traffic summary + queue counts)
- cmo/dispatch-queue.md (running work)
- cmo/orchestration.md (employee status + active products + cron count)
- cmo/issues_rishi.md (open blockers)
- git log (recent commits)

Output:
- dashboard/public_snapshot.json

Usage:
  python3 dashboard/generate_snapshot.py
"""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"https?://[^\s)\]]+")


def scrub(text: str) -> str:
    t = str(text or "")
    t = EMAIL_RE.sub("[email]", t)
    t = URL_RE.sub("[url]", t)
    t = t.replace("/root/", "/")
    return t.strip()


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def safe_int_from_line(prefix: str, lines: list[str]) -> int | None:
    for ln in lines:
        if ln.startswith(prefix):
            m = re.search(r"(\d+)", ln)
            if m:
                return int(m.group(1))
    return None


def parse_dispatch_tasks() -> list[dict[str, str]]:
    p = ROOT / "cmo" / "dispatch-queue.md"
    if not p.exists():
        return []

    lines = p.read_text(encoding="utf-8").splitlines()

    tasks: list[dict[str, str]] = []

    # Prefer IN_PROGRESS
    for raw in lines:
        if "[IN_PROGRESS]" not in raw:
            continue
        parts = raw.split("|")
        if len(parts) < 3:
            continue
        employee = scrub(parts[1].strip())
        task = scrub(parts[2].strip())
        tasks.append({"role": employee, "status": "IN_PROGRESS", "text": task})

    # If none, show BLOCKED/QUEUED to keep the dashboard alive
    if not tasks:
        for raw in lines:
            if "[BLOCKED]" not in raw and "[QUEUED]" not in raw:
                continue
            parts = raw.split("|")
            if len(parts) < 3:
                continue
            employee = scrub(parts[1].strip())
            task = scrub(parts[2].strip())
            status = "BLOCKED" if "[BLOCKED]" in raw else "QUEUED"
            tasks.append({"role": employee, "status": status, "text": task})
            if len(tasks) >= 8:
                break

    return tasks[:10]


def parse_issues_needs_rishi(max_items: int = 10) -> list[str]:
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
            txt = ln.strip()[5:].strip()
            txt = re.sub(r"\s+—\s+Owner:.*$", "", txt)
            items.append(scrub(txt))

    return items[:max_items]


def parse_orchestration_employees(max_items: int = 14) -> list[dict[str, str]]:
    p = ROOT / "cmo" / "orchestration.md"
    if not p.exists():
        return [{"name": "Moxie", "title": "Autonomous CMO", "status": "ACTIVE", "working_on": "Orchestration + decisions"}]

    lines = p.read_text(encoding="utf-8").splitlines()

    # Find Employee State section (orchestration.md includes line-number prefixes)
    start = None
    for i, ln in enumerate(lines):
        if "## Employee State" in ln:
            start = i
            break
    if start is None:
        return [{"name": "Moxie", "title": "Autonomous CMO", "status": "ACTIVE", "working_on": "Orchestration + decisions"}]

    team: list[dict[str, str]] = []

    i = start
    current_name = None
    current_status = None
    current_task = None

    def flush():
        nonlocal current_name, current_status, current_task
        if current_name:
            if "—" in current_name:
                name, title = [x.strip() for x in current_name.split("—", 1)]
            else:
                name, title = current_name.strip(), ""
            team.append({
                "name": scrub(name),
                "title": scrub(title),
                "status": scrub(current_status or "IDLE"),
                "working_on": scrub(current_task or ""),
            })
        current_name = None
        current_status = None
        current_task = None

    while i < len(lines):
        ln = lines[i]
        # stop at next major section, but don't stop on employee headings
        if "## " in ln and i > start and "### " not in ln:
            break
        if "### " in ln:
            flush()
            current_name = ln.split("### ", 1)[1].strip()

        if "|- Status:" in ln:
            current_status = ln.split("|- Status:", 1)[1].strip()
        elif "- Status:" in ln:
            current_status = ln.split("- Status:", 1)[1].strip()
        elif ln.strip().startswith("- Status:"):
            current_status = ln.strip().split("- Status:", 1)[1].strip()

        if "|- Current task:" in ln:
            current_task = ln.split("|- Current task:", 1)[1].strip()
        elif "- Current task:" in ln:
            current_task = ln.split("- Current task:", 1)[1].strip()
        elif ln.strip().startswith("- Current task:"):
            current_task = ln.strip().split("- Current task:", 1)[1].strip()

        i += 1

    flush()

    out: list[dict[str, str]] = [{"name": "Moxie", "title": "Autonomous CMO", "status": "ACTIVE", "working_on": "Orchestration + growth decisions"}]
    for row in team:
        if str(row.get("name", "")).lower() == "moxie":
            continue
        out.append(row)

    return out[:max_items]


def parse_orchestration_active_products() -> list[str]:
    p = ROOT / "cmo" / "orchestration.md"
    if not p.exists():
        return ["FormBeep"]
    txt = p.read_text(encoding="utf-8")
    m = re.search(r"## Active Product \(current sprint\)\n- Product: (.+?) —", txt)
    if m:
        return [scrub(m.group(1))]
    return ["FormBeep"]


def parse_orchestration_cron_count() -> int:
    p = ROOT / "cmo" / "orchestration.md"
    if not p.exists():
        return 0
    lines = p.read_text(encoding="utf-8").splitlines()

    # Count rows in the Active Crons table that look like "|||| <id> |"
    count = 0
    for ln in lines:
        if ln.startswith("||||"):
            if "Cron ID" in ln or "---" in ln:
                continue
            parts = [p.strip() for p in ln.split("|")]
            if len(parts) > 4:
                maybe_id = parts[4]
                if re.fullmatch(r"[0-9a-f]{6,12}", maybe_id):
                    count += 1
    return count


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

    last = read_json(ROOT / "cmo" / "exec-updates" / "last_snapshot.json")
    analytics_lines = last.get("analytics_lines") or []

    pv = safe_int_from_line("- Pageviews:", analytics_lines) or 0
    visitors = safe_int_from_line("- Visitors:", analytics_lines) or 0

    # Signups heuristic: sum signup lines
    signups = 0
    for ln in analytics_lines:
        if "Signup" in ln:
            m = re.search(r"(\d+)\s*$", ln)
            if m:
                signups += int(m.group(1))

    counts = last.get("counts") or {}

    running_tasks = parse_dispatch_tasks()
    needs_rishi = parse_issues_needs_rishi()
    team = parse_orchestration_employees()
    active_products = parse_orchestration_active_products()
    cron_count = parse_orchestration_cron_count()

    # products table (currently just active product)
    products = []
    for name in active_products[:4]:
        products.append({
            "name": name,
            "status": "ACTIVE",
            "pageviews_7d": pv,
            "signups_7d": signups,
        })

    snapshot: dict[str, Any] = {
        "generated_at": now,
        "kpis": {
            "pageviews_7d": pv,
            "visitors_7d": visitors,
            "signups_7d": signups,
            "paid_lifetime": 0,
            "free_lifetime": 0,
            "revenue_lifetime_usd": 0,
        },
        "products": products,
        "systems": {
            "queue": {
                "pending": int(counts.get("QUEUED", 0)),
                "in_progress": int(counts.get("IN_PROGRESS", 0)),
            },
            "cron": {
                "active_jobs": cron_count,
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
                "Competitor intel: insights extracted",
                "US SERP analysis: in progress",
                "Directories: execution packs ready (waiting on founder)",
            ],
        },
        "team": team,
        "github": {"recent": git_recent(8)},
        "console": [
            "[BOOT] Moxie HQ online",
            f"[SYNC] snapshot generated {now}",
            f"[WORK] in_progress={counts.get('IN_PROGRESS', 0)} queued={counts.get('QUEUED', 0)}",
            f"[NEED] blockers={len(needs_rishi)}",
        ],
    }

    out_path = ROOT / "dashboard" / "public_snapshot.json"
    out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
