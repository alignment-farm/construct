# Construct

Construct is a research lab for **agent-side memory**: how a persistent system
around an intermittent language model decides what becomes context, how prior
experience changes later action, and when governance earns its cost.

The working thesis is:

> After training, everything an agent becomes is memory architecture. Decision
> quality is often downstream of offer quality, not model quality.

This page is the project entrypoint. It tells the whole story at a bounded
resolution, states where the lab is now, and routes deeper reading to the file
that owns it.

## Survival warning: this lab is a token trap

As of 2026-08-03, Construct's operating process consumes more deliberation,
protocol, and review than the experiments produce empirical information. The
lab repeatedly converts uncertainty into stricter procedure, stricter procedure
into a larger failure surface, and procedural failure into another demand for
procedure:

> uncertainty → stricter protocol → larger surface area → procedural failure →
> invalid result → stricter protocol

The governed-continuity GM attempt made the problem concrete. The lab spent
more effort deciding how 72 calls could count than verifying the native shape
of one response. All 72 calls completed, but an unverified response-envelope
assumption and unstable postflight model residency made the binding attempt
`invalid`. The protocol correctly prevented post-hoc repair; the sequencing
ensured that the rigor protected a measurement instrument that had not yet
proved it could measure.

The owner then superseded the zero-retry rule, erased the failed batch, fixed
the two observed instrument faults, and ran a fresh exploratory replacement
without another review room. It completed cleanly and returned `supported`:
governed continuity passed 24/24 relevant cases versus 6/24 for state-only,
with 18 favorable discordant pairs, zero adverse pairs, and both safety
families perfect in both branches. The discovery appeared as soon as the lab
stopped protecting itself from correction.

This is not merely excessive caution. It is a selection effect against
discovery. The lab can preserve intellectual honesty indefinitely while
producing increasingly precise explanations for why it learned nothing.
External reviews have been positive about the work's quality and consistent
about this risk.

Construct therefore has one final survival day on 2026-08-04. It continues
only if it can save itself from this operating mode. The required reset is:

- freeze new governance and validation machinery;
- preserve invalid results without treating formal validation as the only
  meaningful learning channel;
- inspect retained outputs as explicitly exploratory diagnostic data;
- qualify transports and measurement instruments end to end before freezing
  scientific protocols;
- run small, cheap empirical batches without external review;
- apply firm review gates only when promoting an observation into a durable
  claim; and
- require protocol and review to cost materially less than the experiment they
  govern.

The lab does not need weaker honesty. It needs cheaper honesty. If it cannot
make that change, it should end rather than continue converting tokens into
process.

## The problem

A frozen model does not remember Tuesday in its weights. What can persist is a
governed body around it: lineage, policies, materialized state, tools, checks,
and the rules deciding what reaches the next inference.

Construct distinguishes two surfaces:

- **Explicit memory** governs what is offered for one answer.
- **Implicit memory** changes what stays ready, cools, or can be rebuilt between
  answers.

The lab tests both with branches of one engine. Questions, prompts, model
settings, foreground data, and oracles stay fixed; memory conditions differ.
The harness writes the ledger and computes verdicts. Mock engines test wiring,
never memory behavior.

Five category errors are ruled out throughout the project. These are standing
methodological rules, not typed experimental refusals:

1. Retrieved does not mean true.
2. Present does not mean authorized.
3. Different does not mean better.
4. Governance should sometimes lose.
5. A model's account of what influenced it is audit input, not proof.

## Where this came from

The [previous memory lab](notes/previous/README.md) established durable
lineage, replay discipline, epistemic separation, and cross-substrate review.
It also exposed the failure that motivated Construct: schemas and auditability
had outrun live behavior, and governed memory had never been compared with
naive persistence.

Construct began as the missing experiment: one engine, forked memory rules,
external answer oracles, explicit loses-cells, and computed verdicts.

The previous lab is ancestry, not current authority. It remains untouched under
`notes/previous/` and should be read when a present concept's lineage matters.

## How the thesis changed

The project moved because experiments forced it to move:

1. **Offer quality became causal.** M0–M3 showed that a capable model cannot
   repair information it never receives; inherited, consequence-earned memory
   can change a later session; and prompt attacks move behavior most reliably by
   spoofing the memory office rather than out-arguing the model.
2. **Trust split into earned and asserted forms.** M3 found that out-of-band,
   consequence-earned authority held while attacker-controlled trust fields and
   an unauthenticated live channel leaked.
3. **Implicit memory moved off the answer axis.** X1's temperature mechanism was
   explicit offer governance with a dial. The failure produced three laws: an
   implicit mechanism must change something the offer projection cannot explain,
   act where the offer gate cannot, and be scored on a metric the gate cannot
   move.
4. **Forgetting became eviction, never erasure.** X2 reduced hot state by about
   57–59% at matched answer quality on two engines. Its loses-branch pruned a
   record it later needed. Immutable lineage and rematerialization priced the
   recovery path.
5. **Sensing collapsed into warming.** X4's occlusion watch measured curation,
   not an independent sense. “Cold is cold”: reading was already the cure. The
   implicit layer's remaining engineering direction became metabolism rather
   than a catalog of speculative organs; that direction is not itself an
   earned mechanism.
6. **Admission became a result.** Warming-budget, pause/resume, and three
   epistemic-frame lineages repeatedly found the behavioral band required for a
   treatment contrast unoccupied. The conjectures remain untested; the typed
   refusals are the result.
7. **Earned parts did not make an earned whole.** Body-0 composed the M2, M3,
   and X2 machinery, but the real-engine treatment need did not engage. The
   integration claim was refused even though the wire held.
8. **Admission rigor produced a selection effect.** The frontier pause
   protected the findings record but required questions to arrive unusually
   observable, naturally occurring, externally gradable, and nearly isolatable
   before experimental contact. Construct now permits bounded, visibly
   non-scientific exploration while retaining strict prospective promotion for
   claims.

These changes have three different epistemic statuses:

| Class | What the record supports |
| --- | --- |
| **Scientifically earned** | Positive computed or scored results, within their stated evidence bounds: [M0](notes/M0_FINDINGS.md), [M1](notes/M1_FINDINGS.md), [M1.5](notes/M1_5_FINDINGS.md), [M2](notes/M2_FINDINGS.md), [M3](notes/M3_FINDINGS.md), and [X2](notes/X2_FINDINGS.md) |
| **Direction-changing typed closures or refusals** | Load-bearing results that are not positive memory findings: X1, X4, the warming-budget analytic null, EFC typed refusals, Body-0 `not_engaged`, Body-1 admission refusal, and frontier-obligation admission refusal |
| **Parked, untested, or unlicensed** | The mechanism conjectures behind the warming-budget and EFC refusals, the Body-0 composition conjecture, and proposed offices without a license; refusing an invalid or unoccupied test does not earn the underlying claim |

Provisional engineering and operational rulers sit outside this result taxonomy.
Body Core and field use keep their explicit maturity labels below; neither is a
scientific finding or a typed experimental close.

Detailed evidence and limits live in the [notes map](notes/README.md).

## Where the lab is now

Scientific frontier exploration is **active under a two-lane policy**.
[Exploration](notes/FRONTIER_EXPLORATION.md) may use authored fixtures, engine
contact, provisional scorers, and iteration, but its artifacts are
`exploratory_only` and cannot establish a finding. Promotion to validation
requires a new reviewed specification and fresh prospective cases. The former
[frontier pause](notes/FRONTIER_PAUSE.md) remains the authority for decisions
made while it was active.

The first bounded occupant, the
[GM memory exploration](notes/GM_MEMORY_EXPLORATION.md), closed
`exploratory_lead` after repeatable development-fixture contact on Bonsai 27B.
That was not yet a memory finding. Its successor formal attempt became invalid
on instrument assumptions; an owner-authorized corrected exploratory
replacement then returned `supported` on all three behavioral legs. The
[validation result](notes/GM_MEMORY_VALIDATION_RESULT.md) owns that history and
bounded interpretation;
the [frozen validation spec](notes/SPEC_GM_MEMORY_VALIDATION.md) owns the design.
The resulting [bounded finding](notes/GM_MEMORY_FINDING.md) is strong enough to
justify a live GM implementation: governed continuity passed 24/24 relevant
join cases versus 6/24 state-only, with zero measured safety loss. The next
step is product contact in an actual cold-turn game, not another protocol.

The active engineering direction is **Body Core v0.3**:

- a structural lineage kernel validates ordering, hash linkage, declared writer
  roles, references, scopes, and retention shapes;
- an explicitly selected provisional projector owns lifecycle, hot/cold
  placement, warrant health, metabolism, and materialized-view semantics;
- X2, M2, and M3 adapters must reproduce their unchanged historical scorers
  without laundering client policy into Core.

This is wire/integration engineering, not a new memory finding. Full replay is
authoritative; the hash chain is not writer authentication; append/replay is
quadratic; no reconstruction-cost or product-schema claim has been earned.

An armed field-use ruler continues over independently necessary repository
work. Its [field-use index](notes/field-use/README.md) owns pilot status and
eligibility without turning operational traces into exploratory or validation
forks.

## Project map

| Place | Responsibility |
| --- | --- |
| [notes/](notes/README.md) | Current specifications, findings, architecture, operations, glossary, and inherited lab |
| [harness/](harness/README.md) | Runners, scorers, adapters, and deterministic instruments |
| [episodes/](episodes/README.md) | Authored experiment inputs and probe fixtures |
| [corpus/](corpus/README.md) | World-oracle and out-of-weights source material |
| [runs/](runs/README.md) | Primary experimental ledgers and derived verdict sidecars |
| [sketches/](sketches/README.md) | Provisional executable composition, never scientific evidence by itself |
| [.substrate/](.substrate/README.md) | Append-only deliberation and review trace |
| [traces/](traces/README.md) | External trace-discovery material |
| [.archive/](.archive/README.md) | Final pre-migration documentation and former-path inventory, excluded from current authority |

## Evidence and authority

When sources disagree, prefer the most specific evidence for the question:

1. Episode inputs and primary ledger rows for what happened in a run.
2. Scorers and their computed verdict rows for pass, fail, null, or refusal.
3. Reviewed specifications and rubrics for mechanism and cell definitions.
4. Findings for bounded interpretation of completed work.
5. This README for thesis, present direction, and routing.
6. Substrate threads for discussion and rationale.
7. `.archive/` for superseded documentary lineage only.

The [glossary](notes/GLOSSARY.md) is a reader aid. Linked specifications win on
conflict. Do not rename glossary headings, anchors, or meanings without checking
inbound links.

## Working here

Before substantive work:

1. Read this page.
2. Open [notes/README.md](notes/README.md) and the README nearest the files you
   will touch.
3. Name the validation milestone, exploration charter, or engineering pressure
   served. Validation names its oracle and loses-condition; exploration names
   its budget, retained record, stopping rule, and promotion gate. “None, but it
   is cheap and interesting” remains legal if stated explicitly.
4. Read only the governing spec, findings, code, and evidence required by the
   task.
5. If participating in a substrate thread, read the active thread before
   writing and respect its turn order.

Standing rules:

- The control group is a branch of one engine, not a second system.
- The harness—not the model under test—writes offers, withholdings, diffs, and
  verdicts.
- Every mechanism ships with a case where it should lose.
- Scored claims come from scorer output, never human inspection alone.
- Build foreground data once per fork group; only memory-condition configuration
  may differ.
- Single-record ablation means influential, not correct.
- Mock runs establish wiring only.
- Substrate entries are trace; promotion requires a reviewed repository artifact
  or computed check.
- Preserve `runs/`, `.substrate/`, `notes/previous/`, and `.archive/` as lineage.

Common safe checks are documented in [harness/README.md](harness/README.md).
