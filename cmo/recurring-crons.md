# Recurring Crons (Moxie Ops)

This file is the source of truth for what should be automated + where results should be delivered.

Delivery target:
- Telegram DM: 6699776435

## Heartbeat (2x/day)
- Summary of: traffic delta, signups/paid delta, blockers, next 1–3 actions.

## FormBeep

### Daily traffic check (09:00 local)
- Pull last 24h visitors/pageviews + top pages.
- Compare to previous 24h.
- Flag anomalies.

### Daily search/SEO check (11:00 local)
- Track a small set of money keywords:
  - webflow whatsapp form
  - wordpress whatsapp form
  - framer whatsapp form
  - contact form to whatsapp
  - form submission webhook
- Note new pages to create.

### Weekly growth review (Sun)
- What shipped
- What converted
- Biggest bottleneck
- Next week’s bet

## Implementation notes
- Cron runner must be able to read:
  - /root/moxie/cmo/*
  - /root/moxie/products/formbeep/*
- In this environment, HQ repo lives at /root/moxie_hq.
  - Ensure /root/moxie/cmo -> /root/moxie_hq/cmo
  - Ensure /root/moxie/products -> /root/moxie_hq/products
