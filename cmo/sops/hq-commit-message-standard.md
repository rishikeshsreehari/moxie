# HQ Commit Message Standard

**Owner:** Forge (Full Stack Engineer)  
**Status:** ACTIVE (implemented 2026-04-01)  
**Applies to:** `/root/moxie_hq` repository only

---

## Problem

Generic commit messages like `Autopush: 2026-04-01T12:00:00Z` provide zero context about what changed, making:
- `git log` useless for understanding history
- Rollbacks/reverts error-prone
- Code review of autopushes impossible without diffing

---

## Solution

Replace generic timestamps with descriptive summaries that identify **what areas changed**.

### New Format

```
HQ sync: <primary area>[, <secondary area>][, ...]

- <file/path.ext>: <brief change description>
- ...
```

### Subject Line Rules

| Pattern | When to Use | Example |
|---------|-------------|---------|
| `HQ sync: dispatch + orchestration` | Queue/state changes | `HQ sync: dispatch + orchestration` |
| `HQ sync: analytics + reports` | Analytics/report updates | `HQ sync: analytics + reports` |
| `HQ sync: SOPs + documentation` | Process docs, SOPs | `HQ sync: SOPs + documentation` |
| `HQ sync: blog content` | Blog drafts, copy edits | `HQ sync: blog content` |
| `HQ sync: outreach assets` | Reddit, directories, email | `HQ sync: outreach assets` |
| `HQ sync: SEO + keywords` | Keyword research, SEO fixes | `HQ sync: SEO + keywords` |
| `HQ sync: multi-area update` | 4+ areas touched | `HQ sync: multi-area update` |

### Body (Optional but Recommended)

When ≥3 files change, include a bullet list of key files:

```
HQ sync: dispatch + orchestration

- dispatch-queue.md: 3 tasks promoted to IN_PROGRESS
- orchestration.md: worker states updated, Ember COMPLETED
- issues_rishi.md: removed resolved BetaList blocker
```

---

## Implementation

### File: `cmo/scripts/hq_autopush_locked.py`

The Python autopush script now:

1. **Analyzes staged changes** using `git diff --cached --name-only`
2. **Maps files to area tags** via classification rules
3. **Generates subject** from top 2-3 area tags
4. **Adds body** when ≥3 files or significant structural changes
5. **Preserves all safety checks:**
   - OS-level file lock on `.git/moxie_autopush.lock` (<=60s wait; implemented via Python `fcntl`, no external `flock` invocation)
   - No empty commits (exits 0 if no staged changes)
   - Rebase-on-reject for non-fast-forward
   - Error logging to `issues_rishi.md`

### Classification Rules

| Path Pattern | Area Tag |
|--------------|----------|
| `cmo/dispatch-queue.md` | dispatch |
| `cmo/orchestration.md` | orchestration |
| `cmo/delegation-queue.md` | delegation |
| `cmo/issues_rishi.md` | governance |
| `products/*/analytics/*` | analytics |
| `products/*/copy/*` | content |
| `products/*/outreach/*` | outreach |
| `products/*/seo/*` | SEO |
| `products/*/distribution/*` | distribution |
| `cmo/sops/*` | SOPs |
| `cmo/employees/*` | team |
| `dashboard/*` | dashboard |

### Example Commit Messages

**Before (old):**
```
Autopush: 2026-04-01T18:45:00Z
```

**After (new):**
```
HQ sync: dispatch + orchestration

- dispatch-queue.md: Kiro task promoted IN_PROGRESS
- orchestration.md: Forge/Ember states updated
```

---

## Rollback / Migration

- **Old commits remain:** History is preserved; only new commits use the format
- **No breaking changes:** This is purely a message format change
- **Fallback:** If classification fails, falls back to `HQ sync: multi-area update`

---

## Validation Checklist

- [x] Script updated with classification logic
- [x] flock locking preserved
- [x] No-empty-commits rule preserved
- [x] Error handling preserved (push failures → issues_rishi.md)
- [x] Rebase-on-reject logic preserved
- [x] Tested with actual staged changes

---

## Related Files

- Implementation: `/root/moxie_hq/cmo/scripts/hq_autopush_locked.py`
- Legacy shell script: `/root/moxie_hq/cmo/scripts/moxie_autopush.sh` (deprecated)
- Lock file: `/root/moxie_hq/.git/moxie_autopush.lock`
