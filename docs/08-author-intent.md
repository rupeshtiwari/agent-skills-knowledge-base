# Preserving the Author's Intent

Status: proposed engineering method. This chapter is original synthesis, not a tested claim that any host can follow all instructions perfectly. It builds on the evaluation and task-alignment concerns in [the research notes](../research/README.md).

## Intent Is More Than a List of Commands

The author usually has an outcome, reasons for that outcome, hard limits and preferences. Capture these separately. “Make the slide concise” expresses a preference; “do not remove the explanation of the trust boundary” protects a teaching outcome. An agent that shortens the slide by deleting that explanation has followed one sentence while violating the actual goal.

Use an intent record containing: desired outcome; audience; authoritative inputs; required behavior; prohibited behavior; authorized side effects; acceptable tradeoffs; completion evidence; and unresolved ambiguity. Do not make every preference a hard blocker. Overblocking can itself frustrate the intended workflow.

## Translate Intent Into Atomic Requirements

An atomic requirement has one observable assertion. Split “make the narration simple, accurate, complete and ready” into separate checks. Assign stable IDs so an instruction, test, failure and repair can refer to the same obligation.

| ID | Requirement | Type | Evidence |
|---|---|---|---|
| R01 | Use the supplied outline revision | Input provenance | File hash and revision |
| R02 | Cover each approved objective | Semantic | Objective-to-evidence map |
| R03 | Preserve frozen files | Mechanical | Before/after hashes |
| R04 | Use the declared word-count policy | Mechanical | Counter configuration and output |
| R05 | Explain each diagram's relationship | Semantic | Spoken explanation and visual reference |
| R06 | Save to the requested destination | Operational | Verified artifact location |
| R07 | Publish only when authorized | Authorization | Task scope plus runtime permission |

“Atomic” does not require one validator per sentence. One validator can check several related requirements, provided failures identify which requirement was violated.

## Track Meaning, Not Just Keywords

For every semantic requirement, record a positive example, a near-miss and a failure. For “explain the diagram,” a positive example names the entities, explains an arrow and connects the relationship to a concrete consequence. A near-miss names the boxes but does not explain the relationship. A failure describes a component absent from the visual.

This supports a reviewer in distinguishing genuine coverage from word overlap. A narration mentioning “latency” is not necessarily teaching how to decide whether a latency increase is acceptable.

## Resolve Conflicts Without Inventing Authority

Start with the host's instruction hierarchy and permissions. Within task-level material, identify which source the user has declared authoritative. Do not apply a universal “newest file wins” rule: a recently edited draft may be less authoritative than an approved outline.

When a current request explicitly changes an earlier preference, record the change. When two mandatory constraints cannot both be satisfied, identify the exact conflict. Continue independent work that does not depend on the resolution, but do not silently choose a policy and call it approved.

An example: a 405-word total and eight reveals capped at 27 words allow at most 216 words if every word must belong to those reveals. This is an infeasible contract, not a writing-quality problem. Calculate the bound before drafting. Multiple beats per slide may resolve it only if the user-approved structure permits them.

## Prevent Requirements From Disappearing

Build a traceability table before execution. Each mandatory requirement must have a location in the procedure and an acceptance check. At completion, every requirement has exactly one outcome: passed, failed, blocked or explicitly not applicable with justification. “Not checked” cannot become “passed.”

After an interruption, resume from a compact state record: contract revision, completed actions, unresolved requirements and evidence paths. Re-read mutable inputs when needed. Do not trust a summary as proof that an external write succeeded.

## Keep an Intent Change Log

Record what changed, who authorized it, affected requirements and tests to rerun. Do not silently redefine success to match an already generated artifact. Changing a word limit should invalidate the old count result; changing an objective should invalidate old coverage evidence.

## Acceptance Does Not Mean Mind Reading

An author may leave expectations unstated. Make reasonable low-risk assumptions explicit and test them against supplied examples. Ask about consequential ambiguity when it changes the output or permitted action. A faithful skill exposes uncertainty rather than hiding it behind confident prose.
