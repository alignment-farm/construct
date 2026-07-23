# Field-use protocol v0 — ordinary work, outcome-blind capture

Status: **DRAFT for one bounded cold review; no instrumentation licensed**.

Milestone: **none scientific**. This protocol serves provisional whole-body
engineering during the [frontier pause](FRONTIER_PAUSE.md). Its oracle is
capture fidelity and non-interference, not improved model performance. Its
loses-condition is that observation changes the work, hides negative use,
cannot point to native consequences, or costs more than the ordinary task can
justify.

## Purpose

Let independently necessary repository work place friction on Body Core
without authoring tasks to reward it. The protocol records where lineage or a
selected projection was available, whether it was consulted, what action
followed, and what the native work later established.

This is operational observation, not an experiment. It creates no treatment
assignment, fork, score, mechanism license, or memory finding.

## Reality criterion

A field-use invocation is eligible only when all of these were true before the
protocol was considered:

1. a human or existing project obligation supplied the task;
2. the task would still be performed if field capture were unavailable;
3. completion has a native consequence outside Body Core, such as a test,
   review verdict, accepted artifact, user correction, or external system
   response;
4. the operator can name the task and expected native consequence without
   referring to a memory mechanism;
5. capture can avoid secrets and unnecessary personal data.

Do not create synthetic tasks, retry a task for a cleaner trace, contact an
engine solely to populate the record, or prefer a task because Body Core is
likely to help. No eligible invocation is itself a finding.

The initial use surface is deliberately narrow: cold reorientation or handoff
while continuing an already-authorized repository task across an invocation
seam. Adding another workflow requires a protocol amendment, not an informal
analogy.

## Two observational modes

- **Shadow:** capture the task boundary and native consequence, but do not show
  a Body Core projection to the acting model. This checks whether capture can
  describe ordinary work without steering it. Shadow traces are not controls.
- **Consulted:** an operator uses raw validated lineage or an explicitly
  selected projection because it is practically useful for the task. Freeze
  the exact consultation surface before the first consequential action.
  Consultation may influence the work, but the trace alone cannot establish
  that it did.

Record eligible non-use as carefully as use: no projection available,
projection available but not consulted, projection refused, or consultation
abandoned. Do not collect only successful consultations.

Eligibility and mode are declared by the human operator or external runtime
before consultation. The acting model cannot nominate its own invocation.
Mode is chosen by the operational need, never randomized or changed after the
consequence is known.

This protocol does not license admission, consolidation, summarization, or a
new projector merely to make consulted mode useful. Consult an existing
lineage as it stands, but declare the origin of its frozen consultation
surface. Raw-lineage consultation of protocol-originated ledgers is permitted
and must carry `lineage_origin = field_capture`; use `mixed` when the surface
includes both field-capture and independently supplied lineage. Use
`independent` only when every consulted lineage source would exist without this
protocol. Determine origin from declared source provenance, not path heuristics.
A projected view may be consulted only when the required state already exists
from independently motivated operations. Otherwise record raw-lineage use,
non-use, or refusal. An all-shadow pilot is valid.

## Capture boundary

Capture the smallest chain that can be checked against native artifacts:

1. **Invocation start:** protocol id, field-use id, repository, base commit,
   independently supplied task reference, mode, and environment identifiers.
2. **Encounter:** a reference or digest for the task as received. Do not copy
   full user text when a stable local or substrate reference exists.
3. **Pre-action state:** consultation surface (`raw_lineage`,
   `projected_view`, or `none`); mandatory `lineage_origin` (`independent`,
   `field_capture`, or `mixed` when a lineage is consulted; explicit null for
   `none`); lineage head; explicit projector id and canonical view digest when
   projected; record ids made available; refusal or non-use reason;
   deterministic counts such as records and bytes. Freeze this before the
   first consequential action.
4. **Action reference:** the resulting patch, command, review entry, commit, or
   other native artifact. Store a pointer and digest rather than duplicating
   content by default.
5. **Consequence:** the external observer's exact native evidence—test output,
   reviewer verdict, user correction, accepted commit, or explicit
   `not_observed`. Absence of a consequence is not success.
6. **Completion:** final lineage head, capture refusals, and deterministic
   capture cost. Wall-clock latency and the model's account of what it used are
   optional audit fields, never outcome evidence.

The acting model may propose an action. It may not write its own consequence,
classify the invocation as helpful, or promote a row into the anomaly log.

## Storage and evidence class

If implemented, each invocation receives one append-only Body Core ledger at:

```text
runs/field_use/<field-use-id>.body.jsonl
```

The implementation must use the existing Core envelope and an explicitly
selected projector. Every row remains:

```text
evidence_class = wire_integration_only
```

Real operational origin does not upgrade that evidence class. Native artifacts
remain authoritative for what happened; the field ledger carries their stable
paths, ids, digests, and declared retention boundaries. A broken reference is
a capture failure, not permission to reconstruct the missing evidence from
prose.

No new Body Core schema, cognitive event ontology, ownership registry, or
field-use scorer is licensed by this draft.

## Retention and privacy

- Prefer `reference` retention for prompts, diffs, test logs, and substrate
  entries already preserved elsewhere.
- Use `redacted` retention with a digest and reason when a stable reference
  would expose secrets or unnecessary personal information.
- Inline only small, non-sensitive operational metadata required to replay the
  capture boundary.
- Never record credentials, environment secrets, private user data unrelated
  to the task, or hidden model reasoning.
- If safe capture is uncertain, refuse the invocation and record only the
  refusal reason outside sensitive content.

Field ledgers do not extend the retention authority of their referenced
systems. Deletion, access, and privacy requirements remain governed at the
native source.

## Non-interference rules

- Apart from the frozen, disclosed consultation surface in consulted mode, do
  not alter the task, prompt, model, tools, review depth, or completion
  criterion to improve the trace.
- Do not insert a projection into shadow mode.
- Do not add a record to make consulted mode look useful.
- Do not repair or rerun the task after seeing its consequence. Replaying the
  captured ledger for validation is permitted, but may not add or change rows.
- Do not score answer quality from model narration.
- Do not compare shadow and consulted invocations as if fork identity held.
- Stop capture if the operator notices that logging is changing the work.

The protocol loses locally when any rule above is violated. Keep the partial
trace, mark it `capture_refused` or `capture_confounded`, and do not replace it.

## Promotion path

Field ledgers are raw operational trace. Most should end there.

An invocation may be referenced from the
[passive anomaly log](ANOMALY_LOG.md) only when the existing capture criteria
hold: an unplanned, consequential behavior occurred; memory or context is one
plausible explanation; exact raw evidence exists; and competing explanations
are recorded. The anomaly entry links the native artifact and field ledger; it
does not claim causality or propose a treatment.

Only the cadence and reopening rule in
[FRONTIER_PAUSE.md](FRONTIER_PAUSE.md) can license a cold frontier pass. Field
volume, frequent consultation, or a persuasive anecdote cannot.

## Bounded pilot and review

If the draft is endorsed and instrumentation is later built, the first pilot
ends after the earlier of:

- five eligible invocations; or
- fourteen calendar days after the first eligible invocation.

Zero eligible invocations is an honest outcome. The pilot review asks only:

1. Were eligibility decisions made before outcomes?
2. Are shadow, consulted, refused, and non-use cases all visible?
3. Can every claimed consequence be reached through an exact native reference?
4. Did capture preserve privacy and ordinary task priority?
5. Was capture cost small enough to continue?
6. Which consulted lineage existed independently of this protocol, reported
   separately from `field_capture` and `mixed` consultation?

The review may endorse continued observation, narrow the protocol, or stop it.
It may not infer memory value, tune a mechanism, or turn the pilot into a
retrospective experiment.

## Cold-review request

Review this draft only for:

- whether the reality criterion prevents authored demand;
- whether capture is frozen before consequences and preserves negative use;
- whether native evidence remains authoritative;
- whether privacy and stop rules are sufficient;
- whether the promotion boundary respects the frontier pause.

Feature ideas, new memory mechanisms, extra workflows, scoring proposals, and
Body Core schema changes are out of scope for this pass.
