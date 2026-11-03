# Discovery and Activation

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: D1, D2, D3, D4. See the evidence ledger for source status and limitations.

## Q001 Why is my skill not working at all?

Start by identifying the failed boundary: package discovery, invocation, execution, or validation. A wrong final answer alone cannot identify which boundary failed.

**Diagnose:** Record the host, workspace, installed skill path and exact prompt. Look for the skill in the host inventory, then try a harmless explicit invocation and inspect the trace.

**Remedy:** Repair the first failing boundary before rewriting the entire skill. Keep a tiny fixture that produces a verifiable file without external services.

**Verify:** The inventory contains the intended skill, the trace loads that version, and the fixture passes an independent check.

## Q002 Why does explicit invocation work but automatic activation fail?

The workflow may be valid while routing is weak. Treat invocation and task quality as separate evaluations.

**Diagnose:** Compare an explicit invocation with several natural paraphrases and unrelated prompts. Check whether automatic invocation is disabled in that host.

**Remedy:** Describe the actual task, inputs and appropriate situations. Avoid vague descriptions such as general assistant or productivity helper.

**Verify:** Positive paraphrases activate the intended skill and unrelated prompts do not. Record failures separately from output defects.

## Q003 Why is the slash command missing?

A package may be in the wrong scope, use an invalid name, or be unsupported on that product surface. Display conventions differ between hosts.

**Diagnose:** Inspect the installed file tree and parser diagnostics rather than guessing from the source repository. Confirm the command is user-invocable.

**Remedy:** Correct the package layout against the exact host documentation. Restart or reload only when that host requires it.

**Verify:** The host resolves the name to the expected installation; a minimal request succeeds without depending on previous conversation state.

## Q004 Why does the wrong skill activate?

Overlapping descriptions and duplicate names can make routing ambiguous. A broad trigger can match a task it should not handle.

**Diagnose:** Run the same prompt with only the intended skill, then with the normal installed set. Compare loaded names and paths.

**Remedy:** Give neighboring skills distinct responsibilities and explicit exclusions. Keep shared background in references rather than duplicating workflows.

**Verify:** Boundary prompts choose the right workflow; ambiguous prompts request the missing task detail instead of silently selecting a risky action.

## Q005 Why does a skill activate on almost every request?

A skill that claims to apply to everything can intercept unrelated work and add needless cost.

**Diagnose:** Test casual questions, read-only requests and tasks owned by neighboring skills. Inspect automatic-invocation settings.

**Remedy:** Narrow the trigger to observable task intent. Use explicit invocation for workflows that should be deliberately selected.

**Verify:** A negative test suite remains unaffected while relevant requests still activate the skill.

## Q006 Why does adding more skills make an existing skill harder to trigger?

Discovery context is finite and descriptions compete for relevance. Do not assume every installed instruction is fully visible on every turn.

**Diagnose:** Compare a small installed set with the full set using identical prompts. Inspect any host diagnostics for omitted descriptions.

**Remedy:** Remove redundant skills, shorten metadata and retain discriminating task language. See the platform notes for host-specific listing behavior.

**Verify:** Measure activation recall and false positives before and after the change; do not accept a single successful demonstration as proof.
