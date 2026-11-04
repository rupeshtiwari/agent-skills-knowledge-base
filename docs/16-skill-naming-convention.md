# Skill Naming Convention

Use two deliberately different forms: **Title Case for the visible skill title**, and **lowercase words separated by hyphens for the machine identifier**. A display-title cleanup should not break working commands.

This repository's visible-title and family-label policy is an engineering convention. The portable identifier constraints come from the [Agent Skills specification](https://agentskills.io/specification). Host discovery and installation remain separate concerns.

## Visible Titles

Use a consistent family label followed by a clear responsibility. Capitalize significant words, preserve brand spelling and standard acronyms, and avoid camelCase, raw command strings or inconsistent sentence casing.

| Avoid | Use |
| --- | --- |
| Pluralsight course orchestrator | Pluralsight Course Orchestrator |
| fsm ps create outline | Pluralsight Outline Builder |
| Pluralsight Slide Deck builder | Pluralsight Slide Builder |
| Apply Rupesh Teaching Style | Pluralsight Narration Builder |
| fsm coursera outline technical review | Coursera Document Reviewer |

These are display titles. The narration title describes its production role; its instructions still preserve Rupesh's teaching style. Keep unrelated domains in their own families rather than labeling every skill Pluralsight.

## Machine Identifiers

Use a short, specific identifier containing lowercase letters, digits and single hyphens. Keep it within 64 characters. Do not use spaces, underscores, camelCase, leading/trailing hyphens or repeated hyphens. Prefer an action-oriented name with a useful family prefix, such as `ps-create-outline` or `coursera-doc-review`.

Descriptions must explain both the task and when to activate it; naming alone cannot establish correct routing. Keep the description within the applicable host/specification limit.

### Established Course-Skill Mapping

Preserve these existing identifiers for compatibility:

| Visible title | Exact machine identifier | Responsibility |
| --- | --- | --- |
| Pluralsight Course Orchestrator | `ps-course-orchestrator` | Coordinate stages, handoffs, evidence and acceptance |
| Pluralsight Outline Builder | `ps-create-outline` | Research, outline authoring and outline validation |
| Pluralsight Repository Builder | `ps-course-repo-builder` | Learner demos, implementation, repositories and production Studios |
| Pluralsight Slide Builder | `ps-build-slide-deck` | Slide content, layouts, diagrams and visual validation |
| Pluralsight Narration Builder | `ps-apply-rupesh-teaching-style` | Spoken teaching, ElevenLabs input and narration validation |

This mapping defines names and responsibilities; it does not certify that every package is installed or every stage has passed. The orchestrator must resolve the actual packages and revisions before dependent execution.

## Safe Renaming

1. Inspect the actual package identity and current frontmatter, display metadata, default prompt and callers
2. Prefer a display-title update when the machine identifier is already valid
3. Keep the default prompt's `$skill-name` and orchestrator routing aligned with the exact machine identifier
4. If an identifier change is explicitly needed, update active callers, metadata, scripts, manifests and release locks; test the affected workflow and record its migration
5. Preserve managed package directory IDs; do not create a second package just to change the title
6. Save through the host's supported workflow and read back the saved result before reporting success

A portable authored package normally has a folder matching its machine name. A host-managed installation may store it under a generated package ID; do not rename that managed folder to imitate a portable example.

## Duplicate Detection

The same skill can appear under **Installed** and **Created by me**. Those are different views and do not by themselves prove duplicate packages.

Compare exact package identities, names, inputs, outputs and responsibilities. Two separate reviewer packages may overlap even when their names differ. Preserve necessary validation and independent review in the responsible workflow before removing redundant packaging. Deleting a reviewer skill must not turn self-review into independent acceptance.

## Creation and Maintenance Checklist

- [ ] Visible title uses consistent Title Case and the correct family label
- [ ] Machine name is valid, specific and unique
- [ ] Description states task, trigger and relevant exclusions
- [ ] Default prompt mentions the exact `$skill-name`
- [ ] Orchestrator names resolve to the intended child packages
- [ ] A title-only rename preserves existing command identifiers
- [ ] Identifier migrations update active dependencies and course locks
- [ ] Managed directory identities and unrelated skills remain intact
- [ ] Required children are available; missing or review-pending children are reported
- [ ] Metadata, local links and affected behavior are validated
- [ ] The saved result is read back; unavailable checks are not claimed as passed

Apply this checklist during creation, updates, renaming and release reviews. For broader workflow design and testing, use the [skill-building guide](15-skill-building-guide.md).
