# OpenCode Quick Start Guide

## What is OpenCode?

OpenCode exists in multiple forms - it's important to understand the difference:

### 1. OpenCode CLI (`opencode` command)
- **Type:** Autonomous coding agent (like Claude Code, Codex CLI)
- **What it does:** Takes prompts, edits files, runs tests, creates PRs
- **How to use:** `opencode run 'your task' --model <model>`
- **Model format:** `opencode/<model>` (e.g., `opencode/qwen3.6-plus-free`)
- **Auth:** Uses `OPENCODE_GO_API_KEY` or `OPENROUTER_API_KEY` from environment

### 2. OpenCode Go (Hermes provider `opencode-go`)
- **Type:** Direct OpenAI-compatible API endpoint
- **What it does:** Provides coding-optimized models via API
- **How to use:** Set `provider: opencode-go` in Hermes config
- **Model format:** `kimi-k2.5`, `glm-5`, `minimax-m2.5` (no prefix)
- **Auth:** Requires `OPENCODE_GO_API_KEY` env var
- **Base URL:** `https://opencode.ai/zen/go/v1`
- **Important:** Use `max_tokens >= 500` for reliable responses

### 3. OpenCode Zen (Hermes provider `opencode-zen`)
- **Type:** Pay-as-you-go API for premium models
- **What it does:** Provides GPT-5, Claude, and other curated models
- **How to use:** Set `provider: opencode-zen` in Hermes config
- **Model format:** `gpt-5.4-pro`, `claude-sonnet-4` (no prefix)
- **Auth:** Requires **separate** `OPENCODE_ZEN_API_KEY` env var
- **Base URL:** `https://opencode.ai/zen/v1`

## Quick Start

### Install OpenCode CLI

```bash
npm i -g opencode-ai@latest
# or
brew install anomalyco/tap/opencode
```

### Verify Installation

```bash
opencode --version
# Expected: opencode/1.3.9 or higher
```

### Authentication

OpenCode CLI automatically detects API keys from environment variables:

```bash
# Option 1: OpenCode Go API key (subscription)
export OPENCODE_GO_API_KEY=sk-xxx...

# Option 2: OpenRouter API key (pay-as-you-go)
export OPENROUTER_API_KEY=sk-or-xxx...
```

**Important:** Do NOT run `opencode auth add` manually - the CLI reads keys from env vars automatically.

### Smoke Test

```bash
# Test with OpenCode models
opencode run 'Respond with exactly: OPENCODE_READY' --model opencode/qwen3.6-plus-free
# Expected: OPENCODE_READY

# Test with OpenRouter models
opencode run 'Say HELLO' --model openrouter/anthropic/claude-sonnet-4
```

## Usage Patterns

### One-Shot Tasks (Recommended for Automation)

```bash
# Simple task
opencode run 'Add retry logic to fetch_data() in src/api.py'

# With explicit model
opencode run 'Fix the bug in auth.py' --model opencode/qwen3.6-plus-free

# With file context
opencode run 'Review this PR' -f diff.txt -f changed-file.py

# With working directory
opencode run 'Run the test suite' --dir /root/moxie/products/formbeep
```

### Interactive Sessions

```bg
opencode
# Opens TUI, type tasks interactively
# Use Ctrl+D to exit
```

For background TUI sessions, see the skill file for process management.

## Available Models

### Via OpenCode CLI (`opencode run --model ...`)

```
opencode/qwen3.6-plus-free     - Qwen 3.6 Plus (free tier)
opencode/big-pickle            - Big Pickle model
opencode/mimo-v2-omni-free     - Mimo V2 Omni (free tier)
opencode/minimax-m2.5-free     - MiniMax M2.5 (free tier)
opencode/nemotron-3-super-free - Nemotron (free tier)
# Run 'opencode models' for full list
```

### Via OpenCode Go Provider (Hermes)

```
kimi-k2.5      - Kimi K2.5 (best for coding)
glm-5          - GLM-5
minimax-m2.5   - MiniMax M2.5
```

### Via OpenCode Zen Provider (Hermes - requires separate key)

```
gpt-5.4-pro     - GPT-5.4 Pro
gpt-5.4         - GPT-5.4  
gpt-5.2         - GPT-5.2
claude-opus-4-6 - Claude Opus 4.6
claude-sonnet-4 - Claude Sonnet 4
# See Hermes models list for full list
```

## Integration with Moxie

### Fallback Chain

When Hermes encounters a rate limit (429) from Codex:
1. First tries Codex again (may be temporary)
2. Falls back to OpenCode Go (`kimi-k2.5`, then `glm-5`, then `minimax-m2.5`)
3. Falls back to OpenRouter free models

### Delegation

Use the `opencode` skill to delegate coding tasks:

```python
# In Hermes/Python
from hermes_tools import terminal

# One-shot delegation
terminal(
    command="opencode run 'Implement user authentication' --model opencode/qwen3.6-plus-free",
    workdir="/root/moxie/products/formbeep"
)
```

## Cost & Usage Management

### OpenCode Go Limits

| Window | Limit | Model Estimates (requests) |
|--------|-------|---------------------------|
| 5 hours | $12 | GLM-5: ~1,150 / Kimi K2.5: ~1,850 / MiniMax M2.5: ~20,000 |
| Weekly | $30 | GLM-5: ~2,880 / Kimi K2.5: ~4,630 / MiniMax M2.5: ~50,000 |
| Monthly | $60 | GLM-5: ~5,750 / Kimi K2.5: ~9,250 / MiniMax M2.5: ~100,000 |

**Cost:** $5 first month, then $10/month subscription.

**Current Usage:** Track in OpenCode dashboard (rolling/weekly/monthly %).
- If limits reached → switch to OpenRouter free models
- Can enable "Use balance" to fall back to Zen balance after limits

### Model Costs (relative)

MiniMax M2.5 is cheapest (~20K requests/5hr), GLM-5 is most expensive (~1.1K requests/5hr).
For routine coding tasks, prefer MiniMax M2.5 or Kimi K2.5 over GLM-5.

### Fallback Order (Updated)

1. **Codex** (gpt-5.2) — Premium, track 5-hour weekly cap
2. **OpenCode Go** (kimi-k2.5 → minimax-m2.5 → glm-5) — Coding subscription
3. **OpenRouter free** — No-cost fallback

**Tracking:** OpenCode Go limits are in the dashboard. Hermes limits are in `/root/moxie/cmo/codex-usage.md`.

## Troubleshooting

### `opencode: command not found`

```bash
# Install
npm i -g opencode-ai@latest

# Verify PATH
which opencode
# Expected: /usr/local/bin/opencode or similar
```

### `No authenticated providers`

The CLI can't find API keys. Ensure one of:
- `OPENCODE_GO_API_KEY` is set
- `OPENROUTER_API_KEY` is set
- Or run `opencode auth login` for interactive auth

### Empty responses from OpenCode Go (Hermes)

Models use reasoning tokens. Always set `max_tokens >= 500`:

```python
response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[...],
    max_tokens=1000  # Required!
)
```

### Model not found error

You're using the wrong model format:
- For OpenCode CLI: use `opencode/qwen3.6-plus-free` (with prefix)
- For Hermes `opencode-go` provider: use `kimi-k2.5` (no prefix)
- For Hermes `opencode-zen` provider: use `gpt-5.4` (no prefix)