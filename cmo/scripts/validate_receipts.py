#!/usr/bin/env python3
"""Validate that completed tasks have evidence receipts in their artifacts.

Minimal receipt definition (any one):
- '## Receipts' or '## Receipt' section
- '## Evidence' section
- a 'Receipt:' header

Contract:
- OK: ...
- ERROR: ...
Exit 0 OK, 1 ERROR

Fast + dependency-free.
"""

from __future__ import annotations

import re
from pathlib import Path

BASE = Path("/root/moxie_hq")
DISPATCH = BASE / "cmo/dispatch-queue.md"


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def _artifact_paths(dispatch_text: str) -> list[Path]:
    paths: list[Path] = []

    for m in re.finditer(r"Output path:\s*(/[^\s]+)", dispatch_text):
        paths.append(Path(m.group(1)))

    for ln in dispatch_text.splitlines():
        if "COMPLETED" not in ln:
            continue
        if "|" in ln and ln.lstrip().startswith("["):
            parts = ln.split("|")
            if len(parts) >= 4:
                candidate = parts[3].strip()
                if candidate.startswith("/"):
                    paths.append(Path(candidate))
                elif candidate:
                    paths.append((BASE / candidate).resolve())

    # Dedup
    out = []
    seen = set()
    for p in paths:
        s = str(p)
        if s not in seen:
            seen.add(s)
            out.append(p)
    return out


def _has_receipt(text: str) -> bool:
    t = text.lower()
    if "## receipts" in t or "## receipt" in t:
        return True
    if "## evidence" in t:
        return True
    if "receipt:" in t:
        return True
    return False


def main() -> int:
    dispatch = _read(DISPATCH)
    artifacts = _artifact_paths(dispatch)

    missing = [p for p in artifacts if str(p).startswith("/") and not p.exists()]
    if missing:
        print(f"ERROR: missing artifact files ({len(missing)})")
        return 1

    no_receipt = []
    for p in artifacts:
        if not p.exists():
            continue
        if not _has_receipt(_read(p)):
            no_receipt.append(p)

    if no_receipt:
        print(f"ERROR: artifacts missing receipts ({len(no_receipt)})")
        return 1

    print("OK: receipts validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
