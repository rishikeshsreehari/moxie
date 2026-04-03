# Operating Assumptions

This file contains stable operational decisions that should not be resurfaced as action items or blockers in audits/status reports.

## Reddit & Social Media
- **Reddit Posting**: Rishi posts himself. Moxie's role is to prepare intel packets, analysis, and execution packs only. NEVER request Reddit credentials.
- **Content Strategy**: All execution packets must be founder-ready (paste-ready patterns, WHERE/WHY/HOW/WHEN, UTC+4 posting windows).

## Credentials & Service Accounts
- **GSC (Google Search Console)**: Service account exists in `/root/moxie/secrets/`. Do NOT flag as missing unless a script actually errors when trying to load it.
- **Directory Submissions**: Only proceed if existing accounts/verification are already available. Do NOT request new credential setup.

## Quality Assurance
- **Dashboard QA**: Already signed off by Rishi. Do NOT resurface as an action item.
- **Code Reviews**: Only require founder review for significant architectural decisions or brand-risk changes.

## Product Context (FormBeep & StackStats)
- **FormBeep ICP Geos**: Western Europe, Malaysia, Singapore, Australia, New Zealand, UAE, Saudi. US mainly for SMS angle.
- **StackStats ICP Geos**: US/EU only (Substack writers).
- **Analytics**: Use shared root keys + per-product website IDs (FormBeep: 750e37be-3e04-4672-abe8-a2983afb9a4d, StackStats: 52a19925-9bf4-4efe-9a42-ecc2a7f08d81).

## System Operations
- **Autopush**: Use `flock -w 60 .git/moxie_autopush.lock` to prevent concurrent pushes. Only push to `/root/moxie_hq` repo.
- **Model Routing**: Minimize Codex burn. Use OpenRouter free-tier for routine tasks; Codex gpt-5.2 for high-leverage decisions.
- **Memory Management**: System memory is near capacity (97-99%). Consolidate facts; use this file for stable operational truths.

## Audit & Reporting Rules
When surfacing audit findings, categorize items as:
- **CURRENT BLOCKER**: Evidence of actual failure (error logs, missing files, failing commands)
- **HISTORICAL/RESOLVED**: Matches assumptions in this file (do not resurface as action item)
- **REQUIRES CLARIFICATION**: Unclear status (flag for founder review)

Last Updated: 2026-04-03