# Long Tasks and Skill Composition

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: D1; existing community ledger includes recursive-wrapper reports. See the evidence ledger for source status and limitations.

## Q031 Why does the skill stop working after a long conversation?

The active context, task assumptions and available tools can change. Compare evidence before attributing the behavior to forgetting.

**Diagnose:** Capture the last correct action, any context reduction and the first deviation. Compare with a fresh-session replay.

**Remedy:** Keep a durable task checkpoint containing requirements, artifact versions, completed work and next actions. Use host-specific restoration when needed.

**Verify:** Resume from the checkpoint and verify that remaining requirements are enforced without repeating completed side effects.

## Q032 Why does clearing the chat change results?

A previous session may contain examples, permissions or decisions missing from a fresh session. Some variation remains even with similar inputs.

**Diagnose:** Replay the minimal task in a fresh session using only the documented prerequisites. Record the full initial conditions.

**Remedy:** Move required task state into explicit inputs instead of relying on accidental conversation history.

**Verify:** Multiple fresh-session runs satisfy the contract; failures are preserved as regression cases rather than explained away.

## Q033 Why does combining two good skills produce a bad result?

Individually useful workflows can impose contradictory output formats, stop conditions or ownership of the same action.

**Diagnose:** Compare their requirement ledgers and identify shared resources and incompatible steps.

**Remedy:** Define one orchestration contract with clear handoffs. Use each skill only for the responsibility it owns.

**Verify:** Test each skill alone and together; the combined run preserves both necessary constraints without duplicate writes.

## Q034 Why does one skill repeatedly invoke itself?

A wrapper or routing rule can create a cycle. The recursion may be indirect through another workflow.

**Diagnose:** Trace invocation names and parent-child relationships. Identify the smallest repeated cycle.

**Remedy:** Remove the cycle in source configuration and add a bounded handoff rule. Avoid treating edits to generated caches as a durable fix.

**Verify:** A regression prompt terminates with one intended execution path and a clear final state.

## Q035 Why does an unrelated installed skill influence my output?

Overbroad instructions or incidental context may cross task boundaries. Diagnose with controlled changes rather than assuming malicious behavior.

**Diagnose:** Repeat the same fixture with the suspect skill disabled, keeping other settings fixed.

**Remedy:** Constrain scope and place reusable style or policy rules at the appropriate host-supported level. Separate task-specific content.

**Verify:** Negative tests show unrelated requests retain their intended behavior with the normal installed set.

## Q036 Why does a subagent miss the parent skill rules?

A delegated worker may receive a different context or tool set. Parent visibility does not prove child visibility.

**Diagnose:** Inspect the actual handoff payload and child capabilities when available. Identify missing requirements and output expectations.

**Remedy:** Pass a compact explicit subtask contract, required sources and return schema. Keep final acceptance owned by the orchestrator.

**Verify:** A child output missing a required field or proof is rejected before the parent presents it as complete.
