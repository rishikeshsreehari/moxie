#!/usr/bin/env python3
"""Safe HQ repo cleanup.

Default: dry-run report.
Optional: apply safe deletions (junk files + __pycache__) via --apply.
"""

import argparse
import os
import shutil
import time
from datetime import datetime
from pathlib import Path

ROOT = Path("/root/moxie_hq")
PROTECTED_PREFIXES = (
    "cmo/sops", "cmo/resources", "cmo/employees", "cmo/strategy",
)
PROTECTED_FILES = {
    "cmo/delegation-queue.md", "cmo/dispatch-queue.md", "cmo/orchestration.md",
    "cmo/rishi_review.md", "cmo/issues_rishi.md",
}

NOW = time.time()
CUTOFF_DAYS = 30
CUTOFF = NOW - CUTOFF_DAYS * 86400


def is_protected(p: Path) -> bool:
    rel = str(p.relative_to(ROOT))
    if rel in PROTECTED_FILES:
        return True
    if any(rel.startswith(pp) for pp in PROTECTED_PREFIXES):
        return True
    # Conservative: never delete structured artifacts under cmo/
    if "cmo" in p.parts and p.suffix in {".md", ".yaml", ".yml", ".txt", ".csv", ".json"}:
        return True
    return False


def classify(fp: Path):
    if fp.name == "__pycache__" and fp.is_dir():
        return "dir.__pycache__"
    if fp.is_file():
        if fp.suffix in {".pyc", ".pyo"}:
            return "file.pyc"
        if fp.name == ".DS_Store":
            return "file.ds_store"
        if fp.suffix in {".swp", ".swo"}:
            return "file.swap"
        if fp.name.endswith("~") or fp.name.startswith(".#"):
            return "file.editor_tmp"
        if fp.name.endswith(".bak"):
            return "file.bak"
        if fp.name.startswith("temp"):
            return "file.temp"
        if "log" in fp.parts and fp.stat().st_mtime < CUTOFF:
            return "file.old_log"
    return None


def gen_candidates():
    candidates = []
    for root, dirs, files in os.walk(ROOT, topdown=True):
        if ".git" in dirs:
            dirs.remove(".git")
        rp = Path(root)

        # dirs
        for d in list(dirs):
            dp = rp / d
            kind = classify(dp)
            if kind == "dir.__pycache__":
                candidates.append((dp, kind))
                dirs.remove(d)  # don't recurse

        # files
        for f in files:
            fp = rp / f
            if is_protected(fp):
                continue
            kind = classify(fp)
            if kind:
                candidates.append((fp, kind))

    return candidates


def delete_path(p: Path):
    if p.is_dir():
        shutil.rmtree(p)
    else:
        p.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Actually delete safe junk candidates")
    args = ap.parse_args()

    cand = gen_candidates()

    rows = []
    total_size = 0
    for p, kind in cand:
        try:
            sz = p.stat().st_size if p.is_file() else 0
        except Exception:
            sz = 0
        rows.append((p, kind, sz))
        total_size += sz

    rows.sort(key=lambda x: x[2], reverse=True)

    out_dir = ROOT / "cmo" / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"repo-health-audit-{datetime.now().strftime('%Y-%m-%d')}.md"

    deleted = []
    errors = []
    if args.apply:
        for p, kind, sz in rows:
            try:
                if is_protected(p):
                    continue
                delete_path(p)
                deleted.append((p, kind, sz))
            except Exception as e:
                errors.append((p, kind, str(e)))

    lines = [
        "# Repo Health Audit\n",
        f"Generated: {datetime.now().isoformat()}\n",
        f"Mode: {'APPLY (deleted)' if args.apply else 'DRY-RUN'}\n",
        f"Total candidates: {len(rows)}\n",
        f"Total size (bytes, files only): {total_size}\n",
        "\n## Candidates (largest first)\n",
        "| Size (KB) | Kind | Path |\n|---:|---|---|",
    ]

    for p, kind, sz in rows[:200]:
        lines.append(f"| {sz//1024} | {kind} | {p} |")

    if args.apply:
        lines += [
            "\n## Deleted\n",
            "| Size (KB) | Kind | Path |\n|---:|---|---|",
        ]
        for p, kind, sz in deleted[:500]:
            lines.append(f"| {sz//1024} | {kind} | {p} |")

        if errors:
            lines += [
                "\n## Errors\n",
                "| Kind | Path | Error |\n|---|---|---|",
            ]
            for p, kind, err in errors:
                lines.append(f"| {kind} | {p} | {err} |")

    out_path.write_text("\n".join(lines))
    print(f"OK {out_path}")


if __name__ == "__main__":
    main()
