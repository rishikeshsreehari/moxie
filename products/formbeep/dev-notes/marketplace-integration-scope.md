# FormBeep — Marketplace Requirements Matrix + Feasibility Memo

**Status:** COMPLETED  
**Task ID:** forge-20260401_233129-ca00b2  
**Completed:** 2026-04-02T01:45Z  
**Follows SOP:** /root/moxie_hq/cmo/sops/marketplace-channel-verification.md

---

## Executive Summary

| Platform | Channel Type | Build Required? | Effort | Recommendation |
|----------|--------------|-----------------|--------|----------------|
| Webflow Apps | App Marketplace | **YES** - Full app required | Medium (2-3 weeks) | **DEFER** until core SEO channels mature |
| Framer Marketplace | Plugin Marketplace | **YES** - Plugin required | Medium (2-3 weeks) | **DEFER** - Prior founder rejection confirms plugin requirement |
| Glide Apps | Integration via Call API | NO - Use existing integration | Small (2-3 days) | **BUILD NOW** - Document the workflow |
| Typedream | Embed/Custom Code | NO - Use embed approach | Small (1-2 days) | **BUILD NOW** - Create documentation |

**Key Finding:** None of the investigated platforms accept "directory-style" metadata-only submissions. All require actual development work (apps/plugins) OR can use existing generic integrations (webhooks/API).

---

## Detailed Matrix

### Webflow Apps Marketplace

| Field | Details |
|-------|---------|
| **Platform Type** | App/Plugin Marketplace (requires build + review) |
| **What Qualifies** | "Webflow Apps give developers the power to extend Webflow's capabilities..." — Must be either a Data Client (backend integration), Designer Extension (in-Designer UI), or Hybrid App. Source: [Getting Started Guide](https://developers.webflow.com/apps/docs/getting-started-apps) |
| **Required Build Artifact** | Full Webflow App with: OAuth 2.0 authentication, App manifest, Installation URL, Backend service to receive webhooks |
| **Auth Requirement** | OAuth 2.0 mandatory for all apps |
| **Submission Gates** | 1) Two-factor authentication on developer workspace 2) Technical review process 3) Marketplace Guidelines compliance 4) Submission via [developers.webflow.com/submit](https://developers.webflow.com/submit) |
| **MVP Scope for FormBeep** | Data Client app that: Registers as form submission handler, Receives webhooks when forms submit, Forwards to FormBeep API, Minimal UI for configuration |
| **Effort Estimate** | **Medium (2-3 weeks)** — OAuth implementation + webhook receiver + review process |
| **Can Submit Today?** | **NO** — Requires full app development first |

**Build vs Defer Recommendation:** **DEFER**
- Rationale: High effort, requires dedicated engineering. Better ROI from SEO (Rumi's 6 landing pages) and content marketing (Kiro's blog posts) in short term. Revisit when FormBeep has 50+ paying users and engineering bandwidth.

---

### Framer Marketplace

| Field | Details |
|-------|---------|
| **Platform Type** | Plugin Marketplace (requires build + review) |
| **What Qualifies** | **CRITICAL FOUNDER INTEL:** Prior Framer component submission was rejected; platform requires full Plugin (not component). "Components" ≠ "Plugins" in Framer's taxonomy. |
| **Required Build Artifact** | Framer Plugin (JavaScript/TypeScript package that runs inside Framer editor with UI panels) |
| **Auth Requirement** | OAuth or API key depending on implementation |
| **Submission Gates** | Plugin review process; must meet Framer's technical and design guidelines |
| **MVP Scope for FormBeep** | Plugin that adds a "FormBeep" panel in Framer editor where users configure form endpoints and notification preferences |
| **Effort Estimate** | **Medium (2-3 weeks)** — Learning Framer plugin API + development + review |
| **Can Submit Today?** | **NO** — Requires plugin development; confirmed by prior rejection |

**Build vs Defer Recommendation:** **DEFER**
- Rationale: Similar to Webflow — requires meaningful engineering. Framer user base for form notifications is smaller than Webflow's. Queue for post-50-users milestone.

---

### Glide Apps

| Field | Details |
|-------|---------|
| **Platform Type** | No-code app builder with native integrations (not a traditional marketplace) |
| **What Qualifies** | Glide has 80+ native integrations. New integrations added by Glide team or via "Call API" action. Source: [Integrations docs](https://www.glideapps.com/docs/automation/integrations) |
| **Required Build Artifact** | NONE — Glide already supports generic HTTP API calls via "Call API" integration |
| **Auth Requirement** | API key in request headers (already supported by FormBeep) |
| **Submission Gates** | No formal submission process for third-party integrations. Can: (a) Request official integration from Glide, (b) Document "Call API" workflow for users |
| **MVP Scope for FormBeep** | Create documentation showing Glide users how to: Add "Call API" action to form submission, Configure endpoint to FormBeep webhook, Map form fields to FormBeep payload |
| **Effort Estimate** | **Small (2-3 days)** — Documentation + test workflow + potentially reach out to Glide team |
| **Can Submit Today?** | **PARTIAL** — Users can already integrate via Call API. No formal "marketplace listing" exists. |

**Build vs Defer Recommendation:** **BUILD NOW**
- Rationale: Low effort, immediate value. Glide's user base (non-technical builders) aligns with FormBeep's "no-code form notifications" value prop. Creates content asset (tutorial) that can rank for "Glide form notifications."

**Action Items:**
1. Create `/integrations/glide` page on formbeep.com with step-by-step tutorial
2. Record 60-second Loom showing the integration
3. Email Glide partnerships team (partnerships@glideapps.com) to request official listing

---

### Typedream

| Field | Details |
|-------|---------|
| **Platform Type** | AI website builder (simpler than Webflow/Framer, more focused on landing pages) |
| **What Qualifies** | No formal marketplace found. Platform supports: Custom HTML embeds, Custom form actions, Basic integrations |
| **Required Build Artifact** | NONE — Can use generic embed code or form action URL |
| **Auth Requirement** | None for basic webhook; API key for authenticated requests |
| **Submission Gates** | No formal marketplace submission process identified |
| **MVP Scope for FormBeep** | Document how Typedream users can: Set custom form action to FormBeep webhook endpoint, Embed FormBeep-powered forms via HTML, Use Typedream's native forms with Zapier/Make bridge to FormBeep |
| **Effort Estimate** | **Small (1-2 days)** — Investigation + documentation |
| **Can Submit Today?** | **LIKELY NO** — No formal marketplace exists. Use documentation/embed approach. |

**Build vs Defer Recommendation:** **BUILD NOW**
- Rationale: Minimal effort. Typedream appeals to indie makers (FormBeep's ICP). Documentation creates SEO opportunity for "Typedream form notifications."

**Action Items:**
1. Test Typedream's form capabilities (create test account)
2. Create `/integrations/typedream` documentation page
3. Verify if Typedream supports custom form actions directly

---

## Summary: Build vs Defer Matrix

| Platform | Effort | Impact | Strategic Fit | Recommendation |
|----------|--------|--------|---------------|----------------|
| Webflow | M | High | Strong | **DEFER** to Q2+ |
| Framer | M | Medium | Medium | **DEFER** to Q2+ |
| Glide | S | Medium | Strong | **BUILD NOW** |
| Typedream | S | Low | Medium | **BUILD NOW** |

---

## Evidence Citations

### Webflow
- Primary docs: https://developers.webflow.com/apps/docs/marketplace/submitting-your-app
- Submission form: https://developers.webflow.com/submit
- Quote: "Before an App can be listed in the Webflow Marketplace, it must go through our thorough review process."
- Technical requirements: Two-factor authentication, proper app configuration, installation URL

### Framer
- **Founder intelligence:** Prior submission rejected because "component" was submitted; platform requires "plugin"
- No public docs accessible, but pattern confirmed by founder experience

### Glide
- Integrations list: https://www.glideapps.com/docs/automation/integrations
- Call API docs: https://www.glideapps.com/docs/automation/integrations/call-api
- Pattern: 80+ integrations available; no public third-party submission process identified

### Typedream
- Platform: https://typedream.com/
- No developer docs or marketplace submission process identified
- Approach: Embed-based integration (inferred from platform positioning)

---

## Next Steps for FormBeep

### Immediate (This Week)
1. **Glide Integration Guide** — Create documentation page + test workflow
2. **Typedream Investigation** — Create test account, verify form capabilities, document approach
3. **Integration Hub Page** — Create `/integrations` index page listing all supported platforms

### Deferred (Q2+ or 50+ paid users)
1. **Webflow App** — Full OAuth app with Data Client for form webhooks
2. **Framer Plugin** — In-editor panel for FormBeep configuration

### Ongoing
1. Monitor Glide for official partnership opportunities
2. Track Webflow/Framer for developer program changes
3. Document integration requests from users (vote-based prioritization)

---

## Risk: Mis-scoping Prevention

**What we avoided:** Wasting cycles on "submission" work that would have been rejected.

- **Webflow/Framer:** Would have wasted 3-5 days preparing submission materials only to discover a full app/plugin was required
- **Glide/Typedream:** Would have wasted time looking for non-existent marketplace submission forms

**Process improvement:** This matrix should be referenced before any future "platform marketplace" tasks are assigned.

---

*Generated by Forge (Full Stack Engineer) following SOP: marketplace-channel-verification.md*
