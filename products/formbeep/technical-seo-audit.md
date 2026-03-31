# FormBeep — Technical SEO Audit (Hugo)

Date: 2026-03-31

## Scope & how this audit was run
- Codebase: `/root/moxie/formbeep/landing` (Hugo site)
- Build used for inspection: `hugo v0.131.0+extended` → `/tmp/formbeep_site_build`
- Checked: indexability, canonicals, sitemap/robots, meta, structured data, internal-link hygiene, and performance (asset sizing + template review).

## Executive summary
**Overall:** solid foundation (canonicals + OpenGraph/Twitter + JSON-LD present). **Primary technical SEO risk is performance**: the built site is ~**37MB**, largely due to **multi‑MB PNGs** in blog posts, plus missing lazy-loading/size attributes in the blog image shortcode.

If you fix only 2 things this week:
1) **Image optimization pipeline** (WebP + resize + compression) for blog images.
2) **Noindex taxonomy pages + remove from sitemap** (or disable taxonomy generation) to avoid low-value index bloat.

---

## Findings (prioritized)

### P0 — Performance / Core Web Vitals risk (largest impact)

#### 1) Blog images are extremely large (multi‑MB PNGs)
Built output size: **37MB**, with several individual images in the **3–7MB** range.
Examples from build:
- `/blog/whatsapp-leads-private-number/whatsapp-form-notifcations.png` ~ **7.3MB**
- Several `*notification.png` images ~ **3.2MB** each

**Why this matters**
- Mobile LCP likely suffers (big hero/content images dominate LCP).
- Crawl efficiency suffers (Googlebot has bandwidth budgets; huge media increases fetch cost).

**Fix (recommended approach)**
- Convert blog images to **WebP** (or AVIF) and resize to a sane maximum width (typically 1200–1600px).
- Ensure `width`/`height` are present to reduce CLS.

**Implementation options**
- **Best**: Hugo image processing via Page Bundles (already used: each post is a bundle). Use `.Resources.GetMatch` + `.Resize`/`.Fit` to generate optimized derivatives.
- **Good**: batch-compress existing PNGs offline (e.g., `cwebp`, `oxipng`) and replace.

---

#### 2) Blog image shortcode does not lazy-load and has no explicit dimensions
File: `/root/moxie/formbeep/landing/layouts/shortcodes/img.html`
Current:
```html
<img src="{{ $src }}" alt="{{ $alt }}" style="width: 100%; height: auto; ...">
```
**Issue:** no `loading="lazy"`, no `decoding="async"`, no width/height.

**Fix (minimum)**
Add:
- `loading="lazy" decoding="async"`
- optional `width`/`height` parameters (or use Hugo resource metadata if processing)

Suggested patch sketch:
```html
<img
  src="{{ $src }}"
  alt="{{ $alt }}"
  loading="lazy"
  decoding="async"
  {{ with .Get "widthPx" }}width="{{ . }}"{{ end }}
  {{ with .Get "heightPx" }}height="{{ . }}"{{ end }}
  style="width: 100%; height: auto; border-radius: 8px; border: 1px solid var(--color-border);">
```

---

### P1 — Indexability / crawl hygiene

#### 3) Taxonomy pages are disallowed in robots.txt but still indexable and included in sitemap
Robots.txt disallows:
- `/categories/`
- `/tags/`

However:
- The built pages include `<meta name="robots" content="index, follow">` for taxonomy pages (because `noindex` isn’t set on those pages).
- The sitemap contains taxonomy URLs (at least `/tags/` was detected in the generated sitemap).

**Why this matters**
- `Disallow` does **not** guarantee deindexing. If other sites link to these pages, Google can still index the URL (often without content), creating low-quality index entries.

**Fix**
- Option A (recommended): **Disable taxonomy generation** in `hugo.toml` if you don’t want them at all.
- Option B: Mark taxonomy/term pages as `noindex` automatically + remove them from sitemap.

**Implementation sketch (meta robots)**
In `layouts/partials/head.html`, change robots logic from only `.Params.noindex` to also cover taxonomies:
```go
{{ $noindex := or .Params.noindex (in (slice "taxonomy" "term") .Kind) }}
<meta name="robots" content="{{ if $noindex }}noindex, nofollow{{ else }}index, follow{{ end }}">
```

---

### P1 — Meta hygiene / correctness

#### 4) `meta name="keywords"` prints YAML arrays as `[...]`
Observed in built output (e.g., integrations pages):
- `content="[framer whatsapp notification,framer form whatsapp,...]"`

Cause:
- `layouts/partials/head.html` prints `.Params.keywords` directly (when it’s a list).

Fix:
```go
<meta name="keywords" content="{{ if .Params.keywords }}{{ delimit .Params.keywords ", " }}{{ else }}...{{ end }}">
```

Note: Google ignores meta keywords, but it’s still worth cleaning up (and other crawlers/tools may flag it).

---

### P2 — Content/HTML quality issues that can become SEO drags

#### 5) One blog image has meaningless alt text
Detected in build:
- `alt="alt text"` on an inline image in `/blog/why-you-are-missing-leads/`

Fix: update the markdown to provide descriptive alt text (or use the `img` shortcode with `alt=`).

#### 6) Homepage H1 is present but `sr-only`
Homepage includes an H1 but it is visually hidden:
- `<h1 class=sr-only>Contact Form to WhatsApp™ Notifications</h1>`

This is not “wrong”, but it’s often better for both users and SEO clarity if the visible hero headline is an `<h1>`.

---

## What’s already good (keep)
- Canonical URLs are present.
- Open Graph + Twitter meta present.
- JSON-LD exists in head (Organization, WebSite, SoftwareApplication, Product; plus FAQ on home).
- Robots.txt includes sitemap and blocks taxonomy paths.
- CSS/JS footprint is small (CSS ~52KB, JS ~2KB); performance issues are primarily images.

---

## Recommended 7-day action list (engineering)
1) **Implement Hugo image processing for blog images** (WebP + resize + quality). Target: largest images < 250KB.
2) Update `layouts/shortcodes/img.html` to add `loading/decoding` + dimensions.
3) Update `layouts/partials/head.html`:
   - `keywords` delimit fix
   - auto-`noindex` for taxonomy/term
4) Remove taxonomy URLs from sitemap (or disable taxonomy output).
5) Quick content pass: fix `alt="alt text"`, ensure each post’s `image:` is set + optimized.

---

## Notes / reproducibility
To reproduce the build inspection locally:
```bash
apt-get update -qq && apt-get install -y -qq hugo
cd /root/moxie/formbeep/landing
hugo --minify --destination /tmp/formbeep_site_build
```
