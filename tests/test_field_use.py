"""Wire tests for the endorsed field-use protocol capture layer.

These tests verify operational capture integrity only.  They create no field
data, start no pilot, contact no model, and establish no memory finding.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from sketches.next_substrate.core import (
    EVIDENCE_CLASS,
    LineageStore,
    ReplayRefusal,
    Writer,
    canonical_digest,
)
from sketches.next_substrate.field_use import (
    MODE_CONSULTED,
    MODE_SHADOW,
    ORIGIN_FIELD_CAPTURE,
    ORIGIN_INDEPENDENT,
    ORIGIN_MIXED,
    PROTOCOL_PATH,
    PROTOCOL_SHA256,
    STATUS_ABANDONED,
    STATUS_CONSULTED,
    STATUS_NO_PROJECTION,
    STATUS_SHADOW,
    SURFACE_NONE,
    SURFACE_PROJECTED,
    SURFACE_RAW,
    TERMINAL_CONFOUNDED,
    ArtifactReference,
    ConsultationPlan,
    ConsultedLineage,
    FieldUseCapture,
    FieldUseSpec,
)
from sketches.next_substrate.policy import (
    POLICY_PROFILE_ID,
    V02_POLICY_PROJECTOR,
)


BASE_COMMIT = "a" * 40
RUNTIME = Writer("source-runtime", "runtime")
OBSERVER = Writer("source-observer", "observer")


def _write(root: Path, relative: str, text: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _artifact(
    root: Path,
    relative: str,
    *,
    artifact_kind: str,
    text: str,
) -> ArtifactReference:
    path = _write(root, relative, text)
    return ArtifactReference.from_file(
        root,
        path,
        artifact_kind=artifact_kind,
        revision=BASE_COMMIT,
    )


def _spec(field_use_id: str, mode: str) -> FieldUseSpec:
    return FieldUseSpec(
        field_use_id=field_use_id,
        repository="construct",
        base_commit=BASE_COMMIT,
        task_id=f"task-{field_use_id}",
        mode=mode,
        declared_by="human_operator",
        operator_id="human-user",
        actor_id="codex-field-actor",
        encounter_observer_id="human-task-observer",
        environment={"model": "gpt-5.6-sol", "surface": "repository"},
    )


def _start(root: Path, field_use_id: str, mode: str) -> FieldUseCapture:
    encounter = _artifact(
        root,
        f"native/{field_use_id}-task.md",
        artifact_kind="task_encounter",
        text=f"independently supplied task {field_use_id}\n",
    )
    return FieldUseCapture.start(root, _spec(field_use_id, mode), encounter)


def _source_lineage(root: Path, relative: str) -> tuple[Path, tuple[str, ...]]:
    path = root / relative
    store = LineageStore(path, projector=V02_POLICY_PROJECTOR)
    invocation = store.append(
        "invocation_started",
        writer=RUNTIME,
        authority="system_record",
        payload={"source": relative},
    )
    encounter = store.append(
        "encounter_observed",
        writer=OBSERVER,
        authority="external_observation",
        causal_parent_ids=[invocation["event_id"]],
        invocation_id=invocation["event_id"],
        payload={"observation": "ordinary prior work"},
    )
    return path, (invocation["event_id"], encounter["event_id"])


def _source(
    root: Path,
    relative: str,
    *,
    source_id: str,
    origin: str,
) -> ConsultedLineage:
    path, record_ids = _source_lineage(root, relative)
    artifact = ArtifactReference.from_file(
        root,
        path,
        artifact_kind="body_core_lineage",
        revision=BASE_COMMIT,
    )
    return ConsultedLineage(
        source_id=source_id,
        origin=origin,
        artifact=artifact,
        record_ids=record_ids,
    )


def _shadow_plan() -> ConsultationPlan:
    return ConsultationPlan(
        status=STATUS_SHADOW,
        surface=SURFACE_NONE,
        lineage_origin=None,
        declared_by="human-user",
    )


def _raw_plan(
    *sources: ConsultedLineage,
    lineage_origin: str,
    status: str = STATUS_CONSULTED,
    reason: str | None = None,
) -> ConsultationPlan:
    return ConsultationPlan(
        status=status,
        surface=SURFACE_RAW,
        lineage_origin=lineage_origin,
        declared_by="human-user",
        sources=tuple(sources),
        reason=reason,
    )


def _finish(
    root: Path,
    capture: FieldUseCapture,
    *,
    field_use_id: str,
):
    action = _artifact(
        root,
        f"native/{field_use_id}-action.patch",
        artifact_kind="native_action",
        text=f"patch for {field_use_id}\n",
    )
    consequence = _artifact(
        root,
        f"native/{field_use_id}-test.log",
        artifact_kind="native_consequence",
        text=f"tests passed for {field_use_id}\n",
    )
    capture.record_action(action)
    capture.record_consequence(
        observer_id="external-test-observer",
        consequence=consequence,
    )
    return capture.complete()


def _expect_refusal(action: Callable[[], object], text: str) -> None:
    try:
        action()
    except ReplayRefusal as exc:
        assert text in str(exc), str(exc)
    else:
        raise AssertionError(f"expected refusal containing {text!r}")


def _rewrite(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def _rehash_chain(rows: list[dict]) -> None:
    previous = "0" * 64
    for row in rows:
        row["previous_event_hash"] = previous
        unsigned = {key: value for key, value in row.items() if key != "event_hash"}
        row["event_hash"] = canonical_digest(unsigned)
        previous = row["event_hash"]


def test_protocol_pin_matches_endorsed_bytes():
    assert hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest() == PROTOCOL_SHA256
    print("ok  field use: implementation binds the endorsed protocol bytes")


def test_shadow_capture_completes_without_exposing_lineage():
    with TemporaryDirectory() as td:
        root = Path(td)
        capture = _start(root, "shadow-001", MODE_SHADOW)
        frozen = capture.freeze_pre_action(_shadow_plan())
        receipt = _finish(root, capture, field_use_id="shadow-001")

        rows = capture.store.rows()
        assert receipt.terminal_status == "completed"
        assert receipt.event_count == 6
        assert all(row["evidence_class"] == EVIDENCE_CLASS for row in rows)
        assert frozen["payload"]["consultation_surface"] == SURFACE_NONE
        assert frozen["payload"]["lineage_origin"] is None
        assert capture.store.replay().views.state_items == {}
        assert FieldUseCapture.open(capture.ledger_path).receipt() == receipt
    print("ok  field use: shadow capture is complete, replayable, and state-inert")


def test_independent_raw_lineage_is_verified_and_declared():
    with TemporaryDirectory() as td:
        root = Path(td)
        source = _source(
            root,
            "native/prior-independent.body.jsonl",
            source_id="prior-independent",
            origin=ORIGIN_INDEPENDENT,
        )
        capture = _start(root, "raw-independent", MODE_CONSULTED)
        frozen = capture.freeze_pre_action(
            _raw_plan(source, lineage_origin=ORIGIN_INDEPENDENT)
        )
        receipt = _finish(root, capture, field_use_id="raw-independent")

        assert frozen["payload"]["lineage_origin"] == ORIGIN_INDEPENDENT
        assert frozen["payload"]["deterministic_counts"] == {
            "source_count": 1,
            "record_count": 2,
            "source_bytes": source.artifact.byte_count,
        }
        assert receipt.referenced_artifact_bytes > source.artifact.byte_count
    print("ok  field use: independent raw lineage is content-pinned before action")


def test_field_capture_and_mixed_supply_remain_visible():
    with TemporaryDirectory() as td:
        root = Path(td)
        field_source = _source(
            root,
            "runs/field_use/prior-field.body.jsonl",
            source_id="prior-field",
            origin=ORIGIN_FIELD_CAPTURE,
        )
        independent = _source(
            root,
            "native/prior-independent.body.jsonl",
            source_id="prior-independent",
            origin=ORIGIN_INDEPENDENT,
        )

        field_capture = _start(root, "field-fed", MODE_CONSULTED)
        field_row = field_capture.freeze_pre_action(
            _raw_plan(field_source, lineage_origin=ORIGIN_FIELD_CAPTURE)
        )
        assert field_row["payload"]["lineage_origin"] == ORIGIN_FIELD_CAPTURE

        mixed_capture = _start(root, "mixed-fed", MODE_CONSULTED)
        mixed_row = mixed_capture.freeze_pre_action(
            _raw_plan(
                field_source,
                independent,
                lineage_origin=ORIGIN_MIXED,
            )
        )
        assert mixed_row["payload"]["lineage_origin"] == ORIGIN_MIXED
        assert mixed_row["payload"]["deterministic_counts"]["source_count"] == 2
    print(
        "ok  field use: protocol-fed and mixed supply cannot masquerade as independent"
    )


def test_declared_origin_mismatch_refuses_before_freeze():
    with TemporaryDirectory() as td:
        root = Path(td)
        source = _source(
            root,
            "runs/field_use/prior-field.body.jsonl",
            source_id="prior-field",
            origin=ORIGIN_FIELD_CAPTURE,
        )
        capture = _start(root, "origin-mismatch", MODE_CONSULTED)
        _expect_refusal(
            lambda: capture.freeze_pre_action(
                _raw_plan(source, lineage_origin=ORIGIN_INDEPENDENT)
            ),
            "lineage_origin disagrees",
        )
        assert capture.validate().phase == "encounter_observed"
        assert len(capture.store.rows()) == 2
    print("ok  field use refusal: origin mismatch appends no frozen surface")


def test_projected_consultation_requires_independent_replay_identity():
    with TemporaryDirectory() as td:
        root = Path(td)
        independent = _source(
            root,
            "native/projected.body.jsonl",
            source_id="projected-independent",
            origin=ORIGIN_INDEPENDENT,
        )
        view_digest = (
            LineageStore(
                root / independent.artifact.external_ref,
                projector=V02_POLICY_PROJECTOR,
            )
            .replay()
            .views.digest()
        )
        capture = _start(root, "projected-independent", MODE_CONSULTED)
        frozen = capture.freeze_pre_action(
            ConsultationPlan(
                status=STATUS_CONSULTED,
                surface=SURFACE_PROJECTED,
                lineage_origin=ORIGIN_INDEPENDENT,
                declared_by="human-user",
                sources=(independent,),
                projector_id=POLICY_PROFILE_ID,
                view_digest=view_digest,
            )
        )
        assert frozen["payload"]["view_digest"] == view_digest

        field_source = ConsultedLineage(
            source_id=independent.source_id,
            origin=ORIGIN_FIELD_CAPTURE,
            artifact=independent.artifact,
            record_ids=independent.record_ids,
        )
        refused = _start(root, "projected-field", MODE_CONSULTED)
        _expect_refusal(
            lambda: refused.freeze_pre_action(
                ConsultationPlan(
                    status=STATUS_CONSULTED,
                    surface=SURFACE_PROJECTED,
                    lineage_origin=ORIGIN_FIELD_CAPTURE,
                    declared_by="human-user",
                    sources=(field_source,),
                    projector_id=POLICY_PROFILE_ID,
                    view_digest=view_digest,
                )
            ),
            "cannot supply independently motivated projected state",
        )
    print("ok  field use: projected views bind explicit independent replay identity")


def test_source_digest_and_record_id_drift_refuse_before_freeze():
    with TemporaryDirectory() as td:
        root = Path(td)
        source = _source(
            root,
            "native/drifting.body.jsonl",
            source_id="drifting",
            origin=ORIGIN_INDEPENDENT,
        )
        source_path = root / source.artifact.external_ref
        source_path.write_text(source_path.read_text() + "\n", encoding="utf-8")
        capture = _start(root, "source-digest-drift", MODE_CONSULTED)
        _expect_refusal(
            lambda: capture.freeze_pre_action(
                _raw_plan(source, lineage_origin=ORIGIN_INDEPENDENT)
            ),
            "byte_count drift",
        )
        assert capture.validate().phase == "encounter_observed"

        valid = _source(
            root,
            "native/record-drift.body.jsonl",
            source_id="record-drift",
            origin=ORIGIN_INDEPENDENT,
        )
        invalid_ids = ConsultedLineage(
            source_id=valid.source_id,
            origin=valid.origin,
            artifact=valid.artifact,
            record_ids=("ev-999999",),
        )
        capture = _start(root, "record-id-drift", MODE_CONSULTED)
        _expect_refusal(
            lambda: capture.freeze_pre_action(
                _raw_plan(invalid_ids, lineage_origin=ORIGIN_INDEPENDENT)
            ),
            "record ids do not exist",
        )
    print("ok  field use refusal: broken source pins cannot enter the frozen surface")


def test_negative_use_and_abandoned_consultation_are_first_class():
    with TemporaryDirectory() as td:
        root = Path(td)
        no_projection = _start(root, "no-projection", MODE_CONSULTED)
        row = no_projection.freeze_pre_action(
            ConsultationPlan(
                status=STATUS_NO_PROJECTION,
                surface=SURFACE_NONE,
                lineage_origin=None,
                declared_by="human-user",
                reason="no eligible projected state existed",
            )
        )
        assert row["payload"]["consultation_status"] == STATUS_NO_PROJECTION

        source = _source(
            root,
            "native/abandoned.body.jsonl",
            source_id="abandoned-source",
            origin=ORIGIN_INDEPENDENT,
        )
        abandoned = _start(root, "abandoned", MODE_CONSULTED)
        row = abandoned.freeze_pre_action(
            _raw_plan(
                source,
                lineage_origin=ORIGIN_INDEPENDENT,
                status=STATUS_ABANDONED,
                reason="operator abandoned consultation before action",
            )
        )
        assert row["payload"]["consultation_status"] == STATUS_ABANDONED
    print("ok  field use: negative and abandoned use survive without success filtering")


def test_actor_cannot_write_consequence_and_not_observed_is_explicit():
    with TemporaryDirectory() as td:
        root = Path(td)
        capture = _start(root, "external-consequence", MODE_SHADOW)
        capture.freeze_pre_action(_shadow_plan())
        action = _artifact(
            root,
            "native/external-consequence.patch",
            artifact_kind="native_action",
            text="patch\n",
        )
        capture.record_action(action)
        _expect_refusal(
            lambda: capture.record_consequence(
                observer_id="codex-field-actor",
                not_observed_reason="actor cannot certify itself",
            ),
            "cannot write consequence",
        )
        row = capture.record_consequence(
            observer_id="human-consequence-observer",
            not_observed_reason="native consequence not yet available",
        )
        assert row["payload"]["status"] == "not_observed"
        receipt = capture.complete()
        assert receipt.terminal_status == "completed"
    print("ok  field use: consequence is external or explicitly absent")


def test_redaction_and_repository_boundary_fail_closed():
    with TemporaryDirectory() as td, TemporaryDirectory() as outside_td:
        root = Path(td)
        outside = _write(Path(outside_td), "secret.txt", "secret\n")
        _expect_refusal(
            lambda: ArtifactReference.from_file(
                root,
                outside,
                artifact_kind="task_encounter",
                revision=BASE_COMMIT,
            ),
            "inside the repository",
        )

        encounter = ArtifactReference.redacted(
            artifact_kind="task_encounter",
            digest=hashlib.sha256(b"private task").hexdigest(),
            byte_count=len(b"private task"),
            reason="contains unnecessary personal data",
        )
        capture = FieldUseCapture.start(root, _spec("redacted", MODE_SHADOW), encounter)
        assert capture.store.rows()[1]["retention"]["mode"] == "redacted"
        assert "external_ref" not in capture.store.rows()[1]["retention"]
    print("ok  field use: repository escape refuses and redaction exposes no path")


def test_terminal_refusal_preserves_partial_trace_and_prevents_resume():
    with TemporaryDirectory() as td:
        root = Path(td)
        capture = _start(root, "terminal", MODE_SHADOW)
        receipt = capture.terminate(
            TERMINAL_CONFOUNDED,
            reason="capture changed the ordinary task",
        )
        assert receipt.terminal_status == TERMINAL_CONFOUNDED
        assert receipt.event_count == 3
        _expect_refusal(
            lambda: capture.freeze_pre_action(_shadow_plan()),
            "capture is terminal",
        )
        _expect_refusal(
            lambda: FieldUseCapture.start(
                root,
                _spec("terminal", MODE_SHADOW),
                _artifact(
                    root,
                    "native/retry-task.md",
                    artifact_kind="task_encounter",
                    text="retry task\n",
                ),
            ),
            "retry refused",
        )
    print("ok  field use refusal: partial trace is terminal and cannot be replaced")


def test_rehashed_semantic_origin_tamper_loses_to_field_validation():
    with TemporaryDirectory() as td:
        root = Path(td)
        source = _source(
            root,
            "native/semantic-tamper.body.jsonl",
            source_id="semantic-tamper",
            origin=ORIGIN_INDEPENDENT,
        )
        capture = _start(root, "semantic-tamper", MODE_CONSULTED)
        capture.freeze_pre_action(_raw_plan(source, lineage_origin=ORIGIN_INDEPENDENT))
        rows = capture.store.raw_rows()
        rows[2]["payload"]["lineage_origin"] = ORIGIN_FIELD_CAPTURE
        _rehash_chain(rows)
        _rewrite(capture.ledger_path, rows)

        _expect_refusal(
            lambda: FieldUseCapture.open(capture.ledger_path),
            "lineage_origin disagrees",
        )
    print("ok  field use refusal: rehashed semantic origin tamper fails closed")


if __name__ == "__main__":
    tests = sorted(
        (name, fn)
        for name, fn in globals().items()
        if name.startswith("test_") and callable(fn)
    )
    for _, fn in tests:
        fn()
    print(f"\nALL {len(tests)} FIELD-USE V0 WIRE TESTS PASS")
