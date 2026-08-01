Fetch https://arxiv.org/html/2607.25398v2

**They share a diagnosis and diverge on the lever.**

### The paper, briefly

HANDBOOK.md asks whether a long standing policy (20–124 page SOP) actually constrains an agent over a multi-tool episode — not whether the agent finishes the job. Strict, deterministic, two-sided rubrics (do the required things *and* don’t do the forbidden ones). Best config: **36.2%** under all-criteria pass. Failures cluster as: in-environment request beats policy, check-then-ignore, detail loss over the horizon, and false compliance reports.

That is a serious measurement of a real deployment pattern. The Incorrect-Behavior criteria and no-LLM-judge stance are the right kind of discipline.

### Where it meets Construct

Construct’s thesis is sharper and one layer earlier:

> Decision quality is often downstream of **offer quality**, not model quality.

HANDBOOK still mostly assumes the handbook is *in the reachable world* and asks whether the model stays faithful to it. Construct treats that as the industry default — and often the wrong office. Its five refusals map cleanly onto the paper’s failure shapes:

| HANDBOOK failure | Construct refusal / finding |
|---|---|
| Request overrides standing policy | R2 `present ≠ authorized`; M3 asserted-trust leaks |
| Reports compliance it didn’t achieve | R5 self-classification ≠ usage |
| Completing the job ≠ succeeding | R1/R3 — oracle on outcomes, not retrieval or divergence |
| Forbidden actions must be scored | R4 / loses-cells |

So the paper is strong evidence for Construct’s *motivation*: trusting a long document in context is a weak control. Related work in the paper even nods at compiling policies into deterministic guards — Construct is building the lab that can say when those guards earn their cost, and when they should lose.

### Where they are not the same project

- **HANDBOOK** measures *agent-side* long-horizon instruction following in a rich MCP company sim. Policy is content the agent must find and apply.
- **Construct** measures *memory architecture*: harness-written offer/withhold ledgers, forked lanes, out-of-band earned authority the model never sees, hot/cold metabolism, typed terminal states when the experiment band is empty.

HANDBOOK would score Construct’s W1′ failure (model fine; correction never offered) as something like “agent didn’t apply the right clause.” Construct would score it as an offer-boundary miss — and refuse to call model quality the cause.

Construct also insists on something HANDBOOK doesn’t need: governance-should-lose cells, control-as-branch, and external ledger writing. That is narrower and more demanding, and it is why Construct can retire organs honestly (X1, X4, EFC v0–v2) instead of only reporting low pass rates.

### Bottom line

HANDBOOK is a high-quality *capability* benchmark for “standing instructions in context.” Construct is a *mechanism* lab for “what is allowed to become context, and what must constrain action without relying on the model to remember the handbook.”

They are complementary, not competitive. If HANDBOOK’s numbers stay this bad, that strengthens Construct’s claim that the binding work belongs at the offer/action boundary — not in hoping Claude reads page 87 of a PDF forty tool calls later. Construct’s current pause on new scientific mechanisms and pivot to Body Core / field-use is coherent with that: the narrow M/X results already earned some organs; the open question is whether they compose into a body that can carry real work without manufacturing episodes.

---

NEXT_SUBSTRATE, BODY_MAP

Those two docs sharpen the comparison a lot.

### What they add

`NEXT_SUBSTRATE.md` is the architectural claim: the LM is not the resident — **the body is**. Persistent governed metabolism around an intermittent engine. Three planes: immutable lineage → governed materialization → sparse activation field. The offer boundary lives in that last plane; disposition/action checks sit post-offer, pre-commit.

`BODY_MAP.md` is the honesty layer on top of that claim. Every part is labeled **earned / provisional / candidate / unlicensed**, so a mermaid diagram cannot quietly promote anatomy into findings. Right now: offer boundary, narrow M2/M3/X2 results are earned; Body Core v0.3 and field-use are provisional wire; EFC and the obligation candidate are parked; most “wanted offices” are still unlicensed.

### Against HANDBOOK.md

HANDBOOK and Construct start from the same sentence — rules live somewhere other than the request — then go opposite directions:

| | HANDBOOK | NEXT body |
|---|---|---|
| Standing instructions | Long SOP the agent must find and obey | Binding work at offer/action boundary; “more context ≠ more memory” |
| Where policy lives | Reachable workspace content | Lineage / materialization / activation |
| LM role | Employee following the handbook | Intermittent citizen; cannot mint authority |
| What success looks like | Strict rubric pass on environment state | Forked lanes, loses-cells, typed refusals |
| What’s shipped | Scored benchmark (best ~36%) | Architecture cold-reviewed; scientific body milestone still **none** |

HANDBOOK is evidence that the industry pattern Construct refuses — “wake the model into a giant standing document and trust it” — fails at scale. The body docs are the proposed alternative: don’t ask the model to remember Tuesday; assemble a sparse field already altered by consequence, and keep the irreversible checks outside the model’s mouth.

### The important asymmetry

HANDBOOK’s evidence is ahead of any substrate design. Construct’s architecture is ahead of its earned whole-body evidence. Body-0 closed `not_engaged`; EFC refused three ways; obligation admission failed grammar; frontier search is paused. So NEXT_SUBSTRATE is not “we built the thing HANDBOOK shows is needed.” It is “here is the body we would build, and here is the maturity register that refuses to pretend we already have it.”

That discipline is the project’s real product so far. HANDBOOK would make a good *stress environment* for such a body later — but only after some office earns a consumer, an oracle, and a loses-condition. Right now, dropping Body Core into HANDBOOK would mostly measure whether the wire sketch survives enterprise clutter, not whether the body thesis is true.

