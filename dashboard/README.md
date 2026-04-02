# SapiensTech Open Ops (Public)

This is a public-safe operations dashboard built with **7.css**.

## What it shows
- CEO metrics (traffic/signups/revenue)
- Execution map (draggable, collision-avoiding)
- Running tasks + highlights
- Team status
- Needs CEO (blockers)
- Products table
- Shipping (recent commits)

## Safety
The snapshot (`public_snapshot.json`) is intended to be sanitized:
- no emails / phone numbers
- no secrets
- no user-level analytics

## Local run
```bash
cd /root/moxie_hq
python3 -m http.server 8099 --directory dashboard
```
Then open `http://127.0.0.1:8099/index.html`.

## Snapshot generation
If you use `generate_snapshot.py`, it can overwrite `public_snapshot.json` with a sanitized snapshot.
