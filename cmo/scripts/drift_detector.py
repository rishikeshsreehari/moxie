#!/usr/bin/env python3
"""Detect truth drift between HQ queues, artifacts, and founder-facing blocker lists.

Contract:
- Print ONE line: OK:..., BLOCKED:..., or ERROR:...
- Exit: 0 OK, 2 BLOCKED, 1 ERROR

Fast + dependency-free.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/root/moxie_hq")
CMO = BASE / "cmo"

DISPATCH = CMO / "dispatch-queue.md"
ISSUES = CMO / "issues_rishi.md"
REVIEW = CMO / "rishi_review.md"
DELEGATION = CMO / "delegation-queue.md"


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def _issues_open_items(text: str) -> list[str]:
    m = re.search(r"## Open(.*?)(?:## Resolved|\Z)", text, re.S)
    if not m:
        return []
    block = m.group(1)
    out = []
    for ln in block.splitlines():
        s = ln.strip()
        if not s.startswith("-"):
            continue
        if "(no open" in s.lower():
            continue
        # checkbox or bullet counts as open item
        if "[ ]" in s or s.startswith("- "):
            out.append(s)
    return out


def _delegation_has_divider_spam(text: str) -> bool:
    # A sign of earlier bug: data rows like "| --- | DISPATCHED | --- | ..."
    return "| --- | DISPATCHED" in text


def _parse_output_paths_from_dispatch(text: str) -> list[Path]:
    paths: list[Path] = []

    for m in re.finditer(r"Output path:\s*(/[^\s]+)", text):
        paths.append(Path(m.group(1)))

    # Standard line format: [P?] product|Seat|Task|output_file|...
    for line in text.splitlines():
        if "|" in line and line.lstrip().startswith("["):
            parts = line.split("|")
            if len(parts) >= 4:
                candidate = parts[3].strip()
                if candidate.startswith("/"):
                    paths.append(Path(candidate))
                elif candidate:
                    paths.append((BASE / candidate).resolve())

    # Dedup
    out: list[Path] = []
    seen = set()
    for p in paths:
        s = str(p)
        if s not in seen:
            seen.add(s)
            out.append(p)
    return out


def main() -> int:
    dispatch = _read(DISPATCH)
    issues = _read(ISSUES)
    review = _read(REVIEW)
    delegation = _read(DELEGATION)

    open_items = _issues_open_items(issues)
    if open_items:
        print("BLOCKED: issues_rishi.md has open items")
        return 2

    if _delegation_has_divider_spam(delegation):
        print("ERROR: delegation-queue contains divider spam rows")
        return 1

    # Completed tasks should have artifacts
    if "COMPLETED" in dispatch:
        paths = _parse_output_paths_from_dispatch(dispatch)
        missing = [p for p in paths if str(p).startswith("/") and not p.exists()]
        if missing:
            print(f"ERROR: missing artifacts for completed tasks ({len(missing)})")
            return 1

    # rishi_review staleness is error (>14d)
    m = re.search(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", review)
    if m:
        try:
            d = datetime.strptime(m.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
            age = (datetime.now(timezone.utc) - d).days
            if age > 14:
                print("ERROR: rishi_review.md is stale (>14d)")
                return 1
        except Exception:
            pass

    print("OK: no drift detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
