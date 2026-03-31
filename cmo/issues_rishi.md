# issues_rishi.md (Human-needed blockers)
# Purpose: capture anything that requires Rishi (human) input/credentials/approval.
# This file is monitored. If new items appear, Moxie will notify on Telegram.

## Open

- [ ] (2026-03-31) WordPress plugin resubmission (WP team feedback) — Status: IN_PROGRESS (Rishi) — Owner: Rishi
- [ ] (2026-03-31) Scope rule: do not push to product dev repos (e.g., formbeep.git). Moxie pushes only to HQ repo; product repos are read-only for suggestions — Owner: Moxie
- [ ] (2026-03-31) Reddit founder-profile scan for Beepmate/Web2Phone is blocked by Reddit network policy from this environment. To analyze their post history/subreddits/angles we need either: (a) a Reddit dev app token + user-agent, or (b) a logged-in session/cookies. — Owner: Rishi + Vale
- [ ] (2026-03-31) WordPress plugin resubmission pending — review/approve Forge’s changes when ready — Owner: Rishi + Forge
- [ ] (2026-03-31) Directory submissions: preferred inbox confirmed as hello@formbeep.com; still need any existing directory accounts/verification access — Owner: Rishi + Jax
- [ ] (2026-03-31) Approve Rumi’s content calendar so Kiro can finalize/write the 2 blog posts — Owner: Rishi + Kiro
- [ ] (2026-03-31) Google Search Console cron is blocked: missing service account JSON at /root/moxie/secrets/formbeep-search-console.json (either provide the file there or tell us the correct mounted path) — Owner: Rishi

(Template)
- [ ] (YYYY-MM-DD) <issue> — <what you need from Rishi> — Owner: <employee>

## Resolved

- [x] (2026-03-31) Dispatch queue contained Luna/Pax/Orion path drift (/root/moxie vs /root/moxie_hq) + Orion output path mismatch; fixed SOUL references + standardized Orion output path — Owner: Rishi + Moxie
- [x] (YYYY-MM-DD) <issue> — resolved notes
