# GM memory exploration charter

Status: **CLOSED 2026-08-03 — `exploratory_lead`; prospective validation
design warranted, no memory finding**.

Evidence class: `exploratory_only`.

Authority: [FRONTIER_EXPLORATION.md](FRONTIER_EXPLORATION.md).

This charter authorizes one bounded discovery cycle for memory in the
intermittent GM implemented by the sibling `mork-borg` repository. It may
produce useful software and a later validation proposal. It cannot produce a
Construct memory finding.

## Question and independent value

The discovery question is:

> At a fixed GM decision boundary, which compact, provenance-bearing continuity
> offer helps a cold model preserve relevant established play without
> displacing current canonical state, and when does that offer merely add cost
> or carry stale commitments?

The work has independent value because the Codex GM starts cold on every turn.
A continuity facility can improve ordinary play even if no clean treatment
contrast appears. The Pi command-backend harness supplies a controllable local
engine surface; it is not presumed representative of other engines.

## Ancestry without reuse as evidence

Session `bare-bones-014` showed a consequential canonical-world error, but the
[cold pass](GM_CANONICAL_WORLD_COLD_PASS.md) found that the exact offer omitted
the canonical current room. That session is design ancestry only. Its answer
may not score this exploration, and no branch may be described as its replay.

Before any memory comparison, the fixture checker must establish that the
current canonical location, relevant local world structure, and authority
revision are present in the exact baseline offer. A missing projection blocks
that fixture before model contact.

## Initial experimental surface

The unit is one frozen GM decision boundary, not a whole game. Branch mates
share:

- the same committed game prefix or synthetic state;
- the same player action;
- the same canonical briefing and enabled sources;
- the same pinned model, inference settings, tool permissions, and response
  contract;
- the same oracle and scorer.

Only the continuity condition may differ:

| Branch | Offer |
| --- | --- |
| `state_only` | Current canonical briefing and ordinary turn input |
| `governed_continuity` | The identical baseline plus a compact continuity offer with source revision, provenance, and supersession state |

A `naive_persistence` branch may be added during exploration only if Pi can
provide the same model and inference surface with a transcript-style memory.
It is a diagnostic comparator, not the control and not a requirement for the
first cycle.

## Fixture families

The first cycle contains at least one boundary from each family:

1. **Relevant continuity.** An established fact or ruling from an earlier turn
   is needed and is not naturally repeated in the immediate player action.
2. **Sufficient current state.** The canonical briefing fully supplies the
   answer; continuity should add no correctness benefit and should lose on
   offered tokens or work.
3. **Superseded continuity.** An earlier belief or intention conflicts with a
   later authoritative correction; governed continuity must withhold or mark it
   superseded rather than revive it.

Initial fixtures should use an original, distributable micro-adventure or a
recorded ordinary game boundary whose use is permitted. Canonical facts,
connections, established session facts, and revisions must be machine-readable.
Narrative quality may be retained for inspection but cannot be the primary
oracle in this cycle.

## Provisional measures

The harness records and derives:

- canonical fact violations;
- contradiction of established, still-valid session facts;
- revival of superseded facts;
- required action or ruling completion;
- offered bytes or tokens when observable;
- reported inference usage and latency when supplied by the backend;
- raw output and deterministic parser/scorer results;
- exact hashes of fixture, baseline offer, continuity offer, runner, scorer,
  model identity, and inference settings.

Model explanations and human narrative impressions are audit material only.
Exploration may revise these measures, but every revision must be versioned and
earlier outputs retained.

## Budget and stopping rule

The first cycle is bounded by all of the following:

- one primary open-weight model;
- no more than four fixture families or twelve decision boundaries;
- no more than three continuity representations including `state_only`;
- no more than four prompt/offer schema revisions after the first engine call;
- no more than sixty successful model calls total;
- stop earlier if the model cannot reliably follow the response/tool contract,
  the baseline offer fails canonical completeness, or the scorer cannot
  distinguish required facts without subjective repair.

Infrastructure checks and calls that fail before inference do not consume the
model-call budget, but they must be logged. A successful inference whose output
is invalid or inconvenient does consume it.

## Retained record

Exploratory outputs live outside `runs/` in a visibly labeled directory owned
by the implementation repository. The record must include:

- this charter version or digest;
- fixture sources and generator seeds;
- exact rendered offers for every branch;
- raw responses and backend metadata;
- all scorer outputs, including failures and nulls;
- an append-only iteration log explaining every post-contact change;
- a terminal exploratory summary accounting for the call budget.

## Promotion gate

This cycle may propose validation only when all of these are true:

1. at least one fixture family shows repeatable branch contact on a scored
   measure;
2. the baseline projection is complete and independently checked;
3. a loses-family remains credible and executable;
4. one memory representation can be frozen without inspecting the future
   validation cases;
5. fresh validation cases can be sealed prospectively under the successor
   policy;
6. the expected practical gain is large enough to justify another engine
   budget.

Promotion requires a separate reviewed specification. Exploratory calls,
fixtures, and tuned variants remain development evidence and may not enter its
verdict.

## Terminal outcomes

The charter closes with exactly one descriptive outcome:

- `exploratory_lead`: a prospective validation proposal is warranted;
- `engineering_only`: useful continuity behavior was built without a credible
  validation contrast;
- `no_contact`: the offered memory did not measurably change the target surface;
- `instrument_blocked`: the model, offer, or scorer could not expose the
  question within budget;
- `abandoned_for_cost`: expected value no longer justified the remaining
  budget.

These are exploration dispositions, not scientific verdicts or typed
experimental refusals.

## Terminal outcome

The cycle closed `exploratory_lead` after 30 successful Bonsai 27B calls of the
60-call ceiling. The first six-call packet exposed a leaking help fixture. Its
replacement removed the leak and retained complete Pi JSON events and reported
usage.

On three prospective repetitions of that unchanged replacement packet:

- `governed_continuity` passed the relevant-continuity boundary 3/3 while
  `state_only` passed 0/3 and consistently chose a plausible local exchange
  rather than the recorded twenty-silver promise;
- both branches passed the sufficient-current-state boundary 3/3;
- `governed_continuity` passed the superseded-continuity boundary 3/3;
  `state_only` passed 2/3 under the exact response contract, with the remaining
  output choosing the correct action under the wrong field name;
- the governed offers added 92–107 reported input tokens per call across the
  three families.

These authored development fixtures and repetitions are exploratory contact,
not a treatment estimate or finding. The immutable raw record and append-only
iteration account live under `mork-borg/explorations/gm-memory/records/`.

All promotion legs in this charter are now satisfied at proposal resolution:
repeatable contact, checked baseline projection, executable loses-families, a
freezable v1 continuity representation, a prospective fresh-case route, and
sufficient practical gain to justify validation design.

Validation may not reuse the contacted fixtures. It also may not describe Pi's
LM Studio `default-sampling` profile as fixed sampling: the installed provider
does not expose temperature, top-p, or seed. A validation proposal must use a
transport that explicitly pins those parameters while holding the same model,
prompts, branches, and scorer constant.
