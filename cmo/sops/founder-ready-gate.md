# Founder-Ready Gate (Deliverable QA)

Purpose: prevent sloppy or factually-wrong deliverables from reaching Rishi.

Rule: A deliverable is only surfaced to Rishi when it passes BOTH:
1) Rubric score (automated)
2) Founder-ready checklist (manual QA by Moxie)

## Workflow (mandatory)
1. Employee writes draft to the task output path.
2. Moxie runs `python3 /root/moxie_hq/cmo/tools/task-scorer.py <employee> <task_id> <output_file>`.
3. Moxie performs a quick founder-ready checklist (below).
4. If FAIL: Moxie does NOT surface to Rishi.
   - Create a rework task in dispatch-queue.md (QUEUED, high priority)
   - Add clear, specific feedback bullets
   - Update orchestration.md employee section to reflect QUEUED/REWORK
5. If PASS: Moxie surfaces it to Rishi (one-by-one), with:
   - Where the file is
   - 30-second summary
   - Exact decision needed

## Founder-ready checklist (Blog posts)
- Facts match canonical source: /root/moxie/products/formbeep/briefings/canonical-facts.md
  - email correct
  - free tier correct
  - pricing/claims correct
- SEO minimums:
  - Target length: 1200–1800 words unless explicitly a “short update” post
  - 6–10 H2 sections (or equivalent structure)
  - Internal links present (at least 2)
- Technical correctness:
  - If discussing Zapier→WhatsApp: confirm whether setup requires WhatsApp Business API provider (Meta Cloud API / Twilio / 360dialog) and reflect accurately
- Frontmatter required:
  - title, description, summary, date, author, image
  - slug (explicit)
  - thumb_prompt (prompt text to generate thumbnail)
- Comparisons:
  - “X vs Y” posts must include a table

## Founder-ready checklist (Copy / content plans / outward-facing messaging)
- Ground truth evidence attached (must be true *before* writing copy):
  - Live-site snapshot (current) OR repo pointers (exact template/section) OR founder-provided current copy pasted in chat
  - If analytics are referenced: link to the source file/API output used
- Claims audit:
  - No assumptions about tiers (“free forever”), platforms (“marketplace submission”), or ICP — must be evidenced
- **Execution OS v3 (hard requirement for calendars):** every planned post must include WHERE, WHY, HOW (paste-ready), WHEN (UTC + target country/timezone), WHY-NOW.
- Decision gating:
  - If evidence is missing, mark deliverable BLOCKED and first queue an evidence-collection task (scrape/snapshot/audit).

## Escalation
If a repeated mistake happens twice (e.g., wrong product facts), patch the employee SOUL to include a hard requirement + reference canonical facts.
