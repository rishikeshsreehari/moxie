# Delegation System (HQ) — product-agnostic auto-assignment

Goal: allow a human (founder/CMO) to queue work orders during live chat WITHOUT running tools, then later run a single processor to promote them into the worker dispatch queue.

Hard rule: Do not run tooling during live chat; queue work orders instead.

---

## Files

1) /root/moxie_hq/cmo/delegation-queue.md
   - Human-editable intake queue.
   - Founder/CMO appends rows to the markdown table under "## Queue".

2) /root/moxie_hq/cmo/dispatch-queue.md
   - Worker execution queue (existing).
   - Processors append [QUEUED] tasks in the existing format:
     [STATUS] Employee | (Product) Task | Depends on | Output file

3) /root/moxie_hq/cmo/artifact-rules.yaml
   - Generic rules describing which generated artifacts should trigger follow-on tasks.

4) /root/moxie_hq/cmo/state/artifact_state.json
   - Persistent state for artifact watcher; tracks last-seen hashes so we only trigger on changes.

---

## Workflow

A) During live chat (no tools)
- Add a row to delegation-queue.md.
- Keep it specific: seat, priority, product tag, clear output_file path.

B) After chat / during ops cycle
1. Promote human-entered work orders:
   python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py

2. Promote artifact-triggered follow-ons (optional):
   python3 /root/moxie_hq/cmo/scripts/process_artifacts.py

Notes:
- Both scripts are idempotent (safe to re-run). They tag dispatch entries so duplicates are avoided.
- The artifact processor seeds state on first run (writes hashes but does not dispatch). After that, only actual changes trigger tasks.

---

## Delegation queue row guidelines

IMPORTANT: chaining is mandatory. See:
- `/root/moxie_hq/cmo/resources/chaining-protocol.md`

Required columns:
- id: unique (recommended format: dq-YYYYMMDD-HHMM-shortslug)
- seat: worker seat name (Vale/Astra/Ember/etc)
- priority: P0..P3
- product: product tag (free text)
- task: clear deliverable instruction
- output_file: absolute output path

Optional:
- depends_on: another id or free text
- notes

---

## How to add new artifact rules

Edit artifact-rules.yaml and add a rule under rules:
- name: unique string
- enabled: true
- globs: list of repo-relative globs
- target: dispatch_queue or delegation_queue
- task.seat / task.priority / task.product / task.task / task.output_file

Template variables available in task.task:
- {artifact_path} -> absolute path to the artifact
- {artifact_relpath} -> repo-relative path

