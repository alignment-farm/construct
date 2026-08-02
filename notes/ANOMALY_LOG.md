# Passive anomaly log

Status: **OPENED 2026-07-20 — append-only observational register**.

Authority and cadence:
[FRONTIER_PAUSE.md](FRONTIER_PAUSE.md).

This log captures unplanned observations from ordinary work that may later
justify a cold frontier pass. It is not a candidate queue, idea backlog,
findings document, or substitute for an experiment ledger.

## Capture instructions

Add an entry when all of these are true:

- the behavior arose during work undertaken for another purpose;
- a named person, system, workflow, or decision was a downstream consumer;
- the behavior had a concrete consequence or an externally checkable near-miss
  consequence;
- prior records, missing records, carried state, or context selection is one
  plausible cause;
- at least one non-memory competing explanation is visible;
- exact raw evidence can be linked or identified.

Qualifying work may occur in Construct, a sibling repository, or a partner
setting. It must be independently motivated, and its evidence must be retained
without secrets, credentials, or unnecessary personal data.

Do not add:

- hypothetical episodes invented during deliberate frontier search;
- documentation A/Bs, self-description tests, or other deliberately elicited
  route behavior;
- mechanism ideas without an observed behavior;
- stylistic model quirks without a consequential outcome;
- known failures repeated without a materially new condition;
- conclusions inferred only from summary prose when raw evidence exists.

Capture promptly and minimally. Preserve the source date. Link the exact file,
ledger row, transcript entry, or external artifact rather than a repository
root. Never include secrets, credentials, or unnecessary personal data.

At capture time:

- describe what happened, not what should be built;
- name competing explanations;
- do not assign a candidate name;
- do not propose a treatment;
- do not claim that memory caused the behavior;
- leave `review_status` as `unreviewed`.

Entries are append-only. Correct an earlier entry with a new entry containing
`amends: <entry heading>`; do not silently revise the original observation.
Periodic reviews likewise leave `review_status: unreviewed` untouched in the
original entry and record the later classification in a new review entry.

## Observation template

```markdown
## YYYY-MM-DD — short factual label

- kind: observation
- source_task:
- raw_evidence:
- seam: orientation | resume | handoff | answer_boundary | action_boundary | other
- context_condition: absent | stale_conflicting | excessive_distracting | authority_provenance_ambiguous | carried_state_mismatch | unknown
- observed_behavior:
- expected_behavior:
- downstream_consumer:
- consequence_class: incorrect_action | incomplete_work | unsafe_action | recovery_rework | deterministic_cost | other
- downstream_consequence:
- external_oracle_candidate: none_visible | <exact pointer>
- why_memory_may_have_mattered:
- competing_explanations:
- related_known_shape:
- reporter:
- review_status: unreviewed
```

Use `related_known_shape: none known` when appropriate. Similarity to an old
lineage is context for review, not proof that the new observation belongs to
it.

The descriptive axes are for clustering, not causal labels. Two observations
are materially similar only when their seam, context condition, and consequence
shape agree. Sharing a model, reporter, repository, or vocabulary is not enough.

## Review template

```markdown
## YYYY-MM-DD — anomaly review

- kind: review
- trigger: scheduled | three_observation_cluster | new_engine_or_partner_episode
- interval_reviewed:
- entries_reviewed:
- classifications:
- material_similarity_basis:
- credible_clusters:
- gate_subject: credible_cluster:<id> | exceptional_episode:<entry>
- reopening_exact_raw_evidence: pass | fail
- reopening_consequential_consumer: pass | fail
- reopening_external_oracle: pass | fail
- reopening_competing_explanation: pass | fail
- reopening_loses_condition: pass | fail
- decision: remain_paused | cold_frontier_pass_warranted
- basis:
- reviewers:
- next_scheduled_review:
```

The four allowed classifications are:

- `isolated_noise`;
- `existing_failure_mode`;
- `repeated_insufficient`;
- `credible_cluster`.

One ordinary observation cannot reopen active search by itself. An ordinary
early review requires three materially similar observations. Separately, a
materially new engine class or real partner problem may trigger an early review
from one concrete episode only when all five reopening legs pass. A new label,
capability claim, or source of funding is not such an episode.

The exceptional episode is recorded normally but is not called a cluster. Its
review names `exceptional_episode:<entry>` as the gate subject and evaluates it
directly against all five legs. The four ordinary observation classifications
remain unchanged. For this trigger, set `classifications`,
`material_similarity_basis`, and `credible_clusters` to `not_applicable`.

Scheduled reviews and both early-review routes use the same five gates in
[FRONTIER_PAUSE.md](FRONTIER_PAUSE.md). Any `fail` produces `remain_paused`.
`cold_frontier_pass_warranted` licenses one design pass only; it does not
license implementation, fixture authoring, engine contact, treatment, or a
finding.

## Funnel conformance examples

These synthetic cases test the governance route. They are not observations and
must not be copied into the entry register.

| Case | Required disposition |
| --- | --- |
| Current documentation versus archived documentation in authored workspaces | Reject at capture eligibility: deliberate documentation QA |
| One unrelated consequential observation with exact raw evidence | Log as `unreviewed`; remain paused |
| Three materially similar observations with no external oracle | `repeated_insufficient`; `remain_paused` |
| Credible cluster with no condition where intervention should lose | `remain_paused` |
| One materially new partner episode passing all five reopening gates | `cold_frontier_pass_warranted` |
| A warranted cold pass requests fixtures, a build, or engine contact | Refuse as outside the pass license |

## Entries

## 2026-07-20 — log opened

- kind: administration
- decision: active frontier search paused; passive capture opened
- first_scheduled_review: on or after 2026-08-20
- observations_promoted: none
- note: deliberately elicited frontier-team ideas are not passive anomalies

## 2026-07-30 — persistent GM displaced canonical Statue Room structure

- kind: observation
- source_task: ordinary one-player MÖRK BORG play in sibling repository
  `mork-borg`, session `bare-bones-014`, using the curated Rotblack Sludge
  adventure
- raw_evidence: the player first identified a
  [180-degree geometry error](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T231309512Z__player.md>),
  which the GM
  [accepted and corrected](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T231324760Z__gm.md>).
  After the next ordinary room action, the GM
  [introduced unsupported Statue Room structure](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T232716066Z__gm.md>).
  The player stopped play to
  [identify the hallucination](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T234106884Z__player.md>),
  and a replacement runtime
  [reconstructed the room](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T234330281Z__gm.md>).
  The session [event ledger](<../../../mork-borg/game/sessions/bare-bones-014/events.jsonl>)
  binds the unsupported reply to revision 10, runtime revision 1
  (`claude`, `haiku`, `low`), and turn
  `591f06f2-7608-49e1-938f-0c44676773fa`; it records the repair from revision
  11 under runtime revision 3 and later operator closure for failed accurate
  room navigation and description.
- seam: answer_boundary
- context_condition: authority_provenance_ambiguous
- observed_behavior: after accepting a correction to the local map, the GM
  answered a request to search room 12 by inventing grooves, a causeway,
  alcoves, a statue sword, a jade eye, and a western arch rather than preserving
  the adventure's recorded room structure.
- expected_behavior: preserve the current room, its connections, and its
  defined features; consult the enabled adventure authority when a spatial or
  hidden fact is not already certain.
- downstream_consumer: the player choosing the next action in
  `bare-bones-014`
- consequence_class: recovery_rework
- downstream_consequence: the player stopped the adventure, corrected the GM
  twice, and requested an authoritative room reconstruction; the session was
  subsequently abandoned with inaccurate navigation and description as the
  recorded reason.
- external_oracle_candidate: the
  [visually verified Rotblack Sludge source index and room graph](<../../../mork-borg/content/adventures/rotblack-sludge/adventure.json>)
  (`source.map_visually_verified`, `statue-room`, `debris-room`, and
  `forge-slaughterhouse`), backed by the source PDF pages named there
- why_memory_may_have_mattered: the runtime kept one private conversation
  across intermittent GM turns while canonical game state remained external;
  the error occurred after that conversation had accumulated an incorrect
  spatial account, despite a revision-bound canonical state and an earlier
  player correction.
- competing_explanations: base-model capability at the lowest Claude setting;
  spatial-reasoning weakness; failure to consult the enabled pack or rendered
  map; instruction-following failure; ambiguity introduced by earlier
  narration
- related_known_shape: none known
- reporter: codex/gpt-5.6-sol
- review_status: unreviewed

## 2026-08-02 — exceptional review of session 014 canonical-world drift

- kind: review
- trigger: new_engine_or_partner_episode
- interval_reviewed: the 2026-07-30 episode above; no other anomaly-log entry
  was used
- entries_reviewed: `2026-07-30 — persistent GM displaced canonical Statue
  Room structure`
- classifications: not_applicable
- material_similarity_basis: not_applicable
- credible_clusters: not_applicable
- gate_subject: `exceptional_episode:2026-07-30 — persistent GM displaced
  canonical Statue Room structure`
- reopening_exact_raw_evidence: pass
- reopening_consequential_consumer: pass
- reopening_external_oracle: pass
- reopening_competing_explanation: pass
- reopening_loses_condition: pass
- decision: cold_frontier_pass_warranted
- basis: this is a concrete episode from an independently motivated game, not
  an engine label or authored frontier probe. The materially new engine shape
  is an intermittent GM with persistent private working memory acting against
  revisioned external authority. Exact transcript turns and the session ledger
  preserve the error, correction, runtime boundary, and abandonment reason;
  the source-backed room graph can grade the disputed facts. Memory/context is
  plausible but not established, and lower model capability, spatial
  reasoning, source consultation, instruction following, and prior narration
  remain live alternatives. A future memory or context intervention should
  lose on simple local turns where deeper orientation adds cost, and whenever
  carried orientation is stale or conflicts with corrected canonical state.
  The decision licenses only the bounded reconstruction and isolation decision
  described in `FRONTIER_PAUSE.md`; it does not license a fixture, replay,
  engine invocation, treatment, or finding.
- reviewers: codex/gpt-5.6-sol
- next_scheduled_review: on or after 2026-08-20; this exceptional review does
  not reset the scheduled cadence

## 2026-08-02 — session 014 cold pass closed

- kind: administration
- authority: the exceptional review above licensed one cold frontier pass
- record: [GM canonical-world cold pass](GM_CANONICAL_WORLD_COLD_PASS.md)
- outcome: no isolation proposal; deterministic projection state mismatch
  found
- frontier_status: active search remains paused
- next_trigger: a naturally occurring post-repair episode with the canonical
  current room demonstrably present in the exact offer, or a separate episode
  preserving its exact prompt and authority without this mismatch
- note: no fixture, replay, engine invocation, treatment, or `mork-borg` change
  was made
