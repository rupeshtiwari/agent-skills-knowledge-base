# Publishing and Updating

Canonical public repository: https://github.com/rupeshtiwari/agent-skills-knowledge-base

Run validation before committing updates:

```bash
python3 scripts/validate_kb.py
python3 -m unittest discover -s tests -v
```

Review the diff, commit the intended files and push to the repository. Preserve unrelated changes. No automatic workflow or scheduled refresh is installed.
