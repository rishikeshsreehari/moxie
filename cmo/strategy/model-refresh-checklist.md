# Model refresh checklist (every 2 weeks)

Owner: Rishi + Moxie
Cadence: every 14 days
Goal: keep model roster current, avoid silent cost creep, and prevent provider/model mismatch failures.

## 0) Snapshot current policy
- Confirm policy file is current: `cmo/strategy/model-orchestration.md`
- Confirm worker buckets:
  - Ops/housekeeping → OpenRouter stepfun/step-3.5-flash:free
  - Writing roles → Codex gpt-5.4-mini
  - Research roles → OpenCode Go kimi-k2.5
  - High-leverage review → Codex gpt-5.2
  - gpt-5.4 escalation = rare + criteria-based

## 1) Provider health + billing sanity

### OpenAI Codex
- Check weekly remaining quota and any unexpected spikes.
- Validate the default premium model is still gpt-5.2 and that only whitelisted jobs use it.

### OpenCode Go
- Check rolling 5h / weekly / monthly usage limits.
- If OpenCode is frequently throttling, consider switching research roles to Codex gpt-5.4-mini temporarily.

### OpenRouter
- Verify OpenRouter balance and whether any “:free” models are actually costing more than expected.
- Confirm the selected free-tier models still exist and are not heavily throttled.

## 2) Free model availability audit (OpenRouter)
- Confirm these still work well enough:
  - stepfun/step-3.5-flash:free (ops)
  - qwen/qwen3.6-plus-preview:free (governance-lite + fallback)
  - minimax/minimax-m2.5:free (last resort)
- If Step gets too shallow/unstable, swap ops to qwen free.

## 3) Cron registry audit (the important one)
Source of truth: `/opt/data/cron/jobs.json`
- Ensure there are **no jobs** with provider/model unset that could inherit defaults.
- Ensure base_url is sane after any provider changes:
  - openai-codex → https://chatgpt.com/backend-api/codex
  - opencode-go  → https://opencode.ai/zen/go/v1/chat/completions
  - openrouter   → https://openrouter.ai/api/v1 (optional)

Quick checks:
- Review: `cmo/audits/model-orchestration-verification-YYYY-MM-DD.md`
- Spot-check last_run_at updated for each worker type.

## 4) “Writing quality” spot test
Pick one typical writing task each:
- Outreach email
- Landing page section rewrite
- X thread draft

Run once using gpt-5.4-mini. Evaluate with a simple rubric:
- Specificity (numbers, concrete claims)
- Non-cringe tone (no generic templates)
- Strong CTA
- ICP alignment (geo + use case)
If quality drops, tighten prompts/SOULs before changing models.

## 5) “Research quality” spot test
Pick one research deliverable:
- competitor scan delta
- SERP gap summary

Run with Kimi K2.5. If it’s verbose or drifts:
- add stricter output format requirements
- consider Kimi → gpt-5.4-mini for that worker temporarily

## 6) Update the master model list
- Add/remove models that changed availability.
- Update notes on failure modes and best uses.
- Make 1 explicit decision: keep vs swap the ops free model.

## 7) Log the refresh
Write a short entry:
- date
- what changed (models, prompts, worker pinning)
- expected cost impact
- any new escalation triggers

Suggested log location:
- `cmo/audits/model-refresh-YYYY-MM-DD.md`
