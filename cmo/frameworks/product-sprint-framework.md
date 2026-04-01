# Moxie Product Sprint Framework (FormBeep-derived)

Purpose
- A reusable, product-agnostic framework to take a new indie product from “we have a landing page” to “repeatable acquisition experiments + first revenue” with minimal founder time.
- This is derived from what we actually executed for FormBeep (SEO + Reddit + directories + partnerships + lifecycle + outbound + analytics + competitor intel + orchestration).

Core operating rules (non-negotiable)
1) Data-first decisions: do not pick geos/channels/keywords on instinct. Use analytics (Umami/GA/GSC) + keyword data.
2) Execution packs over plans: if an action needs founder credentials, create copy/paste bundles + step-by-step so the founder can execute in <15 minutes.
3) Blockers are explicit: anything requiring human input/credentials goes to /root/moxie/cmo/issues_rishi.md under Open with exact “what I need.”
4) Every asset ships to disk under /root/moxie/products/<product>/… with stable paths.
5) Never claim something works unless verified end-to-end.

Directory conventions
- Product root: /root/moxie/products/<product>/
- Always create/maintain: resources.md, overview.md, icp.md, projections.md
- Use subfolders when it becomes execution-heavy:
  - seo/
  - outreach/
  - distribution/
  - partnerships/
  - lifecycle/
  - outbound/
  - dev-notes/
  - briefings/

Phase 0 — Sprint setup (Day 0)
Inputs
- Product URL
- Pricing + plan limits
- Primary notification channel(s) / differentiation
- Founder constraints: max ad budget, time/week, tools allowed

Outputs (ship to disk)
1) /root/moxie/products/<product>/overview.md
   - what it is, who it’s for, main promise, current traction, constraints
2) /root/moxie/products/<product>/resources.md
   - credentials needed list (email inbox, portals, analytics), tool links, IDs
3) /root/moxie/products/<product>/icp.md
   - 1-2 ICPs, pains, triggers, objections, what they currently use
4) /root/moxie/products/<product>/projections.md
   - simple funnel math (traffic → signup → activated → paid)

Gates
- If analytics is not accessible, file a blocker immediately; do not proceed with paid decisions.

Phase 1 — Instrumentation + truth (Day 0–1)
Goal
- Establish “source of truth” for traffic, signups, top pages, referrers, geo, and search queries.

Outputs
1) /root/moxie/products/<product>/analytics-report.md
   - last 7/30 days; PV, visitors, top referrers, top pages, countries, conversion points
2) /root/moxie/products/<product>/analytics.md
   - how to query analytics (IDs, endpoints, dashboards)
3) If SEO matters: /root/moxie/products/<product>/seo/gsc-quick-audit.md

Gates
- If we can’t pull analytics programmatically, document the workaround (host-run, exports, screenshots) and standardize it.

Phase 2 — Acquisition surface area build (Day 1–3)
Goal
- Build the “distribution inventory” so execution is easy as soon as creds exist.

Workstreams + required outputs
A) SEO
- /seo-keywords.md (seed keyword map)
- /technical-seo-audit.md (prioritized fixes + implementation notes)
- /content-gap-scan.md (topics, competitors, internal links)
- /seo/* demand probes (DataForSEO/GSC-driven, not assumptions)

B) Community (Reddit-first if relevant)
- /reddit-strategy.md (positioning, subreddits, do/don’t)
- /outreach/reddit-campaign-plan.md (calendar)
- /outreach/reddit-post-comment-scripts.md (scripts)
- /outreach/reddit-posting-tracker.md (rules table + activity log)
- /outreach/reddit-week1-execution-pack.md (copy/paste posts + comment seeds)

C) Directories
- /directory-submissions-list.md (master list)
- /directory-submissions-p1.md (P1 targets + ready-to-submit bundles)
- /distribution/directory-submissions-log.md (tracker)
- /directory-submissions-today-pick.md (daily “2-pick” execution pack)

D) Partnerships / Marketplaces
- /partnerships/platform-applications-week1.md (and week2/week3)
- Each must include: copy, metadata, screenshots needed, exact submission steps

E) Lifecycle
- /lifecycle/onboarding-emails.md (Day 0/1/3/7/14)

F) Outbound
- /outbound/outbound-pack.md (prospects + sequences)

Phase 3 — Conversion + positioning hardening (Day 3–5)
Goal
- Make the landing page and narrative match the top acquisition hooks.

Outputs
- /pricing-war-room-<month>.md (pricing + packaging recommendations)
- /dev-notes/landing-and-docs.md (copy/UX issues found, quick wins)
- If needed: /tally-growth-teardown.md or competitor teardown to steal winning patterns

Gates
- Any proposed change must specify: impact hypothesis + measurement plan + rollback risk.

Phase 4 — Paid acquisition (ONLY after Phase 1 truth) (Day 5+)
Principle
- Paid is a measurement tool and demand amplifier, not a substitute for distribution.

Requirements before spending even $10
- Confirm geo + conversion propensity from analytics
- Confirm search demand from GSC/keyword tools
- Ensure UTMs and landing tracking

Outputs
- /paid-acquisition-plan.md (data-cited assumptions)
- /paid-ads/plan.md (campaign structure, creatives, UTMs)
- /cmo/sops/paid-ads-sop.md must be followed (naming, UTMs, taxonomy)

Phase 5 — Weekly operating cadence (ongoing)
Daily
- Check KPIs, unblock execution, publish 1 asset (post/submission/email)

Weekly
- Growth review: what moved signups/activated/paid?
- Update: next week’s 3 highest leverage bets

Always
- Keep “issues_rishi.md” current and minimal.

Learning loop (framework evolution)
After every sprint or major experiment:
1) Create a short postmortem:
   - /root/moxie/cmo/frameworks/learned/<YYYY-MM-DD>-<product>-lessons.md
   Must include:
   - What we tried
   - What worked / didn’t
   - What assumptions were wrong
   - What to change in this framework next time
2) Patch the skill (see below) to incorporate the lesson (tighten gates/checklists/templates).

Definition of done (for a “first sprint”)
- Instrumentation verified
- 3 acquisition channels have execution packs ready
- 1 channel has at least 3 execution attempts completed (even if founder-executed)
- Blockers list is accurate and contains only real human needs
- A weekly cadence exists with next 3 bets
