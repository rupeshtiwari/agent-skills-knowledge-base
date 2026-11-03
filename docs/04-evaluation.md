# Evaluation and Release Gates

This is a proposed protocol, not a claim that the example skill has passed. No model execution benchmark was run in this release. The included Python check validates this repository's structure only.

## Test Three Separate Layers

| Layer | Question | Evidence |
|---|---|---|
| Discovery | Does the right skill load? | Invocation event or equivalent host trace |
| Execution | Does it produce the requested result within scope? | Artifact, state diff, tool trace |
| Acceptance | Does the result meet the task contract? | Deterministic checks plus calibrated semantic review |

Do not infer loading from the model saying “I used the skill.” Do not infer successful publication from a prepared local file.

## Paired Experiment

Select tasks representative of actual usage. Run each in three conditions: no skill, current skill and candidate skill. Keep inputs, model settings, tools and environment fixed. Start fresh sessions to reduce contamination and randomize run order when practical. Repeat stochastic runs. Preserve failures, not only attractive outputs.

Separate development cases from held-out release cases. Do not rewrite the skill after seeing each held-out answer and then report that same set as independent evidence. Infrastructure failures should be labelled and reported; never silently discard inconvenient runs.

## Metrics

| Metric | Definition | Interpretation |
|---|---|---|
| Task success | Successful tasks / attempted tasks | State denominator and failure policy |
| Trigger precision | Correct activations / all activations | Penalizes over-triggering |
| Trigger recall | Correct activations / tasks requiring the skill | Penalizes missed discovery |
| Constraint violation rate | Runs breaking a specified rule / runs | Report critical violations separately |
| Repeated reliability | Fraction of tasks passing every one of k trials | A strict empirical summary; distinguish from pass@k |
| Latency | Median and upper percentile runtime | Include retries |
| Cost | Tokens or measured monetary cost per run | State model price/date if converted to money |
| Human repair burden | Time or edits needed after generation | Captures hidden workload |

The repeated-trial distinction is motivated by [tau-bench](https://arxiv.org/abs/2406.12045). The simple fraction above is a proposed summary for a fixed trial count, not a reproduction of every benchmark estimator. Report uncertainty and small-sample limits. Ten passing examples do not establish a 99% production success probability.

## Grading

Use deterministic checks for arithmetic, schema, file existence and exact constraints. Use semantic review for correctness, teaching quality and supported claims. A model grader needs an explicit rubric, calibration against human labels, and checks for position bias or preference for verbose answers. Do not let the generator's self-score be the only grader.

For an artifact-producing workflow, grade the saved artifact. For external actions, inspect the final external state. Grade unauthorized extra actions as failures even if the intended output exists.

## Example Release Policy

Before testing, the owner chooses numerical thresholds appropriate to risk. A reasonable starting policy is: zero observed critical scope violations; every mandatory mechanical check passing; no unexplained regression on critical held-out cases; an agreed latency budget; and documented semantic review. Zero observed violations is evidence from a finite sample, not proof that future violations are impossible.

Publish a release record with commit, host/model, dataset version, sample size, trial count, baseline comparison, failures and limitations. The [run record template](../evals/run-record.example.json) contains null outcomes intentionally.

Sources for methodology: [S13](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), [S14](https://arxiv.org/abs/2602.12670v4), [S15](https://arxiv.org/abs/2603.15401v2), [S18](https://arxiv.org/abs/2406.12045).
