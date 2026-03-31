#!/usr/bin/env python3
"""Forward new/updated worker reports to Rishi via Telegram.

Design goal: workers (Mira/Astra/etc.) ALWAYS write reports to disk.
This script is the single Telegram sender (using the shared bot token).

State is stored in /opt/data/cache/report-forwarder.json
"""

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import requests

STATE_PATH = Path("/opt/data/cache/report-forwarder.json")
ENV_PATH = Path("/opt/data/.env")

DEFAULT_REPORTS = [
    ("formbeep-analytics", "/root/moxie/products/formbeep/analytics-report.md"),
    ("formbeep-umami-raw", "/root/moxie/products/formbeep/umami-full-data.json"),
    ("formbeep-keywords", "/root/moxie/products/formbeep/keyword-briefing.md"),
]


def read_env_value(key: str) -> Optional[str]:
    if not ENV_PATH.exists():
        return None
    m = re.search(rf"^{re.escape(key)}=(.+)$", ENV_PATH.read_text(), re.M)
    return m.group(1).strip() if m else None


def load_state() -> Dict:
    if not STATE_PATH.exists():
        return {"files": {}}
    try:
        return json.loads(STATE_PATH.read_text())
    except Exception:
        return {"files": {}}


def save_state(state: Dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2))


def tg_send_message(token: str, chat_id: str, text: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"Telegram sendMessage HTTP {resp.status_code}: {resp.text[:500]}")


def tg_send_document(token: str, chat_id: str, file_path: Path, caption: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    with file_path.open("rb") as f:
        resp = requests.post(
            url,
            data={"chat_id": chat_id, "caption": caption[:1024]},
            files={"document": (file_path.name, f)},
            timeout=60,
        )
    if resp.status_code != 200:
        raise RuntimeError(f"Telegram sendDocument HTTP {resp.status_code}: {resp.text[:500]}")


def summarize_text(path: Path, max_lines: int = 35) -> str:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return "(unreadable)"
    head = lines[:max_lines]
    more = max(0, len(lines) - len(head))
    s = "\n".join(head)
    if more:
        s += f"\n\n... ({more} more lines)"
    return s


def main(argv: List[str]) -> int:
    token = read_env_value("TELEGRAM_BOT_TOKEN")
    chat_id = read_env_value("TELEGRAM_CHAT_ID") or "6699776435"  # fallback
    if not token:
        print("BLOCKED: TELEGRAM_BOT_TOKEN missing in /opt/data/.env")
        return 2

    mode = "new"
    if "--all" in argv:
        mode = "all"

    state = load_state()
    sent_any = False

    for label, p in DEFAULT_REPORTS:
        path = Path(p)
        if not path.exists():
            continue

        mtime = int(path.stat().st_mtime)
        last_sent = int(state.get("files", {}).get(label, 0) or 0)
        should_send = (mode == "all") or (mtime > last_sent)
        if not should_send:
            continue

        caption = f"{label} updated (mtime={mtime}). Full path: {path}"

        # Prefer sending as a document for long reports
        try:
            if path.suffix in (".md", ".json") and path.stat().st_size < 4_000_000:
                tg_send_document(token, chat_id, path, caption)
            else:
                tg_send_message(token, chat_id, caption + "\n\n" + summarize_text(path))
        except Exception as e:
            print(f"BLOCKED: Telegram delivery failed: {e}")
            return 3

        state.setdefault("files", {})[label] = mtime
        sent_any = True

    save_state(state)

    if not sent_any:
        print("[SILENT]")
    else:
        print("OK: forwarded")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
