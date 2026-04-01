# Moxie Growth Framework — Rules (non-negotiables)

These are the rules we learned the hard way during FormBeep. They exist to prevent "whim decisions" and ensure assets are shippable/reusable.

## Decision-making rules
1) Data-first geo/channel/keyword decisions
- No geo targeting recommendation until we have at least ONE valid data source:
  - Umami/GA country + conversion (preferred)
  - OR GSC query + country
  - OR credible keyword volume/CPC source.
- If analytics is blocked, log it as a blocker and pause paid decisions.

2) Assumptions must be labeled
- Every recommendation must be either:
  - cited (analytics/GSC/keyword data), OR
  - explicitly marked as an assumption + what would falsify it.

3) One variable at a time
- For tiny budgets or early stage, test ONE channel + ONE message angle at a time.

## Execution rules
4) Execution packs > plans
- If something needs founder credentials, we don’t wait — we ship a copy/paste execution pack so founder can run it fast.

5) Ship to disk with stable paths
- Every deliverable lives under `/root/moxie/products/<product>/...`.
- Never leave critical work only in chat.

6) Verification before claims
- Don’t claim “working” unless verified end-to-end.

## Governance / scope rules
7) Blockers are explicit
- Anything requiring human input/credentials goes to `/root/moxie/cmo/issues_rishi.md` with an exact ask.

8) Repo safety
- Never push to product repos (e.g., formbeep.git). HQ only.

9) Communication hygiene
- Default: local-only outputs; only message you when blocked or you explicitly request a report.

## Learning loop rules
10) Every new angle becomes reusable
- After each product/experiment, write a lessons file:
  `/root/moxie/cmo/frameworks/learned/<YYYY-MM-DD>-<product>-lessons.md`
- If it changes the framework, patch the skill/templates immediately.
