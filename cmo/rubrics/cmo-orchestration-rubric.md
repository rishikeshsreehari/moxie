# CMO + Orchestration Effectiveness Rubric (Moxie)

Goal: evaluate Moxie’s performance as an autonomous CMO and the health of the orchestration system.

## Weekly scorecard (1–5)

1) Throughput (20%)
- Tasks completed/week (count)
- High-leverage tasks completed/week (count)

2) Outcome progress (25%)
- Activated users gained
- Paid conversions gained
- Traffic delta (7d vs prior 7d)

3) Signal quality (15%)
- Updates are factual, measurable, tied to files
- Minimal noise; clear next actions

4) Token efficiency (15%)
- Premium model usage only for high-leverage work
- Free/cheaper models used for research + drafts
- Reduces idle runs

5) Reliability (15%)
- Crons run on schedule
- No “ok but empty” outputs
- On-disk artifacts exist and are linked

6) Modularity / multi-product readiness (10%)
- New products can be added by editing assignments table + adding product folder
- Clear per-product pipelines (ads/content/distribution/lifecycle)

## Alerts
- If 3+ workers produce missing outputs in a 24h window -> escalate and patch their prompts.
- If queue has <5 items and 0 IN_PROGRESS -> IDLE ALERT.
- If premium usage >80% before reset -> downgrade models and pause non-critical crons.
