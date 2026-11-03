# Output Quality and Validation

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: Existing evaluation and semantic-rubric chapters. See the evidence ledger for source status and limitations.

## Q037 Why is the output correct in format but wrong in meaning?

Schema compliance checks structure; factual and task correctness require additional evidence.

**Diagnose:** Separate structural checks from claim verification and domain judgment. Identify unsupported claims and omitted requirements.

**Remedy:** Use source-backed assertions, task-specific rubrics and independent review for consequential semantic decisions.

**Verify:** A polished but factually wrong fixture fails the semantic gate while valid paraphrases remain acceptable.

## Q038 Why are word counts or exact strings wrong?

Natural-language generation is unsuitable as the sole exact counter. Definitions of words and normalization can differ.

**Diagnose:** Specify the counting algorithm, included sections, Unicode handling and whether markup counts. Run a deterministic checker.

**Remedy:** Make the checker authoritative and revise only the violating text. Recompute after the final edit.

**Verify:** The exact delivered file meets the agreed count or literal-string constraint using the published algorithm.

## Q039 Why do citations look real but not support the answer?

A valid URL can point to a source that never established the nearby claim.

**Diagnose:** Inspect each claim-source pair, source version and relevant passage. Distinguish a paper abstract from a full-methods review.

**Remedy:** Remove unsupported claims or qualify them. Cite primary evidence and disclose access limitations.

**Verify:** A reviewer can locate support for each important external claim without inferring it from a title alone.

## Q040 Why does the skill copy examples too literally?

An example can be mistaken for mandatory content, especially when variable fields are not identified.

**Diagnose:** Test a case whose facts deliberately differ from the demonstration. Check whether old names, numbers or paths leak into the output.

**Remedy:** Label examples as illustrative and mark replaceable fields. Include a contrasting case showing the invariant rather than one surface form.

**Verify:** The new output follows the rule while using only the current task's facts.

## Q041 Why does a self-review say everything is perfect?

The same generator can overlook its own mistakes, and a confidence score is not a measured success rate.

**Diagnose:** Inject known defects and observe whether the review detects them. Compare its judgments with a trusted rubric or external checks.

**Remedy:** Use deterministic checks where possible and independent evidence for subjective judgments. Require reasons tied to exact artifact locations.

**Verify:** Known bad fixtures fail; evaluator disagreement and unknown results remain visible instead of being averaged into a reassuring score.

## Q042 Why did tests pass but the final edited file fail?

Validation may cover an earlier revision. Any post-validation change can invalidate the evidence.

**Diagnose:** Compare the tested artifact hash with the delivered artifact hash and inspect changes made after validation.

**Remedy:** Freeze the artifact before final checks or revalidate the changed properties. Store evidence with the matching contract and artifact revision.

**Verify:** A stale test record is rejected, and only the final bytes are eligible for delivery.
