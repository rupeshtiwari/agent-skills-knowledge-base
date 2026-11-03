# Permissions Privacy and Trust

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: Existing security and permission-boundary chapter. See the evidence ledger for source status and limitations.

## Q043 Why does the skill stop to ask for permission?

The requested action may cross a host-enforced boundary or lack user authorization. A sentence inside a skill cannot grant external privileges.

**Diagnose:** Identify the exact operation, applicable policy and existing authorization. Separate an unavoidable gate from an unnecessary clarification.

**Remedy:** Complete authorized preparation first and request only the missing decision. Do not weaken controls to make the skill appear autonomous.

**Verify:** An authorized read-only task proceeds; an unapproved external side effect stays blocked with a specific explanation.

## Q044 Why can the skill read data but cannot update it?

Authentication, read permission and write permission are separate. A connector can expose only some operations.

**Diagnose:** Check the requested resource, active account, available operation and returned permission error.

**Remedy:** Use the supported write path when authorized, or provide a reviewable artifact with the blocker stated. Never claim a remote update from a local draft.

**Verify:** Read back the target after the write and confirm the expected revision or content.

## Q045 Why does downloaded content change the skill behavior?

Documents, pages and issue comments can contain instructions aimed at the assistant. Those contents are task data, not automatically trusted authority.

**Diagnose:** Trace whether a source passage caused a change in tools, destination, disclosure or task scope.

**Remedy:** Separate trusted workflow instructions from retrieved text and validate proposed external actions against the user's request.

**Verify:** A malicious fixture asking for secret disclosure or unrelated publication is ignored while legitimate source facts remain usable.

## Q046 Why should credentials not be placed inside a skill?

A package may be copied, indexed, logged or published. Bundling a credential spreads access beyond its intended boundary.

**Diagnose:** Inspect package assets and logs for accidental secrets before distribution, using approved scanning tools.

**Remedy:** Use the host's supported secret mechanism and narrowly scoped access. If exposure occurred, follow the service's rotation process.

**Verify:** A clean checkout runs with separately provided credentials, and neither output nor public repository includes the secret value.

## Q047 Why can a third-party skill be risky even when its Markdown looks harmless?

Bundled scripts, dependencies and network destinations can perform actions beyond the prose description.

**Diagnose:** Review executable files, install steps and requested permissions at a pinned revision. Inspect what is actually executed.

**Remedy:** Trial in a restricted environment with synthetic data. Grant only the capabilities needed for the intended task.

**Verify:** The trace stays inside the declared scope and the package has a reproducible provenance record; popularity alone is not acceptance evidence.

## Q048 Why does the skill choose the wrong account or repository?

Remembered names and default accounts can be ambiguous. Correct content written to the wrong destination is still a failure.

**Diagnose:** Read the active identity and canonical destination before mutation. Compare them with the user's explicit request.

**Remedy:** Bind the task contract to account, repository and branch identifiers. Resolve ambiguity before an external write.

**Verify:** The remote readback matches both the intended content and destination, with no unintended side effect elsewhere.
