# FormBeep Monitoring Cron Plan

Last updated: 2026-03-30
Status: draft

## Goal
Run recurring evaluations of traffic and Google search performance so Moxie can track momentum and spot channel changes early.

## Intended monitoring
### Daily traffic check
Inputs
- Umami traffic metrics
- top pages
- source breakdown
- sign-up intent events if available

Outputs
- daily traffic summary
- changes vs previous period
- anomalies/opportunities

### Twice-weekly search check
Inputs
- Google Search Console clicks
- impressions
- CTR
- average position
- top queries/pages/countries

Outputs
- emerging queries
- falling pages
- opportunities to publish or refresh pages

### Weekly growth report
Inputs
- Umami + Search Console + notable product changes

Outputs
- KPI scorecard
- traffic trend
- acquisition insights
- next-week priorities

## Current status
- Daily founder check-in for free/paid counts is scheduled every 24 hours via cron job `formbeep-daily-user-count-checkin`.
- Traffic/search monitoring crons should be added next now that Umami and GSC are validated.
