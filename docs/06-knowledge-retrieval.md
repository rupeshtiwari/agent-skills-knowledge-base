# Using a Large Knowledge Base

Keep the knowledge base broad and individual skills focused. Loading every article into every task increases context cost and makes it harder to identify the governing requirement. This design recommendation follows the progressive-disclosure pattern in [S01](https://agentskills.io/specification) and context selection principles in [S12](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).

## Suggested Retrieval Record

Store source ID, title, URL, source type, checked date, review depth, applicable platform/version, claim, limitation and original location. The included [JSON catalogue](../catalog/sources.json) supplies the basic provenance fields. It is a source index, not an embedded vector database.

## Retrieval Procedure for a Future Skill

1. Identify the task and platform.
2. Retrieve the small set of relevant source records.
3. Inspect original authoritative sources for changing product behavior.
4. Separate documented behavior, research findings and community hypotheses.
5. Apply only procedures compatible with the user's environment.
6. Return citations and identify unresolved contradictions.

Begin with filename/text search over a well-organized repository. Add embeddings when query volume and semantic retrieval needs justify them. Evaluate retrieval using known questions: did the system return the governing rule, its version and its exception?

## Avoid These Mistakes

Do not turn every retrieved paragraph into a mandatory instruction. Do not concatenate whole books into the skill body. Do not silently replace an old source with a new version while preserving old conclusions. Do not assume retrieval success means the agent followed the retrieved rule.

## Source Freshness

Platform details should be checked before installation or release. Research summaries should retain paper versions. Community reports should retain reported versions and unresolved reproduction status. When sources conflict, preserve both and explain their experimental or product-surface differences.

A future automation could refresh the catalogue, but none is configured in this release. Maintenance remains an explicit workflow documented in CONTRIBUTING.md.
