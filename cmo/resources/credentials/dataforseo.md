# DataForSEO (SERP API) — org credential reference

Owner: Moxie
Added: 2026-04-01

## Policy
- Do NOT run paid SERP queries without explicit Rishi approval.
- Budget remaining: ~$0.50 (as of Rishi note). Treat as scarce.
- Always ask permission before any API call that spends credits.

## Where the secret lives (NOT in git)
- File: /root/moxie_secrets/dataforseo_basic_auth.txt
- Contains: login:password + base64.

## Intended use (first use-case)
- Validate US demand for SMS notifications (keywords: form to SMS, contact form SMS alerts, etc.) before any Twilio/A2P setup.

## API notes
- Auth: Basic Auth (base64 of login:password)
- Use DataForSEO docs to confirm endpoints and pricing per request.

## What to produce from a test run
- 1 test query only (unless Rishi approves more)
- Output: keyword, top 10 results titles/domains, intent notes, and whether the SERP is dominated by incumbents.
