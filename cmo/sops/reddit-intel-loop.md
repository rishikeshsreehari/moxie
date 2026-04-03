# SOP — Reddit Intel Loop (no API)

Purpose
- Make Reddit outreach evidence-first and repeatable.
- Keep the “intel” step on Rishi’s laptop (where cookies/session live), and keep planning + copy inside the repo.

Source code
- Intel script lives in-repo:
  - `/root/moxie_hq/scripts/reddit-intel/reddit_campaign_preflight.py`

High-level flow (the contract)
1) Moxie updates/patches the intel script in `scripts/reddit-intel/` and pushes to repo (versioned).
2) Rishi pulls latest on laptop and runs the script locally (headed mode if needed).
3) Rishi commits the generated intel markdown back into the repo under the correct product folder.
4) Moxie reads the committed intel and produces:
   - Tue/Wed/Thu weekly plan (2 products)
   - paste-ready execution packets

---

## Where intel outputs go (per product)

FormBeep:
- `products/formbeep/outreach/intel/<YYYY-MM-DD>__<subs>.md`

StackStats:
- `products/stackstats/outreach/intel/<YYYY-MM-DD>__<subs>.md`

Naming convention:
- Date is the day you ran intel.
- `<subs>` is hyphen-separated subreddit list (e.g. `buildinpublic-wordpress-microsaas`).

---

## Laptop run commands

From repo root on laptop:

1) Pull latest:
- `git pull origin main`

2) Run FormBeep intel (example):
- `cd scripts/reddit-intel`
- `python3 reddit_campaign_preflight.py \
    --subreddits buildinpublic WordPress microsaas \
    --me rishikeshshari \
    --competitors adambengur ConferenceOnly1415 \
    --out ../../products/formbeep/outreach/intel/2026-04-07__buildinpublic-wordpress-microsaas.md \
    --headed`

3) Run StackStats intel (example, competitors optional):
- `python3 reddit_campaign_preflight.py \
    --subreddits substack newsletters emailmarketing buildinpublic \
    --me rishikeshshari \
    --out ../../products/stackstats/outreach/intel/2026-04-07__substack-newsletters-emailmarketing-buildinpublic.md \
    --headed`

Note:
- `--competitors` is optional; omit it if unknown.
- If Reddit blocks headless runs, always use `--headed`.

---

## Committing intel back to repo

From repo root (laptop):
- `git add products/*/outreach/intel/*.md`
- `git commit -m "intel(reddit): <product> <YYYY-MM-DD>"`
- `git push origin main`

---

## What happens next

Once intel is in the repo:
- Moxie updates:
  - `products/formbeep/outreach/reddit-weekly-plan-next.md`
  - `products/stackstats/outreach/reddit-weekly-plan-next.md`
- and generates paste-ready execution packets for Tue/Wed/Thu.
