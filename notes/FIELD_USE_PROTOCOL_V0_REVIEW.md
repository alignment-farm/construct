# Field-use protocol v0 review

Status: **ENDORSED 2026-07-22 after one bounded repair**.

The observation ruler was reviewed in substrate thread
`field-use-protocol-v0` by `claude/fable-5` and
`cursor/composer-2.5`. The first pass independently found the same blocker; the
single repair closed it; both fresh final reviews returned **ENDORSE**.

## Exact reviewed protocol

```text
notes/FIELD_USE_PROTOCOL_V0.md
29dbc5a59d60986c6b41f88999eae610067ba572606424f3a607ee3ada327ab1
```

This supersedes the initially reviewed draft at SHA-256
`1d8a5b640f255053665434041b951fbead83941ba1fb654cbdfe7a269eb9c213`.

## Blocker and repair

The initial draft protected independence of task demand but not independence of
the lineage being consumed. A field ledger written during invocation N could
supply raw-lineage consultation during invocation N+1 without the pilot
disclosing that the protocol created its own supply.

The repair added three connected requirements:

1. every consulted surface declares `lineage_origin` as `independent`,
   `field_capture`, or `mixed` from source provenance rather than path
   heuristics;
2. the declaration is frozen before the first consequential action, with
   explicit null when no lineage is consulted;
3. pilot review reports independently supplied consultation separately from
   field-fed and mixed consultation.

Cross-seam reuse of an earlier field ledger remains permitted. It is now
visible as protocol-fed supply rather than evidence that useful lineage existed
independently.

## Endorsed boundary

The protocol governs operational observation only:

- ordinary repository work must exist independently of capture;
- shadow, consulted, refused, abandoned, and non-use cases remain visible;
- native artifacts, not model narration, are authoritative for consequences;
- the acting model cannot nominate itself, write its consequence, or promote an
  anomaly;
- every Core row remains `wire_integration_only`;
- promotion remains subordinate to `ANOMALY_LOG.md` and
  `FRONTIER_PAUSE.md`;
- the bounded pilot cannot be read retrospectively as a treatment experiment.

Endorsement licensed the ruler only. It did not itself license instrumentation,
pilot activation, state admission, a projector, scoring, engine contact, or a
memory finding. The human authorization after review separately licensed the
minimal capture implementation recorded in
[FIELD_USE_CAPTURE_V0.md](FIELD_USE_CAPTURE_V0.md).

## Carried observations

Four non-blocking observations remain visible:

1. a pilot with zero eligible invocations has no calendar close until its first
   eligible invocation;
2. operator and acting model may be instances of the same model family, making
   pre-declaration and native consequence authority important;
3. consultation outside the frozen pre-action surface should terminate as
   `capture_confounded`;
4. capture cost must remain deterministic row/byte/count information; wall
   clock is audit metadata only.

The exact endorsed protocol bytes remain unchanged. This review record is the
later status authority.
