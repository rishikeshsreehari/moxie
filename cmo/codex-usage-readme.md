# Codex Usage Automation Notes

Last updated: 2026-03-30

## Files
- /root/moxie/cmo/codex-usage.md
- /root/moxie/cmo/codex-usage-tracker.csv
- /root/moxie/cmo/scripts/update_codex_usage.py

## Purpose
Keep a manual log of Codex usage snapshots so Moxie can estimate burn rate and avoid running out of usage during important work windows.

## Current limitation
There is no direct authenticated API/source wired yet for automatic usage fetching, so the script updates from founder-provided snapshots.

## Example
python3 /root/moxie/cmo/scripts/update_codex_usage.py 53 '10:26 PM' 86 'Apr 6, 2026 5:26 PM' 100 0 'Founder shared live dashboard snapshot in chat'
