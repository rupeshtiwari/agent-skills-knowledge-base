# Tools Scripts and Environment

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: D2; use the linked engineering chapters for implementation details. See the evidence ledger for source status and limitations.

## Q025 Why does the skill describe a tool the agent cannot call?

Instructions do not install a connector or grant access. A tool may be unavailable on that host or session.

**Diagnose:** Compare the required tool contract with the active tool inventory and enabled integration settings.

**Remedy:** Add a preflight capability check and a supported fallback. Report a concrete missing capability instead of inventing execution.

**Verify:** Disable the required tool in a test: the workflow stops or follows the documented fallback without claiming the original action happened.

## Q026 Why does a script work in my terminal but fail inside the agent?

The shell, working directory, PATH, interpreter or environment can differ.

**Diagnose:** Capture a sanitized runtime fingerprint and the actual stderr and exit code. Reproduce using the same invocation and working directory.

**Remedy:** Use explicit runtime requirements, resolve resources from the package root and fail with actionable dependency errors.

**Verify:** Run from an unrelated working directory in a clean environment; the script either succeeds or names the exact missing prerequisite.

## Q027 Why are reference files not read?

A link is not proof that its target is packaged, accessible or needed at the right time.

**Diagnose:** Check the installed reference path and trace whether it was opened before a dependent decision.

**Remedy:** State when each reference is needed and what decision it supports. Keep references close to the entry point and avoid circular navigation.

**Verify:** A task requiring a unique reference fact uses the correct source; a task not needing it avoids unnecessary loading.

## Q028 Why are arguments passed incorrectly to scripts?

Host placeholder substitution, shell parsing and application parsing are different layers. Spaces and special characters expose weak assumptions.

**Diagnose:** Test a harmless argument containing spaces, Unicode and punctuation. Inspect the resulting argument array rather than a printed command string.

**Remedy:** Prefer structured tool arguments or a JSON input file. Validate allowed values and avoid assembling executable shell text from untrusted inputs.

**Verify:** Fixtures preserve literal values and reject invalid inputs without executing injected commands.

## Q029 Why does the agent claim it ran tests when it did not?

Narrative claims are not execution evidence. It may have confused an intended action with a completed one.

**Diagnose:** Require the command, exit status, relevant output and artifact revision. Check that the trace contains the execution event.

**Remedy:** Generate test summaries from runner results. Represent not-run, failed and blocked as separate states.

**Verify:** A run with the test tool disabled cannot produce a passing test record.

## Q030 Why does a successful tool exit still produce a broken artifact?

Exit zero may mean a process completed, not that its result satisfies the task contract.

**Diagnose:** Open the produced file or read back the remote state. Check content, schema and user-visible behavior rather than only existence.

**Remedy:** Validate the output after creation and bind validation to the exact revision delivered.

**Verify:** A deliberately empty, stale or malformed artifact fails even when the generator exits successfully.
