# Failure Recovery and Idempotency

Status: original operational design guidance. Adapt to the actual service API and transaction model; do not assume all tools support idempotency keys.

## Classify the Failure Before Retrying

| Failure | Safe first response | Why |
|---|---|---|
| Input missing | Identify the exact missing input | Repeating cannot create authorization or facts |
| Validation failure | Repair the failed property | Re-running the same draft changes nothing |
| Authentication denied | Report access requirement | Do not seek alternate credentials |
| Rate limit | Follow documented retry guidance within budget | Immediate retries may worsen it |
| Timeout before known completion | Inspect resulting state | The action may already have succeeded |
| Partial multi-file write | Inventory completed writes | Avoid duplicate or inconsistent artifacts |
| Concurrent edit | Read current version and reconcile | Old evidence may no longer apply |
| Irrecoverable dependency error | Preserve draft and report blocker | Endless retries hide the problem |

## Idempotency Means Repeated Intent Has One Effect

For creation operations, use a service-supported idempotency key or a stable operation identifier when available. Without one, a carefully scoped lookup may determine whether the intended object already exists. A matching title alone is often insufficient: two legitimate objects can have the same title.

Do not promise exactly-once execution just because retries are disabled. A crash can leave the outcome unknown. The operational objective is to identify and reconcile the actual state, and avoid uncontrolled duplicate effects.

## Stage, Validate, Commit, Verify

Prepare an artifact in a temporary location. Validate it. Commit it to the requested destination using the service's supported atomic/versioned operation where possible. Verify the resulting object and preserve its identifier. For non-atomic operations, explicitly model partial completion.

Atomic rename is useful for a local file on a compatible filesystem; it does not make a sequence of unrelated remote API calls atomic. State that boundary in the workflow.

## Compensation Is Not Blind Undo

If a workflow creates a draft and later fails, deleting that draft may be appropriate only if its ownership and state are known and deletion is authorized. Do not revert changes made concurrently by someone else. Prefer version-aware recovery and a clear report of residual state.

## Retry Budget

Specify maximum attempts and maximum elapsed time. Each retry needs a reason: new input, fixed dependency, changed artifact or a transient failure with a documented retry path. Stop when the budget is exhausted. Record what remains safe to resume.

## Resume Record

Persist task ID, contract revision, artifact hashes, completed external object IDs, unresolved checks and next safe action. Exclude credentials. On resumption, verify mutable state instead of blindly replaying all commands.

## Example: Public Repository Publication

Creating a repository, uploading files and verifying the default branch are separate actions. If repository creation succeeds but upload fails, retain the repository URL and resume upload after inspecting its contents. Do not create a second repository. If authentication is absent, complete local preparation and accurately report publication as blocked.
