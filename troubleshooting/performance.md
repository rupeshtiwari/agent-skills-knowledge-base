# Slowness Cost and Context

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: C3; recommendations here are our own diagnostic procedures. See the evidence ledger for source status and limitations.

## Q013 Why is my skill slow?

Elapsed time includes model turns, tool execution, network waiting, retries and user approvals. A large prompt is only one candidate cause.

**Diagnose:** Timestamp invocation, first tool, each slow operation and completion. Count calls, retries and transferred bytes on the same representative task.

**Remedy:** Optimize the largest measured component first. Keep a quality gate while reducing unnecessary work.

**Verify:** Compare repeated runs with the same workload and report latency with sample count and success rate; faster failed runs are not an improvement.

## Q014 Why does loading a skill consume so much context?

A workflow may load manuals, examples and unrelated branches before it knows which branch is needed.

**Diagnose:** Inventory what actually entered context, including tool output. Compare it with the material used to make decisions.

**Remedy:** Create a short routing entry point and load references by task. Replace bulk dumps with targeted reads and machine-readable summaries.

**Verify:** Record loaded bytes or tokens where available and verify the reduced context still supports the same successful outputs.

## Q015 Why does the agent keep searching or reading the same files?

It may lack a stopping rule, lose prior findings, or receive changing inputs. Repetition alone does not establish a model defect.

**Diagnose:** List repeated calls with arguments, results and timestamps. Determine whether each repetition obtained new evidence.

**Remedy:** Maintain a small evidence index with freshness conditions. Reuse unchanged results and define what uncertainty still warrants a new lookup.

**Verify:** An unchanged-input run avoids redundant reads; a changed-source case correctly refreshes evidence rather than blindly caching it.

## Q016 Why does excessive verification make the workflow slower?

Multiple checks may measure the same property or repeat after no relevant change. Some checks are essential, others add little coverage.

**Diagnose:** Map each check to the failure it detects and the artifact revision it covers. Identify duplicated checks and missing important ones.

**Remedy:** Run targeted checks after edits and a bounded final gate. Re-run when inputs change or a failure raises a new question.

**Verify:** Show that known defects are still caught and that repeated unchanged checks no longer dominate execution time.

## Q017 Why do parallel agents or tools not make it faster?

Dependency chains, startup overhead, shared-resource contention and reconciliation can outweigh parallel execution.

**Diagnose:** Draw the task dependencies and measure worker setup, useful work and merge time. Check for overlapping edits.

**Remedy:** Parallelize independent reads or isolated artifacts only when supported and authorized. Keep dependent mutations sequential.

**Verify:** Wall-clock time improves without conflicts, duplicated work or weakened evidence; otherwise retain the simpler sequential flow.

## Q018 Why do token costs grow even when the answer is short?

The final answer is only part of the workload. Intermediate reasoning, repeated context, tool payloads and retries may dominate metered usage.

**Diagnose:** Use provider usage records where available and track tool calls separately. Do not estimate billed cost from visible answer length alone.

**Remedy:** Bound output from tools, remove redundant context and avoid retry loops. Cache only when authorization and freshness permit.

**Verify:** Compare actual usage for equivalent successful tasks and document which billing fields are included or unavailable.
