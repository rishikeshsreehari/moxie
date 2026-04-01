#!/usr/bin/env python3
import os
import subprocess
import sys
import datetime

os.chdir('/root/moxie_hq')

# Ensure lock directory exists
lock_path = '.git/moxie_autopush.lock'
open(lock_path, 'a').close()

# Acquire lock via flock
acquire = subprocess.run(['flock', '-w', '60', lock_path, 'true'])
if acquire.returncode != 0:
    print('Failed to acquire lock')
    sys.exit(1)

# Run gated push inside the lock shell
cmd = '''git config user.name "Moxie" && git config user.email "moxie@rishikeshs.com" && git add -A && if git diff --cached --quiet; then echo "No staged changes."; else timestamp=$(date -u +"%Y-%m-%d %H:%M:%S UTC"); git commit -m "Autopush: $timestamp" && git push origin main; fi'''
result = subprocess.run(['bash', '-c', cmd], capture_output=False, text=True)
sys.exit(result.returncode)
