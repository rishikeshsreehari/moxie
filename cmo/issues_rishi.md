# issues_rishi.md (Human-needed blockers)
# Purpose: captureanything that requires Rishi (human) input/credentials/approval.
# This file is monitored. If new items appear, Moxie will notify on Telegram.

##Open
- [ ] (2026-03-31) Reddit founder-profile scan + subreddit intel: (1) this environment is **HTTP 403 Blocked** to reddit.com, and (2) Reddit’s current Data API policy states **approval is required** before accessing Reddit data via API; commercial use requires explicit permission/contract. So we should NOT automate scans unless/until approved + reachable network. Next action: decide whether to apply for approved Data API access or do manual intel only. — Owner: Rishi + Vale

- [ ] (2026-03-31) WordPress plugin resubmission (WP team feedback) — Founder-owned blocker. Moxie/Forge will not touch WP plugin changes; Rishi will handle and we'll plan post-approval launch later. — Owner: Rishi

- [ ] (2026-03-31) Scope rule: do not push to product dev repos (e.g., formbeep.git). Moxie pushes only to HQ repo; product repos are read-only for suggestions — Owner: Moxie

- [ ] (2026-03-31) Reddit founder-profile scan for Beepmate/Web2Phone is blocked by Reddit network policy from this environment. To analyze their post history/subreddits/angles we need either: (a) a Reddit dev app token + user-agent, or (b) a logged-in session/cookies. — Owner: Rishi + Vale

- [ ] (2026-03-31) Directory submissions: preferred inbox confirmed as hello@formbeep.com; still need any existing directory accounts/verification access — Owner: Rishi + Jax

- [ ] (2026-04-01) Platform marketplace portal access: Pax Week 1 application packages (Webflow Apps, Framer Marketplace, Glide Plugins) are100% ready with all copy, metadata, and submission steps — need hello@formbeep.com login credentials or existing developer account access to actually submit the applications — Owner: Rishi + Pax

- [ ] (2026-04-01) Analytics blocker: Umami Cloud API calls from this environment fail. Without a browser-like User-Agent we get HTTP 403 w/ Cloudflare error 1010; with a standard User-Agent we get HTTP 401 Unauthorized (suggesting the UMAMI_API_KEY is invalid/revoked or lacks access). Need: rotate/confirm the Umami Cloud API key + permissions (or alternate export path / allowlisting). — Owner: Rishi + Moxie

##Resolved

- [x] (2026-03-31) OpenCode Go weekly-reset reminder cron: scheduled (UTC) — Owner: Rishi + Moxie
- [x] (2026-03-31) Google Search Console cron — Rishi confirmed it was configured earlier. Verifying access + re-enabling scheduled scans. — Owner: Moxie
- [x] (2026-03-31) Approve Rumi's content calendar so Kiro can finalize/write the2 blog posts — RESOLVED: Kiro blog posts COMPLETED, files delivered to /root/moxie/products/formbeep/copy/blog-posts-v1.md
- [x] (2026-03-31) Dispatch queue contained Luna/Pax/Orion path drift (/root/moxie vs /root/moxie_hq) + Orion output path mismatch; fixed SOUL references + standardized Orion output path — Owner: Rishi + Moxie