# Weekly Operating Audit — 2026-04-02

## What I reviewed
- Recent cron sessions (delegation queue + artifact watcher + autopush)
- Durable operating rules/preferences already in memory/profile
- Open blocker list (`cmo/issues_rishi.md`)

## Findings (actionable)
1) **`cmo/issues_rishi.md` was corrupted** (it contained embedded `read_file` line-number prefixes like `"1|"` inside the file). This makes the founder-attention list fragile and easy to miss.
   - **Fix shipped locally in this run:** rewrote the file as clean markdown.
   - **Prevention:** never copy `read_file` output back into a file verbatim; it includes line numbers.

2) **Autopush reliability: `flock` one-liners can fail** with `flock: bad file descriptor` depending on how the lock is invoked. The current canonical approach is: run the dedicated autopush script (it owns the lock + staging + “no empty commit” guard).

## Stable operating conventions (confirming, not changing)
- Local-only cron runs: no Telegram/external sending unless explicitly requested.
- No new cron scheduling inside these jobs.
- Use lock file `.git/moxie_autopush.lock` for pushes.

## Open items that still require founder input (from issues list)
- Marketplace submissions require product work + platform guidelines matrix (Forge).
- Reddit execution needs post-ready drafts + posting windows; still blocked.
- Directory submissions need verified replacements (avoid paid/age gates).
- Mobile verification of public dashboard needs real-device check (screenshot + device/browser if broken).
