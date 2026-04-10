## Open Issues

- [ ] **Missing Script: process_delegation_queue.py**
  - **Error:** `python3: can't open file '/opt/hermes/cmo/scripts/process_delegation_queue.py': [Errno 2] No such file or directory`
  - **Impact:** Delegation queue processing failed, no tasks promoted or completed.

- [ ] **Missing Script: process_artifacts.py**
  - **Error:** `python3: can't open file '/opt/hermes/cmo/scripts/process_artifacts.py': [Errno 2] No such file or directory`
  - **Impact:** Artifact processing failed, no tasks completed.

## Summary

- **Tasks Promoted:** 0
- **Tasks Completed:** 0
- **New Blockers:** 2 (missing scripts)
- **Errors:** 2 (exact error lines included above)

**Next Steps:** Verify script locations or update deployment configuration to ensure scripts are in /opt/hermes/cmo/scripts/.