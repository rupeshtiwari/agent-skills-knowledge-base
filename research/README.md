# Research Notes

These notes distinguish source findings from proposed applications. Abstract-only review is not full methodological review. Consult full papers before relying on detailed causal or statistical claims.

## SkillsBench, v4

[Source S14](https://arxiv.org/abs/2602.12670v4), abstract reviewed. The current abstract describes 87 tasks across eight domains and 18 model-harness configurations. Its paired comparison reports average pass rate increasing from 33.9% to 50.5% with curated skills. It also reports an advantage for focused packages over larger bundles.

**Application:** use a no-skill baseline and test package size. **Limit:** this aggregate is not the expected gain for every skill. Earlier versions and search excerpts contain different task counts; record the version rather than blending them.

## SWE-Skills-Bench, v2

[Source S15](https://arxiv.org/abs/2603.15401v2), abstract reviewed. The study evaluates 98 public software skills using repository-specific requirements and paired runs. Its abstract reports 92 skills without statistically significant effects and a small aggregate pass-ratio change, 76.6% to 76.9%. It describes harmful cases in which templates displace explicit requirements.

**Application:** reject the assumption that installing a popular skill must help. **Limit:** lack of statistical significance is not proof of zero effect; these tasks and skills differ from SkillsBench.

## Agent Skills Can Be Harmful

[Source S16](https://www.microsoft.com/en-us/research/publication/agent-skills-can-be-harmful-an-empirical-study-of-skill-induced-failures-in-llm-agents/), publisher summary reviewed. The authors study paired failures and cost regressions, reporting both functional errors and excessive procedures. Excessive verification is one reported cost source.

**Application:** track runtime and tool calls alongside task success. **Limit:** an attributed case collection is not a population-wide failure rate. Do not infer that most skills are harmful.

## Lost in the Middle

[Source S17](https://arxiv.org/abs/2307.03172), abstract reviewed. The paper studies position-sensitive retrieval in long contexts on its tested models and tasks.

**Application:** test relevant instructions in long and distracting sessions, and retrieve selectively. **Limit:** historical results do not establish the magnitude of this effect in a particular current model, nor prove the cause of one skipped instruction.

## tau-bench

[Source S18](https://arxiv.org/abs/2406.12045), abstract reviewed. This benchmark compares final database state with goal state and studies repeated-trial reliability.

**Application:** check actual effects and repeated performance. **Limit:** its customer-service environments and original model results are not direct evaluations of present-day skill packages.

## Research to Review Next

[SkillCT](https://arxiv.org/abs/2610.38147) was identified and its metadata inspected; its full methods remain unreviewed. [WebDev-Skills-Bench](https://arxiv.org/abs/2608.23067) was found in search, but the page fetch failed. No numerical findings from either are used as release evidence here.

## What the Evidence Does Not Establish

It does not establish a universal best skill length, an all-platform trigger algorithm, a guaranteed success rate, or a fixed number of review passes sufficient for every task. Those claims require narrower definitions and direct measurement.
