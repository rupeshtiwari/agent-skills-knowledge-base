#!/usr/bin/env python3
"""Offline structural validation. Does not evaluate an AI skill or remote sources."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    sources = json.loads((ROOT / 'catalog/sources.json').read_text())
    ids = [s['id'] for s in sources]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate source IDs')
    for source in sources:
        for field in ('id', 'title', 'url', 'type', 'review_depth', 'notes', 'checked_on'):
            if not source.get(field):
                errors.append(f"Missing {field}: {source.get('id')}")
        if not source['url'].startswith('https://'):
            errors.append(f"Non-HTTPS source: {source['id']}")
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', source['checked_on']):
            errors.append(f"Invalid date: {source['id']}")
    catalogue = (ROOT / 'catalog/README.md').read_text()
    for source in sources:
        if f"## {source['id']}: {source['title']}" not in catalogue:
            errors.append(f"Catalogue missing {source['id']}")
    documents = list(ROOT.rglob('*.md'))
    for doc in documents:
        text = doc.read_text()
        if text.count('```') % 2:
            errors.append(f'Unclosed code fence: {doc.relative_to(ROOT)}')
        for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in dest or dest.startswith('mailto:'):
                continue
            path, _, anchor = dest.partition('#')
            target = (doc.parent / unquote(path)).resolve() if path else doc
            if not target.is_relative_to(ROOT):
                errors.append(f'Path outside repository: {dest}')
            elif not target.exists():
                errors.append(f'Broken local link in {doc.name}: {dest}')
            elif anchor and target.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+)$', target.read_text(), re.M)
                slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
                if anchor not in slugs:
                    errors.append(f'Broken heading link in {doc.name}: {dest}')
    cases = json.loads((ROOT / 'evals/cases.json').read_text())
    if len({c['id'] for c in cases}) != len(cases):
        errors.append('Duplicate evaluation case IDs')
    for case in cases:
        if not all(case.get(f) for f in ('id', 'category', 'input_scenario', 'expected_behavior', 'status')):
            errors.append(f'Incomplete case: {case}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(sources)} sources, {len(documents)} Markdown files, {len(cases)} evaluation scenarios')
    print('Checked metadata, local file/heading links and case completeness. AI evaluations: NOT RUN.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
