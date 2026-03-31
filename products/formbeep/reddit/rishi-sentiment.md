# Rishi Reddit presence + FormBeep mentions (research)

Date: 2026-03-31

## How this research was done
- Direct Reddit browsing from this environment consistently returned 403 (“blocked by network security”).
- Used PullPush (api.pullpush.io) to enumerate submissions/comments by author and to run keyword searches across Reddit.
- Used Bing briefly as a secondary search source; it did not surface any FormBeep-related Reddit results.

## Identity / accounts found

### u/rishikeshshari
- Found as an active Reddit author via PullPush.
- Activity is broad, but a notable cluster of helpful/technical replies is in r/gohugo.

### u/rishikeshsreehari
- No submissions/comments returned via PullPush for this exact author string.
- Note: u/rishikeshshari frequently links to a GitHub account named “rishikeshsreehari” and a personal website rishikeshs.com, suggesting “rishikeshsreehari” is an off-Reddit handle.

### r/rishikeshshari
- No submissions found for subreddit=rishikeshshari via PullPush.
- Likely does not exist, is private, or has no indexed content.

## FormBeep mentions on Reddit

### By Rishi (u/rishikeshshari)
- No evidence of any posts or comments mentioning:
  - “FormBeep”
  - “formbeep”
  - “formbeep.com”
  - variations like “Form Beep” (when searched globally, results were unrelated false positives)

### Global Reddit search
- PullPush keyword search returned 0 results for “FormBeep”, “formbeep”, and “formbeep.com” across both submissions and comments.
- Conclusion: FormBeep appears to have no discoverable footprint on Reddit (at least indexed by PullPush) at the time of this research.

## Closest relevant: Rishi’s “forms” comments + competitor context
Even though FormBeep itself is not mentioned, Rishi has made comments that reveal his current stack/preferences for handling contact forms (especially in static-site workflows).

1) Rishi uses Web3Forms; asks for differentiation/value prop (explicit competitor comparison)
- Subreddit: r/gohugo
- Comment link: https://www.reddit.com/r/gohugo/comments/1elmbfg/affordable_and_simple_form_collection_for_hugo/ligy2ta/
- Comment (verbatim):
  “Hi!  I currently use web3forms.com for my forms. How is this different from this? Would like to know your value proposition!”
- Takeaway:
  - He’s already a user of Web3Forms.
  - He evaluates alternatives by asking directly for “value proposition” (positioning matters; feature diffs alone may not be enough).
  - Tone: neutral/curious.

2) Recommends Web3Forms and Netlify Forms as “best option” depending on hosting
- Subreddit: r/gohugo
- Comment link: https://www.reddit.com/r/gohugo/comments/1id3288/i_would_like_to_start_blogging_with_hugo_but/m9ylg7l/
- Key points:
  - “It is possible to create forms… services like Web3forms…”
  - “If you are using Netlify for hosting, Netlify forms is the best option.”
  - Also mentions Decap CMS (for CMS needs) in the same comment.
- Takeaway:
  - For the “static site + contact form” job, his mental shortlist includes:
    - Web3Forms
    - Netlify Forms
  - Tone: helpful, pragmatic.

Competitors/products implicitly in Rishi’s orbit (forms-adjacent):
- Web3Forms (explicitly used)
- Netlify Forms (explicitly recommended)
- (Not seen in his content: Typeform, Tally, Jotform, Formspree, Basin, etc.)

## What worked (based on Rishi’s own promotional posts)
There are no FormBeep promo posts by Rishi; the next best signal is what worked for his other “I built X” posts.

Highest-performing build post (strong product/community fit):
- r/IndiaInvestments — “I built an NPS Fund NAV Tracker with Free API for Google Sheets/Excel”
  - Link: https://www.reddit.com/r/IndiaInvestments/comments/1fo6au9/i_built_an_nps_fund_nav_tracker_with_free_api_for/
  - Observed performance (PullPush): score ~109, comments ~62
  - Why it likely worked:
    - Clear user value (“free API”, “Google Sheets/Excel” integration)
    - Highly targeted subreddit where the pain is common
    - Utility > novelty

Moderate/low performance build posts (more niche / less urgent need):
- r/InternetIsBeautiful — “I built CricLite – a plain text live cricket score website”
  - Link: https://www.reddit.com/r/InternetIsBeautiful/comments/1jjnai6/i_built_criclite_a_plain_text_live_cricket_score/
  - Performance: score ~5, comments ~2
- r/SideProject — same CricLite post
  - Link: https://www.reddit.com/r/SideProject/comments/1jjnioo/i_built_criclite_a_plain_text_live_cricket_score/
  - Performance: score ~2, comments ~0

Older but decent fit:
- r/DigitalGardens — “I built my Digital Garden using Hugo”
  - Link: https://www.reddit.com/r/DigitalGardens/comments/ohcqri/i_built_my_digital_garden_using_hugo/
  - Performance: score ~15, comments ~7

## What failed / didn’t work (inferred patterns)
- Cross-posting the “same” build into adjacent subs can underperform dramatically versus the best-fit community.
  - Example: NPS tracker did very well in r/IndiaInvestments, but much less so in r/personalfinanceindia.
- Generic “I built X” without a strong, subreddit-specific hook tends to get low traction.
  - Example: CricLite got limited engagement in both r/SideProject and r/developersIndia.

## Sentiment summary (re: forms tools)
- Toward existing tools:
  - Web3Forms: positive/endorsed (he uses it and suggests it).
  - Netlify Forms: strongly positive in the Netlify-hosted context (“best option”).
- Toward alternatives/new offerings:
  - Curious and open, but expects a crisp differentiation/value proposition.

## Implications for FormBeep positioning (based on Rishi’s expressed preferences)
If FormBeep competes in “static site form handling / form endpoints / form collection”:
- You will likely be compared directly against Web3Forms and Netlify Forms.
- The comparison criteria suggested by Rishi’s comments:
  - Value proposition clarity (why switch?)
  - Fit with static-site workflows (Hugo/Netlify)
  - Simplicity and low-friction setup

## Subreddits to revisit (highest probability based on observed history + relevance)
1) r/gohugo
- Rishi is active here; he’s already discussing forms and alternatives.
- Best angle: “static site forms” (Hugo), migration-from-Web3Forms/Netlify-Forms comparison, spam protection, developer UX.

2) r/SideProject
- He has posted here; engagement was low for CricLite, but it’s still a standard launch venue.
- Best angle: concrete differentiator + quick demo + pricing clarity.

3) r/InternetIsBeautiful
- Slightly better results than r/SideProject for his CricLite post.
- Best angle: a genuinely delightful/useful public demo; minimal marketing tone.

4) r/developersIndia
- He posted here; traction was low for CricLite, but could work if the tool is developer-relevant and has a clear “what’s in it for me.”

Additional relevant subs (not evidenced in his posting history, but logically aligned with forms tooling):
- r/webdev, r/selfhosted, r/opensource, r/netlify

## Raw checklist of key links cited
- Web3Forms value-prop question (Rishi): https://www.reddit.com/r/gohugo/comments/1elmbfg/affordable_and_simple_form_collection_for_hugo/ligy2ta/
- Web3Forms + Netlify Forms recommendation (Rishi): https://www.reddit.com/r/gohugo/comments/1id3288/i_would_like_to_start_blogging_with_hugo_but/m9ylg7l/
- NPS tracker (high-performing build post): https://www.reddit.com/r/IndiaInvestments/comments/1fo6au9/i_built_an_nps_fund_nav_tracker_with_free_api_for/
- CricLite (InternetIsBeautiful): https://www.reddit.com/r/InternetIsBeautiful/comments/1jjnai6/i_built_criclite_a_plain_text_live_cricket_score/
- CricLite (SideProject): https://www.reddit.com/r/SideProject/comments/1jjnioo/i_built_criclite_a_plain_text_live_cricket_score/
