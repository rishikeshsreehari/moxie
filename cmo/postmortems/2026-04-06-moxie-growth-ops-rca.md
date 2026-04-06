# RCA — Growth Ops Confusion + Wrong Plugin URL in Directory Packet

Date (UTC): 2026-04-06
Owner: Moxie (CMO agent)
Severity: High (brand / directory submissions could have been poisoned)
Status: Mitigated (packet + source pack patched)

## Incident summary
Two user-facing failures happened:
1) **Wrong WordPress plugin URL** was included in the FormBeep directory submission packet (it pointed to a competitor / unrelated plugin). This could have caused incorrect public listings.
2) **[SILENT] token misuse** in interactive founder chat created confusion and made it look like nothing was happening.

## Impact
- Risk of publishing incorrect information on third-party directories.
- Erosion of trust in the growth system (founder perceived work as deleted / missing).
- Wasted founder time due to unclear “what to do now” instructions.

## What actually caused it (5-Whys)

### A) Why did a competitor plugin URL appear in the directory packet?
1. The packet was generated from an existing “directory submissions pack” that contained a `WordPress plugin` field with a URL.
2. That pack’s `WordPress plugin` field was **stale/incorrect** relative to current reality (“our plugin is in review; do not share URL”).
3. There was **no preflight validation** step that checks directory packets for banned competitor strings/domains (e.g., `beepmate`), nor a rule that blocks including plugin URLs unless verified as shipped.
4. There was **no single truth-layer source-of-truth** enforcing which claims/links are allowed for each product.
5. Result: the packet faithfully copied a wrong field instead of stopping and asking you.

Root cause: **Truth-layer drift + lack of automated validation gate** for directory submission packets.

### B) Why did [SILENT] show up during interactive chat?
1. We have a strict protocol: `[SILENT]` is for scheduled/status runs when there are no findings.
2. I incorrectly applied that protocol to interactive founder questions ("what needs attention?", "what should I do?").
3. The system didn’t clearly separate “status-run output” vs “interactive chat output” in my behavior.

Root cause: **Context-mixing bug in operating behavior** (status-run protocol bleeding into interactive mode).

### C) Why did it look like content strategy was “deleted”?
1. Older “what needs your attention” items were moved from the active file into an archive to keep the active list executable.
2. I did not lead with a persistent index linking: active list → archive → current deliverables.
3. So you experienced it as “stuff is gone.”

Root cause: **Poor surfacing / navigation**, not deletion.

## Detection
- Founder manually noticed the BeepMate URL and flagged it.
- Founder expressed confusion about which directories to submit and why items appeared gone.

## Mitigation (already done)
1) Patched the FormBeep directory execution packet to be truth-layer safe:
- File: `/root/moxie_hq/cmo/deliverables/formbeep_directory_execution_today.md`
- Changes:
  - Removed BeepMate plugin URL
  - Changed copy to WhatsApp-only (removed SMS/email claims)
  - Plugin line now: “Pending WP.org review (do NOT include a plugin URL…)”

2) Patched the upstream source pack so the error doesn’t recur:
- File: `/root/moxie_hq/products/formbeep/directory-submissions-p1.md`
- Removed the incorrect plugin URL; marked as “Pending WP.org review”.

## Prevent recurrence (system fixes)
1) Add a **Truth-Layer Allowlist** per product (single place):
- Create: `/root/moxie_hq/cmo/truth/product-truth-layer.md`
- Must include:
  - Shipped features (allowed claims)
  - Not-shipped features (banned claims)
  - Allowed URLs (site, docs, pricing)
  - Banned competitor strings/domains

2) Add a **Directory Packet Preflight Check** (hard fail):
- Before writing any directory packet, run:
  - Check for banned competitor tokens (e.g., `beepmate`, `web2phone`, etc.)
  - Check for “not shipped” claims (SMS/email) unless explicitly marked “coming soon”.

3) Enforce `[SILENT]` boundary:
- `[SILENT]` only emitted by scheduled jobs.
- Interactive chat must always respond with content if asked a question.

4) Permanent navigation:
- Maintain `/root/moxie_hq/cmo/reports/visibility_master_index.md` as a stable “where everything is” map.

## Founder actions (optional)
- None required to mitigate.
- If you already submitted any directory using the old packet, we should edit those listings; otherwise ignore.

## Verification commands (Docker)
View corrected directory packet:
- `docker exec -it hermes-moxie bash -lc 'cat /root/moxie_hq/cmo/deliverables/formbeep_directory_execution_today.md'`

View this RCA:
- `docker exec -it hermes-moxie bash -lc 'cat /root/moxie_hq/cmo/postmortems/2026-04-06-moxie-growth-ops-rca.md'`
