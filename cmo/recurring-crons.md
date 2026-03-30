# Recurring Crons

Last updated: 2026-03-30
Status: active

## Scheduled jobs

1. formbeep-hourly-heartbeat
- Schedule: every hour
- Purpose: Moxie wakes up, checks priorities/status/signals, sees if subagents need help, and reports anything important to Rishi

2. formbeep-daily-user-count-checkin
- Schedule: every 24 hours
- Purpose: ask Rishi for latest free-user and paid-user counts until Cloudflare access is connected

3. formbeep-daily-traffic-check
- Schedule: daily at 10:00 UTC
- Purpose: pull Umami traffic, top pages, and signup-event movement for the last 24h vs previous 24h

4. formbeep-search-check
- Schedule: Mondays and Thursdays at 10:00 UTC
- Purpose: pull Google Search Console search trends for the last 7d vs previous 7d

5. formbeep-weekly-growth-review
- Schedule: Mondays at 11:00 UTC
- Purpose: produce a weekly KPI and growth review with priorities

## One-shot background work queued
1. formbeep-background-opportunity-scan
- Schedule: once in 30 minutes
- Purpose: deep web research to find high-leverage growth opportunities

2. formbeep-background-competitor-and-copy-review
- Schedule: once in 45 minutes
- Purpose: analyze competitors plus FormBeep repo/site copy and report recommendations

## Operating note
Heavy research belongs in one-shot or periodic background jobs, not in live chat. The hourly heartbeat is for orchestration, prioritization, and escalation — not deep competitor analysis every hour.
