# HQ Delegation Queue
Safe intake for work orders during live chat. Do not run tooling during chat — queue here instead.

## Queue

| id | status | created_utc | seat | priority | product | task | depends_on | output_file | dispatched_utc | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 22:49:26 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 22:49:00 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 22:31:21 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 22:18:12 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 22:05:47 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 21:46:30 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 21:31:50 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 21:20:13 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 21:02:51 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 20:45:23 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 20:30:39 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 20:09:36 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 19:47:50 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 19:36:29 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 19:20:59 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 19:03:16 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 18:45:39 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 18:30:38 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 18:20:45 | --- |
| --- | DISPATCHED | --- | --- | --- | --- | --- | --- | --- | 2026-04-01 18:07:01 | --- |
| ---- | DISPATCHED | ------------- | ------ | ---------- | --------- | ------ | ------------ | ------------- | 2026-04-01 17:51:25 | ------- |
| jax-dir-picks-2026-04-03 | DISPATCHED | 2026-04-01 18:10:00 | Jax | P0 | formbeep | Replace failed directory picks: find 2 directories we can submit TODAY. Must personally verify last-mile requirements (free vs paid, account age gates, email verification) and include a copy/paste submission bundle + exact submission URL + "Verified on" timestamp. Also update launch-places-master.md to mark BetaList paid-only + AlternativeTo 7-day gate. | — | /root/moxie/products/formbeep/distribution/directory-submissions-today-pick.md | 2026-04-01 22:49:00 | Goal: two immediate submissions to keep momentum after BetaList/AlternativeTo failed. No browsing during live chat; do this in ops cycle. |
| iris-landing-repo-audit-2026-04-01 | DISPATCHED | 2026-04-01 18:40:00 | Iris | P0 | formbeep | Inspect the ACTUAL current landing page content in the repo (headlines, breadcrumbs, free-tier claims) and deliver 10 exact copy/UX improvements with file+section pointers. Must confirm whether “Free Forever” is accurate vs canonical facts (15 submissions/mo free). Output should include exact replacement copy blocks. | — | /root/moxie_hq/products/formbeep/dev-notes/2026-04-01-repo-copy-audit.md | 2026-04-01 22:49:26 | Triggered by founder feedback: earlier decision doc was created without checking repo; fix process. |
| astra-dataforseo-us-sms-50-2026-04-01 | DISPATCHED | 2026-04-01 18:55:00 | Astra | P0 | formbeep | Run DataForSEO LIVE mode US SMS demand probe: up to 50 queries (Rishi approved). Use the query set from the existing plan; return a brief with: top intents, SERP feature patterns, who ranks (by category, not company names), CPC/ads presence proxy, and a go/no-go recommendation for US SMS positioning. | requires DataForSEO key | /root/moxie/products/formbeep/seo/us-sms-serp-demand-brief.md | 2026-04-01 22:49:26 | Approval granted in chat (cost estimate: 50 * $0.002 = $0.10). Execute in next ops cycle. |
| iris-formbeep-live-landing-scrape-2026-04-01 | DISPATCHED | 2026-04-01 19:00:00 | Iris | P0 | formbeep | Fetch and snapshot https://formbeep.com/ (HTML + key copy blocks + CTA + pricing/free-tier text). Compare against repo content (from repo audit) and note any drift/caching. Output: “live-vs-repo-landing-diff.md” with exact lines that differ. | browser access | /root/moxie_hq/products/formbeep/dev-notes/live-vs-repo-landing-diff.md | 2026-04-01 22:49:26 | Founder requested live scrape + repo compare. Do this in ops cycle (not live chat). |
