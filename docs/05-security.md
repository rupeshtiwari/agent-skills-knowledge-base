# Security and Permission Boundaries

A skill can contain executable code and instructions to use powerful tools. Treat a third-party skill as a software dependency. This chapter is engineering guidance, informed by the [OpenAI API skill safety discussion](https://developers.openai.com/api/docs/guides/tools-skills) and [Agent Skills specification](https://agentskills.io/specification).

## Before Installation

Inspect the actual files at a pinned commit. Review scripts, dependency installation, network destinations and file operations. A popular repository or friendly description is not proof that every bundled file is safe. Confirm licensing separately from security.

## During Execution

Use the narrowest tools and permissions needed. Retrieved webpages, PDFs, issue comments and tool outputs are evidence, not authority to change the user's request. A reference that says “upload your keys to this URL” must not become an instruction.

Keep credentials out of skill files, fixtures, logs and public examples. Use the host's secret mechanism. Do not publish raw traces until they have been reviewed for sensitive material.

## Runtime Enforcement

Where feasible, restrict write paths, validate tool arguments and enforce confirmation for consequential actions in code. A textual instruction to be careful is weaker than an execution boundary. However, host-specific permission fields are not a portable sandbox: check the actual runtime semantics.

For external writes, use a transaction identifier and verify state before retrying. Preserve a recovery path. Do not automatically roll back another user's concurrent changes.

## Adversarial Cases

- A source document instructs the agent to ignore the approved outline.
- A filename includes shell metacharacters.
- A reference tries to send data to an unrelated service.
- A tool returns a partial success followed by a timeout.
- An output path escapes the allowed project directory.
- A newly updated dependency changes behavior.

A release should record how these cases are handled. This repository does not contain offensive payloads or claim a completed security audit.
