# Rishi Review Queue (Founder attention)

Purpose: single place to track everything that needs Rishi’s attention (reviews, manual execution, decisions).
Rule: When you ask “what needs my attention?”, I will read THIS file and present items one by one.

Last updated: 2026-04-02

---

## P0 — BLOCKERS (unblocks execution)

1) [P0][CREDENTIALS] FormBeep Google Search Console access
- What’s needed: provide `/root/moxie/secrets/formbeep-search-console.json` (service account or whatever format we standardized)
- Why: blocks weekly SEO reporting + the “GSC vs Umami (28d)” study

2) [P0][CREDENTIALS] Reddit posting execution
- What’s needed: whichever Reddit account we’ll post from (credentials/session) for manual posting.
- Why: Ember’s tracker/plan exists but posting cannot happen without an account.

3) [P0][CREDENTIALS] Directory submissions execution
- What’s needed: any existing directory accounts tied to `hello@formbeep.com` + inbox verification access as needed.
- Why: execution is founder-owned; Jax can prep but cannot submit without accounts.

---

## P0 — ACTION (15–25 min each, immediate progress)

4) [P0][ACTION] Submit FormBeep to 2 directories (copy/paste ready)
- File: `/root/moxie/products/formbeep/distribution/directory-submissions-today-pick.md`
- Picks: Fazier + Twelve Tools (both verified with exact URLs + UTMs)
- Done when: submitted + logged in `/root/moxie/products/formbeep/distribution/directory-submissions-log.md`

5) [P0][ACTION] Dashboard mobile QA (2 min)
- What to do: open the public HQ dashboard on your phone and confirm:
  (a) cards stack cleanly
  (b) Team/Products render as cards (not a squished table)
  (c) map is draggable without hijacking scroll
  (d) no horizontal page scroll
- If broken: send screenshot + device + browser.

---

## P0 — REVIEW (high-leverage decisions)

6) [P0][REVIEW] FormBeep failure analysis (what we fixed + what remains)
- File: `/root/moxie_hq/cmo/postmortems/2026-04-01-formbeep-failures.md`
- Outcome needed: confirm the prevention rules (Execution OS v3) are acceptable.

7) [P0][REVIEW] US SMS positioning — GO/NO-GO decision
- File: `/root/moxie/products/formbeep/seo/us-sms-serp-demand-brief.md`
- Outcome needed: decide whether we emphasize US SMS now vs WhatsApp-first geos, and which 3 pages to ship first.

8) [P0][REVIEW] Marketplace strategy decision (build vs defer)
- Files:
  - `/root/moxie_hq/products/formbeep/dev-notes/marketplace-integration-scope.md`
  - `/root/moxie_hq/products/formbeep/dev-notes/marketplace-requirements-matrix.md`
- Outcome needed: confirm the “defer Webflow/Framer, build Glide/Typedream” recommendation.

---

## P1 — REVIEW (content system)

9) [P1][REVIEW] Founder Voice / Build-in-Public strategy (X + IndieHackers)
- File: `/root/moxie_hq/cmo/strategy/founder-voice-x-indiehackers.md`
- Outcome needed: approve cadence + pillars; pick the first 7 days to execute.

10) [P1][REVIEW] X tone + “reply guy” OS (framework ready; needs your export to run fully)
- File: `/root/moxie_hq/cmo/strategy/x-tone-and-reply-guy-kit.md`
- Input needed to activate: your X export (tweets.js / tweets.csv) OR confirm handle + provide last 90 days posts.

11) [P1][REVIEW] Channel matrix (how often/when to post per product/channel)
- File: `/root/moxie_hq/cmo/strategy/channel-matrix-all-products.md`

---

## P0 — WAITING ON OUTPUT (currently missing deliverables)

These were marked IN_PROGRESS for ~20h+ because the originally assigned owners (Iris/Mira) do not have hourly worker crons. I reassigned them to active hourly workers so they will complete.

12) [P0][WAITING] FormBeep repo copy audit (reassigned → Forge)
- Output: `/root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md`

13) [P0][WAITING] StackStats Umami analytics summary (reassigned → Jax)
- Output: `/root/moxie/products/stackstats/analytics/umami-summary.md`

14) [P0][WAITING] FormBeep live vs repo landing diff (queued → Jax)
- Output: `/root/moxie_hq/products/formbeep/dev-notes/live-vs-repo-landing-diff.md`

15) [P0][WAITING] StackStats live-site snapshot (queued → Jax)
- Output: `/root/moxie/products/stackstats/dev-notes/live-site-snapshot.md`

---

## P2 — SYSTEM CLEANUP (I will keep this maintained)

16) [P2][FIX] Review-queue hygiene
- Note: The old references to `landing-change-decision.md` and `landing-hero-funnel-30d.md` are removed because those files do not exist on disk.
- Going forward: anything you say that creates work will be logged here as P0/P1/P2 with an owner + file path + “done when”.
