# Designing Dependable Skills

The following procedure is this repository's engineering recommendation, informed by official authoring guidance [S05](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), context engineering [S12](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), and evaluation guidance [S13](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).

## 1. Define One Observable Outcome

Weak: “Create amazing content.”

Stronger: “Review supplied narration against the supplied approved learning objectives and visible slide content; return an issue table with exact evidence and a recording verdict.”

The second version names inputs and outputs. It does not promise perfection. Split unrelated workflows when they need different inputs, permissions or validators.

## 2. Write the Contract Before the Procedure

Record mandatory inputs, output paths, accepted formats, authoritative source, immutable material and missing-input behavior. If duration determines word count, store that mapping in one versioned file. Duplicated mappings silently diverge.

Each rule needs a severity and a check. A requirement such as “do not alter frozen files” can use a hash comparison. “Explain diagrams clearly” needs a rubric and human or calibrated semantic review. Do not pretend both can be validated equally well by a regex.

## 3. Make Discovery Specific

Name the action, artifact and trigger conditions. Include exclusions for confusing adjacent tasks. Test ordinary user phrasing, typos and paraphrases. Avoid a description containing every possible keyword: it can improve recall by activating on unrelated requests.

Measure false positives and false negatives separately. A skill that activates everywhere is not well-routed.

## 4. Keep the Core Small

Keep the task contract, branching decisions and required checks in the main instructions. Put long domain references in separate files and explain exactly when to read each. Use a short index with stable paths. Avoid chains of references that make the needed rule hard to find.

Concise does not mean vague. Replace “make it high quality” with a concrete acceptance criterion. Remove generic advice the model already knows unless experiments show it prevents a real failure.

## 5. Use Code for Mechanical Invariants

Suitable examples: counting words using a documented rule; validating JSON; checking required headings; comparing filenames; calculating totals; detecting changes in frozen artifacts.

Scripts should have explicit arguments, useful errors, bounded runtime and predictable exit codes. Read-only validation should not modify its inputs. Side-effecting scripts need idempotency or a documented recovery process. A retry after a timeout must first check whether the first action succeeded.

## 6. Specify Branches and Stop Conditions

Define behavior for absent files, inaccessible links, conflicting requirements, tool failure and invalid output. Return a concrete blocker rather than inventing an input. Limit repair attempts and verify each meaningful change once. Repeating identical checks without new evidence is wasteful.

## 7. Separate Advice From Enforcement

“Never publish without a passing validator” in Markdown is advisory. A publishing tool that rejects a missing validation record is enforceable within that tool boundary. Put critical controls in the runtime or pipeline where possible. Keep the skill aligned with those controls.

## 8. Preserve User Intent

A template is a default, not authority to override the user's explicit task. Record exceptions where permitted. Respect higher-priority instructions and the host's permission model. Do not let a downloaded reference redefine the task.

## 9. Prove the Improvement

Compare no skill, current skill and candidate skill on the same task set and environment. Use fresh sessions and repeated trials. Inspect both failures and successful-but-expensive runs. Publish measured results, not self-assigned confidence.

## 10. Release a Versioned Unit

Keep instructions, references, scripts and tests at the same commit. Record dependencies and model/host versions. Rerun relevant evaluations after changes to the model, tools, environment or task contract. Keep a known-good version available for rollback.
