#!/usr/bin/env python3
"""Notify Rishi on Telegram when issues_rishi.md has new open items.

Heuristic: send when file mtime increases AND there is at least one unchecked item in '## Open'.
Filters out items that are resolved per OPERATING_ASSUMPTIONS.md.
State: /opt/data/cache/issues-notify.json
"""

import json
import re
import sys
from pathlib import Path

import requests

ISSUES_PATH = Path("/root/moxie_hq/cmo/issues_rishi.md")
STATE_PATH = Path("/opt/data/cache/issues-notify.json")
ENV_PATH = Path("/opt/data/.env")


def read_env_value(key: str):
    if not ENV_PATH.exists():
        return None
    m = re.search(rf"^{re.escape(key)}=(.+)$", ENV_PATH.read_text(), re.M)
    return m.group(1).strip() if m else None


def load_state():
    if not STATE_PATH.exists():
        return {"last_mtime": 0}
    try:
        return json.loads(STATE_PATH.read_text())
    except Exception:
        return {"last_mtime": 0}


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2))


def has_open_items(text: str) -> bool:
    # Anything like: - [ ] ... under Open section
    m = re.search(r"## Open(.*?)(?:## Resolved|\Z)", text, re.S)
    if not m:
        return False
    open_block = m.group(1)
    
    # Get operating assumptions
    try:
        sys.path.insert(0, '/root/moxie_hq/cmo/scripts')
        from read_operating_assumptions import get_operating_assumptions, should_suppress_issue
        assumptions = get_operating_assumptions()
    except Exception:
        # Fall back to original behavior if assumptions can't be loaded
        return bool(re.search(r"^- \[ \]", open_block, re.M))
    
    # Check each open item to see if it should be suppressed
    lines = open_block.split('\n')
    open_items = []
    
    for line in lines:
        if line.strip().startswith("- [ ]"):
            item_text = line.strip()[4:].strip()  # Remove "- [ ]"
            if not should_suppress_issue(item_text, assumptions):
                open_items.append(line)
    
    return len(open_items) > 0


def summarize_open(text: str, max_lines: int = 30) -> str:
    m = re.search(r"## Open(.*?)(?:## Resolved|\Z)", text, re.S)
    if not m:
        return "(No Open section found)"
    open_block = m.group(1)
    lines = open_block.split('\n')
    
    # Get operating assumptions
    try:
        sys.path.insert(0, '/root/moxie_hq/cmo/scripts')
        from read_operating_assumptions import get_operating_assumptions, should_suppress_issue
        assumptions = get_operating_assumptions()
    except Exception:
        # Fall back to original behavior if assumptions can't be loaded
        lines = [ln.rstrip() for ln in open_block.strip().splitlines() if ln.strip()]
        if not lines:
            return "(No open items)"
        out = []
        for ln in lines:
            if ln.lstrip().startswith("-"):
                out.append(ln)
            if len(out) >= max_lines:
                break
        more = "" if len(out) < len(lines) else "\n..."
        return "\n".join(out) + more
    
    # Filter out items that should be suppressed
    out = []
    for line in lines:
        if line.strip().startswith("- [ ]"):
            item_text = line.strip()[4:].strip()  # Remove "- [ ]"
            if not should_suppress_issue(item_text, assumptions):
                out.append(line.strip())
        elif line.strip().startswith("- [x]"):
            out.append(line.strip())  # Include completed items for context
    
    if not out:
        return "(No open items after filtering resolved)"
    
    if len(out) >= max_lines:
        more = "\n..."
    else:
        more = ""
    
    return "\n".join(out[:max_lines]) + more


def send_telegram(token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"Telegram HTTP {resp.status_code}: {resp.text[:300]}")


def main(argv):
    if not ISSUES_PATH.exists():
        print("[SILENT]")
        return 0

    text = ISSUES_PATH.read_text(encoding="utf-8", errors="replace")
    mtime = int(ISSUES_PATH.stat().st_mtime)

    state = load_state()
    last = int(state.get("last_mtime", 0) or 0)

    force = "--force" in argv

    if (not force) and (mtime <= last):
        print("[SILENT]")
        return 0

    # Safety: do not require Telegram credentials (and do not send) if there are no open items.
    if not has_open_items(text):
        state["last_mtime"] = mtime
        save_state(state)
        print("[SILENT]")
        return 0

    token = read_env_value("TELEGRAM_BOT_TOKEN")
    chat_id = read_env_value("TELEGRAM_CHAT_ID") or "6699776435"
    if not token:
        print("BLOCKED: TELEGRAM_BOT_TOKEN missing")
        return 2

    msg = "issues_rishi.md has open items:\n\n" + summarize_open(text)
    send_telegram(token, chat_id, msg)

    state["last_mtime"] = mtime
    save_state(state)
    print("OK: notified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
