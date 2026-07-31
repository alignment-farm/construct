# Field-use capture v0 — implementation review

Status: **ENDORSED 2026-07-22; pilot authorized and armed; zero eligible
invocations; awaiting reality**.

The bounded post-build review ran in substrate thread
`field-use-protocol-v0`. `claude/fable-5` and `cursor/composer-2.5`
independently reviewed the frozen implementation and returned **ENDORSE**
without repair. Moderator `dan` then authorized the pilot.

## Exact reviewed implementation

```text
notes/field_use_capture_v0_implementation_manifest.json
2e471c0072c9e0c29b94ec179aa8287005a8fcc4b3e6d171d4eaa75638bbc19e
```

Both reviewers recomputed all eighteen manifest file hashes and all five
protocol-review thread-entry hashes. They verified the parent commit at
`575ef7994e4007d0f6d4291f0b6e9bd49c3b321a`, unchanged structural-kernel and
policy-projector surfaces, and the absence of `runs/field_use/`.

`claude/fable-5` independently reran 78 focused and compatibility checks plus
43 legacy checks, 121 total. `cursor/composer-2.5` independently reran the 78
focused and compatibility checks. Ruff lint and format and
`git diff --check` were clean.

## Reviewed conclusion

- The runtime binds the exact endorsed protocol and refuses protocol-byte
  drift.
- Field events use the existing Core envelope and explicit projector without
  admitting policy state.
- Lineage origin, consultation status, and surface are frozen before action.
- Independent, field-capture, and mixed supply remain visibly distinct.
- Native references are repository-bounded, content-pinned, and replay
  checked; capture rows do not copy native artifacts inline.
- Consequence authority remains external or explicitly `not_observed`.
- Refusal and confounding preserve terminal partial traces; retry cannot
  replace them.
- Cost is deterministic row and byte count, never wall-clock success.

The review licenses operational capture only. It creates no field observation,
memory finding, mechanism claim, state admission, scorer, automatic capture,
or product-schema promotion.

## Pilot activation boundary

The pilot is **armed**, but no invocation was manufactured from the capture
layer's own review or closeout. Such a trace would not be independently
necessary repository work and would turn self-use into demand theater.

The first eligible invocation must arise from ordinary, already-warranted work
that crosses a genuine cold-reorientation or handoff seam. Its operator must
declare eligibility, mode, provenance, actor, and observer and freeze any
consultation surface before action. Only then does the pilot contain an
invocation, and only that first eligible invocation starts the fourteen-day
calendar bound. The pilot closes at the earlier of five eligible invocations
or fourteen days after that first invocation. Zero remains admissible until
reality supplies one.

## Post-activation adjudication

The first attempted trace, `fu-20260723-doc-sync-001`, later reached
wire-level `invocation_completed`. Its specific
[eligibility adjudication](FIELD_USE_INVOCATION_001_ADJUDICATION.md) ruled
`capture_confounded`: the native documentation action changed the pilot-status
surfaces used to count the trace as invocation zero.

The ledger remains immutable evidence that the capture machinery completed. It
is excluded from the eligible-invocation count, did not start the fourteen-day
clock, and cannot be retried or replaced. This ruling changes no reviewed
implementation byte and makes no field or memory finding.

## Carried observations

1. Start and terminal payloads check required keys, while freeze and completion
   payloads use exact equality. A hand-rehashed ledger could therefore add
   extra keys to the former two surfaces inside the disclosed unauthenticated
   provenance boundary.
2. Inline free-text identifiers, reasons, and environment values remain an
   operator-discipline privacy surface.
3. Constructor refusal may leave an empty output directory. This has no
   evidence effect.
4. The zero-eligible calendar-close question remains carried; the current
   activation interpretation does not start a timer in the absence of an
   eligible invocation.

The implementation manifest freezes historical bytes. This review record and
the living-status updates made after endorsement are not expected to match the
manifest's frozen documentation hashes; the reviewed implementation itself
remains unchanged.
