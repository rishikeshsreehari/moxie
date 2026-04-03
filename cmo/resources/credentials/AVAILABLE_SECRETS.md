# Available secrets & mounts (worker reference)

Goal: stop asking the founder for exports when credentials are already mounted.

## Umami (Cloud)
- API key: `/opt/data/.env` → `UMAMI_API_KEY=...`
- API base: `https://api.umami.is/v1`
- Timestamp unit: **milliseconds** for startAt/endAt in this environment.

## Google Search Console (GSC)
- Service account JSON (mounted in container):
  - `/root/moxie/secrets/google-service-account.json`
- Verified accessible properties (via API):
  - `sc-domain:formbeep.com`
  - `sc-domain:stackstats.app`

## Notes
- Do not print or commit secret contents.
- Prefer exporting derived artifacts (CSVs, reports) into repo rather than asking Rishi to export manually.
