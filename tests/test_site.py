"""Check deployment portability and emitted HTML navigation."""
import importlib.util
from html.parser import HTMLParser
from pathlib import Path
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.urls, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src'): self.urls.append(value)
            if key == 'id': self.ids.add(value)


@unittest.skipUnless(importlib.util.find_spec('markdown'), 'Install requirements-web.txt for web checks')
class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from build_site import build
        cls.output = build()

    def test_all_generated_links_and_anchors(self):
        pages = {p.resolve(): Links(p.read_text()) for p in self.output.rglob('*.html')}
        for page, parsed in pages.items():
            for url in parsed.urls:
                parts = urlsplit(url)
                if parts.scheme or parts.netloc: continue
                with self.subTest(page=str(page.relative_to(self.output)), url=url):
                    self.assertFalse(parts.path.startswith('/'), 'Must support subpath deployment')
                    target = (page.parent / unquote(parts.path)).resolve() if parts.path else page
                    self.assertTrue(target.is_relative_to(self.output))
                    self.assertTrue(target.is_file(), str(target))
                    if parts.fragment and target in pages:
                        self.assertIn(unquote(parts.fragment), pages[target].ids)

    def test_code_examples_remain_literal(self):
        from build_site import LinkRewriter
        rewriter = LinkRewriter(Path('docs/example.md'))
        rewriter.feed('<pre><code>&lt;a href="README.md"&gt;</code></pre><a href="../README.md#start-here">Home</a>')
        output = ''.join(rewriter.output)
        self.assertIn('&lt;a href="README.md"&gt;', output)
        self.assertIn('href="../index.html#start-here"', output)

    def test_only_public_output_is_served(self):
        self.assertFalse((self.output / '.git').exists())
        self.assertFalse((self.output / '.env').exists())
        self.assertTrue((self.output / 'assets/learning-cards/qna.svg').is_file())
        self.assertTrue((self.output / 'docs/15-skill-building-guide.html').is_file())
        self.assertTrue((ROOT / 'server').stat().st_mode & 0o111)
