# Platform Comparison

Documentation snapshot: 3 November 2026. Installation, discovery, permissions and cloud synchronization are host-specific. A common file format does not imply identical execution behavior.

| Surface | Documented entry point | What to verify before relying on it |
|---|---|---|
| ChatGPT Work | Select a skill with `@`; implicit selection can use its description | Skill is available in this account and tools are connected |
| Codex CLI / IDE | `/skills` or `$` mention; local `.agents/skills` discovery | Working directory, installed version, metadata visibility and dependencies |
| OpenAI API | Skills supplied through the documented API execution environment | Correct API surface, attachment/version format and shell availability |
| Claude Code | `/skill-name`; project `.claude/skills` and user skill locations | Frontmatter, explicit vs automatic invocation, local/cloud behavior |
| Claude app / API | Product-specific skill upload and configuration | Do not assume Code installation equals availability in another surface |
| Kiro | `.kiro/skills` and `~/.kiro/skills`; custom-agent resource configuration | Correct scope and `skill://` resources for the selected agent |
| Cursor | `.agents/skills` or `.cursor/skills`; slash invocation | Workspace scope and local/cloud distribution |

Sources: [OpenAI build guide](https://learn.chatgpt.com/docs/build-skills), [OpenAI API](https://developers.openai.com/api/docs/guides/tools-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Claude overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Kiro](https://kiro.dev/docs/skills/), [Cursor](https://cursor.com/docs/skills).

## OpenAI: ChatGPT and Codex

The current build guide describes progressive loading: metadata first, full instructions when selected. Codex can shorten descriptions or omit skills when its initial skill-list budget is exceeded. Put the distinguishing task first in the description and inspect warnings when many skills are installed. Explicit selection is useful for critical workflows but still does not prove execution succeeded. [S02](https://learn.chatgpt.com/docs/build-skills)

## Claude

Claude Code supports host-specific fields such as `disable-model-invocation`. Use documented controls when a procedure should run only on explicit invocation. Do not treat frontmatter names from one host as portable security policy. Current Code documentation distinguishes content persistence from permission persistence; test multi-turn workflows in the actual host. [S07](https://code.claude.com/docs/en/skills)

## Kiro

Workspace skills take precedence over global skills of the same name. Custom agents need the relevant resource declarations. Kiro's troubleshooting guide recommends checking location and frontmatter for missing skills, and clearer descriptions for incorrect activation. Record which copy loaded before editing anything. [S08](https://kiro.dev/docs/skills/)

## Cursor

Cursor documents automatic discovery and manual invocation. It also distinguishes local skill directories from skills made available to cloud agents. A skill working on a laptop is not proof that a remote worker can read it. Verify synchronization or commit project skills where appropriate. [S09](https://cursor.com/docs/skills), [S10](https://cursor.com/help/customization/skills)

## Portability Test Before Migration

1. Validate against the common specification.
2. List every host-specific frontmatter field and tool name.
3. Resolve paths relative to the installed package, not a personal machine.
4. Check shell, network, dependencies and file-write permissions.
5. Test explicit invocation, then implicit discovery with paraphrased requests.
6. Verify outputs and side effects in the new host.
7. Record the host/model/version in the release evidence.

This checklist is a proposed engineering practice. No cross-platform runtime tests were performed for this knowledge-base release.
