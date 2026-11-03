# Context, Composition and Instruction Conflicts

Status: engineering synthesis informed by [context research](../research/README.md) and [platform documentation](../platforms/README.md). Host behavior varies; no universal loading mechanism is assumed.

## Choose One Owner for Each Output

When multiple skills contribute, assign one workflow responsibility for the final artifact and acceptance decision. Supporting skills may provide domain checks or formatting, but should not each regenerate the whole output. Multiple writers can introduce conflicting edits and erase evidence.

## Define Interfaces Between Skills

Specify the input artifact, schema, expected output and error status. A review skill should return findings rather than silently rewrite files unless authorized. A rendering skill should not change the approved learning objectives. A publisher should consume a validated artifact, not reinterpret its content.

Interfaces are useful even when one agent performs every step. They separate responsibilities and make defects easier to locate.

## Avoid Circular Dependencies

Skill A should not invoke Skill B merely to have B invoke A again. Document dependency direction. Guard repeated calls with task IDs or explicit state where the host supports it. Prefer direct reference loading when the need is information rather than a separate workflow.

## Keep a Small Working Set

Retrieve only the governing references for the current stage. Keep a concise task ledger with contract version, invariant constraints, completed work and unresolved issues. Do not copy the entire knowledge base into every skill.

A dense repository is useful as a reference collection; a dense runtime prompt can be counterproductive. Optimize the amount of relevant, discriminating information rather than raw word count.

## Interruption and Compaction

Treat context summaries as navigation aids. Before modifying a frozen file or external object, inspect its current state. Preserve exact identifiers and hashes outside conversational memory. Resume from evidence, not an assistant's earlier statement that everything passed.

## Detect Conflicting Rules

Create a conflict inventory for duplicated numerical policies, incompatible output formats, overlapping scopes and contradictory approval requirements. Resolve them at the source. A main skill that repeats obsolete requirements from a reference creates two authorities that can drift.

## Composition Tests

Run each skill independently, then together on tasks that require both. Check that adding the formatting skill does not remove technical evidence, and adding a review skill does not unexpectedly publish. Measure cost: a composition can be correct but unreasonably slow.

## When Not to Add Another Skill

Use a direct tool or small script when the procedure is deterministic and well-defined. Use a one-time prompt for a one-off request without reusable structure. Use a reference document for facts that do not need procedural behavior. New skills are justified by a repeatable workflow and measured benefit, not by the availability of another instruction file.
