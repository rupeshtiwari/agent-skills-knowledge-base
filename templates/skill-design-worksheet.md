# Skill Design Worksheet

Complete before drafting instructions.

| Field | Required answer |
|---|---|
| Task and user | Who needs which repeatable outcome? |
| Trigger | What requests should activate this workflow? |
| Exclusions | Which similar requests should not? |
| Inputs | Required files, formats, versions and authoritative source |
| Output | Exact artifact or external state and destination |
| Boundaries | Allowed edits, immutable files and side effects |
| Tools | Required capabilities and permissions |
| Dependencies | Runtime, packages, network and secrets mechanism |
| Mechanical checks | What can code validate? |
| Semantic checks | What needs a rubric or human review? |
| Failure behavior | Missing input, timeout, partial success, conflict |
| Retry budget | Maximum attempts and evidence needed for each retry |
| Evaluation | Baseline, held-out cases, repetitions and metrics |
| Release | Owner, commit, tested versions and rollback |

Write one success example, one near-miss and one out-of-scope request. Explain why each belongs in its category. Do not fill these with generic statements such as “be accurate.”
