# Model orchestration policy (crons + workers)

Last updated (UTC): 2026-04-02
Owner: Rishi + Moxie

Goal: reduce OpenAI/Codex burn while keeping output quality high.

## Defaults (by task type)

### 1) Ops / housekeeping (cron status, queue scan, git autopush)
- Primary: **OpenRouter / stepfun/step-3.5-flash:free**
- Why: cheap + fast; output quality is not the bottleneck.

### 2) Writing roles (content drafts, outreach, lifecycle, copy)
- Primary: **OpenAI Codex / gpt-5.4-mini**
- Why: consistently higher writing quality than OpenRouter free-tier.

### 3) Research roles (long-context synthesis)
- Primary: **OpenCode Go / kimi-k2.5**
- Why: strong long-context synthesis without burning Codex.

### 4) High-leverage decisions / multi-step execution
- Primary: **OpenAI Codex / gpt-5.2**
- Why: sweet-spot premium model for correctness + planning.

## Escalation: when Moxie uses gpt-5.4
Escalate from gpt-5.2 → **gpt-5.4** only if one of:
1) Irreversible strategy changes (positioning/pricing/product direction)
2) Spend decisions > $500
3) Repeated autonomy/system failures (same failure persists across 2+ cycles)
4) High-risk external comms (brand/legal sensitivity)

## Free-model matrix (avoid “Free Models Router”)

### Ops / housekeeping
1) stepfun/step-3.5-flash:free
2) qwen/qwen3.6-plus-preview:free (if Step is too shallow)
3) minimax/minimax-m2.5:free (last resort)

### Writer fallback (if Codex unavailable)
1) llama-3.3-70b (stable writing)
2) gemma-3-27b (very stable, bland)

### Research fallback (if OpenCode fails AND Codex unavailable)
1) qwen/qwen3.6-plus-preview:free
2) minimax/minimax-m2.5:free

## Cron job pinning (what is enforced)

### Ops crons → OpenRouter Step 3.5 Flash
- formbeep-hourly-heartbeat
- formbeep-daily-user-count-checkin
- formbeep-daily-traffic-check
- formbeep-search-check
- codex-dashboard-update-checkin
- weekly-free-models-reminder
- codex-weekly-resume-premium
- issues-rishi-watch
- mira-daily-kpi
- moxie-hq-autocommit-push
- cmo-delegation-queue-runner (already)

### Writing workers → Codex gpt-5.4-mini
- kiro-worker (conversion copy)
- ember-worker (outreach)
- rumi-worker (content)
- luna-worker (lifecycle)
- pax-worker (partnerships)
- orion-worker (outbound)
- nova-worker (paid acquisition)

### Research workers → OpenCode kimi-k2.5
- astra-worker (growth research)
- vale-worker (competitor intel)
- vale-monthly-competitor-scan
- iris-weekly-formbeep-repo-copy-audit

### High-leverage review → Codex gpt-5.2
- formbeep-weekly-growth-review
- moxie-memory-skill-audit
- moxie-daily-self-improvement

### Governance-lite (hourly) → OpenRouter Qwen free
- moxie-daily-governance
- moxie-orchestration-reconciler

Rationale: these run hourly; pinning them to Codex would create steady burn. Escalation happens via the weekly review (gpt-5.2) or manual escalation to gpt-5.4.

## Implementation notes (no code required)
This is implemented by **pinning provider/model per cron job** via the Hermes cron registry.
Important pitfall: when changing providers, also ensure the job’s `base_url` matches the provider.

Suggested `base_url` overrides when pinning:
- openai-codex → https://chatgpt.com/backend-api/codex
- openrouter   → https://openrouter.ai/api/v1 (optional; can be null)
- opencode-go  → https://opencode.ai/zen/go/v1/chat/completions
