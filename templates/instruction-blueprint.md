# Educational Instruction Blueprint

This is a design outline, not an installable SKILL.md or a production-ready skill. Populate the worksheet and validate against the target host before turning it into a package.

## Metadata to Define

Name: one specific task. Description: what it does, when it should activate and the most important exclusion. Compatibility: actual runtime requirements. Use the current Agent Skills specification and document host-specific additions separately.

## Task Contract

Identify required inputs and their source of truth. Specify the output, allowed changes and success criteria. Do not assume missing inputs exist.

## Procedure

1. Read and validate the task inputs.
2. Resolve the relevant reference documents.
3. Check environment and tool prerequisites.
4. Execute only the authorized task.
5. Validate the saved artifact or final external state.
6. Repair a demonstrated failure within the stated budget.
7. Deliver the result with concise evidence and unresolved limitations.

## Branches to Define

Missing input; conflicting requirements; unavailable tool; partial success; timeout; failed validation; exhausted retry budget.

## References to Package

Only domain-specific facts and procedures that the model needs. Explain which branch reads each file. Keep large source collections in the knowledge base and retrieve selectively.

## Release Evidence

Record task cases, run traces, validator outputs, human review where needed, and baseline comparison. Do not call the skill reliable solely because this outline is complete.
