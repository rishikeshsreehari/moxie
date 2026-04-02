# FormBeep — Marketplace Requirements Matrix (must-verify)

Status: **COMPLETED** — Full analysis at [/root/moxie_hq/products/formbeep/dev-notes/marketplace-integration-scope.md](./marketplace-integration-scope.md)

## Goal
Determine, per platform, whether we can: (A) submit today as a listing, (B) submit after creating a dev account, or (C) must build an integration/app/plugin first.

## Matrix (Summary)

| Platform | Channel type | What qualifies | Required build artifact | Auth requirement | Submission gate(s) | MVP for FormBeep | Effort | Can submit today? |
|---|---|---|---|---|---|---|---|---|
| Webflow Apps | App Marketplace | Must be Data Client, Designer Extension, or Hybrid App | Full Webflow App with OAuth | OAuth 2.0 | 2FA required; review process | Data Client for form webhooks | **M** | **NO** |
| Framer Marketplace | Plugin Marketplace | Must be Plugin (not component) | Framer Plugin (JS/TS) | OAuth or API key | Review process | Editor panel for FormBeep config | **M** | **NO** |
| Glide Apps | Integration via Call API | Uses existing "Call API" integration | None — use existing | API key | Contact Glide team | Document Call API workflow | **S** | **PARTIAL** |
| Typedream | Embed/Custom Code | No formal marketplace | None — use embed | None | None identified | Document embed approach | **S** | **NO** |

## Key Findings

| Platform | Recommendation |
|----------|----------------|
| Webflow | **DEFER** — Requires 2-3 weeks of app development. Revisit at 50+ paying users. |
| Framer | **DEFER** — Requires 2-3 weeks of plugin development. Prior rejection confirmed plugin requirement. |
| Glide | **BUILD NOW** — 2-3 days to document Call API integration. Strong ICP fit. |
| Typedream | **BUILD NOW** — 1-2 days to investigate + document. Low effort, SEO opportunity. |

## Notes
- Founder has prior experience: Framer rejected a component submission; required a plugin. Treat this as a red flag that "submission" is not merely copy.
- **Critical finding:** None of the platforms accept metadata-only "directory" submissions. All require actual development OR use of existing generic integrations.
- Use SOP: /root/moxie_hq/cmo/sops/marketplace-channel-verification.md
- Full feasibility memo with citations: [marketplace-integration-scope.md](./marketplace-integration-scope.md)
