# Model Fallback Flow & Usage Guide

## Priority Chain

When executing coding tasks, follow this strict order:

1. **Codex (gpt-5.2 / openai-codex)** — Default/premium model
   - Use for: Complex architecture, production code, critical features
   - Cost: Premium (monitor 5-hour limit)
   - Availability: When Codex window is active (track in `/root/moxie/cmo/codex-usage.md`)

2. **OpenCode Go** — Secondary coding-optimized provider
   - Use for: Feature implementation, refactoring, PR reviews, long-running coding tasks
   - Cost: $10/month subscription for open models
   - Benefits: Coding-optimized models (Kimi, GLM), high reasoning capability
   - Best for: Medium-complexity code work when Codex is rate-limited
   - Models: `kimi-k2.5`, `glm-5`, `minimax-m2.5`
   - API Key: `OPENCODE_GO_API_KEY` (set in `/opt/data/.env`)
   - Base URL: `https://opencode.ai/zen/go/v1`
   - **Note:** These models use reasoning tokens - set `max_tokens >= 500` for reliable responses

3. **OpenRouter Free Models** — Fallback when premium unavailable
   - Fallback order: qwen/qwen3-coder-480b-a35b:free → stepfun/step-3.5-flash:free → minimax/minimax-m2.5:free → llama-3.3-70b-instruct:free
   - Use for: Simple tasks, scripting, configuration, documentation
   - Cost: Free (subject to rate limits)
   - Monitor token usage to avoid hitting free-tier caps

## Quick Decision Matrix

| Task Type | Primary | Fallback 1 | Fallback 2 |
|-----------|---------|------------|------------|
| Production code | Codex | OpenCode Go | OpenRouter free |
| Refactoring | Codex | OpenCode Go | OpenRouter free |
| Bug fixes | Codex | OpenCode Go | OpenRouter free |
| Tests/Scripts | Codex | OpenCode Go | OpenRouter free |
| Documentation | Codex | OpenCode Go | OpenRouter free |
| Quick scripts | Skip Codex | OpenCode Go | OpenRouter free |

## Provider Architecture

### OpenCode CLI vs OpenCode Go vs OpenCode Zen

**OpenCode CLI** (`opencode` command):
- Autonomous coding agent that runs in terminal
- Can use various backend providers (OpenRouter, OpenCode, etc.)
- Models prefixed with `opencode/` (e.g., `opencode/qwen3.6-plus-free`)
- Works with `OPENCODE_GO_API_KEY` or `OPENROUTER_API_KEY` env vars
- Usage: `opencode run 'task' --model opencode/qwen3.6-plus-free`

**OpenCode Go** (Hermes provider `opencode-go`):
- Direct API access to OpenCode's coding-optimized models
- Models: `kimi-k2.5`, `glm-5`, `minimax-m2.5`
- Requires `OPENCODE_GO_API_KEY` env var
- Base URL: `https://opencode.ai/zen/go/v1`
- **Important:** Models use reasoning tokens, set `max_tokens >= 500`

**OpenCode Zen** (Hermes provider `opencode-zen`):
- Pay-as-you-go API for premium models (GPT-5, Claude, etc.)
- Requires separate `OPENCODE_ZEN_API_KEY` env var
- Base URL: `https://opencode.ai/zen/v1`
- Models: `gpt-5.4-pro`, `gpt-5.4`, `claude-sonnet-4`, etc.

## Using OpenCode Go in Hermes

### Direct API Calls

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENCODE_GO_API_KEY"),
    base_url="https://opencode.ai/zen/go/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.5",  # Best coding model
    messages=[{"role": "user", "content": "Write a Python function to parse CSV"}],
    max_tokens=1000  # Required: models use reasoning tokens
)
```

### Via Hermes Fallback

The Hermes fallback chain automatically tries providers in order:
1. primary model (`openai-codex`/`gpt-5.2`)
2. fallback_providers (see `/opt/data/config.yaml`)

When Codex is rate-limited (HTTP 429), Hermes automatically fails over to OpenCode Go models.

### Via OpenCode CLI (Delegation)

For complex autonomous coding tasks:

```bash
# One-shot task
opencode run 'Add retry logic to API calls in src/api.py' --model opencode/qwen3.6-plus-free

# With file context
opencode run 'Review this PR' -f diff.txt -f changed-file.py

# Interactive session
opencode
```

## Configuration Files

### Environment Variables (`/opt/data/.env`)

```bash
# OpenCode Go API key
OPENCODE_GO_API_KEY=sk-xxx...

# OpenRouter (fallback)
OPENROUTER_API_KEY=sk-or-xxx...
```

### Fallback Configuration (`/opt/data/config.yaml`)

```yaml
model:
  default: gpt-5.2
  provider: openai-codex
  base_url: https://chatgpt.com/backend-api/codex
fallback_providers:
  - provider: opencode-go
    model: kimi-k2.5
  - provider: opencode-go
    model: glm-5
  - provider: opencode-go
    model: minimax-m2.5
  - provider: openrouter
    model: qwen/qwen3-coder-480b-a35b:free
  # ... more fallbacks
```

## Verification Tests

### Test OpenCode Go Directly

```bash
# Via OpenAI-compatible API
python3 -c "
from openai import OpenAI
import os
client = OpenAI(
    api_key=os.getenv('OPENCODE_GO_API_KEY'),
    base_url='https://opencode.ai/zen/go/v1'
)
r = client.chat.completions.create(
    model='kimi-k2.5',
    messages=[{'role': 'user', 'content': 'Say: TEST_OK'}],
    max_tokens=100
)
print(r.choices[0].message.content)
"
```

### Test OpenCode CLI

```bash
# Requires OPENCODE_GO_API_KEY or OPENROUTER_API_KEY in env
opencode run 'Respond with exactly: OPENCODE_TEST_OK' --model opencode/qwen3.6-plus-free
# Expected: OPENCODE_TEST_OK
```

## Cost Management

### Codex Limits
- Track 5-hour weekly cap in `/root/moxie/cmo/codex-usage.md`
- When limit hit, switch to OpenCode Go

### OpenCode Go Limits

| Window | Dollar Limit | Est. Requests (Kimi K2.5) |
|--------|--------------|--------------------------|
| 5 hours | $12 | ~1,850 |
| Weekly | $30 | ~4,630 |
| Monthly | $60 | ~9,250 |

**Cost:** $5 first month, then $10/month.

**Model request capacity varies:**
- MiniMax M2.5: ~20,000 requests per 5hr (cheapest)
- Kimi K2.5: ~1,850 requests per 5hr (mid-tier)
- GLM-5: ~1,150 requests per 5hr (most expensive)

**When limits reached:** Fall back to OpenRouter free models.

**Dashboard:** https://opencode.ai/zen (rolling/weekly/monthly usage %)

### OpenRouter Free Limits
- Track token consumption across all workers
- If quotas tight, stagger jobs (max 2 workers/hour) and reduce cadence

## Integration with Moxie Orchestration

- Worker crons should respect the fallback chain automatically.
- If Codex is rate-limited (detect via error messages), retry with OpenCode Go.
- If OpenCode Go unavailable or over limit, fall back to OpenRouter free models.
- Document model choice in worker logs for auditability.

## Troubleshooting

### OpenCode Go returns empty content

- **Cause:** Models use reasoning tokens, `max_tokens` too low
- **Fix:** Set `max_tokens >= 500` (prefer 1000+ for complex responses)

### OpenCode CLI: `opencode: command not found`

- **Fix:** Install with `npm i -g opencode-ai@latest`

### OpenCode CLI: `No authenticated providers`

- **Fix:** Set `OPENCODE_GO_API_KEY` or `OPENROUTER_API_KEY` in environment

### Hermes fallback not working

- **Check:** `grep OPENCODE_GO_API_KEY /opt/data/.env` - key must be present
- **Check:** Config has `opencode-go` in `fallback_providers:`
- **Check:** Model IDs are correct (`kimi-k2.5`, `glm-5`, `minimax-m2.5`)

### Model not supported error

- **Cause:** Using `opencode/` prefix models with direct API
- **Fix:** Use `opencode` CLI for those models, or use Hermes-native provider models