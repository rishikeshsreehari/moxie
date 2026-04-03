#!/usr/bin/env python3
"""
Worker Idle Manager - Auto-pause/resume worker crons based on activity.

Purpose:
- Reduce spend by pausing workers that have been idle for 6+ hours
- Resume automatically when new tasks appear in their queue
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
    # worker-luna, worker-orion, worker-pax, worker-rumi, worker-mira intentionally omitted
    # - they are either not active or don't have dedicated crons
}

# Mapping of worker names to their queue filter patterns
WORKER_QUEUE_FILTERS = {
    "forge": ["|Forge|"],
    "jax": ["|Jax|"],
    "ember": ["|Ember|"],
    "astra": ["|Astra|"],
    "kiro": ["|Kiro|"],
}

# State file
STATE_FILE = REPO / "cmo/state" / "worker_idle_state.json"


def load_state():
    """Load worker idle state from file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"workers": {}}


def save_state(state):
    """Save worker idle state to file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def get_cron_status(cron_name):
    """Get whether a cron job is enabled/disabled."""
    try:
        result = subprocess.run(
            ["hermes", "cron", "show", cron_name],
            capture_output=True, text=True, check=True
        )
        # Parse output to find enabled status
        for line in result.stdout.split('\n'):
            if "enabled:" in line:
                return "true" in line.lower()
        return True  # Default to enabled if not found
    except subprocess.CalledProcessError:
        return False


def set_cron_status(cron_name, enabled):
    """Enable or disable a cron job."""
    action = "resume" if enabled else "pause"
    try:
        subprocess.run(
            ["hermes", "cron", action, cron_name],
            check=True, capture_output=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to {action} {cron_name}: {e.stderr}")
        return False


def check_worker_tasks(worker_name):
    """Check if a worker has any tasks in their queue."""
    filters = WORKER_QUEUE_FILTERS.get(worker_name, [])
    if not filters:
        return False
    
    try:
        # Check dispatch queue for worker tasks
        dq_path = REPO / "cmo" / "dispatch-queue.md"
        if dq_path.exists():
            dq_content = dq_path.read_text(encoding='utf-8')
            for line in dq_content.split('\n'):
                if any(filt in line for filt in filters):
                    # Found a task for this worker
                    return True
        
        # Check delegation queue for worker tasks
        dl_path = REPO / "cmo" / "delegation-queue.md" 
        if dl_path.exists():
            # Simple check - delegation queue is more complex to parse
            # For now, just check if any worker name appears
            dl_content = dl_path.read_text(encoding='utf-8')
            for line in dl_content.split('\n'):
                if worker_name.capitalize() in line:
                    return True
        
        return False
    except Exception as e:
        print(f"ERROR checking tasks for {worker_name}: {e}")
        return False


def main():
    """Main worker idle management logic."""
    print(f"Worker idle manager checking at {datetime.now(timezone.utc).isoformat()}")
    
    state = load_state()
    workers_state = state.get("workers", {})
    now = datetime.now(timezone.utc)
    changes_made = []
    
    # Check each worker
    for cron_name, worker_name in WORKER_CRONS.items():
        current_status = get_cron_status(cron_name)
        has_tasks = check_worker_tasks(worker_name)
        
        # Get previous state
        worker_state = workers_state.get(worker_name, {})
        was_paused = worker_state.get("paused", False)
        last_check = worker_state.get("last_check")
        
        # Determine action
        action = None
        pause_reason = None
        
        if current_status and not has_tasks:
            # Worker is enabled but has no tasks
            if last_check:
                try:
                    last_check_dt = datetime.fromisoformat(last_check.replace('Z', '+00:00'))
                    if now - last_check_dt >= timedelta(hours=6):
                        # Idle for 6+ hours - pause it
                        action = "pause"
                        pause_reason = "idle_6h"
                except Exception:
                    pass
            
        elif not current_status and has_tasks:
            # Worker is paused but now has tasks - resume it
            action = "resume"
            pause_reason = "tasks_available"
        
        # Execute action if needed
        if action:
            success = set_cron_status(cron_name, action == "resume")
            if success:
                # Update state
                workers_state[worker_name] = {
                    "paused": action == "pause",
                    "last_check": now.isoformat(),
                    "last_action": action,
                    "pause_reason": pause_reason,
                    "has_tasks": has_tasks
                }
                changes_made.append(f"{worker_name}: {action} (reason: {pause_reason})")
                print(f"{worker_name}: {action} (has_tasks: {has_tasks}, reason: {pause_reason})")
            else:
                print(f"Failed to {action} {cron_name}")
        else:
            # No action needed, just update last check time
            workers_state[worker_name] = {
                "paused": not current_status,
                "last_check": now.isoformat(),
                "has_tasks": has_tasks,
                "last_action": "no_action"
            }
    
    # Save updated state
    state["workers"] = workers_state
    save_state(state)
    
    # Summary
    if changes_made:
        print(f"Worker idle manager: Made {len(changes_made)} changes:")
        for change in changes_made:
            print(f"  - {change}")
    else:
        print("Worker idle manager: No changes needed")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())