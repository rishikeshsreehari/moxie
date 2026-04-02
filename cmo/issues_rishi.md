- **2026-04-02 11:59:43 UTC** Autopush failed: flock: failed to execute -w: No such file or directory
# issues_rishi.md

## Open

- [ ] (2026-04-01) Platform marketplaces (Webflow Apps / Framer / Glide / Typedream): REQUIRES development + platform-specific guidelines (not just submission). Founder has prior: Framer rejected a component; required a plugin. Root cause: Pax work was mis-scoped and not last-mile verified. Next action: Forge to produce a requirements matrix + MVP build scope (S/M/L) per platform, then decide build vs defer. Owner: Rishi + Forge

- [ ] (2026-04-01) Reddit execution: Founder expects “post-ready” drafts tied to specific subreddits and posting windows. Current work produced tracker/rules but not verified post-ready drafts for time-of-day execution. Owner: Ember + Moxie (system fix)

- [ ] (2026-04-01) Directory distribution: initial picks failed (BetaList paid-only, AlternativeTo age gate). Need replacement directories with verified last-mile requirements and minimal rework. Owner: Jax

- [ ] (2026-04-02) Dashboard mobile verification: I shipped a full modern, mobile-first redesign of the public HQ dashboard (dark glass + SCADA map) and added mobile card views for Team/Products. This container lacks curl/headless Chrome/Playwright so I can’t visually verify responsive breakpoints end-to-end. After redeploy, open the dashboard on phone and confirm: (1) cards stack cleanly, (2) Team/Products show as cards (not squished table), (3) map is visible and draggable without hijacking scroll, (4) no horizontal page scroll. If any issue: send screenshot + device + browser. Owner: Rishi

- [ ] (2026-04-02) X founder tone audit script needs input: please share either (A) your X handle (confirm) + last 90 days post export, or (B) the "Download an archive of your data" file (tweets.js / tweets.csv). I'll run the local script to fingerprint your tone + find what worked and generate a daily "reply guy" packet (10 replies/day). Owner: Rishi
- [ ] (2026-04-02) FormBeep Search Console access missing: Expected credential file at /root/moxie/secrets/formbeep-search-console.json not found. Weekly SEO performance report blocked until credentials provided. Owner: Rishi
