# FormBeep — Reddit Posting Tracker (u/rishikeshshari)

Owner (maintenance): Ember
Execution: Rishi (manual)
Created: 2026-04-01

Purpose:
- Prevent double-posting and rule violations
- Record what we tried, where, and what worked

How to use:
- Before posting in a subreddit: search this file for the subreddit name.
- If we have a recent post there, do comments instead.
- Always log a post/comment immediately after doing it.

---

## A) Subreddit rules + history (source of truth)

| Subreddit | Link policy | Self-promo policy | Flair/format rules | Frequency limits | Have we posted before? | Last post date | Notes |
|---|---|---|---|---|---|---|---|
| r/SaaS | Links allowed if contextual. Text posts preferred | Self-promo OK if value-adding; ~1:10 ratio typical | Flair: Showoff Saturday, Discussion, Marketing | ~1/week per account | NO | — | 215k+ members. Best angles: contrarian/post (Sec 3 playbook). Peak: 18:00-21:00 GST |
| r/smallbusiness | External links DISCOURAGED in posts; fine in comments if contextual | Heavy self-promo gets removed; must be discussion-first | No strict flair requirement; use post flairs when available | ~1 promo post/month max | NO | — | 2.5M+ members. Pain point: missed leads. Angle: "How do you handle form replies when not at desk?" |
| r/microsaas | Links OK if tool is relevant; Showoff Saturdays best for promos | Revenue transparency welcomed; no hard selling | Flair: Show & Tell, Advice, Rant | 1-2/month safest | NO | — | 95k+ members. Best angle: founder story with metrics. Peak: 18:00-21:00 GST |
| r/webdev | Tool links OK in relevant threads; standalone product posts discouraged | Self-promo only in weekend threads (verify "Self-Promo Sunday" still exists) | Flair: Show & Tell for product demos; Discussion for advice | Comments: free. Posts: limited to weekend thread | YES (u/ConferenceOnly1415 / Web2Phone — 4x, 1.0 avg comments) | Prior competitor activity | 1.3M+ members. Target: freelance devs/agencies. Angle: "What form handler for client sites in 2026?" |
| r/EntrepreneurRideAlong | Build diary/journey narratives required | Self-promo is the format; must be honest journey, not marketing | Narrative format; no flair needed | 1-2 posts per journey OK | NO | — | Subset of r/Entrepreneur. Angle: "Day 1: realized form submissions die in email" |
| r/SideProject | Project showcase format; live project links expected | Self-promo welcome; sub exists for this | Flair: Showcase, Feedback common | No hard limit | YES (r/IMadeThis post got 15 comments) | ~Mar 2026 | Good first-post target. Similar vibe to r/EntrepreneurRideAlong |
| r/passive_income | Varies; some weeks strict on promotion | Read sidebar weekly; rules change | No strict flair rules | Low frequency recommended | NO | — | Monitor before posting |
| r/Business_Ideas | Discussion-first, links only if answering question | Self-promo discouraged unless specifically asked | No flair requirements | 1/week max | NO | — | Angle: "Add WhatsApp notifications to any existing form" in response threads |
| r/startup | Links OK if relevant to discussion | Self-promo frowned upon unless in designated threads | Flair: Discussion, Question common | ~1/week | NO | — | Broad audience; only post when lead-routing/customer-comms topic arises |
| r/startups | Similar to r/startup but more active | Self-promo only when adding genuine value | Flair: Show & Tell, Discussion | ~1/week | NO | — | 1.3M+ members. Best for discussion posts, not direct promos |
| r/thesidehustle | Links allowed if contextual | Self-promo OK if discussion-first | No strict flair rules | 1/week max | NO | — | Angle: "Reduce missed leads = more revenue" for side hustlers |
| r/juststart | Links OK; "ship it" culture | Self-promo welcomed; action-oriented sub | No flair requirements | No hard limit | NO | — | Angle: bias for action; "stop overthinking, ship" |
| r/MicroSaas | See r/microsaas (same community, different URL capitalization) | — | — | — | NO | — | Same audience as r/microsaas. Use interchangeably |
| r/Startup_Ideas | Discussion-first, links only if helpful | Self-promo discouraged unless asked | No strict flair rules | 1/week max | NO | — | Lower engagement than r/startups |
| r/ycombinator | Strictly YC ecosystem discussion | No self-promo; must beYC-related or genuinely insightful | No flair | Very limited | NO | — | Only comment when YC/form-handling threads arise |
| r/Entrepreneurs | Links discouraged; discussion-first | Self-promo heavily discouraged outside dedicated threads | Flair: Discussion, Question common | 1/week max | NO | — | ~1M+ members. Broad; quality bar is high |
| r/indiehackers | Cross-post from IH forum preferred | Links to projects OK when asked or in showcase threads | No strict flair | 1-2/month | YES (post got ~14 comments) | ~Mar 2026 | Forum (indiehackers.com) is primary; subreddit is smaller |
| r/GrowthHacking | Links OK if growth-focused | Value-first approach required; data-backed posts preferred | Flair: Case Study, Discussion, Tool common | ~1/week | NO | — | Angle: lead response time as conversion lever |
| r/AppIdeas | Ideas/discussion focus; no product links | Self-promo not appropriate here | No flair requirements | — | NO | — | Low relevance; skip unless form tool discussion arises |
| r/growmybusiness | Links OK when answering specific questions | Self-promo OK only in context | No strict flair rules | 1/week | NO | — | SMB audience; relevant but lower engagement |
| r/buildinpublic | Progress updates welcome; metrics encouraged | Self-promo welcomed if transparent (revenue, traffic, learnings) | Flair: Wins, Lessons, Milestones common | No hard limit | NO | — | Good for transparency posts: traffic data, conversion experiments |
| r/micro_saas | See r/microsaas (underscore variant; same community) | — | — | — | NO | — | Same audience as r/microsaas |
| r/Solopreneur | Links OK if genuinely helpful | Self-promo OK when discussion-first | No strict flair rules | 1/week max | NO | — | Solo-founder audience; moderate engagement |
| r/vibecoding | AI-generated tool posts welcomed | Self-promo expected but must show actual working tool | No strict flair rules | No hard limit | NO | — | Active community. FormBeep fits "AI-built tool" narrative |
| r/startup_resources | Resource-sharing focus; links are expected | Self-promo OK if genuinely useful resource | No strict flair rules | No hard limit | NO | — | Good for soft tool mentions when asked for recommendations |
| r/indiebiz | Emerging community; links OK in context | Self-promo OK when adding value | No strict flair rules | 1/week max | NO | — | Lower volume; growing indie founder base |
| r/AlphaandBetaUsers | Beta-test announcements welcomed | Self-promo is the format; seeking testers | Flair: Alpha, Beta | No hard limit | NO | — | Good for new feature testing announcements |
| r/scaleinpublic | Growth and scaling updates | Self-promo welcomed if transparent | Flair: Wins, Milestones | No hard limit | NO | — | Build-in-public variant for growing businesses |
| r/roastmystartup | Post for critique/feedback | Self-promo IS the ask; people come to critique | No strict flair rules | One roast per startup typically | NO | — | Generates engagement; use when you want brutal feedback |
| r/askmarketing | Answer questions; links only if asked | No self-promo; help-first community | Flair: Question, Discussion | No posting—only answer threads | NO | — | Q&A format; provide insight first; mention FormBeep only if relevant |
| r/localseo | Links OK if discussing local business tactics | Must be educational; pure promo gets removed | Flair: Discussion, Question common | 1 post/2 weeks | NO | — | 80k+ members. Lead response speed angle for local businesses |
| r/WhatsappBusinessAPI | Links OK if solving specific WA API problem | Technical audience; product pitch = ignored | No strict flair rules | 1-2/month | YES (u/rishikeshshari posted on Brazil restrictions) | ~Mar 2026 | 15k+ members. Technical audience; frame as integration solution |

---

## B) Activity log (posts + comments)

### Historical posts (logged from tracking review):

| Date (UTC) | Date (GST) | Subreddit | Type (post/comment) | Title/thread | URL | Link included? | Result (upvotes/comments/DMs) | Notes |
|---|---|---|---|---|---|---|---|---|
| ~Mar 2026 | ~Mar 2026 | r/IMadeThis | Post | FormBeep reveal | (search u/rishikeshshari) | YES | ~15 comments | Decent engagement. First public reveal. |
| ~Mar 2026 | ~Mar 2026 | r/indiehackersindia | Post | FormBeep | (search u/rishikeshshari) | YES | ~14 comments | Good discussion. Second public post. |
| ~Mar 2026 | ~Mar 2026 | r/WhatsappBusinessAPI | Comment | Brazil WA restrictions | (search u/rishikeshshari) | NO | High-quality engagement (score TBD) | Showed real operator knowledge. |
| — | — | r/webdev | — | (competitor u/ConferenceOnly1415 posted 4x) | — | — | ~1 avg comment each | LOW QUALITY posts from Web2Phone — room for better engagement. NOT our account. |
| — | — | — | — | — | — | — | — | Awaiting Week 1 posting |
| — | — | — | — | — | — | — | — | |

---

## C) Quick Reference: "Have we posted here?"

Use this table BEFORE every post/comment. If "YES" in the last 14 days, switch to comments instead.

| Subreddit | Posted by us? | Last posting | Last action | Next post OK? | Cooldown |
|---|---|---|---|---|---|
| r/IMadeThis | YES | ~Mar 2026 | Post (~15 comments) | WAIT (14+ days from last post) | 2 weeks |
| r/indiehackersindia | YES | ~Mar 2026 | Post (~14 comments) | WAIT (14+ days from last post) | 2 weeks |
| r/WhatsappBusinessAPI | YES | ~Mar 2026 | Comment on Brazil WA restrictions | YES (comments only; avoid posts) | — |
| r/webdev | NO | — | Competitor only (u/ConferenceOnly1415) | YES — safe to post | — |
| r/SaaS | NO | — | None | YES | — |
| r/smallbusiness | NO | — | None | YES | — |
| r/microsaas | NO | — | None | YES | — |
| r/EntrepreneurRideAlong | NO | — | None | YES | — |
| r/SideProject | NO | — | None | YES | — |
| r/passive_income | NO | — | None | YES | — |
| r/Business_Ideas | NO | — | None | YES | — |
| r/startup | NO | — | None | YES | — |
| r/startups | NO | — | None | YES | — |
| r/thesidehustle | NO | — | None | YES | — |
| r/juststart | NO | — | None | YES | — |
| r/MicroSaas | NO | — | None | YES | — |
| r/Startup_Ideas | NO | — | None | YES | — |
| r/ycombinator | NO | — | None | Comments only | — |
| r/Entrepreneurs | NO | — | None | Comments only | — |
| r/indiehackers | NO | — | None | YES | — |
| r/GrowthHacking | NO | — | None | YES | — |
| r/AppIdeas | NO | — | None | Skip (low relevance) | — |
| r/growmybusiness | NO | — | None | YES | — |
| r/buildinpublic | NO | — | None | YES | — |
| r/micro_saas | NO | — | None | YES | — |
| r/Solopreneur | NO | — | None | YES | — |
| r/vibecoding | NO | — | None | YES | — |
| r/startup_resources | NO | — | None | YES | — |
| r/indiebiz | NO | — | None | YES | — |
| r/AlphaandBetaUsers | NO | — | None | YES | — |
| r/scaleinpublic | NO | — | None | YES | — |
| r/roastmystartup | NO | — | None | YES | — |
| r/askmarketing | NO | — | None | Comments only | — |
| r/localseo | NO | — | None | YES | — |

## D) Posting Guardrails (Enforced by Ember)

| Rule | Detail |
|---|---|
| **1-in-3 ratio** | Max 1 in 3 comments should mention FormBeep. Other 2 = pure value. |
| **Cooldown** | 7 days minimum between posts to same subreddit. 14 days recommended. |
| **No cross-post spam** | Same content must not appear in multiple subs within 48 hours. |
| **Title variance** | Never reuse same title across subreddits. Customize per community. |
| **Link ratio** | Max 1 external link for every 3 total contributions per session. |
| **Insight-first** | Always lead with value/insight. Product mention only if naturally relevant. |
| **No competitor subs** | Do NOT post FormBeep in competitor-owned subreddits (e.g., r/beepmate for BeepMate). |
| **Log immediately** | Every post/comment must be logged in Section B within 24 hours. |

--

## E) Quick-Access URL Reference

| Subreddit | Post URL | Search for our history |
|---|---|---|
| r/SaaS | reddit.com/r/SaaS/submit/ | reddit.com/r/SaaS/search/?author=rishikeshshari |
| r/smallbusiness | reddit.com/r/smallbusiness/submit/ | reddit.com/r/smallbusiness/search/?author=rishikeshshari |
| r/microsaas | reddit.com/r/microsaas/submit/ | reddit.com/r/microsaas/search/?author=rishikeshshari |
| r/webdev | reddit.com/r/webdev/submit/ | reddit.com/r/webdev/search/?author=rishikeshshari |
| r/startups | reddit.com/r/startups/submit/ | reddit.com/r/startups/search/?author=rishikeshshari |
| r/buildinpublic | reddit.com/r/buildinpublic/submit/ | reddit.com/r/buildinpublic/search/?author=rishikeshshari |
| r/vibecoding | reddit.com/r/vibecoding/submit/ | reddit.com/r/vibecoding/search/?author=rishikeshshari |
| r/indiehackers | reddit.com/r/indiehackers/submit/ | reddit.com/r/indiehackers/search/?author=rishikeshshari |
| r/SideProject | reddit.com/r/SideProject/submit/ | reddit.com/r/SideProject/search/?author=rishikeshshari |
| r/roastmystartup | reddit.com/r/roastmystartup/submit/ | reddit.com/r/roastmystartup/search/?author=rishikeshshari |
