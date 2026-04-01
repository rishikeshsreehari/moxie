# Employee QA Framework (Draft)

Owner: Moxie
Status: DRAFT (needs Rishi review)

Goal: define how work moves from Employees → Moxie QA → Founder-ready.

## Principles
1) “Hard requirements” are conditional by deliverable type (not universal).
2) Canonical facts must be sourced from product truth docs (avoid copy drift).
3) Rubric score is necessary but not sufficient.
4) Founder sees only QA-passed outputs.

## Deliverable Types → QA Checklists

### A) Blog post (non-comparison)
Hard requirements:
- Canonical facts match product truth file (e.g., /root/moxie/products/formbeep/briefings/canonical-facts.md)
- SEO structure: clear H2s, internal links, non-filler expansions
- No incorrect claims (especially integrations)
Should be present:
- Explicit slug (if routing requires it)
- `thumb_prompt` (if we want consistent thumbnail generation)

### B) Blog post (comparison “X vs Y”)
Hard requirements:
- Everything in A
- Comparison table (this is what you meant: only for comparison posts)

### C) Technical SEO fix plan (Forge)
Hard requirements:
- Specific issue → evidence → proposed fix → risk → verification steps
- Patch-ready diffs or exact file/line instructions

### D) Directory submission pack (Jax)
Hard requirements:
- Copy/paste bundle + exact submission URL + what to screenshot/log
- Duplicate check against log

### E) Outreach plan/tracker (Ember/Orion/Pax)
Hard requirements:
- Guardrails + compliance notes + “do not do” list
- A logging schema so we can answer “have we done this before?”

### F) Analytics report (Mira/Astra)
Hard requirements:
- Data source + time window + caveats
- Clear recommended next action and expected impact

## Per-Employee QA Rules (to be copied into SOULs)
- Each employee gets a short “QA contract”: what must be true before marking COMPLETED.
- Moxie owns the founder-ready gate; employees own self-checks and truth docs.

## Rubric improvements (task-scorer.py)
- Add deliverable-type-aware checks (wordcount thresholds for SEO posts, required frontmatter keys, required table for comparison posts).
- Add a “canonical facts lint” hook per product.

## Rollout plan
1) Rishi reviews this doc and marks which items are hard vs optional per deliverable type.
2) Moxie patches each employee SOUL with only the relevant conditional requirements.
3) Update task-scorer.py heuristics accordingly.
4) Apply to new tasks only (don’t retroactively rewrite history).
