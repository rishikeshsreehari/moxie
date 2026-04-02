#!/usr/bin/env python3
"""Safe HQ repo cleanup."""

import os
import time
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path("/root/moxie_hq")
PROTECTED = {
    "cmo/sops", "cmo/resources", "cmo/employees", "cmo/strategy",
    "cmo/delegation-queue.md", "cmo/dispatch-queue.md", "cmo/orchestration.md",
    "cmo/rishi_review.md", "cmo/issues_rishi.md",
}
NOW = time.time()
CUTOFF_DAYS = 30
CUTOFF = NOW - CUTOFF_DAYS * 86400

def is_protected(p: Path) -> bool:
    rel = str(p.relative_to(ROOT))
    if any(rel.startswith(pp) for pp in PROTECTED):
        return True
    if p.suffix in {".md", ".yaml", ".yml", ".txt", ".csv", ".json"} and "cmo" in p.parts:
        return True
    return False

def gen_candidates():
    candidates = []
    for root, dirs, files in os.walk(ROOT, topdown=True):
        # skip .git
        if ".git" in dirs:
            dirs.remove(".git")
        rp = Path(root)
        # dirs
        for d in list(dirs):
            dp = rp / d
            if dp.name == "__pycache__":
                candidates.append(dp)
                dirs.remove(d)  # don't recurse into it
        # files
        for f in files:
            fp = rp / f
            if is_protected(fp):
                continue
            # remove common junk
            if fp.suffix in {".pyc", ".pyo"}:
                candidates.append(fp)
            elif fp.name.endswith("~"):
                candidates.append(fp)
            elif fp.name.startswith(".#"):
                candidates.append(fp)
            elif fp.name == ".DS_Store":
                candidates.append(fp)
            elif fp.suffix == ".swp":
                candidates.append(fp)
            elif fp.name.endswith(".bak"):
                candidates.append(fp)
            elif fp.name.startswith("copy"):
                candidates.append(fp)
            elif fp.name.startswith("temp"):
                candidates.append(fp)
            # very old logs under cmo/logs or cmo/analytics? only if >30d
            elif "log" in fp.parts and fp.stat().st_mtime < CUTOFF:
                candidates.append(fp)
    return candidates

def main():
    cand = gen_candidates()
    report = []
    total_size = 0
    for p in cand:
        try:
            sz = p.stat().st_size if p.is_file() else 0
            total_size += sz
            report.append((p, sz))
        except Exception:
            pass

    report.sort(key=lambda x: x[1], reverse=True)
    out_dir = ROOT / "cmo" / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"repo-health-audit-{datetime.now().strftime('%Y-%m-%d')}.md"
    lines = [
        "# Repo Health Audit\n",
        f"Generated: {datetime.now().isoformat()}\n",
        f"Total candidates: {len(report)}\n",
        f"Total size (bytes): {total_size}\n",
        "\n## Candidates (largest first)\n",
        "| Size (KB) | Path |\n|---|---|",
    ]
    for p, sz in report[:100]:
        lines.append(f"| {sz//1024} | {p} |")
    out_path.write_text("\n".join(lines))
    print(f"OK {out_path}")

if __name__ == "__main__":
    main()
