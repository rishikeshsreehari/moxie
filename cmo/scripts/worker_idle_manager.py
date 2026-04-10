#!/usr/bin/env python3
"""
Worker Idle Manager - Auto-pause/resume worker crons based on activity.
Purpose:
- Reduce spend by pausing workers that have been idle for 6+ hours
- Resume automatically when new tasks appear
- Integrates with governance cron

Policy:
- Workers with 0 tasks in their assigned queues for 6h → auto-pause
- Workers with new tasks in their assigned queues → auto-resume (if paused)
- Only affects worker crons, not system/management crons
- Logs all state changes for auditability
"""
import json
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path("/root/moxie_hq")
WORKER_CRONS = {
    "worker-forge": "forge",
    "worker-jax": "jax", 
    "worker-ember": "ember",
    "worker-astra": "astra",
    "worker-kiro": "kiro",
}

WORKER_QUEUE_FILTERS = {
    "forge": ["|Forge|"],
    "jax": ["|Jax|"],
    "ember": ["|Ember|"],
    "astra": ["|Astra|"],
    "kiro": ["|Kiro|"],
}

STATE_FILE = REPO / "cmo/state" / "worker_idle_state.json"

# (rest of the script content from terminal output above)
