# Contributing

Add a source record with a stable ID, exact title, primary URL, type, checked date, review depth and limitation. Explain which claim it supports. Update both catalogue formats and run the local validator.

Keep vendor behavior, research findings, community observations and recommendations distinct. Cite paper versions. Do not describe a video as watched without reviewing it. Do not infer that an issue is fixed from its closed status alone.

Contribute original summaries and links. Do not upload paid books, full transcripts, private course materials, access tokens or proprietary documents. Check source licenses before including code.

For a proposed practice, add a realistic test case and explain the failure it should prevent. Prefer a small, evidence-backed addition to a large generic checklist. If a source changes, update affected claims and preserve a note explaining the change.

Maintenance cadence is owner-managed: recheck platform details before releases and review stale catalogue entries periodically. No scheduled automation is installed.

## Troubleshooting Contributions

Keep each question in `troubleshooting/qna.json` synchronized with its category Markdown page. Provide an answer, diagnostic step, proposed remedy and verification criterion. Update the question index and homepage count when adding entries. Add external evidence to `troubleshooting/evidence.md` with inspection depth and reproduction status. Never label an untested suggestion as a confirmed fix. Run `python3 scripts/validate_kb.py` before submission.
