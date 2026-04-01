# SapiensTech HQ Dashboard (public-safe)

This is a static dashboard intended to be deployed publicly.

Design goals
- Retro UI using 7.css
- Monochrome / white background
- Mobile responsive
- Shows only sanitized, aggregated signals (no PII)

How it works
- `index.html` loads `public_snapshot.json` via `fetch()`.
- If the snapshot is missing, it falls back to a hardcoded sample.

What to update
- Update `public_snapshot.json` in your deploy pipeline (Cloudflare Pages / GitHub Actions) with sanitized data.

Sanitization rules (do not violate)
Never publish:
- Emails
- Phone numbers
- API keys / tokens
- Chat IDs
- Full URLs with query strings
- Referrer domains if they can identify individuals
- Raw logs

OK to publish:
- Weekly totals (pageviews, visitors, signups)
- Counts of blockers
- Role-only statuses (IDLE/IN_PROGRESS/BLOCKED)
- Counts of active jobs

Local preview
- Open `index.html` directly, or serve the folder:
  - `python3 -m http.server 8000 --directory dashboard`

Notes
- 7.css is loaded from unpkg: https://unpkg.com/7.css/dist/7.scoped.css
- All UI chrome is 7.css; custom styling is in `styles.css`.
