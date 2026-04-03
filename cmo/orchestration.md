# Moxie Orchestration State — Sapiens Technology LLC (SapiensTech)
# Last updated: 2026-04-03T13:14:56Z
# 
# HOW THIS WORKS:
# Every cron job reads this file for context. When done, it updates relevant sections.
# Moxie (CMO) reviews this file and decides next actions.
# No manual prompt updates needed — agents read state from here.
# 
# SYSTEM IMPROVEMENTS (v2):
- Atomic state updates: workers write to tmp files first, then rename
- Retry logic: failed tasks get marked RETRY(1/3) before escalation
- Task prioritization: P0 (blockers), P1 (revenue), P2 (growth), P3 (ops)
- KPI tracking: every task completion updates KPI progress metrics
- Cron collision mitigation: workers staggered across the hour (no longer all at :05)
- Model stability: worker crons pinned to Codex-compatible models (avoid max_retries_exhausted from provider/model mismatch)
# 
# DELEGATION SYSTEM (HQ, product-agnostic):
- "Do not run tooling during live chat; queue work orders instead." Append to: /root/moxie_hq/cmo/delegation-queue.md
- During ops cycle (or by the orchestration reconciler when appropriate), run:
    python3 /root/moxie_hq/cmo/scripts/process_delegation_queue.py
    python3 /root/moxie_hq/cmo/scripts/process_artifacts.py
- These processors ONLY edit HQ files under /root/moxie_hq/cmo and do not require new cron scheduling.
# 
# MISSION
- Company: Sapiens Technology LLC (SapiensTech)
- Goal: grow a portfolio of indie products to consistent revenue via repeatable acquisition + conversion systems
# 
# ACTIVE PRODUCT (current sprint)
- Product: FormBeep — form-to-SMS/WhatsApp/email notifications
- Target: English-speaking SMBs, agencies, freelance devs
- 30-day goals: 10 paid users, $100 MRR, more organic traffic
- Current stage: Pre-revenue, integrations in progress (Webflow done, Framer done, WP pending)
- Primary acquisition channels: SEO, Reddit communities, SaaS directories, WP plugin directory
# 
# KNOWN BLOCKERS
+ Blockers | Owner | Status | Action Needed |
+---------|-------|--------|---------------+
+ Codex 5-hour limit hit | System | RESOLVED | Premium window available now (reset completed) |
+ WordPress plugin resubmission (WP.org) | Rishi | BLOCKED (Founder-owned) | Do not touch/iterate in automation. Rishi will implement + resubmit. After approval, execute post-approval launch plan. |
+ Directory submissions (P1) require founder credentials/verification | Jax + Rishi | BLOCKED | Provide any existing directory accounts / inbox verification access for hello@formbeep.com (see issues_rishi.md) |
+ Umami analytics access | Mira | RESOLVED | Data pulled; see /root/moxie/products/formbeep/analytics-report.md |
+ Luna/Pax/Orion workers were misconfigured / failing (provider-model mismatch) and tasks were incorrectly marked "worker not configured" | Moxie | RESOLVED | Fixed cron providers to OpenRouter where needed; all workers producing outputs; Pax first task COMPLETED |
+ Telegram token | **RESOLVED** | FIXED | Bot paired, delivery confirmed, chat_id: 6699776435 |
+ Hermes config backup | Moxie | COMPLETED | Config backed up to /root/moxie_hq/infrastructure/hermes/ |
# 
# EMPLOYEE STATE
- All employees are SapiensTech (HQ) employees (role-based, product-agnostic). The current sprint focus is FormBeep, so most tasks route there, but no one is “hoired for a product".
# 
