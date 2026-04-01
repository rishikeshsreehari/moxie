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

## Escalation
If a repeated mistake happens twice (e.g., wrong product facts), patch the employee SOUL to include a hard requirement + reference canonical facts.
