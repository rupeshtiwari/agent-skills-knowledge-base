# Community Issue Ledger

Public issue reports provide reproducible leads, not established universal behavior. These reports were inspected on 3 November 2026. None was reproduced locally, and current fix status is not asserted.

| Report | Reported problem | Reported or proposed mitigation | Evidence status |
|---|---|---|---|
| [Claude Code #21947](https://github.com/anthropics/claude-code/issues/21947) | A visible personal skill was not automatically applied | Proposed: test explicit invocation and verify the exact product surface | Issue-body observation only; not a confirmed fix |
| [Claude Code #46952](https://github.com/anthropics/claude-code/issues/46952) | Reporter hypothesizes activation depends on keyword overlap | Proposed: evaluate paraphrases, clear descriptions and installed-set size | Internal routing mechanism not verified; do not teach hypothesis as fact |
| [Claude Code #54535](https://github.com/anthropics/claude-code/issues/54535) | A command wrapper repeatedly re-invokes its own skill | Reporter workaround: use substantive content instead of a wrapper that invokes itself | Reproduction and workaround described by reporter; not independently tested |

For the recursive-wrapper report, prefer correcting source configuration and testing a pinned version rather than relying on manual edits to generated plugin caches. Cache changes can be overwritten. This preference is our engineering recommendation.

## How to Submit a Useful Bug Report

Include host and model versions, skill commit, installation scope, minimal input, expected result, observed trace, tool availability and a sanitized reproduction. State whether the issue occurs with explicit invocation, implicit invocation or both. Remove secrets and private content.

Distinguish a vendor defect from an invalid package, missing dependency, contradictory instructions or a grading mistake. Reproduce on the intended version before claiming a workaround works today.

## Expanded Troubleshooting Research

The [4 November evidence ledger](../troubleshooting/evidence.md) adds Reddit, Cursor forum and Stack Overflow for Agents reports, including access limitations and withdrawn/unverified diagnoses. Use the [60-question Q&A](../troubleshooting/README.md) for practical diagnostic procedures.
