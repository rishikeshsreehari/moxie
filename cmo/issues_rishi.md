# issues_rishi.md (Human-needed blockers)
# Purpose: captureanything that requires Rishi (human) input/credentials/approval.
# This file is monitored. If new items appear, Moxie will notify on Telegram.

##Open
- [ ] (2026-03-31) Reddit posting execution: Ember's 6 post drafts + 4-week campaign plan are complete and ready to publish, but need Reddit account credentials (u/adambengur or dedicated FormBeep Reddit account) to publish posts and seed comments — Owner: Rishi + Ember

- [ ] (2026-03-31) WordPress plugin resubmission (WP team feedback) — Founder-owned blocker. Moxie/Forge will not touch WP plugin changes; Rishi will handle and we'll plan post-approval launch later. — Owner: Rishi

- [ ] (2026-03-31) Scope rule: do not push to product dev repos (e.g., formbeep.git). Moxie pushes only to HQ repo; product repos are read-only for suggestions — Owner: Moxie

- [ ] (2026-03-31) Reddit founder-profile scan for Beepmate/Web2Phone is blocked by Reddit network policy from this environment. To analyze their post history/subreddits/angles we need either: (a) a Reddit dev app token + user-agent, or (b) a logged-in session/cookies. — Owner: Rishi + Vale

- [ ] (2026-03-31) Directory submissions: preferred inbox confirmed as hello@formbeep.com; still need any existing directory accounts/verification access — Owner: Rishi + Jax

- [ ] (2026-04-01) Platform marketplace portal access: Pax Week 1 application packages (Webflow Apps, Framer Marketplace, Glide Plugins) are100% ready with all copy, metadata, and submission steps — need hello@formbeep.com login credentials or existing developer account access to actually submit the applications — Owner: Rishi + Pax

- [ ] (2026-04-01) Analytics blocker: Umami Cloud API requests from this environment are returning HTTP 403 with Cloudflare error code1010 (access denied), so I can't do the data-driven geo/search analysis yet. Need a way to allowlist this server/container IP, run analytics queries from the host network, or provide an alternate export/access path. — Owner: Rishi + Moxie

##Resolved

- [x] (2026-03-31) OpenCode Go weekly-reset reminder cron: scheduled (UTC) — Owner: Rishi + Moxie
- [x] (2026-03-31) Google Search Console cron — Rishi confirmed it was configured earlier. Verifying access + re-enabling scheduled scans. — Owner: Moxie
- [x] (2026-03-31) Approve Rumi's content calendar so Kiro can finalize/write the2 blog posts — RESOLVED: Kiro blog posts COMPLETED, files delivered to /root/moxie/products/formbeep/copy/blog-posts-v1.md
- [x] (2026-03-31) Dispatch queue contained Luna/Pax/Orion path drift (/root/moxie vs /root/moxie_hq) + Orion output path mismatch; fixed SOUL references + standardized Orion output path — Owner: Rishi + Moxie