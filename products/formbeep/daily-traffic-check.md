# FormBeep — Daily traffic check

**Window (UTC):** 2026-03-31 10:02 → 2026-04-01 10:02 (last 24h)

**Compared to:** 2026-03-30 10:02 → 2026-03-31 10:02 (previous 24h)

## Core metrics (last 24h vs previous 24h)

- **Visitors:** n/a (n/a vs prev n/a)
- **Visits:** n/a (n/a vs prev n/a)
- **Pageviews:** n/a (n/a vs prev n/a)

## Top pages (last 24h)

- (no data)

## Top referrers (last 24h)

- (no data)

## Tracked events / CTAs (last 24h)

- (no data)

## Anomalies / opportunities

### Anomalies
- None detected by simple heuristics (check raw series if needed).

### Opportunities (next actions)
- No event data returned (or API endpoint unavailable). Verify Umami custom events are firing on CTAs and that the API supports `metrics?type=event`.

## Data quality / API notes
- This environment cannot currently pull Umami Cloud analytics:
  - Without a browser-like `User-Agent`, requests return **403** with Cloudflare error code **1010**.
  - With a browser-like `User-Agent`, requests return **401 Unauthorized** (suggesting the current `UMAMI_API_KEY` is invalid/revoked or lacks access).
- Result: today’s report is **API-blocked**; metrics/pages/referrers/events couldn’t be fetched.
