# Hermes Configuration Backup

This directory contains the version-controlled backup of Hermes AI assistant configuration files.

## Files

| File | Description |
|------|-------------|
| `config.yaml` | Main Hermes configuration (model routing, fallback providers, toolsets, personalities, etc.) |
| `.env.example` | Template for environment variables (API keys, tokens). Copy to `.env` and fill in real values. |

## What These Files Are

Hermes is a multi-platform AI assistant framework that powers the Moxie CMO system and other automations. These configuration files define:

- **Model routing**: Primary provider (OpenAI Codex) with cascading fallback providers
- **Fallback cascade**: OpenCode Go (Tier 1) → OpenRouter free models (Tier 2)
- **Toolsets**: Available tools (terminal, browser, file, web, vision, etc.)
- **Personalities**: Response styles (kawaii, technical, pirate, etc.)
- **Integrations**: Telegram, Discord, WhatsApp, cron jobs
- **API credentials**: Stored in `.env` (not committed)

## How They're Used

The Hermes Docker container runs with `/opt/data/` bind-mounted from the host system:

```bash
# Container expects config at:
/opt/data/config.yaml
/opt/data/.env

# Host source (production):
/opt/data/config.yaml
/opt/data/.env

# This backup location (version control):
/root/moxie_hq/infrastructure/hermes/
```

## ⚠️ Security Warning

**NEVER commit the real `.env` file with secrets to version control!**

The `.env` file contains:
- API keys (OpenRouter, OpenCode Go, GitHub, Umami)
- Telegram bot tokens
- Other sensitive credentials

Only `.env.example` (with placeholder values) should be committed.

## How to Restore

If the container is deleted/recreated, restore configs from this backup:

```bash
# Restore configuration files
cp /root/moxie_hq/infrastructure/hermes/config.yaml /opt/data/config.yaml

# Create .env from template (fill in real secrets)
cp /root/moxie_hq/infrastructure/hermes/.env.example /opt/data/.env
# Edit /opt/data/.env and add your actual API keys

# Verify files are in place
ls -la /opt/data/
```

## Configuration Highlights

### Fallback Provider Cascade

```yaml
fallback_providers:
  # Tier 1: OpenCode Go (coding-optimized, subscription-based)
  - provider: opencode-go
    model: kimi-k2.5
    base_url: https://opencode.ai/zen/go/v1
    api_key_env: OPENCODE_GO_API_KEY
  # Tier 2: OpenRouter free models (fallback when limits hit)
  - provider: openrouter
    model: qwen/qwen3-coder-480b-a35b:free
```

### Smart Model Routing

Routes simple queries to cheaper models to save on premium API usage.

### Telegram Integration

Configured for Moxie bot delivery with auto-threading enabled.

## Last Updated

- Backup created: 2026-03-31
- Config version: 10 (`_config_version: 10`)
- Source: `/opt/data/config.yaml` and `/opt/data/.env`
