OPERATING_ASSUMPTIONS.md:
# Process HQ Delegation Queue Management

## Worker Idle Management
1. Auto-pause workers if idle >6 hours
2. Auto-resume workers when new tasks appear
3. Maintain worker_idle_state.json synchronization

## Artifact Tracking
- Monitor stackstats.app sales burn rate
- Track FormBeep order completion timelines
- Verify vanity link redirects

## Reporting Protocol
1. [SILENT] for no changes
2. Changelog format:
   - Promoted/Completed: COUNT
   - New blockers: LIST
   - Errors: EXACT ERROR LINE
3. Never combine [SILENT] with content

LAST_UPDATED: 2026-04-04 00:38:24 UTC