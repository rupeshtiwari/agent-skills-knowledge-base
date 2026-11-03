# Semantic Rubrics That Test Meaning

Status: proposed rubric design. A rubric makes judgment inspectable; it does not eliminate reviewer error.

## Turn Abstract Quality Into Observable Behavior

Avoid a single question such as “Is this bar-raiser?” It encourages a broad impression rather than a useful diagnosis. Divide the task into observable dimensions, describe boundaries and require evidence locations.

| Dimension | Strong evidence | Near-miss | Failure |
|---|---|---|---|
| Technical correctness | Claim matches authoritative source and conditions | Correct only under unstated assumptions | False or materially misleading claim |
| Objective coverage | Learner can perform the required decision/action | Terminology mentioned without teaching | Required objective absent |
| Visual alignment | Narration explains visible relationship | Boxes named, relationship unclear | Narration invents unseen element |
| Concrete explanation | Example exposes mechanism and consequence | Example present but disconnected | Pure abstraction where example is needed |
| Spoken clarity | Natural complete thought with clear referents | Understandable after rereading | Ambiguous subject, shorthand or broken flow |
| Scope fidelity | Required content without prohibited drift | Extra content distracts | Violates explicit boundary |

## Require Evidence, Not Adjectives

Each verdict should identify the requirement, the relevant passage or artifact location, the observed issue and its effect. “Unclear” is insufficient. “The arrow points from the cache to the database, but narration says the database fills the cache; clarify which operation the arrow represents” is actionable.

Evidence must exist in the actual artifact. A reviewer should not accept the generator's summary as a substitute for viewing the relevant content.

## Calibrate With Boundary Cases

Build examples that differ by one meaningful property. Compare a correct explanation with one that reverses cause and effect. Compare an objective taught through a decision with the same keyword merely mentioned. Reviewers should agree on why one passes and the other fails.

Use a held-out calibration set and periodically recheck it after changing the grader prompt or model. Avoid examples that reveal the desired answer through a filename such as `bad-example.txt`.

## Separate Severity From Score

A factual error that changes the recommended action can be a blocker even when the rest of the document is excellent. A minor stylistic preference may be optional polish. Do not average a critical failure away with high scores elsewhere.

## Account for Missing Evidence

“Cannot verify” is a legitimate outcome. If the visual is unavailable, visual alignment is blocked. If the approved outline is absent, exact alignment is blocked. The reviewer may still assess grammar or internal consistency, clearly limited to the available evidence.

## Adjudication

When reviewers disagree, compare their cited evidence and assumptions. Resolve the task interpretation before changing the rubric. Preserve the disagreement when evidence remains inconclusive. Multiple reviewers agreeing is useful evidence, not proof; correlated models can share the same error.

## Prevent Grader Gaming

Do not reward length, confident language or the presence of rubric keywords. Give graders access to authoritative inputs and the actual output. Check samples where claims are plausible but false. Require concise rationales tied to observable evidence, not hidden reasoning transcripts.
