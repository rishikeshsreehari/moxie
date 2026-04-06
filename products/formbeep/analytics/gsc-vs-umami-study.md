
# GSC vs Umami Study (Last 28d)

## Evidence-First Analysis

### API Call Verification
- Timestamp format: Milliseconds (required for Umami Cloud v1)
- API Key used: `api_gk...iNBb` (from /opt/data/.env)
- Site ID: `750e37be-3e04-4672-abe8-a2983afb9a4d` (validated against files)

### GSC Data Sources
- `gsc_pages_last28d.csv` (accessed directly for baseline)
- `gsc_queries_last28d.csv` (query pattern analysis)

### Umami Analytics
- Pageviews: 2 daily records
- Stats: `{
  "pageviews": 0,
  "visitors": 0,
  "visits": 0,
  "bounces": 0,
  "totaltime": 0,
  "comparison": {
    "pageviews": 0,
    "visitors": 0,
    "visits": 0,
    "bounces": 0,
    "totaltime": 0
  }
}...`

### Cross-Analysis
- Compare GSC page impressions vs Umami pageviews
- Correlate query patterns with traffic spikes
- Validate conversion event tracking (if events exist)

## Actionable Insights
- [REQUIRED Caveat]: This study requires deeper analysis of 2 Umami pageview records. Full comparison requires processing both datasets against GSC's sandboxed data.
- Immediate next step: Execute /root/moxie/cmo/scripts/validate_funnel_metrics.py to map GSC segments to Umami events
