#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, sys

if len(sys.argv) < 7:
    print('Usage: update_codex_usage.py <five_hour_pct> <five_hour_reset> <weekly_pct> <weekly_reset> <code_review_pct> <credits_remaining> [notes]')
    sys.exit(1)

five_pct, five_reset, weekly_pct, weekly_reset, review_pct, credits = sys.argv[1:7]
notes = ' '.join(sys.argv[7:]).strip()

base = Path('/root/moxie/cmo')
csv_path = base / 'codex-usage-tracker.csv'
md_path = base / 'codex-usage.md'

gst = timezone(timedelta(hours=4))
ts = datetime.now(gst).strftime('%Y-%m-%d %H:%M')
last_updated = datetime.now(gst).strftime('%Y-%m-%d')

with csv_path.open('a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([ts, five_pct, five_reset, weekly_pct, weekly_reset, review_pct, credits, notes])

content = f"""# Codex Usage Tracker

Last updated: {last_updated}
Status: active

## Goal
Track manual Codex usage snapshots so Moxie can estimate burn rate, avoid running out of usage, and adjust work intensity.

## Latest snapshot
- Timestamp (GST): {ts}
- 5-hour remaining: {five_pct}%
- 5-hour reset: {five_reset}
- Weekly remaining: {weekly_pct}%
- Weekly reset: {weekly_reset}
- Code review remaining: {review_pct}%
- Credits remaining: {credits}

## Notes
- Source is founder-provided manual snapshot.
- Until there is a direct way to fetch this automatically, Moxie should update it from chat check-ins.
- Latest note: {notes or 'n/a'}
"""
md_path.write_text(content, encoding='utf-8')
print(f'Updated Codex usage tracker at {ts} GST')
