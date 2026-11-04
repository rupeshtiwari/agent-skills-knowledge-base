#!/usr/bin/env python3
"""Build relocatable HTML from the repository's Markdown; no CDN or runtime API."""
import html
import os
from pathlib import Path
import re
import shutil
from html.parser import HTMLParser
from urllib.parse import urlsplit, urlunsplit, unquote

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '_site'
COLLECTIONS = ('docs', 'catalog', 'research', 'platforms', 'templates', 'examples',
               'evals', 'troubleshooting', 'assets')


def page_path(path):
    return Path('index.html') if path == Path('README.md') else path.with_suffix('.html')


def web_url(value, source):
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or not parts.path:
        return value
    target = Path(os.path.normpath(str(source.parent / unquote(parts.path))))
    if parts.path.endswith('/') and (ROOT / target / 'README.md').is_file():
        target = target / 'README.md'
    if target.suffix == '.md':
        target = page_path(target)
        value = os.path.relpath(target, page_path(source).parent).replace(os.sep, '/')
    else:
        value = parts.path
    return urlunsplit(('', '', value, parts.query, parts.fragment))


class LinkRewriter(HTMLParser):
    """Only rewrite HTML attributes, never code examples or prose."""
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source, self.output = source, []

    def tag(self, tag, attrs, close):
        attrs = [(k, web_url(v, self.source) if k in ('href', 'src') and v else v)
                 for k, v in attrs]
        values = ''.join(' ' + k + (f'="{html.escape(v, quote=True)}"' if v is not None else '')
                         for k, v in attrs)
        self.output.append(f'<{tag}{values}{close}>')

    def handle_starttag(self, tag, attrs): self.tag(tag, attrs, '')
    def handle_startendtag(self, tag, attrs): self.tag(tag, attrs, ' /')
    def handle_endtag(self, tag): self.output.append(f'</{tag}>')
    def handle_data(self, data): self.output.append(data)
    def handle_entityref(self, name): self.output.append(f'&{name};')
    def handle_charref(self, name): self.output.append(f'&#{name};')
    def handle_comment(self, data): self.output.append(f'<!--{data}-->')


def build():
    if OUTPUT.exists(): shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    files = [p for p in ROOT.glob('*.md') if p.name != 'index.md']
    for directory in COLLECTIONS:
        files.extend(p for p in (ROOT / directory).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
    shutil.copyfile(ROOT / 'LICENSE', OUTPUT / 'LICENSE')
    shutil.copyfile(ROOT / 'web/style.css', OUTPUT / 'style.css')
    count = 0
    for source in sorted(files):
        relative = source.relative_to(ROOT)
        destination = OUTPUT / (page_path(relative) if source.suffix == '.md' else relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix != '.md':
            shutil.copyfile(source, destination)
            continue
        text = source.read_text()
        renderer = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'sane_lists'])
        body = renderer.convert(text)
        rewrite = LinkRewriter(relative)
        rewrite.feed(body)
        body = ''.join(rewrite.output)
        title = re.search(r'^# (.+)$', text, re.M)
        title = html.escape(title[1] if title else source.stem)
        prefix = os.path.relpath(OUTPUT, destination.parent).replace(os.sep, '/')
        nav = [('index.html', 'Learning hub'), ('docs/15-skill-building-guide.html', 'Build a skill'),
               ('troubleshooting/README.html', 'Troubleshooting'), ('catalog/collections.html', 'Sources')]
        links = ''.join(f'<a href="{prefix}/{path}">{label}</a>' for path, label in nav)
        destination.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Skills Knowledge Base</title><link rel="stylesheet" href="{prefix}/style.css"></head>
<body><a class="skip" href="#content">Skip to content</a>
<header><a class="brand" href="{prefix}/index.html">Agent Skills Knowledge Base</a><nav aria-label="Main">{links}</nav></header>
<div class="layout"><aside aria-label="On this page"><strong>On this page</strong>{renderer.toc}</aside>
<main id="content">{body}</main></div>
<footer><a href="https://github.com/rupeshtiwari/agent-skills-knowledge-base/blob/main/{relative.as_posix()}">View Markdown source</a> · Built from versioned repository content</footer></body></html>''')
        count += 1
    (OUTPUT / '.nojekyll').touch()
    print(f'Built {count} HTML pages in {OUTPUT}')
    return OUTPUT


if __name__ == '__main__': build()
