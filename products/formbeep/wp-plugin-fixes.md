# FormBeep WordPress plugin resubmission — code audit + recommended fixes

**Scope:** WordPress.org review/resubmission support for the plugin located at:
- `/root/moxie/formbeep/integrations/wordpress/formbeep/`

**What I did:** Reviewed the plugin PHP + readme + admin JS/CSS and flagged the highest-likelihood WP.org review issues (security, privacy, remote calls, claims vs reality). This doc is written to help Rishi resubmit faster.

---

## Executive summary (P0 items)

### P0 — likely to trigger WP.org review rejection / rework
1) **Do not expose the API key to JavaScript**
   - Current: `wp_localize_script(... 'apiKey' => $api_key ...)` in `includes/class-admin.php`.
   - Even if admin-only, reviewers often treat API keys as secrets that should not be passed to JS or the DOM.
   - **Fix:** remove `apiKey` from localized data; use `isConfigured` boolean.

2) **Avoid putting the API key in a URL path for remote requests** (stats call)
   - Current: `GET https://api.formbeep.com/v1/user/stats/<API_KEY>`.
   - Problem: keys in URLs may leak via logs, proxies, caches, referrers, etc.
   - **Fix options:**
     - **Best:** change to `POST https://api.formbeep.com/v1/user/stats` with API key in an HTTP header (or request body) + update the FormBeep API to accept it.
     - **Fastest for submission:** remove the “Monthly Usage” stats feature from the plugin until after initial approval.

3) **Readme claims don’t match the code**
   - `readme.txt` claims:
     - “Optional custom success message support”
     - “Submission logs in your FormBeep dashboard” (product-level true, but plugin doesn’t implement logs; can be misread)
     - “Automatic script injection in page footer” (code currently loads in `<head>`)
   - WP reviewers regularly flag misleading readmes.
   - **Fix:** align readme.txt to what the plugin actually does: store API key + inject FormBeep embed script.

4) **External service disclosure should explicitly cover (a) form data transmission and (b) any admin stats calls**
   - You already have an “External Service” section in `readme.txt` (good). If you keep stats, disclose that opening settings triggers an API request to fetch usage.

---

## What looks good (keep as-is)
- Capability checks: settings page guarded with `manage_options`.
- Settings API used properly with sanitization + settings_errors.
- Output escaping: `esc_html`, `esc_attr`, `wp_kses_post` used appropriately.
- Uninstall cleanup present.
- Embed injection uses `wp_enqueue_script` and escapes the `data-api-key` attribute.

---

## Detailed findings + patches

### 1) Remove API key from localized JS (recommended regardless of stats feature)
**File:** `formbeep/includes/class-admin.php`

**Current (simplified):**
```php
wp_localize_script('formbeep-admin', 'formbeepAdmin', array(
  'ajaxUrl' => admin_url('admin-ajax.php'),
  'nonce'   => wp_create_nonce('formbeep_stats'),
  'apiKey'  => $api_key,
));
```

**Proposed:**
```php
wp_localize_script('formbeep-admin', 'formbeepAdmin', array(
  'ajaxUrl'       => admin_url('admin-ajax.php'),
  'nonce'         => wp_create_nonce('formbeep_stats'),
  'isConfigured'  => true,
  'dashboardUrl'  => 'https://app.formbeep.com',
));
```

**Then update** `assets/admin.js`:
- Replace `if (!formbeepAdmin.apiKey) return;` with `if (!formbeepAdmin.isConfigured) return;`

This change is low-risk and does not require any backend API changes.

---

### 2) Fix stats endpoint to avoid API key in URL (or remove stats entirely)
**File:** `formbeep/includes/class-admin.php` (`ajax_get_stats`)

**Current:**
```php
$response = wp_remote_get(
  'https://api.formbeep.com/v1/user/stats/' . rawurlencode($api_key),
  array('timeout' => 10)
);
```

**Recommended (requires API support):**
```php
$response = wp_remote_post(
  'https://api.formbeep.com/v1/user/stats',
  array(
    'timeout' => 10,
    'headers' => array(
      'X-FormBeep-Api-Key' => $api_key,
      'Accept'            => 'application/json',
    ),
  )
);
```

**If backend cannot be changed quickly:**
- **Remove the stats card + AJAX handler for initial resubmission.**
  - Delete the “Monthly Usage” block in `render_settings_page()`.
  - Remove `wp_ajax_formbeep_get_stats` hook.
  - Remove `admin.js` enqueue + file.

Reasoning: reviewers are most sensitive to admin “phone-home” behavior + API keys.

---

### 3) Align readme.txt with actual functionality
**File:** `formbeep/readme.txt`

Suggested edits:
- Remove claims about “optional custom success message” unless implemented.
- Ensure “automatic script injection” description matches reality:
  - Code currently enqueues script with `$in_footer = false` (loads in head).
- If stats is removed: remove any mention of usage display.
- Screenshots list currently mentions “optional custom success message”; update.

---

### 4) Add missing i18n loader
**File:** `formbeep/formbeep.php`

Even though strings use `__('…','formbeep')`, there is no `load_plugin_textdomain()` call.

Add inside `formbeep_init()` or a `plugins_loaded` hook:
```php
add_action('plugins_loaded', function () {
  load_plugin_textdomain('formbeep', false, dirname(plugin_basename(__FILE__)) . '/languages');
});
```

(This is a “reviewer-pleaser” even if you don’t ship translations yet.)

---

### 5) Fix inconsistent plan defaults
**File:** `includes/class-admin.php` (`ajax_get_stats` success mapping)

Current code defaults `messagesPerMonth` to `50` if absent. Readme says free plan is **15/mo**.

Change default to 15:
```php
'messagesPerMonth' => (int) ($body['messagesPerMonth'] ?? 15),
```

---

## Packaging / submission notes (to avoid avoidable review churn)
- Only zip and submit the **plugin folder**: `integrations/wordpress/formbeep/`.
- Do **not** include wrapper artifacts like `formbeep-instant-alerts.zip` (it’s outside the plugin folder already; just don’t zip the parent directory).

---

## Recommended resubmission sequence (fastest path)
1) Implement **P0.1 (no API key in JS)** + **P0.3 (readme accuracy)**.
2) Decide on stats feature:
   - **Fastest:** remove stats for now.
   - **Best long-term:** change stats endpoint to header-based auth (requires FormBeep API support).
3) Add `load_plugin_textdomain()` (small, safe).
4) Resubmit with a short reviewer note explaining:
   - external service + privacy links
   - no tracking
   - API key stored in options
   - script injection is core functionality

---

## Rishi action needed
- Confirm whether we should **remove stats for initial approval** (recommended) vs updating the FormBeep API to support header-based auth for stats.
- Apply the patch in the FormBeep repo + resubmit to WP.org.
