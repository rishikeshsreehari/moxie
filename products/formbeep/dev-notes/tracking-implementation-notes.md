# FormBeep Umami Event Tracking Implementation Notes

**Task ID:** forge-20260402_001211-30bb2a  
**Generated:** 2026-04-02T03:37:00Z  
**Status:** COMPLETED

---

## Executive Summary

FormBeep landing page already has basic Umami pageview tracking and some click events. This document identifies all CTAs, proposes enhanced event tracking for funnel diagnostics, and establishes UTM hygiene standards.

---

## Current State Analysis

### Umami Configuration (✅ Already Implemented)
```html
<!-- In: landing/layouts/partials/head.html (Line 92) -->
<script defer src="https://cloud.umami.is/script.js" 
        data-website-id="750e37be-3e04-4672-abe8-a2983afb9a4d"></script>
```

### Existing Click Events (✅ Already Implemented)

| Location | File | Element | Event Name |
|----------|------|---------|------------|
| Header | `partials/header.html:13` | "Get Started Free" button | `Signup - Header` |
| Header | `partials/header.html:12` | "Login" button | `Login Click` |
| Header | `partials/header.html:7` | "Docs" link | `Docs Click` |
| Hero | `partials/hero.html:30` | "Get FREE Alerts" CTA | `Signup - Hero` |
| Pricing | `partials/pricing.html:72` | "Get FREE Alerts" CTA | `Signup - Pricing` |
| Final CTA | `layouts/index.html:23` | "Get Started Free" button | `Signup - Final CTA` |

---

## CTA Inventory & Funnel Mapping

### Primary Conversion CTAs (Signup Flow)
```
┌─────────────────────────────────────────────────────────────────┐
│  HEADER: "Get Started Free"  →  https://accounts.formbeep.com/  │
│  HERO:   "Get FREE Alerts"   →  https://accounts.formbeep.com/  │
│  PRICING: "Get FREE Alerts"  →  https://accounts.formbeep.com/  │
│  FINAL:  "Get Started Free"  →  https://accounts.formbeep.com/  │
└─────────────────────────────────────────────────────────────────┘
```

### Secondary CTAs
| CTA | Destination | Current Tracking | Recommendation |
|-----|-------------|------------------|----------------|
| Login | `https://app.formbeep.com/sign-in` | `Login Click` | ✅ Keep |
| Docs | `https://docs.formbeep.com` | `Docs Click` | ✅ Keep |
| Footer: Integrations | `/integrations` | ❌ None | Add tracking |
| Footer: Blog | `/blog` | ❌ None | Add tracking |
| Footer: GitHub Roadmap | External | ❌ None | Add tracking |

---

## Recommended Event Tracking Additions

### 1. Navigation/Engagement Events
```html
<!-- Footer navigation (add to footer.html) -->
<a href="/integrations" data-umami-event="Footer - Integrations">Integrations</a>
<a href="/blog" data-umami-event="Footer - Blog">Blog</a>
<a href="https://github.com/users/rishikeshsreehari/projects/3" 
   data-umami-event="Footer - Roadmap" target="_blank">Roadmap</a>
<a href="/tools" data-umami-event="Footer - Tools">Free Tools</a>
```

### 2. Demo Interaction Events
```html
<!-- Hero WhatsApp demo (add to hero.html:123) -->
<script>
  viewBtn.addEventListener('click', function() {
    // Add this line:
    if (window.umami) window.umami.track('Demo - View Details Click');
    // ... existing code
  });
</script>
```

### 3. Pricing Plan Interest
```html
<!-- Add hover/interest tracking on pricing cards (pricing.html) -->
<div class="pricing-card" 
     data-umami-event="Pricing - View Plan Free"
     data-umami-event-plan="free">
```

---

## UTM Hygiene Standards

### Standard UTM Parameters

All external campaigns should use this structure:

```
https://accounts.formbeep.com/sign-up
  ?utm_source={source}
  &utm_medium={medium}
  &utm_campaign={campaign}
  &utm_content={content_id}
```

### UTM Value Matrix

| Source | Medium | Use Case |
|--------|--------|----------|
| `google` | `cpc` | Google Search Ads |
| `reddit` | `social` | Reddit community posts |
| `twitter` | `social` | X/Twitter posts |
| `indiehackers` | `social` | IndieHackers posts |
| `blog` | `referral` | Blog content links |
| `docs` | `referral` | Documentation links |
| `producthunt` | `referral` | Product Hunt launch |
| `directory` | `referral` | SaaS directory listings |

### Campaign Naming Convention
```
{product}_{channel}_{objective}_{yyyymm}

Examples:
- formbeep_google_signups_202604
- formbeep_reddit_gstlaunch_202604
- formbeep_blog_organic_202604
```

### Content Identifier Convention
```
{location}_{element}_{variant}

Examples:
- header_button_blue
- hero_cta_white
- pricing_bottom_featured
- finalcta_simple
```

---

## Implementation Code Blocks

### Option A: Basic UTM Append (JS)
```javascript
// Add to script.js - automatically append UTMs to signup links
(function() {
  const params = new URLSearchParams(window.location.search);
  const utmParams = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
  
  document.querySelectorAll('a[href*="accounts.formbeep.com"]').forEach(link => {
    const url = new URL(link.href);
    utmParams.forEach(param => {
      if (params.has(param) && !url.searchParams.has(param)) {
        url.searchParams.set(param, params.get(param));
      }
    });
    link.href = url.toString();
  });
})();
```

### Option B: Enhanced Click Tracking with Context
```javascript
// Track clicks with page context
function trackCTAClick(eventName, element) {
  if (window.umami) {
    window.umami.track(eventName, {
      page_path: window.location.pathname,
      referrer: document.referrer || 'direct',
      viewport: `${window.innerWidth}x${window.innerHeight}`
    });
  }
}

// Usage in HTML:
// <a href="..." onclick="trackCTAClick('Signup - Hero', this)">
```

### Option C: Data-Attribute Auto-Tracking
```javascript
// Auto-track all elements with data-track attribute
(function() {
  document.addEventListener('click', function(e) {
    const trackEl = e.target.closest('[data-track]');
    if (trackEl && window.umami) {
      window.umami.track(trackEl.dataset.track, {
        href: trackEl.href,
        text: trackEl.textContent.trim().slice(0, 50)
      });
    }
  });
})();
```

---

## Funnel Conversion Measurement

### Event Flow Map
```
Page View
    ↓
[Scroll Depth: 25%] → umami.track('Scroll - 25%')
    ↓
[Scroll Depth: 50%] → umami.track('Scroll - 50%')
    ↓
[Hero CTA Click] → Signup - Hero
    ↓
[Pricing View] → umami.track('View - Pricing Section')
    ↓
[Pricing CTA Click] → Signup - Pricing
    ↓
[Final CTA Click] → Signup - Final CTA
    ↓
External: accounts.formbeep.com/sign-up
```

### Key Conversion Metrics to Monitor

| Metric | Calculation | Target |
|--------|-------------|--------|
| Hero CTR | Hero clicks / Page views | >5% |
| Pricing CTR | Pricing clicks / Page views | >3% |
| Scroll-to-CTA | CTA clicks / 50% scrolls | >10% |
| Header vs Hero split | Header:Hero ratio | 1:3 |

---

## File Locations Summary

| File | Path | Purpose |
|------|------|---------|
| Umami Script | `landing/layouts/partials/head.html:92` | Global tracking |
| Header CTAs | `landing/layouts/partials/header.html:12-13` | Nav actions |
| Hero CTA | `landing/layouts/partials/hero.html:30` | Primary conversion |
| Pricing CTA | `landing/layouts/partials/pricing.html:72` | Plan conversion |
| Final CTA | `landing/layouts/index.html:23` | Bottom conversion |
| Config | `landing/hugo.toml:7` | Signup URL source |

---

## Quick Reference: Event Naming Convention

```
{Action} - {Location} - {Element}

Actions: Signup, Login, Click, View, Scroll, Demo
Location: Header, Hero, Pricing, Footer, Nav
Element: Button, Link, CTA, Card, Section

Examples:
✅ Signup - Hero
✅ Login - Header
✅ View - Pricing Section
✅ Click - Footer Roadmap
✅ Demo - View Details

❌ CTA Clicked
❌ Button 1
❌ User did something
```

---

## Next Steps (Priority Order)

1. **P1**: Implement UTM parameter preservation (Option A) - 15 min
2. **P1**: Add footer link tracking for key conversion paths - 10 min
3. **P2**: Add demo interaction tracking (WhatsApp mockup clicks) - 20 min
4. **P2**: Implement scroll depth tracking for engagement metrics - 30 min
5. **P3**: Set up Umami Goals for each Signup event variant
6. **P3**: Create dashboard in Umami for funnel visualization

---

## Verification Checklist

- [ ] All signup links have `data-umami-event` attributes
- [ ] UTM parameters persist from landing page to accounts.formbeep.com
- [ ] Events appear in Umami dashboard within 5 minutes of testing
- [ ] Event names follow `{Action} - {Location}` convention
- [ ] No PII (email, phone) is passed to tracking events
- [ ] External links (GitHub, Twitter) open in new tab with security attrs

---

**Document Status:** Ready for implementation review  
**No code changes pushed to product repo per task scope**
