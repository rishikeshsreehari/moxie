# formbeep — GSC vs Umami (last 28d)

## Executive summary
- Umami: 606 pageviews, 436 visitors, 474 visits (last 28d).
- GSC export rows: queries=47, pages=22 (last 28d export).

## Umami — top pages (pageviews)
| pageviews | path |
|---|---|
| 266 | / |
| 63 | /whatsapp-api-pricing/ |
| 30 | /blog/webflow-whatsapp-notifications/ |
| 23 | /integrations/framer/ |
| 17 | /blog/building-formbeep-weekend/ |
| 14 | /blog/ |
| 13 | /tools/whatsapp-link-generator/ |
| 13 | /#pricing |
| 12 | /blog/framer-whatsapp-notifications/ |
| 10 | /blog/why-you-are-missing-leads/ |
| 6 | /privacy/ |
| 6 | /blog/why-formbeep/ |

## Umami — top referrers (visitors)
| visitors | referrer |
|---|---|
| 56 | reddit.com |
| 31 | com.reddit.frontpage |
| 23 | facebook.com |
| 18 | google.com |
| 17 | vibecuterie.com |
| 17 | m.facebook.com |
| 10 | news.ycombinator.com |
| 8 | chatgpt.com |
| 5 | bing.com |
| 5 | substack.com |
| 5 | t.co |
| 3 | rishikeshs.com |

## GSC — top queries (impressions)
| impr | clicks | ctr | pos | query |
|---|---|---|---|---|
| 27 | 0 | 0.00% | 50.7 | whatsapp business api notifications |
| 20 | 0 | 0.00% | 66.4 | contact form 7 whatsapp |
| 19 | 0 | 0.00% | 5.0 | "whatsapp message formatter" online tool |
| 19 | 0 | 0.00% | 63.8 | whatsapp business api |
| 12 | 0 | 0.00% | 61.3 | whatsapp api pricing |
| 10 | 0 | 0.00% | 63.0 | whatsapp business api charges |
| 9 | 0 | 0.00% | 73.2 | whatsapp business api pricing |
| 9 | 0 | 0.00% | 75.7 | ws forms whatsapp |
| 6 | 0 | 0.00% | 54.3 | whatsapp business api get messages |
| 6 | 0 | 0.00% | 50.2 | whatsapp text formatter |
| 5 | 0 | 0.00% | 43.0 | whatsapp business api status |
| 4 | 0 | 0.00% | 88.8 | what is whatsapp api |
| 3 | 0 | 0.00% | 8.7 | whatsapp business api pricing chile 2026 |
| 3 | 0 | 0.00% | 46.7 | whatsapp business api pricing malaysia |
| 3 | 0 | 0.00% | 9.0 | whatsapp payments mexico availability and fees 2026 |

## GSC — top pages (impressions) + Umami pageviews
| impr | clicks | ctr | pos | umami_pv | page |
|---|---|---|---|---|---|
| 2047 | 0 | 0.00% | 8.5 | 63 | https://formbeep.com/whatsapp-api-pricing/ |
| 160 | 0 | 0.00% | 35.6 | 2 | https://formbeep.com/blog/whatsapp-business-api-explained/ |
| 67 | 0 | 0.00% | 27.8 | 2 | https://formbeep.com/tools/whatsapp-contact-form-generator/ |
| 61 | 13 | 21.31% | 1.8 | 266 | https://formbeep.com/ |
| 56 | 0 | 0.00% | 13.5 | 5 | https://formbeep.com/tools/whatsapp-message-formatter/ |
| 31 | 0 | 0.00% | 28.7 | 2 | https://formbeep.com/blog/whatsapp-form-notifications/ |
| 29 | 0 | 0.00% | 6.1 | 10 | https://formbeep.com/blog/why-you-are-missing-leads/ |
| 28 | 0 | 0.00% | 2.1 | 0 | https://formbeep.com/blog |
| 24 | 0 | 0.00% | 8.4 | 12 | https://formbeep.com/blog/framer-whatsapp-notifications/ |
| 23 | 0 | 0.00% | 4.1 | 5 | https://formbeep.com/terms/ |
| 17 | 0 | 0.00% | 10.1 | 30 | https://formbeep.com/blog/webflow-whatsapp-notifications/ |
| 16 | 0 | 0.00% | 43.6 | 1 | https://formbeep.com/tools/whatsapp-qr-code-generator/ |

## Opportunities (high-impr + low-CTR + position 4–20)
Pages:
| impr | ctr | pos | path |
|---|---|---|---|
| 2047 | 0.00% | 8.5 | /whatsapp-api-pricing/ |
| 56 | 0.00% | 13.5 | /tools/whatsapp-message-formatter/ |

Queries: none matched the heuristic (or low GSC volume).

## Prioritized actions (next 7 days)
P0 (instrumentation):
- Add Umami events for key CTAs (pricing CTA click, signup start, signup complete). Without events, we can’t separate ‘traffic problem’ from ‘conversion problem’. 
P0 (search CTR lifts):
- For the top 1–3 pages in the Opportunities table: rewrite title/meta to match the highest-impression queries; add a short FAQ section targeting those queries.
P1 (content alignment):
- Compare Umami top pages vs GSC top pages. If a page is high in Umami but absent in GSC, add internal links + ensure it’s in sitemap + has a clear keyword target.
P2 (ops):
- Automate this report weekly (cron) now that GSC exporter is working in-container.

