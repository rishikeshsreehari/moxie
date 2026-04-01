# issues_rishi.md (Human-needed blockers)
# Purpose: capture anything that requires Rishi (human) input/credentials/approval.
# Companion file: /root/moxie_hq/cmo/rishi_review.md (all founder attention items, incl. reviews + manual execution)
# This file is monitored. If new items appear, Moxie will notify on Telegram.

## Open

- [ ] (2026-03-31) Reddit founder-profile scan + subreddit intel: (1) this environment is **HTTP 403 Blocked** to reddit.com, and (2) Reddit's current Data API policy states **approval is required** before accessing Reddit data via API; commercial use requires explicit permission/contract. So we should NOT automate scans unless/until approved + reachable network. Next action: decide whether to apply for approved Data API access or do manual intel only. — Owner: Rishi + Vale

- [ ] (2026-03-31) WordPress plugin resubmission (WP team feedback) — Founder-owned blocker. Moxie/Forge will not touch WP plugin changes; Rishi will handle and we'll plan post-approval launch later. — Owner: Rishi

- [ ] (2026-03-31) Scope rule: do not push to product dev repos (e.g., formbeep.git). Moxie pushes only to HQ repo; product repos are read-only for suggestions — Owner: Moxie

- [ ] (2026-03-31) Reddit founder-profile scan for Beepmate/Web2Phone is blocked by Reddit network policy from this environment. To analyze their post history/subreddits/angles we need either: (a) a Reddit dev app token + user-agent, or (b) a logged-in session/cookies. — Owner: Rishi + Vale

- [ ] (2026-03-31) Directory submissions: preferred inbox confirmed as hello@formbeep.com; still need any existing directory accounts/verification access — Owner: Rishi + Jax

- [ ] (2026-04-01) Platform marketplaces (Webflow Apps / Framer / Glide / Typedream): NOT just form-filling — requires a real integration/app that meets marketplace guidelines + review. Current plan was mis-scoped as “just submission + credentials”. Next action: decide whether to (A) build a Webflow/Framer/Glide integration (engineering scope) or (B) drop/defer this channel. Owner: Rishi + Forge (scope) + Pax (distribution)

## Resolved

- [x] (2026-04-01) Umami analytics access — Mira completed analytics report via alternate method; data available at /root/moxie/products/formbeep/analytics-report.md

- [x] (2026-04-01) HQ autopush initially failed due to non-fast-forward (remote ahead). Autopush now auto-rebases (`git pull --rebase origin main`) and retries push under lock; state reconciled and pushed.

- [x] (2026-03-31) OpenCode Go weekly-reset reminder cron: scheduled (UTC) — Owner: Rishi + Moxie
- [x] (2026-03-31) Google Search Console cron — Rishi confirmed it was configured earlier. Verifying access + re-enabling scheduled scans. — Owner: Moxie
- [x] (2026-03-31) Approve Rumi's content calendar so Kiro can finalize/write the 2 blog posts — RESOLVED: Kiro blog posts COMPLETED, files delivered to /root/moxie/products/formbeep/copy/blog-posts-v1.md
- [x] (2026-03-31) Dispatch queue contained Luna/Pax/Orion path drift (/root/moxie vs /root/moxie_hq) + Orion output path mismatch; fixed SOUL references + standardized Orion output path — Owner: Rishi + Moxie