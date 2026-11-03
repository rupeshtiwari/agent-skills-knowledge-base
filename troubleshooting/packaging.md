# Packaging Installation and Updates

[All questions](README.md) · [Evidence and platform notes](evidence.md)

**Scope:** Original diagnostic guidance. Each proposed remedy must be tested in your own environment. Related evidence: D2, D3, D4; C4 and C5 describe narrow reports. See the evidence ledger for source status and limitations.

## Q019 Why is a valid-looking SKILL.md rejected?

Human-readable Markdown can still have invalid frontmatter, naming or packaging. Host extensions can impose additional constraints.

**Diagnose:** Validate the actual installed bytes, filename case, directory nesting and metadata types. Compare with the standard and host documentation.

**Remedy:** Start from a minimal valid package, then add fields one at a time. Do not copy unsupported metadata from another product.

**Verify:** The target host discovers the package and reads its metadata without parser warnings.

## Q020 Why does installation report success but the host cannot find the skill?

An installer can finish without proving that every intended destination was populated. Different shells, users or scopes may resolve different paths.

**Diagnose:** Inspect destination files under the account that launches the host. Compare hashes with the intended source and check the host inventory.

**Remedy:** Correct the destination or supported installation route. Preserve local edits before replacing files; avoid blind mirror commands.

**Verify:** Verify content parity and discovery for every target host rather than trusting only an installer exit code.

## Q021 Why does the old version still run after an update?

A second installation, cached session or pinned plugin revision can retain old behavior.

**Diagnose:** Record the loaded path and hash, not merely the repository's latest commit. Search authorized installation scopes for duplicates.

**Remedy:** Update the canonical source and use the host's supported refresh path. Remove an obsolete copy only after confirming ownership and need.

**Verify:** A new run exposes the expected version and the old regression case changes as predicted.

## Q022 Why do two copies of the same skill behave differently?

Names can match while scripts, references, metadata or dependencies differ.

**Diagnose:** Compare the entire package manifest, including referenced assets and runtime versions. Check whether scope precedence selects a different copy.

**Remedy:** Establish one versioned source of truth and documented distribution steps. Keep explicit compatibility adaptations separate.

**Verify:** A clean install produces the same package hashes and passes the same fixture suite on each supported surface.

## Q023 Why does the skill work locally but not in a cloud agent?

Local files, credentials, binaries and personal configuration may not exist remotely. Cloud sync is a separate boundary.

**Diagnose:** Inspect the cloud run's checkout, installed package, tool inventory and account permissions. Compare with local prerequisites.

**Remedy:** Bundle permitted dependencies or provision them through supported configuration. Use repository-relative resources where appropriate.

**Verify:** A fresh cloud environment passes preflight without borrowing undeclared state from the author's computer.

## Q024 Why is cloud skill sync stuck at zero items?

The sync source may contain no eligible folders, unsupported links or an incomplete package. Vendor defects are also possible.

**Diagnose:** Check real directories versus symlinks and the exact source selected for sync. Read the vendor-specific evidence note before changing layout.

**Remedy:** Use the currently supported folder arrangement and preserve a backup. Do not treat a spinner as evidence that files were deleted.

**Verify:** The destination contains the expected package and a new cloud run discovers it; UI completion alone is insufficient.
