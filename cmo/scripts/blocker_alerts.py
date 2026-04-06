#!/usr/bin/env python3
import os, json, pathlib, datetime, sys

ISSUES_PATH = pathlib.Path('/root/moxie_hq/cmo/issues_rishi.md')
STATE_PATH = pathlib.Path('/root/moxie_hq/cmo/state/blocker_alert_state.json')
MAX_PER_DAY = 3

def load_state():
    if STATE_PATH.exists():
        try:
            return json.load(STATE_PATH.open())
        except Exception:
            return {}
    return {}

def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    json.dump(state, STATE_PATH.open('w'))

def main():
    if not ISSUES_PATH.exists():
        print('[SILENT]')
        return 0
    text = ISSUES_PATH.read_text(errors='replace')
    # look for BLOCKED or ERROR lines
    lines = [l for l in text.splitlines() if ('BLOCKED' in l or 'ERROR' in l)]
    if not lines:
        print('[SILENT]')
        return 0
    today = datetime.date.today().isoformat()
    state = load_state()
    count = state.get('date_counts', {}).get(today, 0)
    if count >= MAX_PER_DAY:
        print('[SILENT]')
        return 0
    # send via telegram using existing helper
    from forward_reports import tg_send_message, read_env_value
    token = read_env_value('TELEGRAM_BOT_TOKEN')
    chat_id = read_env_value('TELEGRAM_CHAT_ID') or '6699776435'
    if not token:
        print('BLOCKED: TELEGRAM_BOT_TOKEN missing')
        return 2
    msg = '\n'.join(lines)
    tg_send_message(token, chat_id, msg)
    # update count
    state.setdefault('date_counts', {})[today] = count + 1
    save_state(state)
    return 0

if __name__ == '__main__':
    sys.exit(main())
