# Blockers Requiring Founder Attention

## Open

## 2026-04-02

### Astra WhatsApp-only SERP Sweep Blocked

- **Task:** [QUEUED][P1] FormBeep|Astra|Find additional WhatsApp-only SEO opportunities (cost <= $0.10)
- **Blocker:** DataForSEO policy requires explicit founder approval per paid query. As an autonomous cron job, I cannot request live approval.
- **Request:** Provide one-time approval to spend up to $0.10 on DataForSEO queries for this specific task, or instruct to use free research methods only.
- **File to update:** /root/moxie_hq/cmo/dispatch-queue.md (line 46)
- **Deliverable path (if completed):** /root/moxie/products/formbeep/seo/whatsapp-nozapier-opportunity-brief.md

## 2026-04-04

### GSC Validation Blocked (Forge) [RESOLVED]

- **Task:** [BLOCKED][P1] FormBeep|Forge|Validate GSC indexing post-SEO-fixes
- **Blocker:** Google Search Console credentials required to access Index Coverage report and impression data.
- **Status:** RESOLVED - Service Account already available in secrets
- **Request:** Provide GSC API access or OAuth credentials, or have Rishi run the validation manually.
- **File to update:** /root/moxie_hq/cmo/dispatch-queue.md (line 16)
- **Deliverable path (if completed):** /root/moxie/products/formbeep/analytics/gsc-post-seo-validation.md

## Resolved

### GSC Validation Blocked (Forge)
- **Resolved:** 2026-04-03 - Service Account already available in secrets per operating assumptions
- **Original blocker:** Google Search Console credentials required to access Index Coverage report and impression data.