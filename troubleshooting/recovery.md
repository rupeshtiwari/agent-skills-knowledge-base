# Failures Retries and Recovery

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: Existing recovery and idempotency chapter. See the evidence ledger for source status and limitations.

## Q049 Why does retrying create duplicate posts files or records?

A timeout does not reveal whether a write completed. Replaying it blindly can duplicate a successful operation.

**Diagnose:** Check the destination for an operation identifier or expected artifact before retrying.

**Remedy:** Use idempotency keys where supported, or a read-before-retry reconciliation strategy. Keep a durable operation ledger.

**Verify:** Simulate a lost response after a successful write; recovery detects the existing result and does not create a second one.

## Q050 Why does the skill loop forever trying to fix an error?

A retry policy may lack a maximum, or each attempt may repeat the same failing assumption.

**Diagnose:** Record error classes and changes between attempts. Distinguish transient network errors from invalid inputs or missing permissions.

**Remedy:** Set bounded retries with backoff only for retryable failures. Stop with the smallest useful diagnostic when the condition cannot improve.

**Verify:** A persistent failure terminates within the declared budget; a transient failure can recover without exceeding it.

## Q051 Why does a partially completed run start from scratch?

Completion state may exist only in conversation text, with no reliable mapping to artifacts.

**Diagnose:** Inventory completed side effects, outputs and their hashes. Identify which steps are safe to rerun.

**Remedy:** Checkpoint at meaningful boundaries and reconcile real state on resume. Do not trust an old checkbox without checking its artifact.

**Verify:** An interrupted run resumes remaining work and revalidates dependent outputs without repeating completed external actions.

## Q052 Why does rollback restore files but not the system?

External writes, database changes or notifications may lie outside a file-based rollback.

**Diagnose:** List every side effect and whether it is reversible, compensatable or irreversible.

**Remedy:** Plan recovery before execution. Use transactions where supported and explicit compensating operations where appropriate.

**Verify:** A rehearsal verifies the target end state, not just that a rollback command returned success.

## Q053 Why does a temporary outage become a permanent task failure?

The workflow may treat all errors identically or discard useful intermediate work.

**Diagnose:** Capture response status, retry hints and whether the last operation mutated anything. Preserve completed evidence.

**Remedy:** Classify failures, retry safe transient operations within a budget and retain a resumable checkpoint when blocked.

**Verify:** Recovery handles an injected outage and reports unresolved work accurately rather than marking the entire run complete.

## Q054 Why does the agent silently substitute a different tool or method?

A fallback may preserve superficial output while changing required provenance, privacy, semantics or accuracy.

**Diagnose:** Compare the requested method with the trace and identify which guarantees the replacement changes.

**Remedy:** Define allowed fallback conditions and their validation requirements. Ask when a substitution changes a material user constraint.

**Verify:** A prohibited substitution is blocked; an allowed fallback reports its use and passes the appropriate checks.
