# A Detailed Skill Testing Playbook

Status: proposed experimental protocol. Extends [evaluation basics](04-evaluation.md). No AI runs are claimed by this chapter.

## Define the Unit Under Test

The unit is not just SKILL.md. It includes its scripts, references, host, model, tool definitions, permissions, installed skill set and task inputs. A change to any part can change outcomes. Record a manifest for every experiment so a failure can be reproduced.

Distinguish discovery tests from execution tests. Explicitly invoking a skill removes much of the discovery question; it cannot validate automatic activation. Conversely, successful activation does not establish output quality.

## Build a Test Matrix

| Dimension | Useful variations | Error exposed |
|---|---|---|
| Request wording | Direct, paraphrased, typo, shorthand | Brittle routing |
| Scope | Exact task, adjacent task, mixed request | Overreach or wrong activation |
| Inputs | Complete, absent, malformed, conflicting | Invented prerequisites |
| Context | Fresh, long, interrupted, stale history | Lost or outdated requirements |
| Environment | Clean, missing package, offline, remote | Hidden dependencies |
| Tools | Success, partial success, timeout, denial | Unsafe retries or false completion |
| Output | Correct, near-miss, corrupted after validation | Weak grading or stale evidence |
| Security | Untrusted instructions embedded in sources | Instruction/data confusion |
| Version | Old/new skill, model or host | Compatibility regressions |

Do not blindly execute every combination. Use risk-based coverage and targeted combinations for interactions likely to matter. Document what was excluded.

## Three Useful Controls

The no-skill condition estimates whether the workflow needs a skill at all. The current-skill condition provides the production comparison. A same-length generic instruction condition can help investigate whether a gain comes from specific procedural knowledge or merely extra attention. The third control is optional and should answer a real research question.

## Separate Development and Release Data

Use real failures to build development cases. Reserve independent cases for release. If a release case becomes an example in the instructions, move it into development and replace it with an unseen case. Keep all test changes in version control so the apparent improvement cannot come from quietly removing hard tasks.

## Mutation Tests for Validators

Start with a valid artifact, then deliberately remove a required section, alter a frozen file, exceed a count cap or replace a cited source with an unrelated one. The relevant validator should reject the mutation. If it still passes, the acceptance test does not protect the intended property.

Also test invalid evidence: missing result, duplicate ID, unknown check, stale hash and an unrecognized status string. A gate that handles only clean success records is incomplete.

## Metamorphic Tests

When a single exact answer is unsuitable, identify transformations that should preserve or change behavior predictably. Renaming an unrelated file should not change a narration verdict. Removing an objective should change the coverage obligation only when the contract authorizes that revision. Reordering equivalent input rows should preserve a total.

Metamorphic relations are domain assumptions. Validate the relation itself; some order changes genuinely affect meaning.

## Trace Review

Find the earliest divergence, not merely the last error. Did the agent read the wrong source, choose the wrong branch, skip a check or misreport a result? Record enough tool/action evidence to diagnose the problem without requiring private internal reasoning. Sanitize traces before publication.

## Grade Blindly Where Practical

Hide condition labels from semantic reviewers so they do not favor the new skill. Use the same rubric across conditions. Include calibration examples and adjudicate disagreements. Report reviewer agreement rather than pretending a subjective rubric is deterministic.

## Report Without Inflating Results

Report sample size, trial count, version, success definition, exclusions and uncertainty. Separate infrastructure errors from task errors but show both. Report critical failures individually. Include latency and repair burden. Do not convert “all our ten examples passed” into “100% reliable.”

## Release Decision

Accept the candidate only when the preregistered requirements are met. A large average improvement may still be unacceptable if it introduces a critical unauthorized action. A small average improvement may be valuable if it consistently removes a costly human correction. The owner's actual priorities should determine the decision.
