#!/usr/bin/env python3
"""HQ pipeline runner with Paperclip-like audit logging.

Goals:
- Run the two core steps (delegation queue + artifacts) deterministically.
- Append an immutable JSONL ledger entry per step/run.
- Emit a single-line status usable by cron monitors:
    - 'OK: ...' when clean
    - 'BLOCKED: ...' for missing prerequisites / expected human input
    - 'ERROR: ...' for unexpected failures

This is intentionally small and dependency-free.
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path("/root/moxie_hq").resolve()
SCRIPTS_DIR = BASE_DIR / "cmo/scripts"
STATE_DIR = BASE_DIR / "cmo/state"
# Ledger is intentionally kept OUTSIDE git to avoid repo bloat.
LEDGER_PATH = Path("/opt/data/cache/moxie_run_ledger.jsonl")


@dataclass
class StepResult:
    name: str
    cmd: list[str]
    exit_code: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.exit_code == 0

    def classify(self) -> str:
        text = (self.stdout + "\n" + self.stderr).lower()
        if "blocked" in text:
            return "BLOCKED"
        if "error" in text or self.exit_code != 0:
            return "ERROR"
        return "OK"

    def excerpt(self, limit: int = 800) -> str:
        combined = (self.stdout + "\n" + self.stderr).strip()
        if not combined:
            return ""
        if len(combined) <= limit:
            return combined
        return combined[:limit] + "\n...<truncated>"


def run_step(name: str, script_name: str) -> StepResult:
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        return StepResult(
            name=name,
            cmd=["python3", str(script_path)],
            exit_code=2,
            stdout="",
            stderr=f"BLOCKED: missing script {script_path}",
        )

    p = subprocess.run(
        ["python3", str(script_path)],
        cwd=str(BASE_DIR),
        capture_output=True,
        text=True,
    )
    return StepResult(
        name=name,
        cmd=["python3", str(script_path)],
        exit_code=p.returncode,
        stdout=p.stdout or "",
        stderr=p.stderr or "",
    )


def append_ledger(run_id: str, step: StepResult) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "step": step.name,
        "cmd": step.cmd,
        "exit_code": step.exit_code,
        "status": step.classify(),
        "excerpt": step.excerpt(),
    }
    with LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main(argv: list[str]) -> int:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    steps = [
        ("delegation", "process_delegation_queue.py"),
        ("artifacts", "process_artifacts.py"),
    ]

    results: list[StepResult] = []
    for name, script in steps:
        r = run_step(name, script)
        append_ledger(run_id, r)
        results.append(r)
        if r.classify() in ("BLOCKED", "ERROR"):
            # Emit one-liner and stop.
            print(f"{r.classify()}: {r.excerpt(240).splitlines()[-1] if r.excerpt() else name}")
            return 2 if r.classify() == "BLOCKED" else 1

    # All OK so far. Run drift + receipt validation as guardrails.
    drift = subprocess.run(["python3", str(SCRIPTS_DIR / "drift_detector.py")], cwd=str(BASE_DIR), capture_output=True, text=True)
    drift_line = (drift.stdout or drift.stderr or "").strip().splitlines()[:1]
    drift_line = drift_line[0] if drift_line else "OK: drift check skipped"
    if drift.returncode == 2:
        print(drift_line)
        return 2
    if drift.returncode != 0:
        print(drift_line if drift_line else "ERROR: drift detector failed")
        return 1

    receipts = subprocess.run(["python3", str(SCRIPTS_DIR / "validate_receipts.py")], cwd=str(BASE_DIR), capture_output=True, text=True)
    receipts_line = (receipts.stdout or receipts.stderr or "").strip().splitlines()[:1]
    receipts_line = receipts_line[0] if receipts_line else "OK: receipt check skipped"
    if receipts.returncode != 0:
        print(receipts_line)
        return 1

    # Provide a tiny OK summary line to keep logs readable.
    print("OK: pipeline clean (delegation+artifacts+drift+receipts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
