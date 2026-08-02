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
