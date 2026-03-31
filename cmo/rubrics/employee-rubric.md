# Employee Evaluation Rubric (SapiensTech)

Purpose
- Measure each employee’s effectiveness per cycle and per deliverable.
- Drive self-improvement: update prompts/SOULs/queue rules based on recurring failure modes.

Scoring
- 1 (poor) to 5 (excellent) for each dimension.
- Overall Score = weighted sum (weights below).

## Dimensions (with weights)

1) Output completeness (20%)
- 1: Missing required sections / not written to disk / wrong file path
- 3: Mostly complete, minor gaps
- 5: Fully complete, follows spec exactly, correct paths, includes checklists

2) Business impact / leverage (25%)
- 1: Low-value busywork; unclear use
- 3: Useful but not high-leverage
- 5: Directly improves revenue/acquisition/conversion; clear next action

3) Accuracy & evidence (15%)
- 1: Unverified claims, hallucinated data
- 3: Some evidence, some assumptions
- 5: Links/data/quotes; clearly marks assumptions; no unsupported claims

4) Speed / cycle time (10%)
- 1: Repeatedly misses cycle windows or drags without output
- 3: Normal
- 5: Ships within one cycle or explicitly scopes work into sub-deliverables

5) Autonomy & unblockability (10%)
- 1: Gets stuck without stating what’s needed
- 3: Reports blockers
- 5: Produces partial value even when blocked + logs a crisp blocker in issues_rishi.md

6) Reusability / systemization (10%)
- 1: One-off prose
- 3: Some reusable artifacts
- 5: Templates, SOPs, checklists, tables, repeatable workflow

7) Communication quality (10%)
- 1: Noisy, long, unclear
- 3: Understandable
- 5: Exec-ready summary + exact file path + next actions

## Automatic pass/fail gates
FAIL if any of the below occur:
- Did not write output to disk when required
- Claims “working” without verification
- Violates scope (e.g., tries to push to product repo)

## Reviewer comments template
- What was the promised deliverable?
- What was actually produced?
- Biggest gap?
- Prompt/SOUL change to prevent recurrence?

## Per-role notes
- Analytics (Mira): Accuracy/evidence weight becomes 25%, Speed 5%
- Copy (Kiro/Iris): Business impact 30%, Evidence 10%
- Distribution (Jax/Ember/Pax): Autonomy 15%, Business impact 30%
- Paid ads (Nova): Evidence 20% (targeting rationale), Business impact 30%
