#!/usr/bin/env python3
"""process_artifacts.py

Scan repo artifacts and, based on cmo/artifact-rules.yaml, enqueue or promote follow-on tasks.

Key behavior:
- Generic rules via YAML (product-agnostic)
- Detect changes via sha256(content)
- State stored at cmo/state/artifact_state.json
- First run seeds state but DOES NOT dispatch (so it behaves like "changed since last run")
- Idempotent: dispatch lines are tagged and deduped
- Safe: only writes under /root/moxie_hq/cmo

Usage:
  python3 /root/moxie_hq/cmo/scripts/process_artifacts.py
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import glob
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

REPO_ROOT = Path("/root/moxie_hq")
CMO_DIR = REPO_ROOT / "cmo"
RULES_PATH = CMO_DIR / "artifact-rules.yaml"
STATE_DIR = CMO_DIR / "state"
STATE_PATH = STATE_DIR / "artifact_state.json"
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


def atomic_write_json(path: Path, obj: Any) -> None:
    atomic_write_text(path, json.dumps(obj, indent=2, sort_keys=True) + "\n")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT.resolve()))


def format_task_template(s: str, artifact_path: str, artifact_relpath: str) -> str:
    return s.format(artifact_path=artifact_path, artifact_relpath=artifact_relpath)


def load_rules() -> Dict[str, Any]:
    if not RULES_PATH.exists():
        raise SystemExit(f"Missing {RULES_PATH}")
    data = yaml.safe_load(RULES_PATH.read_text(encoding="utf-8", errors="replace"))
    if not isinstance(data, dict) or "rules" not in data:
        raise SystemExit("artifact-rules.yaml must be a mapping with top-level 'rules:'")
    if not isinstance(data["rules"], list):
        raise SystemExit("artifact-rules.yaml 'rules' must be a list")
    return data


def load_state() -> Tuple[Dict[str, Any], bool]:
    if not STATE_PATH.exists():
        return {"version": 1, "files": {}, "last_run_utc": None}, True
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8", errors="replace")), False
    except Exception:
        return {"version": 1, "files": {}, "last_run_utc": None}, False


def dispatch_queue_contains(tag: str) -> bool:
    if not DISPATCH_QUEUE_PATH.exists():
        return False
    txt = DISPATCH_QUEUE_PATH.read_text(encoding="utf-8", errors="replace")
    return tag in txt


def insert_lines_into_dispatch_queue(new_lines: List[str]) -> int:
    if not new_lines:
        return 0
    txt = DISPATCH_QUEUE_PATH.read_text(encoding="utf-8", errors="replace")
    lines = txt.splitlines(True)

    insert_at = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## queue"):
            j = i
            while j < len(lines) and "Format:" not in lines[j]:
                j += 1
            if j >= len(lines):
                insert_at = i + 1
                break
            k = j + 1
            while k < len(lines) and lines[k].strip() != "":
                k += 1
            insert_at = k + 1 if k + 1 <= len(lines) else len(lines)
            break

    if insert_at is None:
        raise RuntimeError("could not find insertion point in dispatch-queue.md")

    # Dedupe is handled before we generate lines (via event_tag checks).
    lines[insert_at:insert_at] = new_lines
    atomic_write_text(DISPATCH_QUEUE_PATH, "".join(lines))
    return len(new_lines)


def append_row_to_delegation_queue(row: Dict[str, str]) -> None:
    """Append a row to the delegation queue table.

    This is intentionally minimal and assumes delegation-queue.md follows the spec.
    """
    if not DELEGATION_QUEUE_PATH.exists():
        raise SystemExit(f"Missing {DELEGATION_QUEUE_PATH}")

    txt = DELEGATION_QUEUE_PATH.read_text(encoding="utf-8", errors="replace")
    lines = txt.splitlines(True)

    # Find the table header and append after the last row.
    hdr_idx = None
    sep_idx = None
    for i in range(len(lines) - 1):
        if lines[i].strip().lower().startswith("| id |") and "| status |" in lines[i].lower():
            hdr_idx = i
            sep_idx = i + 1
            break
    if hdr_idx is None:
        raise SystemExit("delegation-queue.md missing expected table header")

    j = sep_idx + 1
    last_row_idx = j
    while last_row_idx < len(lines) and lines[last_row_idx].strip().startswith("|"):
        j = last_row_idx
        last_row_idx += 1

    # Build row in spec order
    cols = [
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
        "notes",
    ]
    row_line = "| " + " | ".join((row.get(c, "") or "").replace("\n", " ").strip() for c in cols) + " |\n"

    lines.insert(last_row_idx, row_line)
    atomic_write_text(DELEGATION_QUEUE_PATH, "".join(lines))


def main() -> int:
    rules_doc = load_rules()
    state, first_run = load_state()
    files_state: Dict[str, Any] = state.get("files", {}) if isinstance(state.get("files"), dict) else {}

    if not DISPATCH_QUEUE_PATH.exists():
        raise SystemExit(f"Missing {DISPATCH_QUEUE_PATH}")

    queued_lines: List[str] = []
    enqueued_rows: List[Dict[str, str]] = []

    for rule in rules_doc.get("rules", []):
        if not isinstance(rule, dict):
            continue
        if not rule.get("enabled", True):
            continue

        name = str(rule.get("name", "")).strip()
        if not name:
            continue

        globs_list = rule.get("globs", [])
        if isinstance(globs_list, str):
            globs_list = [globs_list]
        if not isinstance(globs_list, list) or not globs_list:
            continue

        target = str(rule.get("target", "dispatch_queue")).strip()
        task_spec = rule.get("task", {}) if isinstance(rule.get("task"), dict) else {}

        for pat in globs_list:
            abs_pat = str(REPO_ROOT / pat)
            matches = sorted(set(glob.glob(abs_pat, recursive=True)))
            for m in matches:
                ap = Path(m)
                if not ap.exists() or ap.is_dir():
                    continue

                rel = repo_rel(ap)
                h = sha256_file(ap)

                key = f"{name}::{rel}"
                prev = files_state.get(key, {}) if isinstance(files_state.get(key), dict) else {}
                prev_hash = prev.get("sha256")

                # Record new state regardless
                files_state[key] = {"sha256": h, "last_seen_utc": utc_now_iso()}

                if first_run:
                    continue

                if prev_hash == h:
                    continue

                # Changed since last run -> create follow-on
                event_tag = f"[ARTIFACT:{name}:{h[:8]}]"
                if dispatch_queue_contains(event_tag):
                    continue

                seat = str(task_spec.get("seat", "")).strip()
                priority = str(task_spec.get("priority", "P2")).strip().upper()
                product = str(task_spec.get("product", "General")).strip()
                task_txt = str(task_spec.get("task", "")).strip() or f"Review updated artifact: {rel}"
                task_txt = format_task_template(task_txt, artifact_path=str(ap), artifact_relpath=rel)
                depends_on = str(task_spec.get("depends_on", "None")).strip() or "None"
                output_file = str(task_spec.get("output_file", "TBD")).strip() or "TBD"

                if target == "delegation_queue":
                    enqueued_rows.append(
                        {
                            "id": f"art-{name}-{h[:8]}",
                            "status": "NEW",
                            "created_utc": utc_now_iso(),
                            "seat": seat,
                            "priority": priority,
                            "product": product,
                            "task": f"{task_txt} {event_tag}",
                            "depends_on": depends_on,
                            "output_file": output_file,
                            "dispatched_utc": "",
                            "notes": f"Triggered by artifact: {rel}",
                        }
                    )
                else:
                    # dispatch_queue
                    prefix = "9."
                    if priority == "P0":
                        prefix = "0."
                    elif priority == "P1":
                        prefix = "1."
                    elif priority == "P2":
                        prefix = "2."
                    elif priority == "P3":
                        prefix = "3."

                    line = (
                        f"{prefix} [QUEUED] {seat} | ({product}) {task_txt} {event_tag} | {depends_on} | {output_file}\n"
                    )
                    queued_lines.append(line)

    # Apply changes
    inserted = 0
    if queued_lines:
        inserted = insert_lines_into_dispatch_queue(queued_lines)

    for row in enqueued_rows:
        append_row_to_delegation_queue(row)

    state["files"] = files_state
    state["last_run_utc"] = utc_now_iso()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    atomic_write_json(STATE_PATH, state)

    if first_run:
        print("Seeded artifact state (first run): no tasks dispatched.")
        return 0

    print(f"Artifact-triggered: {inserted} dispatch item(s), {len(enqueued_rows)} delegation item(s)")
    if not queued_lines and not enqueued_rows:
        print("No matching changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
