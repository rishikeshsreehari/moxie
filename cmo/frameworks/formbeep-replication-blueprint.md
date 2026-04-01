# FormBeep Replication Blueprint (what you sent, what we changed, what we analyzed, how we target)

This is the “copy this playbook for the next product” document.

## A) What you typically send me (Product Intake)
When you drop a new product in chat, capture the same inputs we used on FormBeep:
1) Product URL(s): landing, app, docs
2) One-sentence promise (in your words)
3) Primary delivery channel dependency (e.g., WhatsApp-first, SMS-first, email-first)
4) Pricing + limits + free plan details
5) Current traction snapshot (even if tiny): PV, visitors, signups, top referrers, top countries
6) Constraints: ad budget (hard cap), time/week, “don’t touch” areas (e.g., WP plugin is founder-owned)
7) Execution credentials available vs blocked (email inbox, portals, social accounts)

Template to use next time:
- /opt/data/skills/productivity/product-sprint-framework/templates/product-intake.md

## B) What we tweaked / shipped (Asset Map)
For FormBeep, we consistently produced the same categories of shipped assets:

1) Truth & instrumentation
- analytics-report.md (7/30 day truth)
- analytics.md (how to query / IDs / dashboards)
- gsc-quick-audit.md (search truth)

2) SEO foundation
- seo-keywords.md (keyword map)
- technical-seo-audit.md (fix list + patches/notes)
- content-gap-scan.md (what to write + internal links)
- demand probes (DataForSEO/GSC-driven)

3) Community distribution (Reddit)
- reddit-strategy.md (positioning, subreddits)
- reddit-campaign-plan.md (calendar)
- reddit-post-comment-scripts.md (scripts)
- reddit-posting-tracker.md (rules + activity log)
- week execution packs (copy/paste bundles)

4) Directories
- directory-submissions-list.md (master list)
- directory-submissions-p1.md (P1 pack)
- directory-submissions-today-pick.md (2-pick bundle)
- directory-submissions-log.md (dedupe + tracker)

5) Partnerships / marketplaces
- platform-applications-week1/2/3.md (submission packs)

6) Lifecycle
- onboarding-emails.md

7) Outbound
- outbound-pack.md

8) Positioning & pricing
- pricing-war-room-<month>.md
- dev-notes/landing-and-docs.md

## C) What analysis we did (Decision memos)
The key is not the number of docs; it’s the decision pattern:
- We separate “truth” (analytics + search) from “opinions.”
- Every recommendation must cite a source or be explicitly labeled an assumption.

Standard decision memo format (use for geo targeting, channel selection, pricing changes):
- /opt/data/skills/productivity/product-sprint-framework/templates/decision-memo.md

## D) How we approach targeting (repeatable method)
We target in this order:

1) Dependency-first filter
- If product’s core value depends on WhatsApp adoption, we *exclude* geos with low WA usage regardless of purchasing power.

2) Conversion propensity (not just traffic)
- Look at: signup conversion by country, paid conversion by country (if any), and “activation” proxy (did they complete setup?).

3) Intent-first keywords
- Prefer “I need X” queries over broad “best tools” queries at low traffic.

4) Execution reality
- If a channel is blocked on credentials, we still ship the execution pack so founder can run it fast.

Targeting matrix template:
- /opt/data/skills/productivity/product-sprint-framework/templates/targeting-matrix.md

## E) Blockers handling (so you don’t get spammed)
- Any credential/approval requirement becomes one bullet in /root/moxie/cmo/issues_rishi.md.
- Everything else proceeds autonomously.

## F) What rules we enforce (so decisions aren’t on a whim)
Canonical rule list:
- /root/moxie/cmo/frameworks/framework-rules.md

Key rules (summary)
- No geo/channel/keyword calls without data (analytics/GSC/keyword data) or explicitly labeled assumptions.
- Paid only after Phase 1 truth.
- Execution packs > plans when creds are blocked.
- Ship to disk with stable paths; verify before claiming.

## G) File paths checklist (so replication is mechanical)
Canonical checklist:
- /root/moxie/cmo/frameworks/deliverable-paths-checklist.md

## H) Reusable team structure (worker roles + SOULs)
We don’t redesign teams per product. We reuse these stable role identities, each with its own SOUL that defines output expectations.

FormBeep team (replicable for next product):
- Astra — Growth Research Lead (SEO, keywords, demand probes)
- Ember — Outreach & Distribution Lead (Reddit, directories)
- Jax — SaaS Growth Operations Lead (distribution ops, daily picks)
- Kiro — Conversion Copy Lead (landing, blog, emails)
- Mira — Analytics & Reporting Lead
- Vale — Competitor Intelligence Lead
- Pax — Partnerships / BD Lead (marketplaces, integrations)
- Rumi — Blog & Content Analyst (content gap, topics)
- Luna — Lifecycle / CRM Lead (onboarding emails)
- Orion — Outbound Lead (cold email packs)
- Forge — Product/Codebase Inspector (technical SEO, GSC fixes)

Each role:
- Has a SOUL at `/root/moxie/cmo/employees/<role>-soul.md`
- Knows its output directory (product-agnostic; set per product)
- Follows quality gates: must read KPIs, produce complete deliverables, use atomic writes

If a new product needs a new specialty (e.g., “paid media”), add a new role and its SOUL, then add it to the framework’s “standard roles” list so it becomes reusable.

## I) How this blueprint evolves (learning loop)
When a new product teaches us a new angle, we do two things:
1) Write a lessons entry:
   /root/moxie/cmo/frameworks/learned/<YYYY-MM-DD>-<product>-lessons.md
2) Patch the framework skill/templates so the next product automatically benefits.
