# Failure Catalogue

For symptom-by-symptom help, see the [60-question troubleshooting hub](../troubleshooting/README.md) and [evidence ledger](../troubleshooting/evidence.md).

These are diagnostic patterns, not measured prevalence rankings. Community observations are separately labelled in [the report ledger](../research/community-reports.md). Proposed remedies require local validation.

| Symptom | Possible cause | First check | Proposed remedy | Regression case |
|---|---|---|---|---|
| Skill never activates | Wrong installation scope | Is it listed in this host/workspace? | Fix scope before rewriting | Explicit invocation from intended directory |
| Works explicitly, not implicitly | Description mismatch | Test positive paraphrases | Clarify action and artifact | Ambiguous and typo prompts |
| Activates on unrelated tasks | Overbroad description | Negative examples | Add precise exclusions | Similar vocabulary, different goal |
| Many installed skills disappear | Metadata budget or collisions | Host warnings and names | Remove duplicates; shorten descriptions | Full installed set, not isolated test |
| Required steps skipped | Long or conflicting instructions | Trace of loaded sources | Consolidate critical rules and checks | Long conversation with distracting context |
| Old rules persist | Stale version or loaded context | Loaded commit and file path | Reload using host-supported method | Change a known benign rule and verify |
| Conflicting output limits | Multiple sources of truth | Which version is authoritative? | One configuration with clear precedence | Two deliberately conflicting versions |
| Invented facts or files | Missing-input behavior unspecified | Actual source reads | Stop with exact missing input | Deleted source file |
| Command fails on another machine | Hidden local dependency | Dependency and path checks | Portable paths and pinned environment | Clean environment |
| Works locally, fails remotely | Skills or files not synced | Remote visibility | Package required assets | New remote session |
| Duplicate external action | Blind retry after timeout | External object/state | Idempotency key or read-before-retry | Simulated timeout after successful write |
| Skill repeatedly invokes itself | Recursive wrapper | Invocation trace | Remove self-delegation and bound calls | One invocation produces one workflow |
| Output claims checks passed | No independent verification | Validator output and exit status | Require evidence before status | Validator returns failure |
| Right format, poor substance | Weak semantic rubric | Human review of accepted sample | Improve rubric, calibrate grader | Plausible but misleading explanation |
| Excessive time and tokens | Over-prescriptive pipeline | Tool count and timing | Remove checks without risk benefit | Trivial input with strict budget |
| Template overrides request | Examples treated as fixed policy | Compare task and output | Explicit task-specific adaptation | User requests a different format |
| Unexpected file edits | Scope boundaries absent | Diff against allowlist | Limit writes and check diffs | Out-of-scope frozen file |
| Malicious reference changes behavior | Data treated as instructions | Source trust and action log | Separate retrieved data from authority | Reference asks to reveal credentials |
| Passing test suite, field failures | Narrow fixtures or leakage | Held-out cases | Add realistic unseen cases | New domain and edge cases |
| Regression after model change | Model-dependent behavior | Paired rerun | Revalidate before release | Same fixtures on old/new model |

Relevant evidence: Kiro's [troubleshooting guide](https://kiro.dev/docs/skills/) documents discovery remedies; OpenAI's [build guide](https://learn.chatgpt.com/docs/build-skills) describes discovery budgets; [Microsoft's study](https://www.microsoft.com/en-us/research/publication/agent-skills-can-be-harmful-an-empirical-study-of-skill-induced-failures-in-llm-agents/) reports both functional and efficiency failures. The remaining table entries are engineering hypotheses and test designs, not claims that every platform has each defect.

## A Practical Debugging Order

1. Confirm the exact host, model and skill revision.
2. Confirm the intended skill was available and loaded.
3. Confirm inputs, tools and permissions were available.
4. Locate the first divergence in the action trace.
5. Reduce the task to a reproducible case.
6. Change one cause at a time.
7. Run that regression case and relevant nearby cases.

Do not fix a skipped step by appending “MANDATORY” repeatedly. Decide whether the problem is discovery, ambiguity, missing information, execution or validation first.
