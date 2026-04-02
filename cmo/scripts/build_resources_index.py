#!/usr/bin/env python3
"""Generate cmo/resources/INDEX.md

Usage:
  python3 cmo/scripts/build_resources_index.py

Writes:
  cmo/resources/INDEX.md
"""

import os
from pathlib import Path
from collections import defaultdict

ROOT = Path('/root/moxie_hq')
RES = ROOT / 'cmo' / 'resources'

TAG_RULES = [('credentials', ['credentials', 'apikey', 'token', 'keys']), ('distribution', ['distribution', 'directory', 'directories', 'launch-places', 'launchplaces', 'betalist', 'alternativeto']), ('seo', ['seo', 'serp', 'gsc', 'sitemap', 'indexing', 'schema']), ('analytics', ['analytics', 'umami', 'gsc', 'tracking', 'events', 'utm']), ('copy', ['copy', 'landing', 'positioning', 'messaging', 'headline', 'cta']), ('reddit', ['reddit', 'subreddit']), ('x', ['x', 'twitter']), ('indiehackers', ['indiehackers', 'ih']), ('marketplaces', ['marketplace', 'webflow', 'framer', 'glide', 'typedream']), ('ops', ['sop', 'runbook', 'process', 'cadence']), ('reading', ['reading', 'notes', 'taker', 'book', 'article']), ('product-onboarding', ['onboarding', 'questionnaire', 'product-onboarding'])]


def infer_tags(path: str):
    p = path.lower()
    tags = set()
    parts = p.split('/')
    for part in parts:
        if part in {'credentials','distribution','reading','product-onboarding'}:
            tags.add(part)
    for tag, keys in TAG_RULES:
        if any(k in p for k in keys):
            tags.add(tag)
    return sorted(tags)


def main():
    files = []
    for root, _, fs in os.walk(RES):
        for fn in fs:
            files.append(str((Path(root)/fn).relative_to(ROOT)))
    files = sorted(files)

    entries = []
    for f in files:
        rel = f.replace('cmo/resources/','')
        section = rel.split('/')[0] if '/' in rel else '(root)'
        tags = infer_tags(f)
        entries.append((section, rel, tags))

    by_tag = defaultdict(list)
    for section, rel, tags in entries:
        for t in tags:
            by_tag[t].append(rel)

    lines = []
    lines.append('# Resources Index')
    lines.append('')
    lines.append('Purpose: make cmo/resources navigable + searchable. This is a generated index (safe to edit, but prefer regenerating via script).')
    lines.append('')
    lines.append('Quick search:')
    lines.append('- `rg -n "<keyword>" cmo/resources`')
    lines.append('- `rg -n "X|Twitter|IndieHackers|Reddit" cmo/resources`')
    lines.append('')
    lines.append('## Directory map')
    lines.append('')
    lines.append('| Section | File | Tags |')
    lines.append('|---|---|---|')
    for section, rel, tags in sorted(entries, key=lambda x:(x[0], x[1])):
        tag_str = ', '.join(tags) if tags else '—'
        lines.append(f'| `{section}` | `{rel}` | {tag_str} |')

    lines.append('')
    lines.append('## Tag index')
    lines.append('')
    for tag in sorted(by_tag.keys()):
        lines.append(f'### {tag}')
        for rel in sorted(set(by_tag[tag])):
            lines.append(f'- `{rel}`')
        lines.append('')

    (RES/'INDEX.md').write_text('\n'.join(lines), encoding='utf-8')
    print('OK', RES/'INDEX.md')


if __name__ == '__main__':
    main()
