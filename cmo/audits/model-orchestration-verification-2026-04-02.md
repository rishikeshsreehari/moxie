# Model orchestration verification — cron registry

Run (UTC): 2026-04-02 09:00:16Z
Source of truth: /opt/data/cron/jobs.json (cron scheduler registry)

What this verifies: provider/model/base_url pinning + last_run_at/last_status for sanity.
Limit: per-run output markdown does not embed model/provider; runtime selection is validated via registry + successful runs.

| Category | Job ID | Name | Provider | Model | Base URL | Last run (UTC) | Last status | Expected |
|---|---|---|---|---|---|---|---|---|
| Ops cron (git) | 868bd30fe7c1 | moxie-hq-autocommit-push | openrouter | stepfun/step-3.5-flash:free |  | 2026-04-02T08:28:29.618476+00:00 | ok | openrouter stepfun/step-3.5-flash:free |
| Ops cron (checkin) | 6effbb323126 | formbeep-daily-user-count-checkin | openrouter | stepfun/step-3.5-flash:free |  | 2026-04-01T14:06:30.753922+00:00 | ok | openrouter stepfun/step-3.5-flash:free |
| Writing worker | affd389a7783 | rumi-worker | openai-codex | gpt-5.4-mini |  | 2026-04-02T08:30:10.494201+00:00 | ok | openai-codex gpt-5.4-mini |
| Outreach worker | eb803b7d69a3 | ember-worker | openai-codex | gpt-5.4-mini |  | 2026-04-02T08:34:03.269476+00:00 | ok | openai-codex gpt-5.4-mini |
| Research worker | 7067633e99b9 | astra-worker | opencode-go | kimi-k2.5 | https://opencode.ai/zen/go/v1/chat/completions | 2026-04-02T08:23:46.950773+00:00 | ok | opencode-go kimi-k2.5 (fallback target: 5.4-mini then free) |
| Competitor scan | a468835d1396 | vale-monthly-competitor-scan | opencode-go | kimi-k2.5 | https://opencode.ai/zen/go/v1/chat/completions | 2026-04-01T10:09:15.630111+00:00 | ok | opencode-go kimi-k2.5 |
| High-leverage review | 753d42f32fbb | formbeep-weekly-growth-review | openai-codex | gpt-5.2 |  |  |  | openai-codex gpt-5.2 |
| Moxie audit | b0492991a3cd | moxie-memory-skill-audit | openai-codex | gpt-5.2 |  | 2026-04-02T08:59:43.686521+00:00 | ok | openai-codex gpt-5.2 |

## Jobs with unset provider/model (should be near-zero)

- 904c65910bfe moxie-forward-reports-to-telegram provider=None model=qwen/qwen3-coder-480b-a35b:free
- 97eacc1cb3fa codex-online-check provider=None model=None
