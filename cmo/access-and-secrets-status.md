# Shared Access and Secrets Status

Last updated: 2026-03-30

## GitHub
- A shared GitHub PAT is used across product repos.
- Repo URL changes per product; auth method stays the same.
- Current status: authenticated git read access working from this environment.
- Storage: machine git credentials (not committed to repo).

## Analytics
- Umami credentials stored in root .env
- Search Console service account stored in root secrets/

## Founder-updated business metrics
Until direct Cloudflare access is connected, founder will provide FormBeep free-user and paid-user counts manually in chat on a recurring cadence.
