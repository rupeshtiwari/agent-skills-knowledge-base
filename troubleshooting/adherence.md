# Missed Instructions and Author Intent

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: D1; C1 and C2 are reports, not established causes. See the evidence ledger for source status and limitations.

## Q007 Why are not all skill instructions followed?

Loading instructions is not an enforcement mechanism. Requirements can be ambiguous, incompatible, unavailable at the decision point, or simply missed.

**Diagnose:** Turn each requirement into a ledger row with an expected artifact, event or review criterion. Identify the first unmet requirement in the trace.

**Remedy:** Keep essential invariants explicit and move mechanically checkable conditions into validators. Stop delivery when a required check is missing.

**Verify:** The final artifact satisfies every applicable requirement; skipped and blocked checks are visible rather than silently counted as passed.

## Q008 Why does the agent skip the first mandatory step?

A first-step sentence expresses order but does not itself prevent later actions. Separate a sequencing defect from a tool that could not run.

**Diagnose:** Check the first executed action, tool availability and whether the exact skill version loaded. Compare fresh and established sessions.

**Remedy:** For a hard prerequisite, make later operations require a real output from that prerequisite, such as a validated manifest. Do not rely on capital letters alone.

**Verify:** A deliberate missing-prerequisite test prevents downstream execution, and the successful trace shows the prerequisite before dependent work.

## Q009 Why does the agent obey the beginning but forget the end?

Long trajectories can leave distant instructions less useful at execution time; truncation or compaction may also intervene. These are hypotheses to test, not universal explanations.

**Diagnose:** Compare a minimal task with a long task and inspect any context events. Check whether late-stage requirements were ever available.

**Remedy:** Use short phase contracts and explicit completion criteria. Re-establish the current contract when resuming rather than repeating the entire knowledge base.

**Verify:** A long-context regression case still checks final-stage requirements against the artifact actually delivered.

## Q010 Why does repeating MUST and NEVER not fix the problem?

Repetition does not make an unenforced requirement executable, and contradictory repetitions can increase ambiguity.

**Diagnose:** Rewrite the failed rule as a condition that an external observer could judge. Ask what evidence would distinguish compliance from a confident claim.

**Remedy:** Replace emphasis with an input condition, required action, stop condition and validation method. Preserve a concise explanation where judgment is needed.

**Verify:** A negative test violating that rule is rejected even when the response confidently claims success.

## Q011 Why does the agent interpret my instruction differently from my intent?

Terms such as professional, complete or concise leave room for multiple reasonable outputs. More words do not necessarily resolve the ambiguity.

**Diagnose:** Compare your accepted example, a rejected near-miss and the written rule. Identify the difference the rule failed to express.

**Remedy:** Add a rubric with boundary examples and state priorities when goals conflict. Keep illustrative examples separate from required literal text.

**Verify:** A reviewer can explain why each held-out example passes or fails without relying on the author's unstated preferences.

## Q012 Why does a later user request conflict with the skill?

A reusable workflow cannot anticipate every task-specific exception. Skills must operate within the host's instruction hierarchy and the user's authorized scope.

**Diagnose:** Identify the exact conflicting clauses and whether the later request changes scope, style, safety or acceptance criteria.

**Remedy:** Apply the host's precedence rules. Ask only when unresolved ambiguity materially changes the work; record authorized exceptions in the task contract.

**Verify:** The result follows the applicable task instructions and lists any requirement that could not be satisfied; it does not secretly ignore the conflict.
