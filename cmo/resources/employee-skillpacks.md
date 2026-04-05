# Employee Skills System - Canonical Skill Packs

*Last updated: 2026-04-05 13:45 UTC*

This file defines reusable skill packs for each employee role. All skills
reference existing toolkits/scripts without duplicating their content.

---

## 1. Skill Definitions (Canonical)

| ID | Name | Description | Prerequisites |
|---|---|---|---|
| SP001 | Umami daily pull | Pull Umami analytics for a product site into `inputs/` | `UMAMI_API_KEY` |
| SP002 | GSC export & study | Export Google Search Console data and produce insights | GSC service account |
| SP003 | Reddit intel loop | Gather competitor & self-history intel via browser automation | none |
| SP004 | Reddit weekly plan | Generate Tue/Wed/Thu Reddit posting plan with copy & windows | SP003 output |
| SP005 | X execution packet | Build Twitter/X posting threads with timing & copy | X account access |
| SP006 | DataForSEO SERP brief | Generate SEO opportunity brief from SERP probe | DataForSEO creds OR free fallback |
| SP007 | Directory last-mile QA | Verify listing requirements before submitting to directories | none |
| SP008 | GSC vs Umami study | Cross-analyse search vs on-site behaviour | SP001 + SP002 outputs |
| SP009 | Competitor scan | Scripted pricing/features/positioning scrape | none |
| SP010 | HQ autopush | Safely commit+push HQ repo with `flock` lock | GitHub write PAT |

---

## 2. Employee → Skill Mapping

### Astra (Growth Research Lead)
| Skill | Frequency | Notes |
|---|---|---|
| SP003 | Mon | Run before weekly plan |
| SP004 | Mon | Produces `/products/<prod>/outreach/reddit-weekly-plan-next.md` |
| SP006 | Bi-weekly | SERP gap analysis |
| SP009 | Weekly | Competitor intel |

### Jax (Outreach & Distribution Lead)
| Skill | Frequency | Notes |
|---|---|---|
| SP005 | Tue–Thu | Execution packets for founder |
| SP007 | Ad-hoc | Pre-submission QA |

### Kiro (SEO Strategist)
| Skill | Frequency | Notes |
|---|---|---|
| SP002 | Monthly | GSC export + insights |
| SP006 | Weekly | SERP briefs |
| SP008 | Bi-weekly | GSC↔Umami cross-analysis |

### Mira (Analytics Lead)
| Skill | Frequency | Notes |
|---|---|---|
| SP001 | Daily | Umami pull → `umami-daily.json` |
| SP008 | Bi-weekly | GSC vs Umami study |
| SP002 | Monthly | GSC export |

### Forge (Full Stack Engineer) — **YOU**
| Skill | Frequency | Notes |
|---|---|---|
| SP001 | Infra | Build/maintain Umami pull scripts |
| SP010 | Daily | HQ autopush (locking) |
| SP007 | Infra | QA scripts for directory submissions |

### Ember (Content Production Lead)
| Skill | Frequency | Notes |
|---|---|---|
| SP005 | As-needed | Draft X threads |
| SP009 | Weekly | Competitor content scan |

---

## 3. SOP References

All SOPs live under `/root/moxie_hq/cmo/sops/`. The master index
is `SOP_INDEX.md`. Employees should consult their SOUL.md for
directives on when to use each SOP.
