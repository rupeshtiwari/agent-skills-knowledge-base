# Release, Maintenance and Measured Claims

Status: proposed governance process. It does not imply an automation or release pipeline has been installed.

## Version the Complete Package

Record instructions, references, scripts, fixtures and dependencies at one revision. A Markdown version label is insufficient if a referenced script changes independently. Store a manifest of hashes for release artifacts.

Use a changelog that explains behavioral changes: a new trigger, changed output schema, removed requirement, dependency upgrade or stricter acceptance gate. Re-run affected tests based on impact, not merely file extension.

## Release Record

Include task scope, intended users, supported environments, model/host versions, evidence set, sample size, pass criteria, observed failures, runtime cost and rollback target. Report untested surfaces prominently. “Works with the standard” is not equivalent to “tested on all compatible products.”

## Canary Use

Start with a limited set of low-risk real tasks. Observe repair burden and unexpected activation. Maintain a direct way to return to a known-good revision. Do not silently widen scope after a few successes.

## Drift Triggers

Re-evaluate when the model, host, tool schema, permissions, source policy, dependency version or task distribution changes. A skill can remain byte-identical while its environment invalidates prior evidence.

## Failure Intake

Record symptom, expected behavior, task class, versions, sanitized inputs, evidence and impact. Link each confirmed defect to a regression case. Avoid immediately adding prose for every complaint; sometimes the correct fix is removing a conflicting instruction or repairing a tool.

## Honest Reliability Claims

Use language such as “passed 45 of 50 held-out tasks in the stated environment” and describe important failures. A 100% observed pass rate is about a finite test set. It is not a probability guarantee for all future requests.

For a mathematical illustration only, if n independent, identically distributed Bernoulli trials all succeed, a one-sided 95% exact lower bound on success probability is 0.05 raised to the power 1/n. At n=100 this is about 97.05%, not 100%. Real agent tasks often violate the identical-distribution or independence assumptions, so this illustration is not a ready-made confidence claim for your workflow.

## Stop Doing Unproductive Work

Retire skills that do not improve outcomes or that create disproportionate cost. Consolidate duplicates only after checking differences in scope and user expectations. Archive a prior version before removal so regressions can be traced.

## Knowledge-Base Maintenance

The source catalogue should track what was read, what remains a lead and when platform details were checked. Keep research findings tied to paper versions. Add contradictory evidence rather than deleting it to preserve a preferred narrative.
