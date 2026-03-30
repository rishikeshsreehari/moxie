# Orchestration Audit (Codex Premium Window)

Date: 2026-03-30/31
Scope reviewed:
- State: `/root/moxie/cmo/orchestration.md`, `/root/moxie/cmo/dispatch-queue.md`, `/root/moxie/cmo/kpis.md`, `/root/moxie/cmo/kpi-dashboard.md`
- Crons: `hermes cron list`
- Employee SOULs: `/root/moxie/cmo/employees/*.md`
- Recent cron session dumps: `/opt/data/sessions/request_dump_cron_*.json`
- FormBeep analytics snapshot: `/root/moxie/products/formbeep/umami-full-data.json`

## System health score: **56 / 100**

**Why:** the structure is solid (state files, dependency queue, KPIs, roles), but execution reliability is currently low due to (1) cron collisions on shared state writes, (2) worker/model request failures (max_retries_exhausted) causing “IN_PROGRESS” tasks to never complete, and (3) inconsistent scheduling/ownership between the dispatch-orchestrator and the worker crons.

---

## Critical issues (must fix now)

### 1) Worker crons collide (race condition on shared state)
**Evidence:** all workers run at the same minute: `5 * * * *` (Vale/Astra/Kiro/Ember/Forge/Jax/Rumi). If they all read→write `orchestration.md` / `dispatch-queue.md` concurrently, atomic rename alone does **not** prevent last-writer-wins clobbering.

**Impact:** silent loss of updates, phantom “stuck” tasks, corrupted queue state.

**Fix (recommended):** stagger worker schedules + add a lock.
- Stagger: Vale 05, Astra 10, Jax 15, Rumi 20, Ember 25, Mira 30, Forge 35, Kiro 40 (each hour)
- Add file locking on any write to shared state files (e.g., `flock /tmp/moxie_state.lock ...`).

### 2) Workers not executing reliably (max_retries_exhausted)
**Evidence:** cron request dumps show repeated failures before any assistant output (example: `request_dump_cron_8bcfe505...` and `...7067633e...` have `reason=max_retries_exhausted`, with sessions containing only the user prompt and no assistant messages).

**Impact:** queue items remain “IN_PROGRESS” forever; no deliverables get written; downstream dependencies never promote.

**Fix (recommended):**
- Add governance rule: if a worker has N consecutive request failures, **pause** that worker cron and open a P0 ops ticket.
- Ensure workers use a provider/model that is known-good in this environment (premium window: default to Codex model; fallback list for off-peak).
- Log “last successful completion” per worker in state (separate from “last run”).

### 3) Dispatch system is ambiguous (duplicated orchestrator vs always-on workers)
**Evidence:**
- There is a `cmo-dispatch-orchestrator` cron every 240m.
- Separately, workers also run hourly.
- State file implies the orchestrator “spawns the right employee”, but workers are already scheduled.

**Impact:** dispatch latency + unclear single source of truth. If dispatch orchestrator is meant to be the only dispatcher, workers shouldn’t also fire every hour.

**Fix (recommended): choose one architecture**
A) **Pull-based (simplest):** remove/pause dispatch orchestrator; workers pull their assigned IN_PROGRESS task from `dispatch-queue.md` and exit.
B) **Push-based (cleaner):** pause worker hourly crons; orchestrator dispatches only the one worker needed. (Harder to implement but avoids collisions.)

### 4) State is stale/inconsistent across files
Examples:
- `orchestration.md` still lists “Codex 5-hour limit hit” as WAITING with a specific reset time; this cron job is a *one-shot*, and in practice premium can be available now.
- KPI dashboard risk heat map still claims Telegram delivery failing at 100% probability, while orchestration marks Telegram as resolved.

**Impact:** governance decisions based on wrong blockers; wasted cycles.

**Fix:** governance cron should “reconcile truth” from:
- `hermes cron list` + last run outcomes
- existence/mtime of expected output files
- presence of recent session dumps for failure reasons

---

## Improvements (should fix this sprint)

### 5) Make dispatch-queue updates atomic and machine-mergeable
Right now it’s freeform markdown. That’s human-friendly, but concurrency-unfriendly.

**Fix options:**
- Convert queue to JSON (`dispatch-queue.json`) and have humans view a rendered markdown summary.
- Or enforce per-task IDs and require workers to only patch their own line.

### 6) KPI measurability: add “instrumented metrics” not just targets
Current funnel table is aspirational; actual tracking is “TBD”. We *do* have Umami traffic snapshots:
- Last 7d: 76 visits, bounce rate **88.2%**, avg time **6.9s**
- Last 30d: 728 visits, bounce rate **89.6%**, avg time **20.6s**

**Interpretation:** we have a **top-of-funnel quality + landing clarity problem**. Either:
- traffic is unqualified (bad sources), or
- landing page fails to communicate value quickly, or
- tracking is counting single-page sessions as bounces with minimal engagement.

**Fix:** make KPI dashboard show:
- weekly visits + bounce rate + top pages
- CTA clicks (Umami events) and click→signup rate
- activation events (Connected WhatsApp, First form alert)

### 7) Add “activation” tasks explicitly (fastest lever to paid)
To hit 10 paid in 30 days, we need not only traffic but activation. Missing concrete tasks:
- Instrument `Connected WhatsApp` and `First alert received` events (app-side)
- Improve onboarding checklist and time-to-first-alert
- Add “test webhook / send test message” CTA to drive activation
- Add email sequence: Day0 setup, Day1 nudge, Day3 case study, Day7 upgrade

### 8) WP plugin is the highest leverage channel; make it a P0 war room
The plan assumes WP directory yields 6 paid. Right now it’s blocked.

**Fix:**
- Forge to run full WP compliance audit immediately (now that premium window is back)
- Create a “WP rejection reasons checklist” doc and close them systematically
- Add a founder (Rishi) 15-min review SLA (otherwise the whole funnel stalls)

---

## Nice-to-haves (defer to next sprint)
- Replace markdown state with a small SQLite/JSON state store.
- Add automatic “report diff” to Telegram (only what changed since last run).
- Add weekly retrospective auto-patches to SOULs to remove stale lines like “Telegram broken”.

---

## Recommended cron configuration changes

### Stagger workers (avoid collisions)
Current: all at `5 * * * *`.

Recommended (example):
- Vale: `5 * * * *`
- Astra: `10 * * * *`
- Jax: `15 * * * *`
- Rumi: `20 * * * *`
- Ember: `25 * * * *`
- Mira: `30 * * * *`
- Forge: `35 * * * *`
- Kiro: `40 * * * *`

### Make governance the only writer to shared state (optional, safer)
Workers write to per-worker output + a small status file; governance merges into orchestration/queue.

### Dispatch-orchestrator frequency
If kept, move from every 240m → every 15m or event-driven.

---

## Missing roles / gaps
- **Lifecycle/Email lead** (can be Kiro temporarily) for onboarding + activation + upgrade nudges.
- **Product QA / Support** (Forge can cover) to ensure “first alert works” across integrations.
- **Partnerships/Affiliates** (Ember/Jax hybrid) to recruit agencies & freelancers.

---

## Funnel optimization recommendations (what to do next)

1) **Fix landing bounce/clarity** (highest immediate lever)
- Rewrite hero to “Get a WhatsApp ping the moment someone submits your form (no Zapier)”
- Above-the-fold: platform badges (Webflow/WordPress/Framer) + 1-step CTA
- Add 2-min setup video or GIF

2) **Activation instrumentation + checklist**
- Track: CTA click → signup → connect WhatsApp → first alert → paid
- Add “Send test alert” button post-connect

3) **WP plugin sprint**
- Unblock Forge; treat WP approval as P0 acquisition unlock

4) **Directory submissions + Reddit**
- Once positioning wedge is written (Vale → Kiro), Ember runs 3–5 posts/week with measurable CTAs.

---

## Immediate action list (next 24h)
- Stagger worker crons to eliminate collisions.
- Add a lock around state writes (or governance-only merging).
- Reconcile stale blockers in orchestration/kpi-dashboard.
- Convert the 6 “IN_PROGRESS” queue items into “RETRY(1/3)” if no output exists by next run.
