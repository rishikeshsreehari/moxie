# BLOCKER DETECTED

The required script `hq_autopush_locked.py` is missing from `/root/moxie_hq/cmo/scripts/`. This prevents the HQ autopush process from executing.

éfono: /opt/hermes/cmo/scripts/hq_autopush.sh exists but locked version is absent.

Action required: Either create `hq_autopush_locked.py` with proper locking protocol or update references to use `hq_autopush.sh` with appropriate safeguards.