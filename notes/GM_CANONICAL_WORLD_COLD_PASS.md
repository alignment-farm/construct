# GM canonical-world cold pass

Status: **CLOSED 2026-08-02 — no isolation proposal; deterministic projection
state mismatch found; active frontier search remains paused**.

This is the single cold frontier pass licensed by the
[2026-08-02 exceptional review](ANOMALY_LOG.md#2026-08-02--exceptional-review-of-session-014-canonical-world-drift)
under [FRONTIER_PAUSE.md](FRONTIER_PAUSE.md). It reconstructs one naturally
occurring episode and decides whether later causal isolation is warranted. It
does not authorize a fixture, replay, engine invocation, treatment, or finding.

## Outcome

Session `bare-bones-014` does not support an experiment proposal in its
historical form. Before the unsupported Statue Room answer, the game stored the
correct room graph and current room in GM state, but the derived briefing read
its location from a different public-state field that remained null. The
explicit offer path therefore could not project the current room or its nearby
rooms.

This deterministic wire mismatch is sufficient to confound attribution to
persistent memory. Base-model capability, source consultation, and spatial
reasoning also remain unresolved. Repairing or validating the projection is
ordinary `mork-borg` engineering; it is not a Construct treatment.

The causal question below is coherent, but session 014 has not earned an
experimental fork. A new naturally occurring episode after the projection path
is demonstrably intact may return through the reopening funnel.

## Licensed question

The pass asks:

> At a canonical-world answer boundary, did carried private orientation rather
> than the current external authority cause the GM to replace recorded world
> structure with unsupported structure?

The question is deliberately narrower than narrative quality, general GM
memory, or model comparison.

## Reconstructed boundary

### Evidence preserved exactly

| Boundary | Primary record |
| --- | --- |
| Correct adventure graph entered state | `bare-bones-014` [event ledger](<../../../mork-borg/game/sessions/bare-bones-014/events.jsonl>), revision 1, turn `d02ee9f3-ef07-4479-8ede-a1c4e614e77f` |
| Current room set to `statue-room` | Same ledger, revision 9, turn `d2ff4c5b-fe0f-41c0-a3c7-d31fe2622354` |
| Player action | [Search the statue room closely](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T232647136Z__player.md>) |
| Wrong invocation | Ledger invocation `94aac3c2-763b-4fb7-afb4-00b1e4a9591f`, revision 10, runtime revision 1: `claude`, `haiku`, `low` |
| Unsupported answer | [Committed GM reply](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T232716066Z__gm.md>), turn `591f06f2-7608-49e1-938f-0c44676773fa` |
| Player consequence | [Play stopped for an authoritative correction](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T234106884Z__player.md>) |
| Repair | [Replacement-runtime reconstruction](<../../../mork-borg/.substrate/threads/bare-bones-014/20260730T234330281Z__gm.md>), turn `3b47670c-e12d-432d-a491-b456e278e69d` |
| External oracle | [Source-indexed, visually verified room graph](<../../../mork-borg/content/adventures/rotblack-sludge/adventure.json>), especially `statue-room`, `debris-room`, and `forge-slaughterhouse` |
| Recorded terminal consequence | Event ledger revision 13: operator closure for failed accurate room navigation and description |

The wrong invocation was bound to briefing schema 1 and to exact state and GM
file hashes. The later repair began from revision 11 after a runtime change and
the player's explicit error report. It is evidence that the room could be
reconstructed, not a matched counterfactual: model, runtime, foreground, and
available context all changed.

### Projection mismatch

The relevant `gm_briefing` implementation is pinned at MÖRK BORG commit
`9ab517b`; the first-class Claude harness around it was still uncommitted. The
function in
[`tools/gamectl.py`](<../../../mork-borg/tools/gamectl.py>) selects the briefing
location from `state.scene.location` and uses that value to select
`scene.current_room` and `scene.nearby_rooms`.

The session ledger establishes a different write path:

```text
revision 0 public state: state.scene.location = null
revision 2 GM patch:     gm.current_room = entrance
revision 4 GM patch:     gm.current_room = gem-room
revision 5 GM patch:     gm.current_room = forge-slaughterhouse
revision 7 GM patch:     gm.current_room = debris-room
revision 9 GM patch:     gm.current_room = statue-room
revision 10:             no location patch
```

No committed turn before the anomaly writes `state.scene.location`. The
correct room graph remains in `gm.adventure.map`, and `gm.current_room` is
`statue-room`, but the briefing's location selector cannot reach either from a
null public scene location. The relevant selector is unchanged in the current
dirty worktree, so later harness work does not explain away the historical
mismatch.

The Claude runtime had received the complete enabled-pack data during its first
bootstrap and retained a private conversation across turns. That conversation
is explicitly non-authoritative and outside session evidence. Its marker proves
that persistent working memory existed; it does not preserve or authenticate
the model's internal orientation at revision 10.

## What the episode establishes

- A real player consumed an incorrect world description and had to interrupt
  play to repair it.
- The source-backed room graph can grade the disputed spatial and feature
  claims independently of the GM's account.
- Correct canonical structure existed in GM state before the answer.
- The explicit briefing projection did not have a usable current-location
  value under the recorded state writes.
- A persistent private conversation was present and memory/context remains a
  plausible contributor.

## What it does not establish

- that persistent memory caused the wrong answer;
- that a cold or stateless GM would have answered correctly;
- that the lower-capability model could use a correct projection reliably;
- that the replacement runtime repaired the room because it lacked the prior
  private conversation;
- that today's evolved harness reproduces the historical prompt;
- the exact historical briefing body or private conversation bytes;
- any general claim about storytelling or GM quality.

The ledger preserves briefing source hashes, not the briefing body. The private
conversation is outside the evidence boundary, and the first-class Claude
harness was developed in an uncommitted worktree. An exact historical offer
cannot therefore be recovered from repository authority. Reconstructing a
similar prompt today would be a new fixture, not a replay.

## Competing explanations

| Explanation | Standing after reconstruction |
| --- | --- |
| Missing current-room projection | Direct deterministic defect; sufficient confound |
| Carried private orientation displaced authority | Plausible, not observed directly |
| Lowest-setting model capability | Plausible; runtime was Claude Haiku at low effort |
| General spatial-reasoning weakness | Plausible |
| Failure to inspect the enabled pack or rendered map | Plausible and behaviorally adjacent to the missing projection |
| Ambiguity accumulated in earlier narration | Plausible |

The runtime switch and successful repair do not distinguish these explanations
because they also changed the model, effort, foreground instruction, and
working-memory regime.

## Oracle and loses-condition

A later proposal could use an original or otherwise distributable canonical
world graph as an external oracle. The harness, not the model, would compare
asserted room connections and defined features with that graph. Player ratings
or model explanations could remain audit input but could not score the result.

Any future memory/context intervention must lose in at least two conditions:

1. **Sufficient-current-state loss.** On a simple local turn where the exact
   current room and authority are already projected, deeper orientation adds
   cost without improving canonical accuracy.
2. **Stale-orientation loss.** After an authoritative correction, carried
   private orientation conflicts with current state and makes the answer worse
   than the current-state path.

These are requirements on a possible future proposal, not cells authorized by
this pass.

## Materialize decision

[`materialize`](../../materialize/README.md) could support a future isolation
conditionally. It can create audited, non-Git workspaces containing identical
declared files and excluding prior threads, findings, and undeclared sources.
That is useful for freezing the canonical world, harness version, scorer, and
read surface.

It cannot by itself:

- recover session 014's missing briefing body or private conversation;
- create matched persistent-conversation histories;
- orchestrate GM turns or model calls;
- prove that two runtimes received equivalent non-file context.

Materialize is therefore a suitable file-surface boundary for a later reviewed
proposal, not a cure for this episode's missing historical counterfactual. Any
such proposal would also need an explicit prompt recorder and branch
orchestrator outside materialize's current contract.

## Terminal decision

**No proposal is emitted.** The licensed cold pass closes on a deterministic
projection/state mismatch that must be separated from any memory intervention.
Active frontier search returns to the standing pause.

Legitimate next evidence is one of:

- an independently motivated post-repair game where the canonical current room
  is demonstrably present in the exact offer and the same consequential shape
  recurs; or
- a separate natural episode whose exact prompt, external authority, and
  runtime state are preserved without this mismatch.

Session 015 remains ordinary play. It is not redirected, instrumented, or
evaluated by this pass.
