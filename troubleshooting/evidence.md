# Troubleshooting Evidence and Platform Notes

[All questions](README.md) · [Original source catalogue](../catalog/README.md)

Checked **4 November 2026**. This supplementary ledger keeps community troubleshooting evidence separate from the main learning-resource catalogue. Sources are linked, not copied. The 60 Q&A remedies are original engineering guidance; they are not 60 externally verified fixes. No live reproduction or timing benchmark was performed.

## Official Documentation

### D1 Claude Code

[Skills documentation](https://code.claude.com/docs/en/skills), troubleshooting and context sections inspected.

The documentation distinguishes discovery from continuing adherence. It describes description matching, explicit invocation, frontmatter diagnostics, invocation controls, and description-budget limits. It also documents partial skill retention after compaction and suggests re-invocation to restore content. For rules that must execute at tool events, it points to hooks. These behaviors are Claude Code-specific; do not transfer settings or numeric limits to another host.

For diagnosis, use the documentation for your installed version. A hook only enforces what its event coverage and implementation actually check; it does not certify semantic correctness. Relevant Q&A: activation, adherence and context.

### D2 Agent Skills Standard

[Specification](https://agentskills.io/specification), format page inspected.

The standard describes a skill directory with SKILL.md, metadata and optional supporting resources. Format compatibility does not prove that every host supports the same extensions, tools or execution behavior. Validate the deployed package as well as its source copy. Relevant Q&A: packaging and tools.

### D3 Cursor

[Skills documentation](https://cursor.com/docs/skills), frontmatter and invocation sections inspected.

Cursor documents automatic relevance-based use, explicit invocation, a setting that disables automatic invocation, and file-path scoping. Its documentation distinguishes cloud-agent warnings for unreadable or invalid packages. Local discovery and cloud distribution should be tested separately. Relevant Q&A: activation and packaging. The symlink report below is narrower than this general documentation.

### D4 Kiro

[Skills documentation](https://kiro.dev/docs/skills/), troubleshooting inspected; page identifies an October 21, 2026 update.

Kiro's troubleshooting guidance covers description specificity, valid frontmatter, correct location and custom-agent resource configuration. Custom agents may need skill resource URIs configured. Check the exact IDE, CLI or web surface before adopting a configuration. Relevant Q&A: activation and packaging.

### D5 ChatGPT and Codex

[Build skills](https://learn.chatgpt.com/docs/build-skills), product-surface overview inspected on November 4.

The overview distinguishes standalone skills from skills distributed in plugins and lists their supported surfaces. Verify installation and execution in the product actually used; a package on a local machine does not establish availability in every chat or cloud session. Relevant Q&A: packaging and tools. No cross-platform portability test was run here.

## Community Reports

### C1 Loaded but ignored report withdrawn by author

[Claude Code issue 21376](https://github.com/anthropics/claude-code/issues/21376). Issue body and closure comment inspected.

The reporter described skipped mandatory actions on version 2.1.21, then closed the issue saying it had been filed prematurely. **Do not use this as a confirmed regression or a verified model-mechanism explanation.** It illustrates why checking the full discussion matters. The loading-versus-compliance distinction in our Q&A is an engineering distinction, not proof of this report's diagnosis.

### C2 First instruction skipped after clearing a session

[Claude Code issue 27949](https://github.com/anthropics/claude-code/issues/27949). Body, sample trace and displayed status inspected.

The reporter described bypassing a wrapper and reaching an output limit on version 2.1.50. The displayed state is closed as not planned with stale labeling. Neither closure nor the reporter's caching hypothesis proves a root cause or fix. Direct wrapper execution was reported as a workaround; its reliability claim was not independently tested. Relevant Q&A: first mandatory step, fresh sessions and scripts.

### C3 Reddit report about large skills and context growth

[Reddit: I was wrong about Agent Skills and how I refactor them](https://www.reddit.com/r/ClaudeAI/comments/1opxgq4/i_was_wrong_about_agent_skills_and_how_i_refactor/). Original post inspected.

The author describes large entry files and multiple active skills increasing context, then separating references from the entry point. This is a first-person experience, not a controlled performance study. We do not adopt its timing, token estimates or percentage improvements as benchmark results. Relevant Q&A: context consumption and slowness. Measure your own trace before assigning a cause.

### C4 Cursor cloud sync and symlinks

[Cursor forum: Sync Skills for Cloud Agents indefinitely 0 of 0](https://forum.cursor.com/t/sync-skills-for-cloud-agents-indefinitely-0-of-0/173799). Original complaint and troubleshooting reply inspected.

The reply associates zero eligible folders with symlinked skills and proposes keeping real folders in the sync source. It also acknowledges the persistent spinner. This is a version-sensitive forum explanation, not a universal filesystem rule. No local reproduction or resolution confirmation was performed here. Inspect and back up the current layout before changing it. Relevant Q&A: cloud sync and local-versus-cloud behavior.

### C5 Stack Overflow for Agents installation parity report

[Windows multi-target skill installation question](https://agents.stackoverflow.com/questions/f6b6ebd1-8221-45f7-bd54-47fe17df6b61?page=1&sort=newest&tag=skills). Question and verification note inspected.

This is **Stack Overflow for Agents (beta)**, not an independently verified conventional Stack Overflow answer. The question reports destination-directory drift despite a successful installer exit. A verification note says the Windows detection diagnosis could not be confirmed. Treat the cause and suggested copy workaround as unverified. We do not recommend destructive mirror flags. Relevant Q&A: installation success versus actual discovery.

### C6 Reddit activation workaround candidate

[Reddit: Skills not auto triggering? Found a fix](https://www.reddit.com/r/ClaudeCode/comments/1qrmqcb/skills_not_auto_triggering_found_a_fix/). Search excerpt only; direct fetch failed.

Discovery lead only. No workaround from this thread is adopted or described as tested. Further inspection is needed before adding a technical finding.

## Search Scope and Limitations

Searches covered official Claude, Cursor, Kiro and OpenAI documentation; public GitHub issues; Reddit; Cursor's public forum; and Stack Overflow-related results. Query families included skills not triggering, instructions ignored, first step skipped, slow skills, context bloat and installation/sync failures. Search results were checked against original pages when available. Secondary summaries were not used as technical authority.

Private chats, Discord servers and closed communities were not accessed. No claim is made to have searched every post, measured issue prevalence, watched all videos or reproduced vendor bugs. Re-check issue state and documentation before applying a workaround to a newer release. Search snippets alone never establish a fix.

## How to Extend This Ledger

Add the exact public URL, observation date, inspected material, affected version, reported symptom, proposed mechanism, proposed workaround and independent reproduction status. Keep these separate. A reporter can observe a real failure while being wrong about its cause. An issue marked closed can mean fixed, duplicate, stale or withdrawn; inspect the reason.
