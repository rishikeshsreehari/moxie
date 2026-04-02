# Orchestration Reconciler Report
**Ran:** 2026-04-02T12:26:10Z

## Drift Summary
- **Malformed dispatch line 17:** Fixed corrupted delegation marker `[---] —|[DELEGATION:—]|#|caption:—` → replaced with clean separator `—`.
- **Repeat counts drifted across 14 hourly crons:** All counters advanced 2–3 ticks since last doc write. These are expected incremental drifts from normal cron execution. Updated doc values to match live:
  - moxie-daily-governance (2553a683): 59/100 → 61/100
  - vale-worker (8bcfe505): 61/100 → 63/100
  - astra-worker (7067633e): 61/100 → 64/100
  - kiro-worker (3171d2c2): 59/100 → 61/100
  - ember-worker (eb803b7d): 59/100 → 61/100
  - forge-worker (401e59cc): 60/100 → 62/100
  - jax-worker (4bdcef11): 59/100 → 61/100
  - rumi-worker (affd389a): 60/100 → 62/100
  - nova-worker (91520aa6): 58/100 → 60/100
  - luna-worker (3e93c4f5): 60/100 → 62/100
  - pax-worker (cf1a8f9e): 58/100 → 60/100
  - orion-worker (0ed491f6): 60/200 → 62/200
  - moxie-orchestration-reconciler (1c008e06): 50/100 → 52/100
- **IN_PROGRESS tasks still running (no output yet, expected for active cycles):**
  - Iris repo copy audit — no output file at `/root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md` yet
  - Mira StackStats Umami analytics — no output file at `/root/moxie/products/stackstats/analytics/umami-summary.md` yet
  - Forge analytics review — no output dir `/root/moxie_hq/cmo/analytics/` yet
- **QUEUED tasks (correctly staying queued):**
  - Line 16: Forge GSC validation — correctly future-gated to 2026-04-04
  - Line 21: Iris live-vs-repo landing scrape — implicitly QUEUED (no status tag)
- **Live cron registry matches documented cron table perfectly** — no missing/extra/stale jobs
- **No new blockers identified** — no issues_rishi.md updates needed

## What Remains Open
- Iris/Mira output files pending (expected once workers produce results)
- Line 21 dispatch entry lacks explicit [QUEUED]/[IN_PROGRESS] status tag (cosmetic)
