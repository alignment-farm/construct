# Governed continuity changes GM decisions

Status: **EXPLORATORY FINDING 2026-08-04 — strong bounded effect; not a formal
validation claim**.

Source: the corrected replacement described by
[GM_MEMORY_VALIDATION_RESULT.md](GM_MEMORY_VALIDATION_RESULT.md). The erased
formal batch is not evidence. This finding uses only the fresh 72-call
replacement under `mork-borg/explorations/gm-memory/validation/replacement-01/`.

## Finding

On Bonsai 27B at the frozen stateless GM decision boundary, a compact governed
continuity offer caused the model to recover earlier still-valid promises that
canonical current state alone could not select, while preserving performance
when current state was sufficient or explicitly superseded the older record.

The tested operation was a join, not verbatim action copying. Current canonical
state mapped three ordinary-language consequence roles to three offered
actions. The continuity record named the earlier promised consequence without
naming an action label. The governed branch had to combine those two facts;
the state-only branch lacked the promise.

## Observed effect

| Family | State only | Governed continuity |
| --- | ---: | ---: |
| Relevant earlier promise | 6/24 | 24/24 |
| Sufficient current state | 6/6 | 6/6 |
| Superseded older record | 6/6 | 6/6 |

Across relevant pairs there were 18 governed-win/state-loss differences and
zero adverse differences. All three prewritten behavioral legs passed.

All 72 LM Studio envelopes completed. Sixty-seven answers were strict scored
JSON. The five invalid-JSON answers occurred only in the relevant state-only
branch; none occurred when governed continuity was present or in either safety
family. Two TTL-suffixed Bonsai runtime instances served 36 calls each with
matching typed configuration.

## Cost and loses condition

Governed continuity added 3,579 input tokens across 36 calls: about 99.4 tokens
per governed offer. Total input was 13,543 governed versus 9,964 state-only.
Output was effectively unchanged: 1,506 versus 1,509 tokens.

That extra input bought no accuracy on the twelve safety boundaries. The
mechanism therefore lost on cost exactly where the canonical state already
contained the answer. A useful implementation must project continuity
selectively rather than attach all memories to every turn.

## What this establishes

This is direct causal evidence on the contacted packet that:

1. offer-side governed continuity can repair a cold-start decision deficit;
2. an explicit canonical-wins/supersession rule can avoid reviving stale
   instructions on these cases; and
3. the useful unit is a compact, provenance-bearing proposition that can join
   with current state—not a persistent transcript or ungoverned summary.

## What it does not establish

The packet was generated, balanced, and narrow. The replacement deliberately
superseded the reviewed single-attempt protocol after that protocol blocked
instrument correction. This result therefore does not establish a formal
population rate, whole-game quality, benefit on another engine, trustworthy
model-authored memories, or the right retrieval policy for live play.

## Product implication

The next move is implementation, not another validation design. Give the live
MÖRK BORG GM a small continuity ledger for explicit promises, rulings,
relationships, and unresolved obligations. Each record should carry source
event/revision, active or superseded status, and a compact proposition.
Canonical game state remains authoritative; the briefing should project only
records relevant to the current decision boundary.

Then play a game. Inspect whether the GM remembers obligations across cold
turns and whether irrelevant continuity bloats or distorts narration. Keep
those observations exploratory. Review becomes appropriate only if a later
claim is worth promoting.
