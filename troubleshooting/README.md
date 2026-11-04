# Skill Troubleshooting Q&A

[Home](../#learning-hub) · [Evidence and platform notes](evidence.md) · [Machine-readable Q&A](qna.json)

**60 questions across 10 categories. Updated 4 November 2026.** These are diagnostic patterns and original engineering recommendations, not a measured ranking of the most frequent bugs. No live-host reproductions were run for this edition. Community posts establish reported symptoms, not universal causes or verified fixes.

## Start With the Failed Boundary

| Observation | Start here |
|---|---|
| Skill missing or not selected | [Discovery and activation](activation.md) |
| Skill loaded but instructions missed | [Adherence and author intent](adherence.md) |
| Too slow or expensive | [Performance](performance.md) |
| Local success, cloud failure | [Packaging and updates](packaging.md) |
| Calls fail or tools are absent | [Tools and environment](tools.md) |
| Long sessions or multiple skills diverge | [Context and composition](context.md) |
| Output looks right but fails requirements | [Quality and validation](quality.md) |
| Access or authorization blocks work | [Permissions and trust](permissions.md) |
| Duplicates, loops or partial completion | [Recovery](recovery.md) |
| Uncertain benefit or regressions | [Evaluation](evaluation.md) |

## Question Index

### Discovery and Activation

- [Q001: Why is my skill not working at all?](activation.md#q001-why-is-my-skill-not-working-at-all)
- [Q002: Why does explicit invocation work but automatic activation fail?](activation.md#q002-why-does-explicit-invocation-work-but-automatic-activation-fail)
- [Q003: Why is the slash command missing?](activation.md#q003-why-is-the-slash-command-missing)
- [Q004: Why does the wrong skill activate?](activation.md#q004-why-does-the-wrong-skill-activate)
- [Q005: Why does a skill activate on almost every request?](activation.md#q005-why-does-a-skill-activate-on-almost-every-request)
- [Q006: Why does adding more skills make an existing skill harder to trigger?](activation.md#q006-why-does-adding-more-skills-make-an-existing-skill-harder-to-trigger)

### Missed Instructions and Author Intent

- [Q007: Why are not all skill instructions followed?](adherence.md#q007-why-are-not-all-skill-instructions-followed)
- [Q008: Why does the agent skip the first mandatory step?](adherence.md#q008-why-does-the-agent-skip-the-first-mandatory-step)
- [Q009: Why does the agent obey the beginning but forget the end?](adherence.md#q009-why-does-the-agent-obey-the-beginning-but-forget-the-end)
- [Q010: Why does repeating MUST and NEVER not fix the problem?](adherence.md#q010-why-does-repeating-must-and-never-not-fix-the-problem)
- [Q011: Why does the agent interpret my instruction differently from my intent?](adherence.md#q011-why-does-the-agent-interpret-my-instruction-differently-from-my-intent)
- [Q012: Why does a later user request conflict with the skill?](adherence.md#q012-why-does-a-later-user-request-conflict-with-the-skill)

### Slowness Cost and Context

- [Q013: Why is my skill slow?](performance.md#q013-why-is-my-skill-slow)
- [Q014: Why does loading a skill consume so much context?](performance.md#q014-why-does-loading-a-skill-consume-so-much-context)
- [Q015: Why does the agent keep searching or reading the same files?](performance.md#q015-why-does-the-agent-keep-searching-or-reading-the-same-files)
- [Q016: Why does excessive verification make the workflow slower?](performance.md#q016-why-does-excessive-verification-make-the-workflow-slower)
- [Q017: Why do parallel agents or tools not make it faster?](performance.md#q017-why-do-parallel-agents-or-tools-not-make-it-faster)
- [Q018: Why do token costs grow even when the answer is short?](performance.md#q018-why-do-token-costs-grow-even-when-the-answer-is-short)

### Packaging Installation and Updates

- [Q019: Why is a valid-looking SKILL.md rejected?](packaging.md#q019-why-is-a-valid-looking-skillmd-rejected)
- [Q020: Why does installation report success but the host cannot find the skill?](packaging.md#q020-why-does-installation-report-success-but-the-host-cannot-find-the-skill)
- [Q021: Why does the old version still run after an update?](packaging.md#q021-why-does-the-old-version-still-run-after-an-update)
- [Q022: Why do two copies of the same skill behave differently?](packaging.md#q022-why-do-two-copies-of-the-same-skill-behave-differently)
- [Q023: Why does the skill work locally but not in a cloud agent?](packaging.md#q023-why-does-the-skill-work-locally-but-not-in-a-cloud-agent)
- [Q024: Why is cloud skill sync stuck at zero items?](packaging.md#q024-why-is-cloud-skill-sync-stuck-at-zero-items)

### Tools Scripts and Environment

- [Q025: Why does the skill describe a tool the agent cannot call?](tools.md#q025-why-does-the-skill-describe-a-tool-the-agent-cannot-call)
- [Q026: Why does a script work in my terminal but fail inside the agent?](tools.md#q026-why-does-a-script-work-in-my-terminal-but-fail-inside-the-agent)
- [Q027: Why are reference files not read?](tools.md#q027-why-are-reference-files-not-read)
- [Q028: Why are arguments passed incorrectly to scripts?](tools.md#q028-why-are-arguments-passed-incorrectly-to-scripts)
- [Q029: Why does the agent claim it ran tests when it did not?](tools.md#q029-why-does-the-agent-claim-it-ran-tests-when-it-did-not)
- [Q030: Why does a successful tool exit still produce a broken artifact?](tools.md#q030-why-does-a-successful-tool-exit-still-produce-a-broken-artifact)

### Long Tasks and Skill Composition

- [Q031: Why does the skill stop working after a long conversation?](context.md#q031-why-does-the-skill-stop-working-after-a-long-conversation)
- [Q032: Why does clearing the chat change results?](context.md#q032-why-does-clearing-the-chat-change-results)
- [Q033: Why does combining two good skills produce a bad result?](context.md#q033-why-does-combining-two-good-skills-produce-a-bad-result)
- [Q034: Why does one skill repeatedly invoke itself?](context.md#q034-why-does-one-skill-repeatedly-invoke-itself)
- [Q035: Why does an unrelated installed skill influence my output?](context.md#q035-why-does-an-unrelated-installed-skill-influence-my-output)
- [Q036: Why does a subagent miss the parent skill rules?](context.md#q036-why-does-a-subagent-miss-the-parent-skill-rules)

### Output Quality and Validation

- [Q037: Why is the output correct in format but wrong in meaning?](quality.md#q037-why-is-the-output-correct-in-format-but-wrong-in-meaning)
- [Q038: Why are word counts or exact strings wrong?](quality.md#q038-why-are-word-counts-or-exact-strings-wrong)
- [Q039: Why do citations look real but not support the answer?](quality.md#q039-why-do-citations-look-real-but-not-support-the-answer)
- [Q040: Why does the skill copy examples too literally?](quality.md#q040-why-does-the-skill-copy-examples-too-literally)
- [Q041: Why does a self-review say everything is perfect?](quality.md#q041-why-does-a-self-review-say-everything-is-perfect)
- [Q042: Why did tests pass but the final edited file fail?](quality.md#q042-why-did-tests-pass-but-the-final-edited-file-fail)

### Permissions Privacy and Trust

- [Q043: Why does the skill stop to ask for permission?](permissions.md#q043-why-does-the-skill-stop-to-ask-for-permission)
- [Q044: Why can the skill read data but cannot update it?](permissions.md#q044-why-can-the-skill-read-data-but-cannot-update-it)
- [Q045: Why does downloaded content change the skill behavior?](permissions.md#q045-why-does-downloaded-content-change-the-skill-behavior)
- [Q046: Why should credentials not be placed inside a skill?](permissions.md#q046-why-should-credentials-not-be-placed-inside-a-skill)
- [Q047: Why can a third-party skill be risky even when its Markdown looks harmless?](permissions.md#q047-why-can-a-third-party-skill-be-risky-even-when-its-markdown-looks-harmless)
- [Q048: Why does the skill choose the wrong account or repository?](permissions.md#q048-why-does-the-skill-choose-the-wrong-account-or-repository)

### Failures Retries and Recovery

- [Q049: Why does retrying create duplicate posts files or records?](recovery.md#q049-why-does-retrying-create-duplicate-posts-files-or-records)
- [Q050: Why does the skill loop forever trying to fix an error?](recovery.md#q050-why-does-the-skill-loop-forever-trying-to-fix-an-error)
- [Q051: Why does a partially completed run start from scratch?](recovery.md#q051-why-does-a-partially-completed-run-start-from-scratch)
- [Q052: Why does rollback restore files but not the system?](recovery.md#q052-why-does-rollback-restore-files-but-not-the-system)
- [Q053: Why does a temporary outage become a permanent task failure?](recovery.md#q053-why-does-a-temporary-outage-become-a-permanent-task-failure)
- [Q054: Why does the agent silently substitute a different tool or method?](recovery.md#q054-why-does-the-agent-silently-substitute-a-different-tool-or-method)

### Evaluation Regression and Support

- [Q055: How do I know whether a skill actually improves results?](evaluation.md#q055-how-do-i-know-whether-a-skill-actually-improves-results)
- [Q056: How many tests are enough to claim the skill is reliable?](evaluation.md#q056-how-many-tests-are-enough-to-claim-the-skill-is-reliable)
- [Q057: Why does a model or host update break a previously good skill?](evaluation.md#q057-why-does-a-model-or-host-update-break-a-previously-good-skill)
- [Q058: Why does the skill work on easy examples but fail in real work?](evaluation.md#q058-why-does-the-skill-work-on-easy-examples-but-fail-in-real-work)
- [Q059: How should I report a skill bug so others can reproduce it?](evaluation.md#q059-how-should-i-report-a-skill-bug-so-others-can-reproduce-it)
- [Q060: Can a skill be made to work 100 percent exactly as its author intended?](evaluation.md#q060-can-a-skill-be-made-to-work-100-percent-exactly-as-its-author-intended)

## Capture a Reproducible Incident

Use the [incident template](../templates/incident-record.md). Preserve the exact prompt, host/model versions, skill revision, installation scope, tool availability, expected result, observed trace and final artifact. Redact private data before sharing. Distinguish missing invocation, failed execution and failed acceptance.

## Continue Into the Engineering Chapters

- [Failure catalogue](../docs/03-failures.md)
- [Evaluation and release gates](../docs/04-evaluation.md)
- [Security](../docs/05-security.md)
- [Author intent](../docs/08-author-intent.md)
- [Enforcement architecture](../docs/09-enforcement-architecture.md)
- [Testing playbook](../docs/10-testing-playbook.md)
- [Recovery](../docs/11-recovery-and-idempotency.md)
- [Semantic rubrics](../docs/12-semantic-rubrics.md)
- [Context and composition](../docs/13-context-and-composition.md)
