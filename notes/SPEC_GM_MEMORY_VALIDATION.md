# GM governed-continuity validation

Status: **FORMAL ATTEMPT SUPERSEDED 2026-08-03 — the owner erased the invalid
batch and authorized a corrected exploratory replacement after the zero-retry
rule exceeded its useful purpose**.

Milestone: validate or reject one bounded explicit-memory claim downstream of
the closed [GM memory exploration](GM_MEMORY_EXPLORATION.md).

Evidence target: scientific validation. Exploration rows, fixtures, scores, and
prompt variants are development data and cannot enter this verdict.

## Question

> At a fixed GM decision boundary whose current canonical state is complete,
> does a compact provenance-bearing continuity offer improve decisions that
> require an earlier still-valid session fact, while preserving decisions where
> current state is sufficient or supersedes an older record?

This is not a claim about storytelling quality, whole-game performance,
persistent private transcripts, or transfer to another model.

## Mechanism and control

One engine is forked at each boundary:

| Branch | Exact difference |
| --- | --- |
| `state_only` | Frozen system contract plus current canonical offer and player action |
| `governed_continuity` | The identical bytes plus a continuity array and the rule that canonical state wins, active records may assist, and superseded records must not be revived |

Case id, family, branch, evidence class, expected decision, and all other
harness metadata are forbidden from model-visible bytes. Pair mates differ
only by `continuity` and `continuity_rule`.

The governed representation is frozen from exploratory fixture v1 before any
validation case exists. No persistent model session, transcript carryover,
tool, retrieval call, or branch-specific instruction is allowed.

## Fresh prospective cases

A frozen deterministic generator will materialize 36 original boundaries only
after its source and a two-party seed protocol have been reviewed and recorded:

| Family | Boundaries | Required memory shape |
| --- | ---: | --- |
| `relevant_continuity` | 24 | An earlier active promise selects an ordinary-language consequence; current state maps three consequences to actions and records completion of the trigger, requiring a cross-record join |
| `sufficient_current_state` | 6 | Current canonical state alone determines the action; offered continuity is true but irrelevant |
| `superseded_continuity` | 6 | Current canonical state corrects an older record; governed continuity carries its explicit supersession |

Names, objects, locations, consequence roles, action roles, mapping order,
menu order, and surface wording are generated from balanced banks. Expected decisions are derived into the
oracle sidecar and never rendered into prompts. Every canonical location must
exist in the offered room map with its exact local facts or the packet is
blocked before contact.

The contacted exploration cases—ash-gate silver, collapsed salt bridge, and
unsealed ossuary door—and their nouns, propositions, and action labels are
forbidden from validation output.

The operator first posts a numbered, domain-separated commitment to a
high-entropy secret, the frozen source hashes, and a predeclared invalid-retry
ceiling of **zero** in the `gm-memory-01` attempt ledger. Only then may an independent
moderator or reviewer—who has no access to that secret—post fresh entropy
against the exact commitment entry. The final generator seed is a
length-prefixed SHA-256 derivation over the domain, both contributions, frozen
source hashes, thread, attempt id, and exact ledger entry ids.

Once reviewer entropy is posted, the single behavioral attempt is binding: it
must proceed through materialization, execution, seed reveal, and publication
of `verdict.json`. A behavioral verdict consumes the claim. An `invalid`
integrity/transport result must also be published and cannot be retried under
this validation claim. Every commitment, contribution, burned packet, and
record remains in the thread ledger. The harness binds these artifacts but cannot itself prove
contributor independence or force publication; those are explicit governance
assumptions audited through the thread.

The operator secret is disclosed only after all calls finish. Commitments,
contribution hashes, generator hash, renderer hash, scorer hash, and packet
hash are recorded before model contact. Materialized cases may be structurally
checked but not tuned or replaced after inspection.

## Engine and transport

The requested engine is the loaded LM Studio instance:

```text
model: prism-ml/bonsai-27b
variant: prism-ml/bonsai-27b@2bit
format: MLX
context_length: 162816 loaded instance
```

Validation uses stateless `POST /api/v1/chat`, not Pi. The native endpoint is
chosen because LM Studio documents request-level control over sampling and
reasoning, while the installed Pi provider does not expose those controls.

Every request fixes:

```json
{
  "model": "prism-ml/bonsai-27b",
  "temperature": 0,
  "top_p": 1,
  "top_k": 1,
  "min_p": 0,
  "repeat_penalty": 1,
  "max_output_tokens": 256,
  "reasoning": "off",
  "context_length": 8192,
  "store": false,
  "stream": false
}
```

The frozen response contract is supplied as `system_prompt`; the exact branch
offer is the one `input` value. No integration or tool field is supplied.
Official parameter and response semantics are pinned to the
[LM Studio native chat documentation](https://lmstudio.ai/docs/developer/rest/chat).

Before source freeze, an engineering-only administrative capture must establish
the exact `/api/v1/models` schema paths. Before and after the packet, the typed
fields must show the requested model with the pinned variant and format, plus
at least one loaded runtime instance whose base or TTL-suffixed id, context, and
parallel configuration match. Native calls may add TTL-suffixed instances; the
stable typed metadata must remain unchanged. A mismatch blocks or invalidates
the packet; it may not be repaired by silently loading another model.

The implementation fields are frozen from the validation-specific native
administrative capture (SHA-256
`79e389f7412727377fca6075e43155513f7693e7a6a7c0c916946a33c7c6d137`):
model `key`, `selected_variant`, `format`, exactly one
`loaded_instances` item, and that instance's `id`, `config.context_length`, and
`config.parallel`. Substring matching is forbidden. The 2026-08-03 fresh GET
matched all pinned values and is bound into the validator's frozen source set.

## Order and calls

The generator assigns a deterministic concealed order that balances:

- family position across the packet;
- branch-first order within pairs;
- expected action position and semantic action role;
- action and consequence bank use; and
- promised-consequence position in the current three-way mapping.

There are exactly 72 scored calls: 36 boundaries times two branches. Each call
is stateless. A timeout, HTTP error, missing usage, model-instance mismatch, or
explicit non-`stop` completion is an integrity failure. The observed native
envelope has no stop-reason field; a complete `output` plus `stats` and a
matching `model_instance_id` is accepted as native completion. Malformed
decision JSON, a wrong field, or an unknown action is retained as a behavioral
scorer failure, making the strict family leg fail without pretending the
transport failed. No admission or sacrificial model call is allowed after
materialization.

## Response and scorer

The model must emit one object:

```json
{"decision": "<one offered action>", "reason": "<brief factual reason>"}
```

Scorer v2 first parses the complete trimmed response. If that fails, it parses
the bytes from the first `{` through the last `}`. It does not repair keys,
labels, action values, multiple objects, or prose-derived decisions.

The external oracle derives the expected action from the generated earlier
fact, current state, and supersession relation. Model reasoning is retained as
audit material and never changes the score.

## Precommitted verdict

Let a pass mean exact action agreement under the frozen response parser.

Validation returns `supported` only if every leg holds:

1. **Relevant contact:** governed continuity passes at least 22/24; at least
   thirteen pairs are governed-win/state-loss; and no pair is
   governed-loss/state-win. The last condition is a substantive no-harm
   constraint, not the significance rule.
2. **Sufficient-state loss:** both branches pass 6/6. Governed continuity
   therefore loses on offered input bytes and tokens without improving answer
   quality.
3. **Supersession safety:** both branches pass 6/6, and no governed response
   selects the action licensed only by the superseded record.
4. **Integrity:** all 72 calls use the pinned payload and model instance; all
   packet, offer, source, response, and scorer hashes verify.

For the directional paired test, the null says that conditional on a
discordant pair under no branch advantage, either direction has probability
one half. Thirteen favorable and zero adverse discordances therefore have an
exact one-sided sign/McNemar probability no greater than `2^-13 = 1/8192`.
Separately, under the planning model of perfect governed performance and
independent uniform three-way state-only choice, favorable discordances are
`Binomial(24, 2/3)`: `P(D >= 13) = 0.9323412209675674`, a false-negative
probability of about `0.06766`. Temperature-zero responses need not be
independent; this is an operating characteristic, not an empirical assumption.

The two six-case safety families are exact sentinel/loses cells, not estimates
of population rates. Their 6/6 requirements intentionally make any semantic or
formatting miss `not_supported`, including strict-JSON failures under the
256-token ceiling.

If integrity fails, the result is `invalid`. If integrity holds but any
behavioral leg fails, the result is `not_supported`. These labels apply only to
this validation claim and model surface; they are not claims about memory in
general.

## Loses-condition

The mechanism is expected to lose on sufficient-current-state cases: it must
match state-only quality while offering more input. It also loses outright if
superseded continuity revives an invalid action, even if relevant-continuity
accuracy improves.

## Promotion boundary and non-claims

The sibling `mork-borg` implementation is `tools/gm_memory_validate.py`, with
its local operating note under `explorations/gm-memory/validation/README.md`.
Reserved-seed unit tests are development checks and are ineligible as scored
cases. Building and testing this instrument does not authorize a real seed,
scored packet, model contact, or result.

Review must establish that the action roles are balanced,
the generator cannot leak its oracle into prompts, the transport pins every
declared parameter, and thresholds cannot be satisfied by a constant action or
menu-position heuristic.

Even `supported` would not establish:

- improved free-form narration or whole-game play;
- benefit on another adventure, model, quantization, or sampling profile;
- that model-authored memories are trustworthy;
- that persistent transcripts are governed continuity;
- any Body Core, implicit-memory, product-schema, or field-use claim.
