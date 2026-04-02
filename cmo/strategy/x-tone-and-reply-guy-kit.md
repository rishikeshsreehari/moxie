# X Founder Tone + Reply-Guy Kit

Generated: 2026-04-02 09:04:57Z (UTC)
Handle: @rishikeshshari

## 1) Inputs needed (so this becomes accurate)
- Best: X export file (tweets.js or tweets.csv) with engagement fields (likes/replies/retweets/impressions).
- If you don’t want to share export: at minimum confirm your handle + a CSV dump of last 90 days with text + likes/replies/retweets.

## 2) What the script found (current corpus)
Posts analyzed: 121
Length (chars): avg=393, median=168, p25=104, p75=458
Hook signals: questions=13%, numbers=62%, first-person(I)=19%, direct-you=18%
Heuristic tone fingerprint: metric-forward / specific numbers, first-person builder voice

Top recurring words (rough): r, no, form, 1, formbeep, yes, if, email, comments, post, reddit, 2, none, or
Top bigrams: no none, yes r, none yes, --- ---, reddit com, com r, r microsaas, r saas, r webdev, r smallbusiness
Top trigrams: no none yes, none yes r, reddit com r, --- --- ---, no strict flair, strict flair rules, submit reddit com

## 3) What worked (needs X export to be definitive)
Engagement metrics not present in corpus; rerun with X export to score what worked.

## 4) Founder tone tweaks (practical, not cringe)
Make posts and replies follow one of these three shapes:
A) Observation → metric → lesson
B) Mistake → what changed → result
C) Tactic → who it’s for → exact steps

Rules:
- One concrete number per post when possible (time, $, %, count).
- Keep sentences short (aim: 12–18 words).
- Prefer ‘here’s exactly how’ over ‘excited to announce’.
- If pitching FormBeep/StackStats: 80% value, 20% link. Links go in follow-up reply.

## 5) Daily ‘reply guy’ workflow (10 replies/day)
Goal: earn attention + DMs without selling. You’re borrowing distribution.

Daily block (20–30 min):
1) Pick 3 lanes (rotate): indie SaaS building, SEO/content, ops/analytics.
2) Find 10 posts in-lane (mix: big accounts + mid-tail builders).
3) Reply using templates below (2–4 lines).
4) Log each reply (so we learn what converts).

Reply log format (copy/paste into a note):
- date | author | tweet_url | lane | reply_type | outcome (likes/replies/dm) | note

## 6) Reply templates (choose based on the tweet)
1. (Agree + add a missed edge case) ‘Yes — one edge case that bit me: ___. Fix: ___.’
2. (Mini playbook) ‘If I had to do this today: 1) ___ 2) ___ 3) ___.’
3. (Operator metric) ‘We saw ___ drop from ___ to ___. The lever was ___.’
4. (Counterpoint politely) ‘Small disagree: ___ matters less than ___. Because ___.’
5. (Question that upgrades the thread) ‘Curious: are you optimizing for ___ or ___? That changes the move.’
6. (Example) ‘Concrete example: ___ (1 sentence). Result: ___.’
7. (Tool-neutral stack) ‘The stack doesn’t matter; the sequence does: capture → qualify → notify → follow-up.’
8. (Caution) ‘Watch out for ___ — it creates ___ failure mode.’
9. (Checklist) ‘Quick checklist: [ ] ___ [ ] ___ [ ] ___.’
10. (Offer) ‘If you want, I can share a template for ___ — no pitch.’

## 7) Next step
Once you drop the X export file, rerun:
python3 cmo/scripts/x_founder_tone_audit.py --export /path/to/tweets.js --handle @YOURHANDLE --out cmo/strategy/x-tone-and-reply-guy-kit.md

