#!/usr/bin/env python3
"""
Process the delegation queue: promote work orders into dispatch-queue.md.
Idempotent: uses [DELEGATION:<id>] tags to avoid duplicates.
"""

import sys
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path('/root/moxie_hq').resolve()
DELEGATION_QUEUE = BASE_DIR / 'cmo/delegation-queue.md'
DISPATCH_QUEUE = BASE_DIR / 'cmo/dispatch-queue.md'

# Safety: ensure we stay within /root/moxie_hq/cmo
if not str(DELEGATION_QUEUE).startswith(str(BASE_DIR / 'cmo')):
    print("ERROR: Delegation queue path outside allowed dir")
    sys.exit(1)
if not str(DISPATCH_QUEUE).startswith(str(BASE_DIR / 'cmo')):
    print("ERROR: Dispatch queue path outside allowed dir")
    sys.exit(1)

def parse_table_lines(lines):
    """Parse markdown table rows, return header and data rows.
    Handles rows with or without trailing pipe."""
    header = None
    rows = []
    in_table = False
    for line in lines:
        line = line.rstrip()
        if line.startswith('|'):
            in_table = True
            # Remove leading and trailing pipe if present, then split
            stripped = line.strip()
            if stripped.startswith('|'):
                stripped = stripped[1:]
            if stripped.endswith('|'):
                stripped = stripped[:-1]
            cells = [c.strip() for c in stripped.split('|')]
            if header is None:
                header = cells
            else:
                rows.append(cells)
        elif in_table:
            break  # table ended
    return header, rows

def find_row_by_id(rows, row_id):
    for i, row in enumerate(rows):
        if row and row[0] == row_id:
            return i, row
    return None, None

def update_delegation_queue(header, rows, updates):
    """Write updated delegation queue with modified rows."""
    with open(DELEGATION_QUEUE, 'r') as f:
        content = f.read()

    # Reconstruct table
    table_lines = []
    table_lines.append('| ' + ' | '.join(header) + ' |')
    table_lines.append('|' + '|'.join(['---'] * len(header)) + '|')
    for row in rows:
        table_lines.append('| ' + ' | '.join(row) + ' |')

    # Find where table ends (after header and separator and rows)
    # Replace only the table portion after the header line containing '|'
    before = content.split('\n')[0:2]  # assume first two lines are title and table header? Actually need to find the table start
    # Simpler: rewrite the whole file preserving prelude
    prelude = []
    for line in content.split('\n'):
        if line.startswith('|'):
            break
        prelude.append(line)
    new_content = '\n'.join(prelude) + '\n' + '\n'.join(table_lines) + '\n'
    with open(DELEGATION_QUEUE, 'w') as f:
        f.write(new_content)

def get_dispatch_queue_lines():
    if not DISPATCH_QUEUE.exists():
        return []
    with open(DISPATCH_QUEUE, 'r') as f:
        return [line.rstrip() for line in f if line.strip()]

def append_dispatch_item(seat, priority, product, task, output_file, depends_on, tags):
    """Create a dispatch queue line in standard format."""
    # Format: [PRIORITY] Product|Seat|Task|output_file|id|TAGS|#meta|caption:...
    # We'll generate an id from timestamp and a short hash
    import hashlib
    ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    task_hash = hashlib.sha1(task.encode()).hexdigest()[:6]
    item_id = f"{seat.lower()}-{ts}-{task_hash}"
    # Build line
    meta = ""
    caption = ""
    tags_str = tags if tags else ""
    line = f"[{priority}] {product}|{seat}|{task}|{output_file}|{item_id}|{tags_str}|#{meta}|caption:{caption}"
    return line

def main():
    print(f"Processing delegation queue: {DELEGATION_QUEUE}")
    if not DELEGATION_QUEUE.exists():
        print("ERROR: Delegation queue file not found")
        sys.exit(1)

    with open(DELEGATION_QUEUE, 'r') as f:
        content = f.read()

    header, rows = parse_table_lines(content.split('\n'))
    if header is None:
        print("ERROR: No table found in delegation queue")
        sys.exit(1)

    # Normalize header names
    col_idx = {name.lower(): i for i, name in enumerate(header)}
    required = ['id', 'status', 'seat', 'priority', 'product', 'task', 'output_file']
    for r in required:
        if r not in col_idx:
            print(f"ERROR: Missing required column '{r}' in table header")
            sys.exit(1)

    dispatch_lines = get_dispatch_queue_lines()

    updated_rows = []
    any_updates = False
    for row in rows:
        row = row[:]  # copy
        row_id = row[col_idx['id']]
        status_idx = col_idx['status']
        status = row[status_idx].upper()
        if status in ('DISPATCHED', 'CANCELLED'):
            updated_rows.append(row)
            continue
        # Check if already dispatched by tag
        tag = f"[DELEGATION:{row_id}]"
        already_dispatched = any(tag in line for line in dispatch_lines)
        if already_dispatched:
            # Mark as dispatched
            row[status_idx] = 'DISPATCHED'
            row[col_idx.get('dispatched_utc', 8)] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            any_updates = True
            updated_rows.append(row)
            continue

        # Gather task fields
        seat = row[col_idx['seat']]
        priority = row[col_idx['priority']]
        product = row[col_idx['product']]
        task = row[col_idx['task']]
        output_file = row[col_idx['output_file']]
        depends_on = row[col_idx.get('depends_on', 6)] if 'depends_on' in col_idx else ''
        # Notes column might exist for caption
        notes_idx = col_idx.get('notes')
        caption = row[notes_idx] if notes_idx is not None else ''
        caption_part = f"caption:{caption}" if caption else ""
        meta = ""

        tags = tag
        dispatch_line = append_dispatch_item(seat, priority, product, task, output_file, depends_on, tags)
        # The append_dispatch_item builds a full line with meta and caption; we need to adjust to match the expected format:
        # Standard format: [PRIORITY] Product|Seat|Task|output_file|id|TAGS|#meta|caption:...
        # Let's reconstruct exactly:
        import hashlib
        ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        task_hash = hashlib.sha1(task.encode()).hexdigest()[:6]
        item_id = f"{seat.lower()}-{ts}-{task_hash}"
        line = f"[{priority}] {product}|{seat}|{task}|{output_file}|{item_id}|{tag}|#{meta}"
        if caption:
            line += f"|caption:{caption}"
        else:
            # Ensure trailing pipe? Actually format ends with caption, but if empty, no pipe.
            pass
        # Append to dispatch queue
        with open(DISPATCH_QUEUE, 'a') as dq:
            dq.write(line + '\n')
        dispatch_lines.append(line)

        # Mark row dispatched
        row[status_idx] = 'DISPATCHED'
        row[col_idx.get('dispatched_utc', 8)] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        any_updates = True
        updated_rows.append(row)

    # Write updated delegation queue if any changes
    if any_updates:
        update_delegation_queue(header, updated_rows, any_updates)
        print(f"Dispatched {len([r for r in updated_rows if r[status_idx] == 'DISPATCHED'])} items")
    else:
        print("No new items to dispatch")

if __name__ == '__main__':
    main()
