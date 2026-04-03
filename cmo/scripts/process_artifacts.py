#!/usr/bin/env python3
"""
Artifact watcher: rules trigger follow-on tasks when files change.
First run seeds state; subsequent runs dispatch on hash changes.
"""

import sys
import yaml
import hashlib
from datetime import datetime
from pathlib import Path

BASE_DIR = Path('/root/moxie_hq').resolve()
RULES_FILE = BASE_DIR / 'cmo/artifact-rules.yaml'
STATE_FILE = BASE_DIR / 'cmo/state/artifact_state.json'
DISPATCH_QUEUE = BASE_DIR / 'cmo/dispatch-queue.md'
DELEGATION_QUEUE = BASE_DIR / 'cmo/delegation-queue.md'

def file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def load_state():
    import json
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_state(state):
    import json
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def load_rules():
    with open(RULES_FILE, 'r') as f:
        return yaml.safe_load(f).get('rules', [])

def get_dispatch_lines():
    if not DISPATCH_QUEUE.exists():
        return []
    with open(DISPATCH_QUEUE, 'r') as f:
        return [line.rstrip() for line in f if line.strip()]

def get_delegation_lines():
    if not DELEGATION_QUEUE.exists():
        return []
    with open(DELEGATION_QUEUE, 'r') as f:
        return [line.rstrip() for line in f if line.strip()]

def append_dispatch_item(seat, priority, product, task, output_file, depends_on, tags):
    import hashlib
    ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    task_hash = hashlib.sha1(task.encode()).hexdigest()[:6]
    item_id = f"{seat.lower()}-{ts}-{task_hash}"
    meta = ""
    caption = ""
    line = f"[{priority}] {product}|{seat}|{task}|{output_file}|{item_id}|{tags}|#{meta}"
    if caption:
        line += f"|caption:{caption}"
    with open(DISPATCH_QUEUE, 'a') as f:
        f.write(line + '\n')
    return line

def append_delegation_item(seat, priority, product, task, output_file, depends_on, tags):
    """Append to delegation-queue.md table."""
    # Read current delegation file
    with open(DELEGATION_QUEUE, 'r') as f:
        content = f.read()
    # Find table start
    lines = content.split('\n')
    # Find header line that starts with '| id'
    table_start_idx = None
    for i, line in enumerate(lines):
        if line.startswith('|') and 'id' in line.lower():
            table_start_idx = i
            break
    if table_start_idx is None:
        print("ERROR: No table found in delegation-queue.md")
        return
    # Build new row
    import hashlib
    ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    task_hash = hashlib.sha1(task.encode()).hexdigest()[:6]
    item_id = f"{seat.lower()}-{ts}-{task_hash}"
    status = "DISPATCHED"  # auto-dispatched from artifact
    created_utc = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    dispatched_utc = created_utc
    # We need to fill columns: id, status, created_utc, seat, priority, product, task, depends_on, output_file, dispatched_utc, notes
    # We'll match the header order. Get header cells:
    header_cells = [c.strip() for c in lines[table_start_idx].split('|')[1:-1]]
    num_cols = len(header_cells)
    row = [''] * num_cols
    # Map by header name (case-insensitive)
    col_idx = {name.lower(): i for i, name in enumerate(header_cells)}
    for col in ['id', 'status', 'created_utc', 'seat', 'priority', 'product', 'task', 'depends_on', 'output_file', 'dispatched_utc', 'notes']:
        if col in col_idx:
            idx = col_idx[col]
            if col == 'id':
                row[idx] = item_id
            elif col == 'status':
                row[idx] = status
            elif col == 'created_utc':
                row[idx] = created_utc
            elif col == 'seat':
                row[idx] = seat
            elif col == 'priority':
                row[idx] = priority
            elif col == 'product':
                row[idx] = product
            elif col == 'task':
                row[idx] = task
            elif col == 'depends_on':
                row[idx] = depends_on if depends_on else ''
            elif col == 'output_file':
                row[idx] = output_file
            elif col == 'dispatched_utc':
                row[idx] = dispatched_utc
            elif col == 'notes':
                row[idx] = tags
    # Insert row right after the separator line (which is table_start_idx+1)
    new_row_str = '| ' + ' | '.join(row) + ' |'
    lines.insert(table_start_idx + 2, new_row_str)
    # Write back
    with open(DELEGATION_QUEUE, 'w') as f:
        f.write('\n'.join(lines))
    return new_row_str

def main():
    print(f"Processing artifacts with rules: {RULES_FILE}")
    if not RULES_FILE.exists():
        print("ERROR: artifact-rules.yaml not found")
        sys.exit(1)

    rules = load_rules()
    state = load_state()
    dispatch_lines = get_dispatch_lines()
    delegation_lines = get_delegation_lines()

    # Performance: avoid repeated O(n) scans with `any(tag in line for line in ...)`
    dispatch_text = "\n".join(dispatch_lines)
    delegation_text = "\n".join(delegation_lines)
    base_dir = BASE_DIR

    changed_any = False
    for rule in rules:
        if not rule.get('enabled', True):
            continue
        rule_name = rule['name']
        target = rule.get('target', 'dispatch_queue')
        globs = rule['globs']
        task_cfg = rule['task']

        # Gather matching files
        matches = []
        for glob in globs:
            # Simple glob using pathlib Path.rglob pattern (glob in rglob is **/*.md style)
            # But rglob doesn't support ** directly, we can use rglob with pattern relative
            if glob.startswith('**/'):
                pattern = glob[3:]  # strip **/
            else:
                pattern = glob
            # Use rglob for recursive
            matches.extend(base_dir.rglob(pattern))
        # Dedupe and restrict to files
        matches = [p for p in set(matches) if p.is_file()]

        for path in matches:
            try:
                relpath = str(path.relative_to(base_dir))
                current_hash = file_hash(path)
                key = f"{rule_name}:{relpath}"
                old_hash = state.get(key)
                if old_hash is None:
                    # First run: seed state
                    state[key] = current_hash
                    print(f"Seeded {key}")
                    continue
                if current_hash == old_hash:
                    continue
                # Hash changed: dispatch
                state[key] = current_hash
                # Build task message with template substitution
                task = task_cfg['task'].format(artifact_path=str(path), artifact_relpath=relpath)
                seat = task_cfg.get('seat', '')
                priority = task_cfg.get('priority', 'P2')
                product = task_cfg.get('product', '*')
                output_file = task_cfg.get('output_file', '')
                depends_on = task_cfg.get('depends_on', '')
                caption = ''  # could be extracted from notes?
                tag = f"[ARTIFACT:{rule_name}:{current_hash[:8]}]"
                if target == 'dispatch_queue':
                    # Dedupe: check if this tag already exists in dispatch queue
                    if tag in dispatch_text:
                        print(f"Skipping duplicate dispatch for {key}")
                        continue
                    line = append_dispatch_item(seat, priority, product, task, output_file, depends_on, tag)
                    dispatch_lines.append(line)
                    changed_any = True
                    print(f"Dispatched to dispatch-queue: {key}")
                elif target == 'delegation_queue':
                    # Dedupe: check delegation queue
                    if tag in delegation_text:
                        print(f"Skipping duplicate delegation for {key}")
                        continue
                    # Append a row to delegation-queue.md
                    row_line = append_delegation_item(seat, priority, product, task, output_file, depends_on, tag)
                    delegation_lines.append(row_line)
                    changed_any = True
                    print(f"Dispatched to delegation-queue: {key}")
            except Exception as e:
                print(f"Error processing {path}: {e}")
                continue

    # Save updated state
    save_state(state)
    if changed_any:
        print("Artifact processing completed with dispatches")
    else:
        print("No artifact changes detected")

if __name__ == '__main__':
    main()
