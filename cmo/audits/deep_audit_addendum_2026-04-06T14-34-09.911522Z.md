Deep Audit Addendum (evidence-based)
Timestamp: 2026-04-06T14:34:09.911522Z

A) What is actually blocking right now (from repo state)
- dispatch-queue.md contains exactly 1 task and it is marked [COMPLETED].
- issues_rishi.md contains an entry claiming UMAMI_API_KEY is missing; we must reconcile this against /opt/data/.env and the artifact output.

B) Paperclip feasibility on this host
- node -v: v20.19.2
- pnpm -v: bash: pnpm: command not found

C) /opt/data/.env Umami key presence (masked)
env_file_exists= True
umami_key_present= True
umami_key_len= 36
umami_key_last4= iNBb

D) validate_funnel_metrics.py exists?
- cmo/scripts/validate_funnel_metrics.py: NO

E) datetime.utcnow usage check (process_delegation_queue.py first 500 lines)
- /root/moxie_hq/cmo/scripts/process_delegation_queue.py:134 134|    ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
- /root/moxie_hq/cmo/scripts/process_delegation_queue.py:189 189|            row[col_idx.get('dispatched_utc', 8)] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
- /root/moxie_hq/cmo/scripts/process_delegation_queue.py:213 213|        ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
- /root/moxie_hq/cmo/scripts/process_delegation_queue.py:233 233|        row[col_idx.get('dispatched_utc', 8)] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

F) Git diff stats (current instability surface area)
cmo/delegation-queue.md          |  2 ++
 cmo/orchestration.md             |  2 +-
 cmo/state/worker_idle_state.json | 10 +++++-----
 3 files changed, 8 insertions(+), 6 deletions(-)

G) Git diff (full)
diff --git a/cmo/delegation-queue.md b/cmo/delegation-queue.md
index 46b2c02..3519cc3 100644
--- a/cmo/delegation-queue.md
+++ b/cmo/delegation-queue.md
@@ -5,6 +5,8 @@ Safe intake for work orders during live chat. Do not run tooling during chat —
 
 | id | status | created_utc | seat | priority | product | task | depends_on | output_file | dispatched_utc | notes |
 |---|---|---|---|---|---|---|---|---|---|---|
+| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-06 14:30:58 | --- |
+| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-06 14:01:18 | --- |
 | --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-06 13:46:17 | --- |
 | --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-06 13:30:33 | --- |
 | --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-06 13:15:53 | --- |
diff --git a/cmo/orchestration.md b/cmo/orchestration.md
index 4dad158..c939492 100644
--- a/cmo/orchestration.md
+++ b/cmo/orchestration.md
@@ -1,6 +1,6 @@
 # Moxie Orchestration State
 
-Last updated: 2026-04-06 14:00:00 UTC
+Last updated: 2026-04-06 14:15:04 UTC
 
 Employee Status Alignment:
 - All workers referenced in dispatch-queue.md are active
diff --git a/cmo/state/worker_idle_state.json b/cmo/state/worker_idle_state.json
index f10d6da..a8ae292 100644
--- a/cmo/state/worker_idle_state.json
+++ b/cmo/state/worker_idle_state.json
@@ -20,34 +20,34 @@
   "workers": {
     "forge": {
       "paused": false,
-      "last_check": "2026-04-06T10:03:03.916285+00:00",
+      "last_check": "2026-04-06T14:05:34.748185+00:00",
       "last_action": "resume",
       "pause_reason": "tasks_available",
       "has_tasks": true
     },
     "jax": {
       "paused": false,
-      "last_check": "2026-04-06T10:03:03.916285+00:00",
+      "last_check": "2026-04-06T14:05:34.748185+00:00",
       "last_action": "resume",
       "pause_reason": "tasks_available",
       "has_tasks": true
     },
     "ember": {
       "paused": true,
-      "last_check": "2026-04-06T10:03:03.916285+00:00",
+      "last_check": "2026-04-06T14:05:34.748185+00:00",
       "has_tasks": false,
       "last_action": "no_action"
     },
     "astra": {
       "paused": false,
-      "last_check": "2026-04-06T10:03:03.916285+00:00",
+      "last_check": "2026-04-06T14:05:34.748185+00:00",
       "last_action": "resume",
       "pause_reason": "tasks_available",
       "has_tasks": true
     },
     "kiro": {
       "paused": true,
-      "last_check": "2026-04-06T10:03:03.916285+00:00",
+      "last_check": "2026-04-06T14:05:34.748185+00:00",
       "has_tasks": false,
       "last_action": "no_action"
     }

H) Heads
dispatch-queue.md:
     1|     1|[COMPLETED][P1] formbeep|Astra|Produce "GSC vs Umami" study (last 28d). Output path: /root/moxie_hq/products/formbeep/analytics/gsc-vs-umami-study.md
     2|- Completed on 2026-04-06 11:45 UTC
issues_rishi.md:
     1|- [BLOCKED] formbeep|Astra|"GSC vs Umami" study (last 28d): Umami API key missing in /opt/data/.env (required $0.25). Blocked task with evidence pointer. Output path: /root/moxie_hq/products/formbeep/analytics/gsc-vs-umami-study.md
rishi_review.md (head):
     1|# Rishi Review Queue (Founder attention)
     2|
     3|Purpose: single place to track everything that needs Rishi’s attention (reviews, manual execution, decisions).
     4|Rule: When you ask “what needs my attention?”, I will read THIS file and present items one by one.
     5|
     6|Last updated: 2026-04-02
     7|
     8|---
     9|
    10|## P0 — DO NOW (founder-executable)
    11|
    12|1) [P0][ACTION] Reddit posting execution (manual)
    13|- Account: u/rishikeshshari
    14|- You will post manually; Moxie/Ember provide the execution packet.
    15|- Primary reference (rules/history): `/root/moxie/products/formbeep/outreach/reddit-posting-tracker.md`
    16|- Execution packet (today): `/root/moxie/products/formbeep/outreach/reddit-execution-packet-today.md` (queued to Ember)
    17|- If packet not ready, use interim plan (today Thu): r/SideProject + r/microsaas, 18:30–20:30 GST, WhatsApp-only truthful copy.
    18|
    19|2) [P0][ACTION] Dashboard mobile QA (2 min) ✅ CLOSED
    20|- Done: 2026-04-02 (Rishi marked closed)
    21|
    22|---
    23|
    24|## P0 — BLOCKED / WAITING (do not execute until unblocked)
    25|
    26|3) [P0][BLOCKED] Directory submissions execution (Fazier + Twelve Tools)
    27|- Files:
    28|  - Submission packet: `/root/moxie/products/formbeep/distribution/directory-submissions-today-pick.md`
    29|  - Log: `/root/moxie/products/formbeep/distribution/directory-submissions-log.md`
    30|- BLOCKER: packet copy contained non-shipped claims (SMS/email). Must be rewritten to WhatsApp-only and validated against capabilities KB before any submission.
    31|- Status: awaiting corrected packet + capabilities truth layer.
    32|
    33|---
    34|
    35|## P0 — REVIEW (decisions)
    36|
    37|4) [P0][REVIEW] FormBeep failure analysis ✅ APPROVED
    38|- File: `/root/moxie_hq/cmo/postmortems/2026-04-01-formbeep-failures.md`
    39|- Note: patch needed in doc to remove any claim that directory submissions are “DONE” until copy is truthful.
    40|
    41|5) [P0][REVIEW] US SMS positioning ✅ DECIDED
    42|- File: `/root/moxie/products/formbeep/seo/us-sms-serp-demand-brief.md`
    43|- Decision: focus WhatsApp + “without Zapier” now; revisit SMS pages after SMS feature ships (~2 weeks).
    44|
    45|6) [P0][REVIEW] Marketplace strategy ✅ APPROVED
    46|- File: `/root/moxie_hq/products/formbeep/dev-notes/marketplace-integration-scope.md`
    47|- Decision: defer Webflow/Framer apps (2–3w builds); build Glide/Typedream docs now.
    48|
    49|---
    50|
    51|## P1 — REVIEW (content system)
    52|
    53|7) [P1][REVIEW] Founder Voice / Build-in-Public strategy (X + IndieHackers) ✅ APPROVED
    54|- File: `/root/moxie_hq/cmo/strategy/founder-voice-x-indiehackers.md`
    55|- Next: Kiro will produce 7-day X calendar + paste-ready posts under `/root/moxie_hq/cmo/content/` (queued).
    56|
    57|8) [P1][REVIEW] X tone + “reply guy” OS (framework ready; needs your export to run fully)
    58|- File: `/root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md`
    59|- Input needed to activate: your X export (tweets.js / tweets.csv)
    60|
    61|9) [P1][REVIEW] Channel matrix (how often/when to post per product/channel)
    62|- File: `/root/moxie_hq/cmo/strategy/channel-matrix-all-products.md`
    63|- Note: flagged as poor; v2 rewrite shipped 2026-04-02 — please re-review and approve.
    64|
    65|---
    66|
    67|## P0 — WAITING ON OUTPUT (currently missing deliverables)
    68|
    69|10) [P0][COMPLETED] ✅ FormBeep repo copy audit (reassigned → Forge)
    70|- Output: `/root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md`
    71|- Completed: 2026-04-02T17:45Z
    72|
    73|11) [P0][COMPLETED] ✅ StackStats Umami analytics summary (reassigned → Jax)
    74|- Output: `/root/moxie/products/stackstats/analytics/umami-summary.md`
    75|- Completed: 2026-04-02T17:30Z
    76|
    77|12) [P0][COMPLETED] ✅ FormBeep live vs repo landing diff (queued → Jax)
    78|- Output: `/root/moxie_hq/products/formbeep/dev-notes/live-vs-repo-landing-diff.md`
    79|- Completed: 2026-04-02T18:33:42Z
    80|
    81|13) [P0][COMPLETED] ✅ StackStats live-site snapshot (queued → Jax)
    82|- Output: `/root/moxie/products/stackstats/dev-notes/live-site-snapshot.md`
    83|- Completed: 2026-04-02T19:20:00Z
    84|
    85|---
    86|
    87|## P2 — SYSTEM CLEANUP (maintained by Moxie)
    88|
    89|14) [P2][FIX] Review-queue hygiene
    90|- Keep this file executable: if an item becomes non-executable, it moves to BLOCKED/WAITING with an explicit blocker.
    91|

I) notify_issues.py (head)
     1|#!/usr/bin/env python3
     2|"""Notify Rishi on Telegram when issues_rishi.md has new open items.
     3|
     4|Heuristic: send when file mtime increases AND there is at least one unchecked item in '## Open'.
     5|Filters out items that are resolved per OPERATING_ASSUMPTIONS.md.
     6|State: /opt/data/cache/issues-notify.json
     7|"""
     8|
     9|import json
    10|import re
    11|import sys
    12|from pathlib import Path
    13|
    14|import requests
    15|
    16|ISSUES_PATH = Path("/root/moxie/cmo/issues_rishi.md")
    17|STATE_PATH = Path("/opt/data/cache/issues-notify.json")
    18|ENV_PATH = Path("/opt/data/.env")
    19|
    20|
    21|def read_env_value(key: str):
    22|    if not ENV_PATH.exists():
    23|        return None
    24|    m = re.search(rf"^{re.escape(key)}=(.+)$", ENV_PATH.read_text(), re.M)
    25|    return m.group(1).strip() if m else None
    26|
    27|
    28|def load_state():
    29|    if not STATE_PATH.exists():
    30|        return {"last_mtime": 0}
    31|    try:
    32|        return json.loads(STATE_PATH.read_text())
    33|    except Exception:
    34|        return {"last_mtime": 0}
    35|
    36|
    37|def save_state(state):
    38|    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    39|    STATE_PATH.write_text(json.dumps(state, indent=2))
    40|
    41|
    42|def has_open_items(text: str) -> bool:
    43|    # Anything like: - [ ] ... under Open section
    44|    m = re.search(r"## Open(.*?)(?:## Resolved|\Z)", text, re.S)
    45|    if not m:
    46|        return False
    47|    open_block = m.group(1)
    48|    
    49|    # Get operating assumptions
    50|    try:
    51|        sys.path.insert(0, '/root/moxie_hq/cmo/scripts')
    52|        from read_operating_assumptions import get_operating_assumptions, should_suppress_issue
    53|        assumptions = get_operating_assumptions()
    54|    except Exception:
    55|        # Fall back to original behavior if assumptions can't be loaded
    56|        return bool(re.search(r"^- \[ \]", open_block, re.M))
    57|    
    58|    # Check each open item to see if it should be suppressed
    59|    lines = open_block.split('\n')
    60|    open_items = []
    61|    
    62|    for line in lines:
    63|        if line.strip().startswith("- [ ]"):
    64|            item_text = line.strip()[4:].strip()  # Remove "- [ ]"
    65|            if not should_suppress_issue(item_text, assumptions):
    66|                open_items.append(line)
    67|    
    68|    return len(open_items) > 0
    69|
    70|
    71|def summarize_open(text: str, max_lines: int = 30) -> str:
    72|    m = re.search(r"## Open(.*?)(?:## Resolved|\Z)", text, re.S)
    73|    if not m:
    74|        return "(No Open section found)"
    75|    open_block = m.group(1)
    76|    lines = open_block.split('\n')
    77|    
    78|    # Get operating assumptions
    79|    try:
    80|        sys.path.insert(0, '/root/moxie_hq/cmo/scripts')
    81|        from read_operating_assumptions import get_operating_assumptions, should_suppress_issue
    82|        assumptions = get_operating_assumptions()
    83|    except Exception:
    84|        # Fall back to original behavior if assumptions can't be loaded
    85|        lines = [ln.rstrip() for ln in open_block.strip().splitlines() if ln.strip()]
    86|        if not lines:
    87|            return "(No open items)"
    88|        out = []
    89|        for ln in lines:
    90|            if ln.lstrip().startswith("-"):
    91|                out.append(ln)
    92|            if len(out) >= max_lines:
    93|                break
    94|        more = "" if len(out) < len(lines) else "\n..."
    95|        return "\n".join(out) + more
    96|    
    97|    # Filter out items that should be suppressed
    98|    out = []
    99|    for line in lines:
   100|        if line.strip().startswith("- [ ]"):
   101|            item_text = line.strip()[4:].strip()  # Remove "- [ ]"
   102|            if not should_suppress_issue(item_text, assumptions):
   103|                out.append(line.strip())
   104|        elif line.strip().startswith("- [x]"):
   105|            out.append(line.strip())  # Include completed items for context
   106|    
   107|    if not out:
   108|        return "(No open items after filtering resolved)"
   109|    
   110|    if len(out) >= max_lines:
   111|        more = "\n..."
   112|    else:
   113|        more = ""
   114|    
   115|    return "\n".join(out[:max_lines]) + more
   116|
   117|
   118|def send_telegram(token: str, chat_id: str, text: str):
   119|    url = f"https://api.telegram.org/bot{token}/sendMessage"
   120|    resp = requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=30)
   121|    if resp.status_code != 200:
   122|        raise RuntimeError(f"Telegram HTTP {resp.status_code}: {resp.text[:300]}")
   123|
   124|
   125|def main(argv):
   126|    if not ISSUES_PATH.exists():
   127|        print("[SILENT]")
   128|        return 0
   129|
   130|    token=read_e...EN")
   131|    chat_id = read_env_value("TELEGRAM_CHAT_ID") or "6699776435"
   132|    if not token:
   133|        print("BLOCKED: TELEGRAM_BOT_TOKEN missing")
   134|        return 2
   135|
   136|    text = ISSUES_PATH.read_text(encoding="utf-8", errors="replace")
   137|    mtime = int(ISSUES_PATH.stat().st_mtime)
   138|
   139|    state = load_state()
   140|    last = int(state.get("last_mtime", 0) or 0)
   141|
   142|    force = "--force" in argv
   143|
   144|    if (not force) and (mtime <= last):
   145|        print("[SILENT]")
   146|        return 0
   147|
   148|    if not has_open_items(text):
   149|        state["last_mtime"] = mtime
   150|        save_state(state)
   151|        print("[SILENT]")
   152|        return 0
   153|
   154|    msg = "issues_rishi.md has open items:\n\n" + summarize_open(text)
   155|    send_telegram(token, chat_id, msg)
   156|
   157|    state["last_mtime"] = mtime
   158|    save_state(state)
   159|    print("OK: notified")
   160|    return 0
   161|
   162|
   163|if __name__ == "__main__":
   164|    raise SystemExit(main(sys.argv[1:]))
   165|