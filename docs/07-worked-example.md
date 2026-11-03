# Worked Example: A Course Narration Workflow

This is an illustrative design exercise, not an installed or tested production skill. The numbers below are example task-contract values, not industry-wide narration standards.

## Task Contract

Input: approved learning objectives, slide/reveal content, duration, prior approved content for duplication checks, and a word-count policy. Output: spoken narration mapped to reveals, a count report, evidence-backed issues and a readiness verdict.

Suppose the supplied policy requires a 3-minute narration to contain exactly 405 whitespace-delimited tokens. A reveal has a ceiling of 27 tokens. The skill must not silently substitute a different policy from memory.

## Convert Preferences Into Checks

| Requirement | Proposed check | Limitation |
|---|---|---|
| Exactly 405 words | Deterministic counter with documented tokenization | Token count does not measure actual audio duration |
| At most 27 per reveal | Counter on each reveal field | Spoken pacing still varies |
| Explain only visible material | Match narration claims to visual evidence | Requires semantic judgment |
| Cover the approved objective | Evidence map from objective to narration | Keyword matching alone is insufficient |
| No relative course navigation | Phrase scan plus semantic review | Literal scan misses paraphrases |
| Frozen files unchanged | Hash comparison before and after | Check correct paths and baseline |
| Natural spoken delivery | Read-aloud/TTS review | Different voices may pronounce differently |
| No fabricated personal story | Require supplied experience source | Personal tone does not authorize invented history |

## Proposed Workflow

Read the current inputs and validate the contract. Review slide content before narration. Draft by reveal. Run mechanical checks. Review technical support, objective coverage and spoken clarity. Repair only failed checks within a bounded number of attempts. Return the final artifact and evidence, or a specific HOLD reason.

For example, if a diagram contains three boxes but narration refers to a fourth stage, the remedy may be to fix the visual or narrow the spoken claim. Repeating “explain the diagram clearly” does not identify the mismatch.

## Example Failure and Recovery

An agent produces 405 words but misses one learning objective. The count check passes; the coverage check fails. The result remains HOLD. The agent revises relevant reveals, then reruns both count and coverage checks because the repair can affect both.

If the approved outline is inaccessible, the agent reports that blocker. It must not reconstruct the outline from an old conversation and label it exact alignment.

## What to Measure

Use the [40 starter cases](../evals/cases.json), add real anonymized failures, and reserve unseen cases. Compare no-skill and skill-assisted outcomes. Measure editing time as well as pass rate: a skill that saves prompting but doubles correction time is not necessarily useful.

This example is original synthesis. It is not a claim that any vendor recommends these exact word counts or that the checks have already been executed against a model.
