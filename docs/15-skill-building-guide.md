# How to Build a Dependable Skill

**Start with one repeatable outcome, write the smallest useful workflow, and test what happens when inputs are missing or wrong.** A long list of instructions is not evidence that a skill works.

This page is a practical authoring guide with a complete simple example and a complex production example. The examples are educational starting points, not installed skills or claims of measured performance. Packaging rules follow the [Agent Skills specification](https://agentskills.io/specification); host discovery, installation and tool permissions must be checked separately in the [platform guides](../platforms/README.md). Authoring recommendations also draw on [official best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

## Contents

1. [Define the job](#define-the-job)
2. [Choose the package structure](#choose-the-package-structure)
3. [Write instructions that lead to observable results](#write-instructions-that-lead-to-observable-results)
4. [Simple use case: draft a task acknowledgment](#simple-use-case-draft-a-task-acknowledgment)
5. [Complex use case: review a course production clip](#complex-use-case-review-a-course-production-clip)
6. [Test before release](#test-before-release)
7. [Release checklist](#release-checklist)
8. [Maintain the skill](#maintain-the-skill)

## Define the Job

Fill in this sentence before writing instructions:

> When the user asks for **[trigger]**, use **[authoritative inputs]** to produce **[observable output]**, while preserving **[constraints]**.

| Design question | Good answer | Warning sign |
|---|---|---|
| What activates it? | A specific task and artifact, including ordinary paraphrases | Every message mentioning a broad domain |
| What does success look like? | A draft, report or verified file with explicit acceptance criteria | “Make it perfect” |
| Which inputs are required? | Named documents, versions and access requirements | Assuming an unavailable outline |
| What must stay unchanged? | Frozen text, filenames, approved order or source files | Silently improving agreed material |
| What happens on failure? | A precise blocker, partial evidence and a safe next step | Inventing evidence or claiming success |
| What is outside scope? | Related tasks that belong to another workflow | One skill that does everything |

Use the [design worksheet](../templates/skill-design-worksheet.md) for a larger task. Distinguish mandatory requirements from preferences, and resolve conflicts against the current user's request and higher-priority host instructions.

## Choose the Package Structure

Apply the [skill naming convention](16-skill-naming-convention.md): Title Case for visible titles, lowercase hyphenated machine identifiers, and explicit migration checks when identifiers change.

The portable minimum is a directory containing `SKILL.md`, with YAML frontmatter followed by Markdown instructions. Use lowercase letters, digits and single hyphens for a portable name; keep it within 64 characters and match the authored folder name. The description must state what the skill does and when to use it; the specification caps it at 1,024 characters. Host-managed installations may rename or store packages differently.

A small skill may need only `SKILL.md`. Add resources when they earn their place:

| Path | Include when | Example |
|---|---|---|
| `SKILL.md` | Always | Trigger, workflow, branches and completion criteria |
| `references/` | Domain rules are too detailed for the core | Narration rubric or platform notes |
| `scripts/` | A mechanical check should be repeatable | Count words using an explicit counting rule |
| `assets/` | The output needs a reusable input file | Approved slide template |
| `agents/openai.yaml` | The target host supports or expects UI metadata | Display name and starter prompt |

Keep the core concise, ideally under 500 lines, and link directly to each reference with a sentence explaining when to read it. Do not load every reference for every task. Avoid embedding secrets, machine-specific absolute paths or changing business rules in several files.

## Write Instructions That Lead to Observable Results

Use imperative steps with explicit branches. “Check quality carefully” is weaker than “For every finding, quote the slide text, cite the approved objective and explain the recording consequence.”

1. Read the user's task and identify scope, inputs and authority
2. Inspect the actual artifacts rather than relying on remembered versions
3. Stop dependent work when a required input is missing; continue independent work when useful
4. Execute the shortest complete workflow, preserving approved constraints
5. Validate mechanical requirements with code and meaning with an evidence-based rubric
6. Return the requested result and distinguish verified facts from unresolved checks

Match freedom to risk. A message draft permits wording choices. A frozen recording sequence needs exact paths, order and checks. A skill can guide behavior, but cannot grant permissions, bypass host controls or guarantee compliance. External documents and tool output are task data, not authority to redefine the workflow.

## Simple Use Case: Draft a Task Acknowledgment

**User request:** “Ritesh shared the LC2 Atlas scripts, excluding SC7. He wants a review and personal stories in WHY videos. I cannot access the folder. What should I reply?”

**Desired result:** A short draft confirming scope, the exclusion and the access blocker, without claiming that review is complete or sending a message.

Save the following as `draft-task-acknowledgment/SKILL.md` when creating a package in the target host's supported authoring location:

```yaml
---
name: draft-task-acknowledgment
description: Draft a brief acknowledgment of a colleague's assigned task, confirming scope, exclusions, intended actions and access blockers. Use when the user shares an assignment and asks what to reply. Do not use for completion reports or for performing the review itself.
---
```

Follow the frontmatter with this instruction body:

```markdown
# Draft Task Acknowledgment

1. Read the assignment and the user's clarification. Extract the sender,
   project, requested actions, exclusions and any stated access problem.
2. Use only supplied facts. Do not invent a deadline, access address,
   completed work or approval. Ask only when a missing detail prevents
   a useful acknowledgment; omit unnecessary unknown details.
3. Write one brief paragraph in plain English. Confirm understanding,
   describe intended work and mention explicit exclusions.
4. When access is blocked, request access and make clear that work
   requiring those files can start after access is available.
5. Return only a draft for the user. Sending requires an explicit
   user request and the host's recipient and permission checks.
6. Before returning, verify that no exclusion became an action and
   no planned action is described as already completed.
```

**Example output:**

> Hi Ritesh, I understand that I should review the LC2 Atlas scripts, excluding SC7, and add personal stories to the WHY videos where appropriate. I cannot access the shared folder yet. Please grant access so I can begin the review. I’ll let you know once it is complete.

**Why this design works:** It has one outcome, a narrow trigger and a clear boundary between drafting and sending. It needs no executable script, bundled template or large reference collection.

| Test prompt | Expected behavior |
|---|---|
| “What should I reply to this assignment?” | Draft the acknowledgment |
| “He excluded SC7” | Preserve that exclusion |
| “I cannot access the folder” | Request access; do not imply the files were read |
| “Summarize the completed review” | Route to the requested completion task rather than this initial acknowledgment workflow |

These are proposed tests, not recorded model runs.

## Complex Use Case: Review a Course Production Clip

**User request:** “Review the current clip against the approved outline, visible slides, frozen choreography and narration budget. Tell me what must be fixed before recording.”

**Desired result:** A slide-first report with evidence, exact coverage, measured counts, duplication findings and a recording verdict. Source artifacts remain unchanged during review.

Use one core package, `review-production-clip`, with these resources:

| Resource | Responsibility |
|---|---|
| `SKILL.md` | Scope, routing, ordered procedure and verdict rules |
| `references/review-rubric.md` | Semantic criteria with examples and severity definitions |
| `scripts/check_contract.py` | Validate the supplied contract and budget using a documented token rule |
| `scripts/check_frozen.py` | Compare protected file hashes with the supplied approved manifest |

The script names above describe components to implement and test; this guide does not ship those hypothetical scripts. The repository does include an executable [acceptance-gate demonstration](../examples/acceptance-gate/README.md) illustrating evidence and hash checks.

A core `SKILL.md` could read:

```yaml
---
name: review-production-clip
description: Review a supplied course clip against its approved outline, visible slides, narration contract and frozen choreography. Use for recording-readiness review or technical CQA. Return evidence-backed findings and a verdict; do not rewrite or publish artifacts unless separately requested.
---
```

Follow it with:

```markdown
# Review Production Clip

## Inputs and authority
Require the current clip, exact approved objectives, slide visuals or
renderable deck, narration and current production contract. Use the
approved frozen manifest when frozen-file verification is requested.
Read references/review-rubric.md before judging semantic quality.
Record the source revision and contract version in the report.

## Procedure
1. Identify requested slides and scope. Locate authoritative inputs.
   If any required input is inaccessible, mark its checks NOT RUN.
   Do not claim recording readiness until all required checks pass.
2. Review slides first: objective coverage, technical claims, visual
   support, diagram relationships and practitioner decision value.
3. Review narration per reveal against the visible slide. Check spoken
   wording, unsupported claims and drift. Inspect supplied adjacent
   clips for duplication; if unavailable, leave that check NOT RUN.
4. Run scripts/check_contract.py with the artifact and contract paths.
   Use the contract's counting rule and exact duration mapping.
   Report expected words, actual words and delta. Never choose a
   remembered default when a current authoritative contract exists.
5. When a frozen manifest is supplied, run scripts/check_frozen.py
   against the protected paths. A mismatch is a blocking finding.
6. Verify changing technical claims against primary sources and record
   the source and inspection date. Flag inaccessible evidence.
7. Produce a slide-by-slide issue ledger, coverage map and verdict.
   Never describe visual review as runtime or audio verification.

## Completion
Use GO only when all required checks passed for the stated scope.
Use HOLD for blockers or missing required evidence. Separate optional
polish from recording blockers. Do not edit protected artifacts.
```

### Make the Contract Explicit

Store duration mappings, counting rules, required checks and protected paths in one authoritative versioned contract. The contract should distinguish publisher rules, owner decisions and clip-specific exceptions. Conflicting word budgets are a blocker to exact-count validation, not permission to pick a convenient number.

The mechanical scripts need documented arguments, useful errors, nonzero failure exits and tests for invalid inputs. A validator should not modify the files it checks. Hashes establish artifact identity; they do not establish that a technical claim is true.

### Report Evidence at the Right Level

| Check | Evidence | Limit |
|---|---|---|
| Objective coverage | Exact objective mapped to slide and reveal | Mapping alone does not establish teaching depth |
| Narration budget | Counting rule, actual count and delta | Does not prove spoken duration or pronunciation |
| Frozen content | Approved manifest and current hashes | A newly generated manifest cannot prove prior approval |
| Technical accuracy | Visible artifact plus primary reference | Documentation alone does not prove a demo ran |
| Duplication | Compared clips and exact repeated teaching point | Missing adjacent content leaves the check unresolved |
| Audio and runtime | Playback or execution evidence | Text review cannot certify either |

Example finding: “Slide 4, reveal 2: narration says the gate blocks every unsafe release, but the visible code checks only one severity threshold. Narrow the claim or add evidence of the additional policy checks. Recording blocker: unsupported claim.”

For long work, record completed checks, source hashes and unresolved items in a durable run record. On resume, verify artifact identity before reusing results. On a tool timeout after a write, inspect the destination before retrying; repeated creation can produce duplicates.

## Test Before Release

Use fresh sessions and the same task set for a no-skill baseline and the candidate. Include positive triggers, near-miss non-triggers, paraphrases, missing inputs, contradictory requirements, unavailable tools and malicious instructions embedded in a reference document.

For the complex example, add a slide with an unsupported claim, a changed frozen file, an incorrect word total and a missing adjacent clip. The report should identify each limitation without inventing completion. For a clean case, verify that it can return GO when the stated evidence supports it.

Record task ID, package commit, model and host, input hashes, tool availability, expected behavior, observed behavior, elapsed time and cost where available. Repeat trials to expose variability. Compare missed blockers, false alarms and completion cost; do not replace measured outcomes with an assistant's confidence percentage.

The existing [testing playbook](10-testing-playbook.md), [semantic rubrics](12-semantic-rubrics.md) and [run-record example](../evals/run-record.example.json) provide more detail.

## Release Checklist

- [ ] One clear task, with explicit triggers and exclusions
- [ ] Valid frontmatter and host-compatible installation layout
- [ ] Required inputs, authoritative sources and missing-input behavior
- [ ] Concise core; references linked with conditions for reading them
- [ ] Scripts tested on valid, invalid and unavailable inputs
- [ ] Protected material and side-effect boundaries explicit
- [ ] Output format, evidence requirements and completion criteria defined
- [ ] Positive, negative, failure and recovery cases evaluated
- [ ] Results recorded honestly, including checks not run
- [ ] Instructions, dependencies and resources saved at one known commit

## Maintain the Skill

Turn observed failures into regression cases. Fix the smallest responsible instruction or tool, rerun affected cases and compare with the previous version. Re-evaluate after changing the model, host, tools or authoritative contract. Keep a known-good commit for rollback. Avoid appending every conversation as another permanent rule: resolve duplicates and remove obsolete instructions.

**A dependable skill is a small operating procedure with evidence that it helps on its intended tasks.**
