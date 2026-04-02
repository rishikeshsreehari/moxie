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
import sqlite3
import subprocess
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"https?://[^\s)\]]+")
UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)

SAFE_URL_PREFIXES = (
    "https://formbeep.com",
    "https://stackstats.app",
    "https://rishikeshs.com",
    "https://github.com/rishikeshsreehari/",
)



def scrub(text: str, *, allow_safe_urls: bool = False) -> str:
    t = str(text or "")
    t = EMAIL_RE.sub("[email]", t)
    t = UUID_RE.sub("[id]", t)

    # Defense-in-depth: redact common analytics identifiers even if not UUID-shaped
    t = re.sub(r"(?i)(website[_-]?id|umami[_-]?id)\s*[:=]?\s*[^\s,;\)\]]+", r"\1 [redacted]", t)

    if allow_safe_urls:
        def repl(m: re.Match) -> str:
            u = m.group(0)
            for p in SAFE_URL_PREFIXES:
                if u.startswith(p):
                    return u
            return "[url]"

        t = URL_RE.sub(repl, t)
    else:
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


def parse_open_threads(max_items: int = 10, last_snapshot: dict[str, Any] | None = None) -> list[str]:
    """Public list of open threads.

    Prefer cmo/exec-updates/last_snapshot.json issues_open (already curated),
    fallback to any checkbox items in cmo/issues_rishi.md.
    """

    items: list[str] = []

    if isinstance(last_snapshot, dict):
        for raw in (last_snapshot.get("issues_open") or [])[: max_items * 2]:
            t = scrub(raw)
            # normalize "[ ] ... — Owner: ..."
            t = re.sub(r"^\[\s*\]\s*", "", t).strip()
            t = re.sub(r"\s+—\s+Owner:.*$", "", t).strip()
            t = t.replace("Rishi", "Founder")
            if t:
                items.append(t)

    if len(items) >= max_items:
        return items[:max_items]

    p = ROOT / "cmo" / "issues_rishi.md"
    if p.exists():
        lines = p.read_text(encoding="utf-8").splitlines()
        for ln in lines:
            s = ln.strip()
            if s.startswith("- [ ]"):
                t = s[5:].strip()
                t = re.sub(r"\s+—\s+Owner:.*$", "", t).strip()
                t = scrub(t).replace("Rishi", "Founder")
                if t:
                    items.append(t)
            if len(items) >= max_items:
                break

    # de-dupe preserve order
    out: list[str] = []
    seen = set()
    for x in items:
        if x in seen:
            continue
        seen.add(x)
        out.append(x)
        if len(out) >= max_items:
            break

    return out


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


def _git_remote_http_base(repo_dir: Path) -> str | None:
    """Return https://github.com/<owner>/<repo> if the repo has a GitHub remote."""
    try:
        url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=str(repo_dir),
            text=True,
        ).strip()
    except Exception:
        return None

    if not url:
        return None

    m = re.match(r"git@github\\.com:([^/]+)/([^/]+?)(?:\\.git)?$", url)
    if m:
        return f"https://github.com/{m.group(1)}/{m.group(2)}"

    m = re.match(r"https?://github\\.com/([^/]+)/([^/]+?)(?:\\.git)?$", url)
    if m:
        return f"https://github.com/{m.group(1)}/{m.group(2)}"

    return None


def git_recent_portfolio(max_items: int = 10) -> list[dict[str, str]]:
    """Combined recent commits across HQ + product repos (when present locally)."""

    repos: list[tuple[str, Path]] = [
        ("hq", ROOT),
        ("formbeep", Path("/root/moxie/products/formbeep")),
        ("stackstats", Path("/root/moxie/products/stackstats")),
    ]

    commits: list[dict[str, Any]] = []
    for name, path in repos:
        if not (path / ".git").exists():
            continue
        try:
            out = subprocess.check_output(
                ["git", "log", "-n6", "--pretty=format:%h|%ct|%s"],
                cwd=str(path),
                text=True,
            )
        except Exception:
            continue

        base = _git_remote_http_base(path)

        for ln in out.splitlines():
            h, ts, subj = (ln.split("|", 2) + ["", "", ""])[:3]
            try:
                t = int(ts)
            except Exception:
                t = 0
            commits.append(
                {
                    "repo": name,
                    "hash": h,
                    "ts": t,
                    "when": datetime.fromtimestamp(t, tz=timezone.utc).strftime("%Y-%m-%d"),
                    "subject": scrub(subj),
                    "url": (f"{base}/commit/{h}" if (base and h) else ""),
                }
            )

    commits.sort(key=lambda x: int(x.get("ts") or 0), reverse=True)

    out_rows: list[dict[str, str]] = []
    for c in commits[:max_items]:
        out_rows.append(
            {
                "repo": scrub(c.get("repo") or ""),
                "hash": scrub(c.get("hash") or ""),
                "when": scrub(c.get("when") or ""),
                "subject": scrub(c.get("subject") or ""),
                "url": scrub(c.get("url") or "", allow_safe_urls=True),
            }
        )

    return out_rows


def model_usage_7d(db_path: Path = Path("/opt/data/state.db"), days: int = 7) -> dict[str, Any]:
    """Aggregate Hermes session usage by model (public-safe aggregates)."""

    if not db_path.exists():
        return {"window": f"{days}d", "items": []}

    cutoff = datetime.now(timezone.utc).timestamp() - (days * 86400)

    try:
        con = sqlite3.connect(str(db_path))
        cur = con.cursor()
        cur.execute(
            """
            SELECT model,
                   COALESCE(SUM(input_tokens),0) AS in_tok,
                   COALESCE(SUM(output_tokens),0) AS out_tok,
                   COALESCE(SUM(tool_call_count),0) AS tool_calls
            FROM sessions
            WHERE started_at >= ?
              AND model IS NOT NULL
              AND TRIM(model) != ''
            GROUP BY model
            ORDER BY (COALESCE(SUM(input_tokens),0) + COALESCE(SUM(output_tokens),0)) DESC
            LIMIT 12
            """,
            (cutoff,),
        )
        rows = cur.fetchall()
        con.close()
    except Exception:
        return {"window": f"{days}d", "items": []}

    items: list[dict[str, Any]] = []
    for model, in_tok, out_tok, tool_calls in rows:
        total = int(in_tok or 0) + int(out_tok or 0)
        value = int(round(total / 1000.0))  # K tokens
        items.append({"label": scrub(model), "value": value, "tokens": total, "tool_calls": int(tool_calls or 0)})

    return {"window": f"{days}d", "items": items}


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
    open_threads = parse_open_threads(last_snapshot=last)
    team = parse_orchestration_employees()
    active_products = parse_orchestration_active_products()
    cron_count = parse_orchestration_cron_count()

    revenue = read_json(ROOT / "cmo" / "metrics" / "revenue.json")
    portfolio = revenue.get("portfolio") if isinstance(revenue, dict) else {}

    # products table (portfolio)
    products: list[dict[str, Any]] = []
    prod_cfg = revenue.get("products") if isinstance(revenue, dict) else {}

    if isinstance(prod_cfg, dict) and prod_cfg:
        for key, meta in prod_cfg.items():
            if not isinstance(meta, dict):
                meta = {}

            k = str(key).lower().strip()
            disp = "FormBeep" if k == "formbeep" else ("StackStats" if k == "stackstats" else str(key))
            url = "https://formbeep.com" if k == "formbeep" else ("https://stackstats.app" if k == "stackstats" else "")

            paid = meta.get("paid_lifetime")
            free = meta.get("free_lifetime")

            users = None
            try:
                users = (int(paid) if paid is not None else 0) + (int(free) if free is not None else 0)
            except Exception:
                users = paid if paid is not None else (free if free is not None else None)

            products.append(
                {
                    "name": scrub(disp),
                    "status": "ACTIVE" if scrub(disp) in active_products else "IDLE",
                    "url": url,
                    "link_label": url.replace("https://", "") if url else "",
                    "users_lifetime": users,
                    "paid_lifetime": paid,
                    "free_lifetime": free,
                    "revenue_lifetime_usd": meta.get("lifetime_revenue_usd"),
                    "mrr_usd": meta.get("mrr_usd"),
                    "pageviews_7d": pv if k == "formbeep" else None,
                    "signups_7d": signups if k == "formbeep" else None,
                }
            )
    else:
        # fallback: at least show active sprint product
        for name in active_products[:4]:
            products.append({"name": name, "status": "ACTIVE", "pageviews_7d": pv, "signups_7d": signups})

    # rollups
    paid_life = portfolio.get("paid_lifetime")
    free_life = portfolio.get("free_lifetime")
    users_life = portfolio.get("users_lifetime")

    if paid_life is None:
        try:
            paid_life = sum(int(p.get("paid_lifetime") or 0) for p in products)
        except Exception:
            paid_life = 0

    if users_life is None:
        # Only compute if at least one product has a known users_lifetime.
        try:
            known = [p.get("users_lifetime") for p in products if p.get("users_lifetime") is not None]
            if known:
                users_life = sum(int(x or 0) for x in known)
            else:
                users_life = None
        except Exception:
            users_life = None

    snapshot: dict[str, Any] = {
        "generated_at": now,
        "kpis": {
            "pageviews_7d": pv,
            "visitors_7d": visitors,
            "signups_7d": signups,
            "users_lifetime": (None if users_life is None else int(users_life or 0)),
            "paid_lifetime": int(paid_life or 0),
            "free_lifetime": (None if free_life is None else int(free_life or 0)),
            "revenue_lifetime_usd": float(portfolio.get("lifetime_revenue_usd", 0) or 0),
            "mrr_usd": float(portfolio.get("mrr_usd", 0) or 0),
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
                "count": len(open_threads),
                "needs_rishi": open_threads,
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
        "shipping": {"recent": git_recent_portfolio(10)},
        "github": {"recent": git_recent_portfolio(10)},
        "models": model_usage_7d(),
        "console": [
            "[BOOT] SapiensTech Open Ops online",
            f"[SYNC] snapshot generated {now}",
            f"[WORK] in_progress={counts.get('IN_PROGRESS', 0)} queued={counts.get('QUEUED', 0)} blocked={counts.get('BLOCKED', 0)}",
            f"[THREADS] open={len(open_threads)}",
        ],
        "terminal_lines": [],
    }

    # Build a fun "terminal" transcript from snapshot (safe aggregates only)
    recent = snapshot.get("github", {}).get("recent") or []
    term: list[str] = []
    term.append("$ moxie status")
    term.append(f"in_progress={counts.get('IN_PROGRESS', 0)} queued={counts.get('QUEUED', 0)} blocked={counts.get('BLOCKED', 0)} completed={counts.get('COMPLETED', 0)}")
    term.append("")
    term.append("$ traffic --7d")
    term.append(f"pageviews={pv} visitors={visitors} signups={signups}")
    term.append("")
    term.append("$ revenue")
    term.append(f"mrr_usd={snapshot['kpis'].get('mrr_usd', 0)} lifetime_usd={snapshot['kpis'].get('revenue_lifetime_usd', 0)}")
    term.append("")
    term.append("$ git log -3 --oneline")
    if recent:
        for c in recent[:3]:
            repo = c.get("repo", "")
            term.append(f"{repo} {c.get('hash','')} {c.get('subject','')}")
    else:
        term.append("(no commits found)")

    snapshot["terminal_lines"] = [scrub(x) for x in term if x is not None]

    out_path = ROOT / "dashboard" / "public_snapshot.json"
    out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
