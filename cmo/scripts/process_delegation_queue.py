#!/usr/bin/env python3
"""process_delegation_queue.py

Promote human-authored work orders from cmo/delegation-queue.md into cmo/dispatch-queue.md.

Design goals:
- Product-agnostic (no hard-coded product logic)
- Idempotent (won't duplicate if already promoted)
- Safe (only edits files under /root/moxie_hq/cmo)

Usage:
  python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py

Exit codes:
  0 success (including no-op)
  2 malformed delegation table
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path("/root/moxie_hq")
CMO_DIR = REPO_ROOT / "cmo"
DELEGATION_QUEUE_PATH = CMO_DIR / "delegation-queue.md"
DISPATCH_QUEUE_PATH = CMO_DIR / "dispatch-queue.md"

ALLOWED_WRITE_PREFIXES = [str(CMO_DIR)]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _assert_safe_write(path: Path) -> None:
    p = str(path.resolve())
    if not any(p.startswith(prefix + os.sep) or p == prefix for prefix in ALLOWED_WRITE_PREFIXES):
        raise RuntimeError(f"Refusing to write outside cmo/: {p}")


def atomic_write_text(path: Path, text: str) -> None:
    _assert_safe_write(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    _assert_safe_write(tmp)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


@dataclass
class MdTable:
    header_cols: List[str]
    rows: List[Dict[str, str]]
    start_line_idx: int
    end_line_idx: int


def parse_markdown_table(lines: List[str], header_required: List[str]) -> MdTable:
    """Find and parse the first markdown table containing all required headers.

    Returns start/end line indices (inclusive start, exclusive end) for replacement.
    """

    def split_row(line: str) -> List[str]:
        # naive but sufficient for our controlled spec (no escaped pipes).
        parts = [p.strip() for p in line.strip().split("|")]
        # remove leading/trailing empty due to starting/ending pipe
        if parts and parts[0] == "":
            parts = parts[1:]
        if parts and parts[-1] == "":
            parts = parts[:-1]
        return parts

    for i in range(len(lines) - 1):
        if "|" not in lines[i]:
            continue
        hdr = split_row(lines[i])
        if not hdr:
            continue
        hdr_lc = [h.strip().lower() for h in hdr]
        if not all(req.lower() in hdr_lc for req in header_required):
            continue
        # next line must look like separator
        if i + 1 >= len(lines):
            continue
        sep = lines[i + 1].strip()
        if not (sep.startswith("|") and set(sep.replace("|", "").strip()) <= set("-: ")):
            continue

        # rows until blank line or non-table
        rows = []
        j = i + 2
        while j < len(lines):
            line = lines[j]
            if line.strip() == "":
                break
            if "|" not in line:
                break
            vals = split_row(line)
            if len(vals) != len(hdr):
                break
            row = {hdr[k].strip().lower(): vals[k].strip() for k in range(len(hdr))}
            rows.append(row)
            j += 1

        return MdTable(header_cols=[h.strip() for h in hdr], rows=rows, start_line_idx=i, end_line_idx=j)

    raise ValueError("delegation queue table not found")


def normalize_seat(seat: str) -> str:
    s = seat.strip()
    if not s:
        return s
    # Title-case but preserve internal hyphens.
    return "-".join([p[:1].upper() + p[1:].lower() if p else p for p in s.split("-")])


def priority_to_prefix(priority: str) -> str:
    p = priority.strip().upper()
    if p == "P0":
        return "0."
    if p == "P1":
        return "1."
    if p == "P2":
        return "2."
    if p == "P3":
        return "3."
    return "9."


def build_dispatch_line(row: Dict[str, str]) -> str:
    rid = row.get("id", "").strip()
    seat = normalize_seat(row.get("seat", ""))
    prio = row.get("priority", "").strip()
    product = row.get("product", "").strip()
    task = row.get("task", "").strip()
    deps = (row.get("depends_on", "") or "").strip() or "None"
    out = (row.get("output_file", "") or "").strip() or "TBD"

    prefix = priority_to_prefix(prio)

    tag = f"[DELEGATION:{rid}]"
    # Keep stable dispatch-queue format:
    # N. [STATUS] Employee | (Product) Task | Depends on | Output file
    return f"{prefix} [QUEUED] {seat} | ({product}) {task} {tag} | {deps} | {out}\n"


def insert_into_dispatch_queue(new_lines: List[str]) -> int:
    if not new_lines:
        return 0

    txt = DISPATCH_QUEUE_PATH.read_text(encoding="utf-8", errors="replace")
    if "## Queue" not in txt:
        raise RuntimeError("dispatch-queue.md missing '## Queue' section")

    # Dedupe based on delegation tags
    existing = set(re.findall(r"\[DELEGATION:([^\]]+)\]", txt))
    filtered = []
    for line in new_lines:
        m = re.search(r"\[DELEGATION:([^\]]+)\]", line)
        if m and m.group(1) in existing:
            continue
        filtered.append(line)

    if not filtered:
        return 0

    lines = txt.splitlines(True)

    # Insert after the 'Format:' line block beneath '## Queue'
    insert_at = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## queue"):
            # look for line that starts with "Format:" then insert after the next blank line
            j = i
            while j < len(lines) and "Format:" not in lines[j]:
                j += 1
            if j >= len(lines):
                # fallback: insert right after the Queue header
                insert_at = i + 1
                break
            k = j + 1
            # move to first blank line after format line
            while k < len(lines) and lines[k].strip() != "":
                k += 1
            # insert after that blank line (or at EOF)
            insert_at = k + 1 if k + 1 <= len(lines) else len(lines)
            break

    if insert_at is None:
        raise RuntimeError("could not find insertion point in dispatch-queue.md")

    lines[insert_at:insert_at] = filtered
    atomic_write_text(DISPATCH_QUEUE_PATH, "".join(lines))
    return len(filtered)


def rebuild_table(table: MdTable) -> str:
    cols = table.header_cols
    hdr_line = "| " + " | ".join(cols) + " |\n"
    sep_line = "|" + "---|" * len(cols) + "\n"

    def get_cell(row: Dict[str, str], col: str) -> str:
        return (row.get(col.strip().lower(), "") or "").strip()

    body_lines = []
    for row in table.rows:
        body_lines.append("| " + " | ".join(get_cell(row, c) for c in cols) + " |\n")

    return hdr_line + sep_line + "".join(body_lines)


def main() -> int:
    if not DELEGATION_QUEUE_PATH.exists():
        raise SystemExit(f"Missing {DELEGATION_QUEUE_PATH}")
    if not DISPATCH_QUEUE_PATH.exists():
        raise SystemExit(f"Missing {DISPATCH_QUEUE_PATH}")

    dq_txt = DELEGATION_QUEUE_PATH.read_text(encoding="utf-8", errors="replace")
    dq_lines = dq_txt.splitlines(True)

    try:
        table = parse_markdown_table(
            dq_lines,
            header_required=[
                "id",
                "status",
                "created_utc",
                "seat",
                "priority",
                "product",
                "task",
                "depends_on",
                "output_file",
                "dispatched_utc",
            ],
        )
    except Exception as e:
        print(f"ERROR: {e}")
        return 2

    # Determine which rows are eligible
    dispatch_lines: List[str] = []
    promoted_ids: List[str] = []
    already_present_ids: List[str] = []

    dispatch_txt = DISPATCH_QUEUE_PATH.read_text(encoding="utf-8", errors="replace")
    existing_ids = set(re.findall(r"\[DELEGATION:([^\]]+)\]", dispatch_txt))

    now = utc_now_iso()

    for row in table.rows:
        rid = (row.get("id", "") or "").strip()
        if not rid:
            continue
        status = (row.get("status", "") or "").strip().upper()
        if status in ("CANCELLED", "CANCELED"):
            continue
        if "DISPATCHED" in status:
            continue

        if rid in existing_ids:
            # mark dispatched without inserting another line
            row["status"] = "DISPATCHED"
            row["dispatched_utc"] = row.get("dispatched_utc", "").strip() or now
            already_present_ids.append(rid)
            continue

        dispatch_lines.append(build_dispatch_line(row))
        promoted_ids.append(rid)
        row["status"] = "DISPATCHED"
        row["dispatched_utc"] = now

    inserted = insert_into_dispatch_queue(dispatch_lines)

    # Replace table region
    new_table_txt = rebuild_table(table)
    new_lines = list(dq_lines)
    new_lines[table.start_line_idx : table.end_line_idx] = [new_table_txt]
    atomic_write_text(DELEGATION_QUEUE_PATH, "".join(new_lines))

    print(f"Promoted: {inserted} new item(s)")
    if already_present_ids:
        print(f"Marked DISPATCHED (already present): {len(already_present_ids)}")
    if not promoted_ids and not already_present_ids:
        print("No eligible items.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
