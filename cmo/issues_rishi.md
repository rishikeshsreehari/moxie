     1|# issues_rishi.md
     2|
     3|## Open
     4|
     5|- [ ] (2026-04-02) CRITICAL: Hermes cron registry appears wiped (hermes cron list => “No scheduled jobs”; /opt/data/cron/jobs.json recreated empty at 2026-04-02T19:46Z). This disables all workers + autopush + governance automations. Need approval to restore/recreate the prior cron set from recent session dumps / known job list. Owner: Rishi + Moxie
     6|
     7|- [ ] (2026-04-01) Platform marketplaces (Webflow Apps / Framer / Glide / Typedream): REQUIRES development + platform-specific guidelines (not just submission). Founder has prior: Framer rejected a component; required a plugin. Root cause: Pax work was mis-scoped and not last-mile verified. Next action: Forge to produce a requirements matrix + MVP build scope (S/M/L) per platform, then decide build vs defer. Owner: Rishi + Forge
     8|
     9|- [ ] (2026-04-01) Reddit execution: Founder expects “post-ready” drafts tied to specific subreddits and posting windows. Current work produced tracker/rules but not verified post-ready drafts for time-of-day execution. Owner: Ember + Moxie (system fix)
    10|
    11|- [ ] (2026-04-01) Directory distribution: initial picks failed (BetaList paid-only, AlternativeTo age gate). Need replacement directories with verified last-mile requirements and minimal rework. Owner: Jax
    12|
    13|- [ ] (2026-04-02) Dashboard mobile verification: I shipped a full modern, mobile-first redesign of the public HQ dashboard (dark glass + SCADA map) and added mobile card views for Team/Products. This container lacks curl/headless Chrome/Playwright so I can’t visually verify responsive breakpoints end-to-end. After redeploy, open the dashboard on phone and confirm: (1) cards stack cleanly, (2) Team/Products show as cards (not squished table), (3) map is visible and draggable without hijacking scroll, (4) no horizontal page scroll. If any issue: send screenshot + device + browser. Owner: Rishi
    14|
    15|- [ ] (2026-04-02) X founder tone audit script needs input: please share either (A) your X handle (confirm) + last 90 days post export, or (B) the "Download an archive of your data" file (tweets.js / tweets.csv). I'll run the local script to fingerprint your tone + find what worked and generate a daily "reply guy" packet (10 replies/day). Owner: Rishi
    16|
    17|- [x] (2026-04-02) FormBeep Search Console access: ✅ Verified. Service account email added to GSC for formbeep.com and stackstats.app with Full permission. API access confirmed: both properties appear with siteFullUser. Unblocks weekly SEO reporting and Mira's GSC-vs-Umami study.
    18|
    19|## Resolved
    20|
    21|- [x] (2026-04-02) HQ autopush flock errors (`flock: failed to execute -w` / `flock: -c requires exactly one command argument`) — Fixed by updating HQ autopush crons to call `python3 cmo/scripts/hq_autopush_locked.py` (fcntl lock; no `flock`), and deprecating the legacy `cmo/scripts/run_autopush.py`.
    22|
BLOCKED: Astra task awaiting DataForSEO approval

**Task:** Astra
**Product:** 46
**Output Path:** Find additional WhatsApp-only SEO opportunities (NOT SMS yet): run a small SERP/keyword sweep for 'form notifications without zapier' + 'whatsapp form notifications' clusters; include suggested slugs, intent, SERP patterns, and prioritization. Keep cost <= /usr/bin/bash.10. Output /root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md.
**Task ID:** /root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md
**Queue Line:**     46|    46|[QUEUED][P1] FormBeep|Astra|Find additional WhatsApp-only SEO opportunities (NOT SMS yet): run a small SERP/keyword sweep for 'form notifications without zapier' + 'whatsapp form notifications' clusters; include suggested slugs, intent, SERP patterns, and prioritization. Keep cost <= /usr/bin/bash.10. Output /root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md.|/root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md|astra-wa-opps-2026-04-02T19:02Z|WA_OPPS_BRIEF|#p1|queued:2026-04-02T19:02Z

**Reason:** Requires DataForSEO SERP queries (estimated cost <= $0.10) but lacks explicit Rishi approval per policy /root/moxie_hq/cmo/resources/credentials/dataforseo.md.

**Needed:** Explicit approval to proceed with up to $0.10 spend on DataForSEO queries for WhatsApp-only SEO opportunity brief.

**Options:**
1. Approve: Reply "approve astra /root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md" and I'll execute.
2. Adjust scope: Provide revised cost limit or keyword list.
3. Cancel: Reply "cancel astra /root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md" to remove from queue.

Timestamp: 2026-04-02T22:18:42.338658Z
