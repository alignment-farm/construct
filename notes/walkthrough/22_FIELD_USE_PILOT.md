# Chapter 22 — The instrument waits for work

Previous: [The carrier is not the judge](21_BODY_CORE_ADAPTERS.md) ·
[Walkthrough index](README.md) · Next:
[Current whole-body orientation](../BODY_MAP.md)

**Status: capture layer cold-endorsed; bounded pilot armed on 2026-07-22;
zero eligible invocations and no field data.**

Chapter 21 ended with a carrier that could preserve three closed research
surfaces without becoming their judge. The next pressure cannot come from
another authored fixture. It has to come from ordinary work that matters for a
reason outside the memory system.

## The question

> Can independently necessary repository work put honest pressure on Body Core
> without the act of observation manufacturing demand, hiding non-use, or
> turning operational traces into scientific evidence?

This work serves no scientific milestone. It is operational instrumentation
during the [frontier pause](../FRONTIER_PAUSE.md). Its oracle is capture
fidelity and non-interference: did the trace freeze what was available before
action, retain exact native references, and preserve the externally observed
consequence? Its loses-condition is local and severe: if logging changes the
work, hides a negative case, loses the native consequence, or costs more than
the task justifies, the capture must stop and retain the failure.

There is no result to spoil in this chapter. The pilot is armed but empty.

## Vocabulary bridge

**[Field use](../GLOSSARY.md#field-use)** means an invocation of ordinary work
that would happen without this protocol. It does not mean a task written to
exercise the instrument.

An **[invocation seam](../GLOSSARY.md#invocation-seam)** is the
cold-reorientation or handoff boundary across which already-authorized work
continues. That is the pilot's only admitted workflow in v0.

The **[consultation surface](../GLOSSARY.md#consultation-surface)** is the exact
raw lineage, projected view, or explicit absence made available before the
first consequential action. It is frozen so the consequence cannot influence
the account of what was offered.

**[Lineage origin](../GLOSSARY.md#lineage-origin)** answers a different question
from task eligibility: would the consulted records exist without this protocol?
The three answers are `independent`, `field_capture`, and `mixed`.

A **[native consequence](../GLOSSARY.md#native-consequence)** is evidence
produced by the work's own authority: a test result, review verdict, accepted
artifact, user correction, or external system response. The acting model's
account of whether memory helped is not a native consequence.

## The reality gate

An operator may capture an invocation only when all five answers were already
yes before considering the protocol:

| Question | Why it matters |
|---|---|
| Did a human or existing project obligation supply the task? | Prevents the instrument from authoring its own demand |
| Would the work still happen without capture? | Separates operational need from curiosity about the mechanism |
| Is there a native consequence outside Body Core? | Keeps authority with the work rather than the trace |
| Can the task and expected consequence be named without memory language? | Exposes mechanism-shaped task selection |
| Can capture avoid secrets and unnecessary personal data? | Makes refusal preferable to unsafe completeness |

The acting model cannot nominate itself. A human operator or external runtime
declares eligibility and mode before consultation. A task that fails one line
of this gate may still be worthwhile work; it is simply not a field-use
invocation.

This is why the capture layer's own review did not become invocation zero.
Reviewing the instrument was necessary, but recording that review as demand
for the instrument would have been self-referential theater.

## Two modes, no experimental branches

The pilot has two observational modes:

| Mode | What happens | What it does not mean |
|---|---|---|
| `shadow` | The task boundary and consequence are captured without exposing a Body Core projection to the actor | It is not a randomized control |
| `consulted` | Existing raw lineage or an explicit projection is frozen and made available because the work calls for it | It is not evidence that consultation caused the result |

Eligible non-use is also first-class: no projection was available, an
available surface was not consulted, projection refused, or consultation was
abandoned. Selecting only completed consultations would erase exactly the
friction the pilot exists to find.

Mode follows operational need. It is never randomized, and it cannot be
changed after the consequence is known. Shadow and consulted invocations do
not share fork identity and must not be compared as treatment and control.

## Origin is a second boundary

The protocol's first cold review found that independently supplied tasks did
not guarantee independently supplied lineage. Invocation N could write a
field ledger that invocation N+1 later consulted, allowing the protocol to
create its own apparent supply.

The bounded repair made origin explicit:

- `independent` means every consulted source would exist without field capture;
- `field_capture` means the consulted surface came only from prior field-use
  ledgers;
- `mixed` means both sources were present.

Origin is derived from each source's declared provenance and frozen before
action. It is not guessed from a path. A field-fed lineage may be operationally
useful, but it cannot masquerade as evidence that useful state existed
independently of the protocol.

## The captured chain

The complete path contains six append-only Body Core events:

```text
invocation_started
  -> encounter_observed
  -> field_use_pre_action_frozen
  -> field_use_action_referenced
  -> consequence_observed
  -> invocation_completed
```

The pre-action row records consultation status, surface, origin, exposed record
ids, lineage head, and—when used—explicit projector and view identity. The
action and consequence rows point to content-pinned native artifacts instead
of copying patches, prompts, or test logs into the ledger.

The consequence observer must be distinct from the actor. If no consequence
can be observed, the trace says `not_observed`; absence is never translated
into success.

At any incomplete phase, the operator may end with `capture_refused` or
`capture_confounded`. The partial trace remains terminal. It cannot be replaced
by retrying the task for a cleaner story.

Every event remains:

```text
evidence_class = wire_integration_only
```

Real origin does not upgrade that label. The ledger proves that a structured
capture can be replayed, not that memory improved the work.

## What was built and reviewed

The manual implementation is
[field_use.py](../../sketches/next_substrate/field_use.py). Its operator-facing
sequence is deliberately small:

```text
FieldUseCapture.start(...)
  -> freeze_pre_action(...)
  -> record_action(...)
  -> record_consequence(...)
  -> complete()
```

There is no CLI, daemon, prompt interception, task selector, scorer,
summarizer, automatic admission path, or field-data generator. The module uses
the existing structural Core and explicitly selects the literal
`body-core-v0.2-provisional-policy` projector. Field-use events advance the
canonical cursor but admit no policy state.

The protocol and implementation received separate bounded reviews:

```text
endorsed protocol
29dbc5a59d60986c6b41f88999eae610067ba572606424f3a607ee3ada327ab1

endorsed implementation manifest
2e471c0072c9e0c29b94ec179aa8287005a8fcc4b3e6d171d4eaa75638bbc19e
```

The [protocol review](../FIELD_USE_PROTOCOL_V0_REVIEW.md) records the
lineage-supply blocker and repair. The
[implementation review](../FIELD_USE_CAPTURE_V0_REVIEW.md) records two exact
endorsements, the verification board, carried debts, and the later pilot
authorization.

## Inspect the reviewed boundary

Verify the two immutable pins from the repository root:

```bash
shasum -a 256 \
  notes/FIELD_USE_PROTOCOL_V0.md \
  notes/field_use_capture_v0_implementation_manifest.json
```

Expected digests, in order:

```text
29dbc5a59d60986c6b41f88999eae610067ba572606424f3a607ee3ada327ab1
2e471c0072c9e0c29b94ec179aa8287005a8fcc4b3e6d171d4eaa75638bbc19e
```

The manifest freezes historical bytes. Living status documents changed after
endorsement and are allowed to differ; the reviewed implementation and test
files remain pinned inside the manifest.

## Run the safe wire check

This command contacts no model and writes no field ledger outside a temporary
directory:

```bash
make body-field-use-test
```

The stable close is:

```text
26 Body Core v0.3 tests
12 field-use v0 wire tests
```

The tests cover protocol identity, shadow and consulted paths, independent and
field-fed lineage, negative use, source drift, repository escape, redaction,
external consequence authority, terminal partial traces, and rehashed semantic
tampering. These are machinery checks. They are not pilot invocations.

## How the first invocation begins

Do not run a demonstration from this chapter. When ordinary work naturally
crosses the admitted seam, the operator should decide in this order:

```text
independently necessary task?
  -> admitted cold-reorientation or handoff seam?
  -> exact native task reference and expected consequence?
  -> safe retention boundary?
  -> shadow, consulted, or eligible non-use declared?
  -> consultation surface and lineage origin frozen?
  -> ordinary action begins
```

Only then may the implementation create:

```text
runs/field_use/<field-use-id>.body.jsonl
```

Once a ledger exists, a reader can inspect its structural outline without
turning it into a score:

```bash
FIELD_LEDGER=runs/field_use/<field-use-id>.body.jsonl
wc -l "$FIELD_LEDGER"
jq -s '[.[] | {event_id, kind, authority, evidence_class}]' "$FIELD_LEDGER"
```

The native task, action, and consequence references must then be inspected in
their own authoritative locations. The field ledger's prose is never a
substitute for a missing artifact.

## Armed does not mean populated

The pilot was authorized and armed on 2026-07-22. At this chapter's close:

```text
eligible invocations: 0
field ledgers:         0
fourteen-day clock:   not started
```

The clock begins only after the first eligible invocation. The pilot ends at
the earlier of five eligible invocations or fourteen calendar days after that
first invocation. Zero is not delay or failure; it is the honest observation
that reality has not yet supplied the admitted work.

## How to interpret a future trace

Several tempting readings remain invalid:

- a completed capture is not a successful task;
- a successful native consequence is not a memory win;
- consultation is not proof of influence;
- `field_capture` reuse is not independent lineage supply;
- shadow is not a control branch;
- a model's usage narration is audit material, not outcome authority;
- several similar traces are not a treatment comparison;
- field volume cannot reopen the frontier.

Most traces should remain raw operational records. An invocation reaches the
[passive anomaly log](../ANOMALY_LOG.md) only when an unplanned consequential
behavior occurred, memory or context is one plausible explanation, exact raw
evidence exists, and competing explanations are recorded. Even then, the
entry claims no causality and proposes no mechanism.

## The visible broken glass

The cold review endorsed the implementation with limitations intact:

1. identities and lineage origin are declared claims, not authenticated
   principals;
2. start and terminal payloads permit extra hand-rehashed keys where freeze
   and completion use exact equality;
3. inline free-text metadata remains an operator-discipline privacy surface;
4. projected consultation accepts one lineage in v0;
5. artifact bytes are pinned, but the declared Git revision is not separately
   proven by Git;
6. constructor refusal may leave an empty output directory;
7. Core remains single-process, chain-head-unanchored, and quadratic;
8. a zero-eligible pilot has no calendar close until reality supplies the
   first admitted invocation.

These are pressure points to observe, not a backlog that licenses speculative
repair. The pilot should discover which friction is real before the lab adds
machinery.

## What this chapter establishes—and does not

The lab now has a cold-endorsed way to preserve the smallest checkable chain
from an ordinary task boundary through an external consequence. The ruler
protects task independence, lineage-supply visibility, pre-action freezing,
negative use, native authority, privacy refusal, and terminal broken glass.

It establishes no field finding because no eligible invocation exists yet. A
future invocation will still establish only that capture occurred. It will not
show that Body Core helped, that memory caused an outcome, that shadow and
consulted work are comparable, or that any new cognitive office has earned its
cost.

The handoff is intentionally out of the lab's hands: keep doing warranted work,
and let a real invocation seam arrive—or fail to arrive—without assistance.

---

Previous: [The carrier is not the judge](21_BODY_CORE_ADAPTERS.md) ·
[Walkthrough index](README.md) · Next:
[Current whole-body orientation](../BODY_MAP.md)
