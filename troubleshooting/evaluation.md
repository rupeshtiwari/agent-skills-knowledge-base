# Evaluation Regression and Support

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: Existing evaluation and testing-playbook chapters. See the evidence ledger for source status and limitations.

## Q055 How do I know whether a skill actually improves results?

A successful demonstration does not establish improvement over using no skill.

**Diagnose:** Run matched tasks with and without the skill using the same environment, tools and grading criteria. Preserve both successes and failures.

**Remedy:** Use held-out tasks, repeated runs and task-category breakdowns. Track quality, time and cost rather than a single vanity score.

**Verify:** Report sample sizes and limitations; adopt only improvements supported by the intended workload.

## Q056 How many tests are enough to claim the skill is reliable?

There is no universal count. Task diversity, failure consequences and environment variability determine coverage needs.

**Diagnose:** List required behaviors, negative cases, boundary inputs, recovery paths and supported platforms. Find untested combinations.

**Remedy:** Choose a risk-based release threshold before measuring. Add cases from real incidents without turning the entire holdout into training examples.

**Verify:** State exactly what was tested and what remains unknown; never turn zero observed failures into a universal guarantee.

## Q057 Why does a model or host update break a previously good skill?

Runtime behavior, tool APIs, routing and instruction interpretation can change independently of the package.

**Diagnose:** Record a version matrix and compare old and new environments on the same frozen fixtures.

**Remedy:** Pin dependencies where supported, review release notes and stage updates behind a regression gate.

**Verify:** A release report identifies changed failure categories and blocks deployment when required acceptance criteria regress.

## Q058 Why does the skill work on easy examples but fail in real work?

Examples may omit ambiguity, malformed inputs, large artifacts, unavailable services and competing instructions.

**Diagnose:** Compare production incidents with the test distribution. Look for categories absent from the benchmark.

**Remedy:** Add realistic but sanitized fixtures, boundary cases and adversarial inputs. Keep task requirements explicit.

**Verify:** The suite catches previously missed incident classes without merely memorizing exact prompts.

## Q059 How should I report a skill bug so others can reproduce it?

A complaint without versions, inputs and evidence cannot isolate routing, package or execution defects.

**Diagnose:** Prepare a minimal harmless package, exact prompt, host/model versions, scope, expected behavior and sanitized trace.

**Remedy:** Include explicit-versus-implicit results, a clean-session comparison and the smallest reproducer. Separate observations from theories.

**Verify:** Another person can reproduce the symptom or explain the differing prerequisite; a closed issue alone is not proof of a fix.

## Q060 Can a skill be made to work 100 percent exactly as its author intended?

No finite test suite or instruction document establishes flawless behavior for every future input and environment. Some deterministic properties can be enforced within a defined boundary.

**Diagnose:** Define the supported task domain, failure conditions and acceptance checks. Identify which requirements still need judgment.

**Remedy:** Combine bounded workflows, executable checks, least-privilege tools and honest stop conditions. Make unsupported cases explicit.

**Verify:** Claim measured results only for the tested conditions and refuse delivery when required evidence is missing.
