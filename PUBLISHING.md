# Publishing and Updating

Canonical repository: https://github.com/rupeshtiwari/agent-skills-knowledge-base

## Local Website

Requires Python 3.10+; install the pinned renderer once:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-web.txt
./server
```

The launcher uses `.venv/bin/python` when available, otherwise `python3`; override it with `PYTHON` when needed. It builds the site and serves only `_site/` at http://127.0.0.1:8000/. Use `--port 8001` to avoid an occupied port. It binds to localhost by default. Stop with Ctrl+C. Restart after source edits; there is no live reload.

## Static Build and Hosting

```bash
.venv/bin/python scripts/validate_kb.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/build_site.py
```

Upload the contents of `_site/` to any static host, with `index.html` as its entry point. There is no backend, API key, CDN requirement or client router. HTML links and assets are relative, so both domain-root and repository-subpath hosting work without a base URL setting. Keep filenames and case intact. `_site/` is generated and ignored by Git.

The builder uses README.md as the home page, renders collection Markdown to HTML, rewrites local Markdown links (including raw HTML resource cards), retains heading anchors and copies public collection assets/data. It does not publish the Git directory, environment files or private workspace files. Markdown is trusted repository content; review contributions before rendering, as raw HTML is supported.

The old Jekyll entry configuration has been replaced by this single build path; do not point a Jekyll branch build at the sources.

## Optional GitHub Pages Deployment

A manual workflow is included at `.github/workflows/pages.yml`. It validates, tests, builds, uploads and deploys `_site/` using GitHub Pages artifacts. It does not run on every push.

When ready to publish:

1. In the repository, open **Settings → Pages → Build and deployment** and choose **GitHub Actions** as the source
2. Open **Actions → Build and deploy documentation → Run workflow** on the intended branch
3. Inspect the deployment job for the actual public URL and verify a nested page and image

No hosted deployment is claimed until that workflow succeeds. The Pages environment may require approval under your repository settings. Official reference: [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Updating Content

Edit Markdown and assets in their existing source locations. Validate, build and review the intended diff before pushing. The HTML builder is an offline conversion step; it does not run an AI skill or validate remote claims. A successful structural test is not evidence that the educational skill examples were evaluated with a model.
