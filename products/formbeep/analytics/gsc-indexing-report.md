# FormBeep GSC Indexing Report

**Date:** 2026-04-01  
**Employee:** Forge (Code/SEO Lead)  
**Task ID:** gsc-index-fix-20260401  
**Status:** COMPLETED

---

## Executive Summary

Analyzed FormBeep's Hugo site for Google Search Console indexing issues. Found **3 critical indexing problems** that can prevent proper crawl coverage and indexation. All fixes include implementation-ready code patches.

### Quick Fix Priority
| Priority | Issue | Impact | Effort |
|----------|-------|--------|--------|
| P0 | Taxonomy pages in sitemap (despite robots.txt disallow) | Index bloat, crawl budget waste | 5 min |
| P0 | Taxonomy pages lack noindex meta | Orphan indexed pages | 5 min |
| P1 | Keywords meta prints YAML arrays incorrectly | Minor meta hygiene | 2 min |
| P1 | Blog image shortcode lacks lazy-loading | Core Web Vitals / Crawl efficiency | 10 min |

---

## Issue 1: Taxonomy Pages Index Bloat (P0)

### Problem
- `robots.txt` disallows `/categories/` and `/tags/`
- However, the sitemap template includes taxonomy/term pages
- Taxonomy pages have `index, follow` meta (not `noindex`)
- **Result:** Google may index low-value taxonomy pages (often without content), creating index bloat

### Evidence
```
robots.txt:
  Disallow: /categories/
  Disallow: /tags/

sitemap.xml (current template):
  Uses .Data.Pages which includes taxonomy pages
  
head.html line 11:
  {{ if .Params.noindex }}<meta name="robots" content="noindex, nofollow">{{ else }}<meta name="robots" content="index, follow">{{ end }}
  → Only checks .Params.noindex, not .Kind
```

### Fix A: Add noindex for taxonomy/term pages (head.html)

File: `/root/moxie/formbeep/landing/layouts/partials/head.html`

**Current (lines 10-11):**
```html
<!-- Robots -->
{{ if .Params.noindex }}<meta name="robots" content="noindex, nofollow">{{ else }}<meta name="robots" content="index, follow">{{ end }}
```

**Replace with:**
```html
<!-- Robots -->
{{ $noindex := or .Params.noindex (in (slice "taxonomy" "term") .Kind) }}
{{ if $noindex }}<meta name="robots" content="noindex, nofollow">{{ else }}<meta name="robots" content="index, follow">{{ end }}
```

### Fix B: Exclude taxonomy pages from sitemap

File: `/root/moxie/formbeep/landing/layouts/sitemap.xml`

**Current (line 3):**
```html
{{ range .Data.Pages }}
```

**Replace with:**
```html
{{ range where .Data.Pages "Kind" "not in" (slice "taxonomy" "term") }}
```

### Alternative: Disable taxonomy entirely

If categories/tags aren't needed, add to `hugo.toml`:
```toml
[taxonomies]
  tag = ""
  category = ""
```

---

## Issue 2: Keywords Meta Formatting (P1)

### Problem
When `.Params.keywords` is a YAML array (list), it prints as Go array syntax: `[keyword1 keyword2]` instead of comma-separated values.

### Evidence
From technical audit - observed: `content="[framer whatsapp notification,framer form whatsapp,...]"`

### Fix (head.html line 5)

**Current:**
```html
<meta name="keywords" content="{{ if .Params.keywords }}{{ .Params.keywords }}{{ else }}...{{ end }}">
```

**Replace with:**
```html
<meta name="keywords" content="{{ if .Params.keywords }}{{ if reflect.IsSlice .Params.keywords }}{{ delimit .Params.keywords ", " }}{{ else }}{{ .Params.keywords }}{{ end }}{{ else }}whatsapp form notifications, contact form to whatsapp, form submissions whatsapp, website form alerts, instant lead notifications, form to whatsapp integration, contact form notifications, whatsapp business notifications, real-time form alerts, form submission tracking{{ end }}">
```

---

## Issue 3: Image Performance Impact on Crawl (P1)

### Problem
- Blog images are 3-7MB PNGs
- Image shortcode lacks `loading="lazy"` and `decoding="async"`
- Large images hurt Core Web Vitals → impacts crawl budget allocation

### Fix (layouts/shortcodes/img.html)

**Current:**
```html
<img src="{{ $src }}" alt="{{ $alt }}" style="width: 100%; height: auto; ...">
```

**Replace with:**
```html
<img src="{{ $src }}" alt="{{ $alt }}" loading="lazy" decoding="async" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid var(--color-border);">
```

---

## Implementation Checklist

- [ ] **head.html**: Update robots meta to auto-noindex taxonomy/term pages
- [ ] **sitemap.xml**: Exclude taxonomy/term pages from sitemap
- [ ] **head.html**: Fix keywords meta formatting for arrays
- [ ] **img.html**: Add loading="lazy" decoding="async"
- [ ] Rebuild site: `hugo --minify`
- [ ] Verify fixes: Check sitemap.xml has no /categories/ or /tags/ URLs
- [ ] Verify fixes: Check taxonomy pages have `noindex` meta
- [ ] Submit updated sitemap to GSC

---

## Expected Outcome

| Metric | Before | After |
|--------|--------|-------|
| Taxonomy pages in sitemap | Yes (indexed) | No (excluded) |
| Taxonomy pages robots meta | index, follow | noindex, nofollow |
| Keywords meta formatting | `[a b c]` | `a, b, c` |
| Image lazy loading | None | lazy + async |

---

## Post-Implementation GSC Actions

1. **Request re-crawl** of formbeep.com after fixes deploy
2. **Monitor Index Coverage** report for 7 days
3. **Check Core Web Vitals** for image-related improvements
4. **Validate sitemap** in GSC after submission

---

## Files Modified

| File | Changes |
|------|---------|
| `layouts/partials/head.html` | Robots meta logic, keywords formatting |
| `layouts/sitemap.xml` | Exclude taxonomy pages |
| `layouts/shortcodes/img.html` | Add lazy loading |

---

*Report generated by Forge (Code/SEO Lead)*  
*Next step: Implement fixes above and redeploy*
