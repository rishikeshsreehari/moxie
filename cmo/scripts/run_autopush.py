#!/usr/bin/env python3
"""DEPRECATED shim.

This file previously attempted to use `flock` but accidentally released the lock
before running git commands (lock scope bug).

Use the canonical autopush entrypoint instead:
  python3 /root/moxie_hq/cmo/scripts/hq_autopush_locked.py

This shim remains for backwards compatibility and simply forwards to the
canonical script.
"""

import os
import subprocess
import sys

REPO = "/root/moxie_hq"


def main() -> int:
    os.chdir(REPO)
    return subprocess.run([sys.executable, "cmo/scripts/hq_autopush_locked.py"]).returncode


if __name__ == "__main__":
    raise SystemExit(main())
