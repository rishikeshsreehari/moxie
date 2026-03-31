#!/usr/bin/env python3
"""
Token Optimizer — Pause idle workers, reduce cron frequency
Usage: python token-optimizer.py [--apply]
"""
import subprocess
import sys
import re
from datetime import datetime

IDLE_THRESHOLD_HOURS = 6  # Pause workers idle for 6+ hours
WORKER_CRONS = [
    "vale-worker", "astra-worker", "kiro-worker", "ember-worker",
    "forge-worker", "jax-worker", "rumi-worker", "nova-worker",
    "luna-worker", "pax-worker", "orion-worker"
]

def get_cron_list():
    """Get current cron jobs."""
    result = subprocess.run(
        ["hermes", "cron", "list"],
        capture_output=True, text=True
    )
    return result.stdout

def parse_cron_status(output):
    """Parse cron list to find worker statuses."""
    workers = {}
    for line in output.split('\n'):
        for worker in WORKER_CRONS:
            if worker in line:
                # Extract state
                if "paused" in line.lower():
                    workers[worker] = "paused"
                elif "scheduled" in line.lower():
                    workers[worker] = "scheduled"
                else:
                    workers[worker] = "unknown"
    return workers

def check_worker_idle_time(worker):
    """Check if worker has been idle (no tasks completed recently)."""
    # Read orchestration.md to find last completion
    try:
        with open("/root/moxie_hq/cmo/orchestration.md") as f:
            content = f.read()
        
        # Look for worker name in completed deliverables
        pattern = rf"\| ([0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}}) \| {worker.capitalize()} \|"
        matches = re.findall(pattern, content)
        
        if not matches:
            return float('inf')  # Never completed anything
        
        last_date = max(matches)
        last_dt = datetime.strptime(last_date, "%Y-%m-%d")
        hours_idle = (datetime.utcnow() - last_dt).total_seconds() / 3600
        return hours_idle
    except Exception as e:
        print(f"Error checking {worker}: {e}")
        return 0

def pause_worker(worker):
    """Pause a worker cron."""
    # Find cron ID
    output = get_cron_list()
    for line in output.split('\n'):
        if worker in line:
            parts = line.split()
            if parts:
                cron_id = parts[0]
                subprocess.run(
                    ["hermes", "cron", "pause", cron_id, 
                     "--reason", f"Idle {IDLE_THRESHOLD_HOURS}+ hours — auto-paused by token-optimizer"],
                    capture_output=True
                )
                print(f"  Paused {worker} ({cron_id})")
                return True
    return False

def resume_worker(worker):
    """Resume a worker cron."""
    output = get_cron_list()
    for line in output.split('\n'):
        if worker in line and "paused" in line.lower():
            parts = line.split()
            if parts:
                cron_id = parts[0]
                subprocess.run(
                    ["hermes", "cron", "resume", cron_id],
                    capture_output=True
                )
                print(f"  Resumed {worker} ({cron_id})")
                return True
    return False

def main():
    apply_mode = "--apply" in sys.argv
    
    print("Token Optimizer Analysis")
    print("=" * 50)
    
    cron_output = get_cron_list()
    worker_status = parse_cron_status(cron_output)
    
    to_pause = []
    to_resume = []
    
    for worker in WORKER_CRONS:
        status = worker_status.get(worker, "unknown")
        idle_hours = check_worker_idle_time(worker)
        
        print(f"\n{worker}:")
        print(f"  Status: {status}")
        print(f"  Idle: {idle_hours:.1f} hours")
        
        if status == "scheduled" and idle_hours > IDLE_THRESHOLD_HOURS:
            to_pause.append(worker)
            print(f"  → RECOMMEND: PAUSE (idle {idle_hours:.1f}h)")
        elif status == "paused" and idle_hours < IDLE_THRESHOLD_HOURS / 2:
            to_resume.append(worker)
            print(f"  → RECOMMEND: RESUME (active again)")
        else:
            print(f"  → No action")
    
    print("\n" + "=" * 50)
    print(f"Recommended pauses: {len(to_pause)}")
    print(f"Recommended resumes: {len(to_resume)}")
    
    if not apply_mode:
        print("\nRun with --apply to execute changes")
        return
    
    print("\nApplying changes...")
    for worker in to_pause:
        pause_worker(worker)
    for worker in to_resume:
        resume_worker(worker)
    
    print("\nDone. Run 'hermes cron list' to verify.")

if __name__ == "__main__":
    main()
