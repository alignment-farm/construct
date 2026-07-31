# Field-use invocation 001 — eligibility adjudication

Status: **ADJUDICATED 2026-07-25 — `capture_confounded`; excluded from the
bounded pilot's eligible-invocation count; pilot clock not started**.

Milestone: **none scientific**. This adjudication applies the endorsed
[field-use protocol v0](FIELD_USE_PROTOCOL_V0.md) to one operational trace. It
does not amend the protocol, alter the reviewed implementation, create a
finding, or reopen the frontier.

## Trace

```text
field_use_id: fu-20260723-doc-sync-001
ledger:       runs/field_use/fu-20260723-doc-sync-001.body.jsonl
mode:         shadow
wire phase:   invocation_completed
consultation: none
```

Source artifacts:

- [append-only ledger](../runs/field_use/fu-20260723-doc-sync-001.body.jsonl);
- [native documentation patch](../runs/field_use/native/fu-20260723-doc-sync-001.docs.patch);
- [native consequence commit patch](../runs/field_use/native/fu-20260723-doc-sync-001.commit.patch).

The six-row ledger is structurally valid and remains append-only. It records a
pre-action freeze, a native documentation patch, an externally observed commit,
and deterministic completion cost. That establishes that the capture machinery
ran end to end. It does not establish pilot eligibility.

## Question

Does this trace satisfy the protocol's reality criterion and non-interference
rules strongly enough to count as the first eligible invocation and start the
fourteen-day pilot clock?

## Evidence

1. The start row declared the task eligible before action and named
   `docs-sync-playlist-quotes-20260723` as its task id.
2. The frozen mode was `shadow`; no Body Core lineage or projection was exposed
   to the acting model.
3. The native action patch changed the pilot's own living status surfaces from
   “armed at zero” to “first eligible invocation begun; clock started.”
4. The consequence commit was itself titled “Sync living docs to the first
   field-use invocation” and carried the four-row in-progress ledger. The
   action therefore helped create the pilot status that the trace was offered
   to establish.
5. The protocol requires demand to exist independently of capture, prohibits
   preferring or creating work to populate the record, and says to stop with
   `capture_confounded` when logging changes the work.
6. The later `consequence_observed` and `invocation_completed` rows prove
   structural completion only. Native consequence authority cannot cure a
   failed pre-action independence or non-interference condition.

## Ruling

`fu-20260723-doc-sync-001` is **`capture_confounded` at the pilot-eligibility
layer**.

The trace is excluded because its action changed the pilot-status surfaces
whose change was then used to count the trace as invocation zero. The
pre-action declaration was necessary but not sufficient: the protocol's loses
condition was observed during the work.

The raw ledger is not rewritten or extended:

- append-only history remains evidence of what the runtime recorded;
- `invocation_completed` remains the correct wire-level phase;
- the implementation refuses mutation after completion;
- no new event kind, sidecar schema, or retrospective repair is licensed.

This adjudication is the more specific status authority for pilot counting. It
does not claim that the documentation patch lacked value, that the external
consequence was fabricated, or that the capture implementation failed its wire
contract.

## Pilot disposition

```text
eligible invocations:       0
excluded completed traces:  1 (capture_confounded)
consulted invocations:      0
fourteen-day clock:         not started
scientific findings:        0
```

There is no retry or replacement for this trace. The next countable invocation
must arise from unrelated ordinary work that would proceed without field
capture, cross the admitted cold-reorientation or handoff seam, and preserve a
native consequence outside the pilot's own status machinery. If such an
invocation is eligible, it becomes invocation one and starts the fourteen-day
clock.
