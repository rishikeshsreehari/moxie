import json, datetime, os
state_path='cmo/state/worker_idle_state.json'
log_entry={
    'timestamp': datetime.datetime.now(datetime.UTC).isoformat(),
    'action': 'governance_hourly',
    'changes': [
        {'worker': 'forge', 'action': 'resume', 'reason': 'tasks_available'},
        {'worker': 'jax', 'action': 'resume', 'reason': 'tasks_available'}
    ]
}
# Load existing state or initialize a fresh structure. The state file is a JSON
# object that contains a top-level ``history`` list.  Older revisions of the
# script created the file with only a ``history`` key, but a missing file or a
# corrupted file could result in the key being absent.  We therefore guard
# against both ``FileNotFoundError`` and a missing ``history`` entry.
if os.path.exists(state_path):
    try:
        with open(state_path) as f:
            data = json.load(f)
    except Exception:
        # If the JSON is malformed, start fresh to avoid crashing the governance run.
        data = {}
else:
    data = {}

# Ensure the ``history`` list exists.
if not isinstance(data.get('history'), list):
    data['history'] = []

# Append the new log entry.
data['history'].append(log_entry)
with open(state_path,'w') as f:
    json.dump(data,f,indent=2)
print('logged state')
