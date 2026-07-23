"""Field-use capture over Body Core v0.3.

This module implements the ruler in ``notes/FIELD_USE_PROTOCOL_V0.md``.  It
records independently motivated repository work without assigning treatment,
scoring model behavior, admitting cognitive state, or promoting operational
origin into evidence.  Every row remains ``wire_integration_only``.

The capture layer is intentionally manual.  It does not intercept prompts or
commands, choose tasks, create a projector, or start the bounded pilot.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from .core import LineageStore, Writer, replay, require
from .policy import POLICY_PROFILE_ID, V02_POLICY_PROJECTOR


PROTOCOL_ID = "field-use-protocol-v0"
PROTOCOL_SHA256 = "29dbc5a59d60986c6b41f88999eae610067ba572606424f3a607ee3ada327ab1"
PROTOCOL_PATH = (
    Path(__file__).resolve().parents[2] / "notes" / "FIELD_USE_PROTOCOL_V0.md"
)

MODE_SHADOW = "shadow"
MODE_CONSULTED = "consulted"
MODES = frozenset({MODE_SHADOW, MODE_CONSULTED})

SURFACE_NONE = "none"
SURFACE_RAW = "raw_lineage"
SURFACE_PROJECTED = "projected_view"
CONSULTATION_SURFACES = frozenset({SURFACE_NONE, SURFACE_RAW, SURFACE_PROJECTED})

STATUS_SHADOW = "shadow"
STATUS_CONSULTED = "consulted"
STATUS_NO_PROJECTION = "no_projection_available"
STATUS_NOT_CONSULTED = "available_not_consulted"
STATUS_REFUSED = "projection_refused"
STATUS_ABANDONED = "consultation_abandoned"
CONSULTATION_STATUSES = frozenset(
    {
        STATUS_SHADOW,
        STATUS_CONSULTED,
        STATUS_NO_PROJECTION,
        STATUS_NOT_CONSULTED,
        STATUS_REFUSED,
        STATUS_ABANDONED,
    }
)

ORIGIN_INDEPENDENT = "independent"
ORIGIN_FIELD_CAPTURE = "field_capture"
ORIGIN_MIXED = "mixed"
LINEAGE_ORIGINS = frozenset({ORIGIN_INDEPENDENT, ORIGIN_FIELD_CAPTURE, ORIGIN_MIXED})
SOURCE_ORIGINS = frozenset({ORIGIN_INDEPENDENT, ORIGIN_FIELD_CAPTURE})

TERMINAL_REFUSED = "capture_refused"
TERMINAL_CONFOUNDED = "capture_confounded"
TERMINAL_KINDS = frozenset({TERMINAL_REFUSED, TERMINAL_CONFOUNDED})

EVENT_SEQUENCE = (
    "invocation_started",
    "encounter_observed",
    "field_use_pre_action_frozen",
    "field_use_action_referenced",
    "consequence_observed",
    "invocation_completed",
)

FIELD_RUNTIME = Writer("field-use-runtime-v0", "runtime")
FIELD_CONTROLLER = Writer("field-use-freezer-v0", "controller")

_SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
_EVENT_ID = re.compile(r"^ev-[0-9]{6}$")


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def _is_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _require_text(value: Any, name: str) -> str:
    require(isinstance(value, str) and value.strip(), f"{name} is required")
    return value


def _require_safe_id(value: Any, name: str) -> str:
    text = _require_text(value, name)
    require(bool(_SAFE_ID.fullmatch(text)), f"{name} has unsafe characters")
    return text


def _protocol_digest() -> str:
    require(PROTOCOL_PATH.is_file(), "endorsed field-use protocol is missing")
    return hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest()


def _verify_protocol_pin() -> None:
    require(
        _protocol_digest() == PROTOCOL_SHA256,
        "field-use protocol bytes disagree with the endorsed pin",
    )


def _resolve_reference(repository_root: Path, artifact: ArtifactReference) -> Path:
    require(artifact.mode == "reference", "artifact is not a retrievable reference")
    root = Path(repository_root).resolve()
    resolved = (root / artifact.external_ref).resolve()
    require(
        resolved.is_relative_to(root),
        "referenced artifact escapes the repository",
    )
    require(resolved.is_file(), "referenced artifact is missing")
    data = resolved.read_bytes()
    require(len(data) == artifact.byte_count, "referenced artifact byte_count drift")
    require(
        hashlib.sha256(data).hexdigest() == artifact.digest,
        "referenced artifact digest drift",
    )
    return resolved


@dataclass(frozen=True)
class ArtifactReference:
    """A content-pinned native artifact without copied artifact content."""

    artifact_kind: str
    digest: str
    byte_count: int
    mode: str
    external_ref: str | None = None
    revision: str | None = None
    reason: str | None = None

    @classmethod
    def from_file(
        cls,
        repository_root: Path,
        path: Path,
        *,
        artifact_kind: str,
        revision: str,
    ) -> ArtifactReference:
        root = Path(repository_root).resolve()
        resolved = Path(path).resolve()
        require(
            resolved.is_relative_to(root),
            "referenced artifact must remain inside the repository",
        )
        require(resolved.is_file(), "referenced artifact does not exist")
        data = resolved.read_bytes()
        return cls(
            artifact_kind=_require_safe_id(artifact_kind, "artifact_kind"),
            digest=hashlib.sha256(data).hexdigest(),
            byte_count=len(data),
            mode="reference",
            external_ref=resolved.relative_to(root).as_posix(),
            revision=_require_text(revision, "artifact revision"),
        )

    @classmethod
    def redacted(
        cls,
        *,
        artifact_kind: str,
        digest: str,
        byte_count: int,
        reason: str,
    ) -> ArtifactReference:
        artifact = cls(
            artifact_kind=_require_safe_id(artifact_kind, "artifact_kind"),
            digest=digest,
            byte_count=byte_count,
            mode="redacted",
            reason=_require_text(reason, "redaction reason"),
        )
        artifact.validate()
        return artifact

    def validate(self) -> None:
        _require_safe_id(self.artifact_kind, "artifact_kind")
        require(_is_sha256(self.digest), "artifact digest must be lowercase SHA-256")
        require(
            isinstance(self.byte_count, int) and self.byte_count >= 0,
            "artifact byte_count must be a non-negative integer",
        )
        require(self.mode in {"reference", "redacted"}, "invalid artifact mode")
        if self.mode == "reference":
            _require_text(self.external_ref, "artifact external_ref")
            _require_text(self.revision, "artifact revision")
            require(
                self.reason is None, "reference artifact cannot have redaction reason"
            )
        else:
            _require_text(self.reason, "redaction reason")
            require(self.external_ref is None, "redacted artifact cannot expose a path")
            require(self.revision is None, "redacted artifact cannot expose a revision")

    def as_metadata(self) -> dict[str, Any]:
        self.validate()
        metadata: dict[str, Any] = {
            "artifact_kind": self.artifact_kind,
            "byte_count": self.byte_count,
            "digest": self.digest,
            "mode": self.mode,
        }
        if self.mode == "reference":
            metadata["external_ref"] = self.external_ref
            metadata["revision"] = self.revision
        else:
            metadata["reason"] = self.reason
        return metadata

    def as_retention(self) -> dict[str, Any]:
        metadata = self.as_metadata()
        retention = {"mode": metadata.pop("mode"), **metadata}
        return retention


@dataclass(frozen=True)
class FieldUseSpec:
    field_use_id: str
    repository: str
    base_commit: str
    task_id: str
    mode: str
    declared_by: str
    operator_id: str
    actor_id: str
    encounter_observer_id: str
    environment: Mapping[str, str] = field(default_factory=dict)

    def validate(self) -> None:
        _require_safe_id(self.field_use_id, "field_use_id")
        _require_safe_id(self.repository, "repository")
        _require_text(self.task_id, "task_id")
        require(
            isinstance(self.base_commit, str)
            and len(self.base_commit) == 40
            and all(character in "0123456789abcdef" for character in self.base_commit),
            "base_commit must be a lowercase 40-character Git object id",
        )
        require(self.mode in MODES, "field-use mode must be shadow or consulted")
        require(
            self.declared_by in {"human_operator", "external_runtime"},
            "eligibility must be declared by a human operator or external runtime",
        )
        _require_text(self.operator_id, "operator_id")
        _require_text(self.actor_id, "actor_id")
        _require_text(self.encounter_observer_id, "encounter_observer_id")
        require(
            self.encounter_observer_id != self.actor_id,
            "acting model cannot observe its own encounter",
        )
        require(isinstance(self.environment, Mapping), "environment must be a mapping")
        for key, value in self.environment.items():
            _require_safe_id(key, "environment key")
            _require_text(value, f"environment[{key!r}]")


@dataclass(frozen=True)
class ConsultedLineage:
    source_id: str
    origin: str
    artifact: ArtifactReference
    record_ids: tuple[str, ...]

    def validate(self) -> None:
        _require_safe_id(self.source_id, "consulted source_id")
        require(self.origin in SOURCE_ORIGINS, "invalid consulted source origin")
        self.artifact.validate()
        require(
            self.artifact.mode == "reference",
            "consulted lineage must have a retrievable reference",
        )
        require(
            self.artifact.artifact_kind == "body_core_lineage",
            "consulted source must be a Body Core lineage",
        )
        require(bool(self.record_ids), "consulted source requires exact record ids")
        require(
            len(self.record_ids) == len(set(self.record_ids)),
            "consulted source contains duplicate record ids",
        )
        require(
            all(
                isinstance(event_id, str) and _EVENT_ID.fullmatch(event_id)
                for event_id in self.record_ids
            ),
            "consulted source has an invalid Body Core event id",
        )

    def as_metadata(self) -> dict[str, Any]:
        self.validate()
        return {
            "source_id": self.source_id,
            "origin": self.origin,
            "artifact": self.artifact.as_metadata(),
            "record_ids": list(self.record_ids),
        }


@dataclass(frozen=True)
class ConsultationPlan:
    status: str
    surface: str
    lineage_origin: str | None
    declared_by: str
    sources: tuple[ConsultedLineage, ...] = ()
    projector_id: str | None = None
    view_digest: str | None = None
    reason: str | None = None


@dataclass(frozen=True)
class FieldCaptureState:
    phase: str
    mode: str
    actor_id: str
    invocation_id: str
    encounter_id: str
    terminal_status: str | None = None


@dataclass(frozen=True)
class FieldUseReceipt:
    field_use_id: str
    ledger_path: Path
    terminal_status: str
    final_event_id: str
    final_lineage_head: str
    event_count: int
    inline_payload_bytes: int
    referenced_artifact_bytes: int


def _computed_origin(sources: Sequence[ConsultedLineage]) -> str | None:
    origins = {source.origin for source in sources}
    if not origins:
        return None
    if origins == {ORIGIN_INDEPENDENT}:
        return ORIGIN_INDEPENDENT
    if origins == {ORIGIN_FIELD_CAPTURE}:
        return ORIGIN_FIELD_CAPTURE
    require(origins == SOURCE_ORIGINS, "consulted source origins are invalid")
    return ORIGIN_MIXED


def _validate_consultation(mode: str, plan: ConsultationPlan) -> dict[str, Any]:
    require(mode in MODES, "invalid field-use mode")
    require(plan.status in CONSULTATION_STATUSES, "invalid consultation status")
    require(plan.surface in CONSULTATION_SURFACES, "invalid consultation surface")
    _require_text(plan.declared_by, "consultation declared_by")

    source_ids: set[str] = set()
    for source in plan.sources:
        source.validate()
        require(source.source_id not in source_ids, "duplicate consulted source_id")
        source_ids.add(source.source_id)

    computed_origin = _computed_origin(plan.sources)
    require(
        plan.lineage_origin == computed_origin,
        "declared lineage_origin disagrees with source provenance",
    )

    if plan.surface == SURFACE_NONE:
        require(not plan.sources, "none consultation surface cannot include sources")
        require(
            plan.lineage_origin is None,
            "none consultation surface requires null lineage_origin",
        )
        require(
            plan.projector_id is None and plan.view_digest is None,
            "none consultation surface cannot carry a projector or view digest",
        )
    else:
        require(bool(plan.sources), "consulted surface requires lineage sources")
        require(
            plan.lineage_origin in LINEAGE_ORIGINS,
            "consulted surface requires lineage_origin",
        )

    if plan.surface == SURFACE_RAW:
        require(
            plan.projector_id is None and plan.view_digest is None,
            "raw-lineage consultation cannot carry a projected view",
        )
    elif plan.surface == SURFACE_PROJECTED:
        require(
            plan.projector_id == POLICY_PROFILE_ID,
            "projected consultation requires the explicit endorsed projector",
        )
        require(_is_sha256(plan.view_digest), "projected view digest is invalid")
        require(
            plan.lineage_origin != ORIGIN_FIELD_CAPTURE,
            "field-capture-only lineage cannot supply independently motivated projected state",
        )

    if mode == MODE_SHADOW:
        require(plan.status == STATUS_SHADOW, "shadow mode requires shadow status")
        require(plan.surface == SURFACE_NONE, "shadow mode cannot expose lineage")
    else:
        require(plan.status != STATUS_SHADOW, "consulted mode cannot use shadow status")

    if plan.status == STATUS_CONSULTED:
        require(plan.surface != SURFACE_NONE, "consulted status requires a surface")
    if plan.status in {STATUS_NO_PROJECTION, STATUS_NOT_CONSULTED, STATUS_REFUSED}:
        require(
            plan.surface == SURFACE_NONE, "negative non-use status requires no surface"
        )
    if plan.status not in {STATUS_SHADOW, STATUS_CONSULTED}:
        _require_text(plan.reason, "negative consultation reason")

    sources = [source.as_metadata() for source in plan.sources]
    record_count = sum(len(source.record_ids) for source in plan.sources)
    source_bytes = sum(source.artifact.byte_count for source in plan.sources)
    return {
        "consultation_status": plan.status,
        "consultation_surface": plan.surface,
        "lineage_origin": plan.lineage_origin,
        "declared_by": plan.declared_by,
        "sources": sources,
        "projector_id": plan.projector_id,
        "view_digest": plan.view_digest,
        "reason": plan.reason,
        "deterministic_counts": {
            "source_count": len(sources),
            "record_count": record_count,
            "source_bytes": source_bytes,
        },
        "freeze_boundary": "before_first_consequential_action",
    }


def _verify_consulted_sources(
    repository_root: Path,
    capture_path: Path,
    plan: ConsultationPlan,
) -> None:
    for source in plan.sources:
        path = _resolve_reference(repository_root, source.artifact)
        require(path != capture_path.resolve(), "capture cannot consult its own ledger")
        rows = LineageStore(path).rows()
        known_ids = {row["event_id"] for row in rows}
        require(
            set(source.record_ids).issubset(known_ids),
            "consulted record ids do not exist in the referenced lineage",
        )
    if plan.surface == SURFACE_PROJECTED:
        require(
            len(plan.sources) == 1,
            "v0 projected consultation requires exactly one lineage source",
        )
        source_path = _resolve_reference(repository_root, plan.sources[0].artifact)
        projected = LineageStore(
            source_path,
            projector=V02_POLICY_PROJECTOR,
        ).replay()
        require(
            projected.views.digest() == plan.view_digest,
            "declared projected view digest disagrees with source replay",
        )


def _artifact_from_metadata(metadata: Mapping[str, Any]) -> ArtifactReference:
    return ArtifactReference(
        artifact_kind=metadata.get("artifact_kind"),
        digest=metadata.get("digest"),
        byte_count=metadata.get("byte_count"),
        mode=metadata.get("mode"),
        external_ref=metadata.get("external_ref"),
        revision=metadata.get("revision"),
        reason=metadata.get("reason"),
    )


def _plan_from_payload(payload: Mapping[str, Any]) -> ConsultationPlan:
    sources: list[ConsultedLineage] = []
    raw_sources = payload.get("sources")
    require(isinstance(raw_sources, list), "frozen consultation sources must be a list")
    for raw_source in raw_sources:
        require(isinstance(raw_source, dict), "consulted source must be an object")
        artifact = raw_source.get("artifact")
        require(
            isinstance(artifact, dict), "consulted source artifact must be an object"
        )
        record_ids = raw_source.get("record_ids")
        require(isinstance(record_ids, list), "consulted record_ids must be a list")
        sources.append(
            ConsultedLineage(
                source_id=raw_source.get("source_id"),
                origin=raw_source.get("origin"),
                artifact=_artifact_from_metadata(artifact),
                record_ids=tuple(record_ids),
            )
        )
    return ConsultationPlan(
        status=payload.get("consultation_status"),
        surface=payload.get("consultation_surface"),
        lineage_origin=payload.get("lineage_origin"),
        declared_by=payload.get("declared_by"),
        sources=tuple(sources),
        projector_id=payload.get("projector_id"),
        view_digest=payload.get("view_digest"),
        reason=payload.get("reason"),
    )


def _capture_cost(rows: Sequence[dict[str, Any]]) -> tuple[int, int]:
    inline_payload_bytes = sum(
        len(_canonical_bytes(row["payload"]))
        for row in rows
        if row["retention"]["mode"] == "inline"
    )
    referenced_artifact_bytes = sum(
        int(row["retention"].get("byte_count", 0))
        for row in rows
        if row["retention"]["mode"] in {"reference", "redacted"}
    )
    pre_action = next(
        (row for row in rows if row["kind"] == "field_use_pre_action_frozen"),
        None,
    )
    if pre_action is not None:
        referenced_artifact_bytes += int(
            pre_action["payload"]["deterministic_counts"]["source_bytes"]
        )
    return inline_payload_bytes, referenced_artifact_bytes


def _validate_retained_artifact(row: Mapping[str, Any], expected_kind: str) -> None:
    retention = row["retention"]
    artifact = ArtifactReference(
        artifact_kind=retention.get("artifact_kind"),
        digest=retention.get("digest"),
        byte_count=retention.get("byte_count"),
        mode=retention.get("mode"),
        external_ref=retention.get("external_ref"),
        revision=retention.get("revision"),
        reason=retention.get("reason"),
    )
    artifact.validate()
    require(
        artifact.artifact_kind == expected_kind, f"expected {expected_kind} artifact"
    )


def validate_field_capture(rows: Sequence[dict[str, Any]]) -> FieldCaptureState:
    """Validate the field-use phase machine after untrusting Core replay."""
    validated = replay(rows, projector=V02_POLICY_PROJECTOR).rows
    require(len(validated) >= 2, "field-use capture requires start and encounter")

    terminal_status: str | None = None
    sequence_rows = validated
    if validated[-1]["kind"] in TERMINAL_KINDS:
        terminal_status = validated[-1]["kind"]
        sequence_rows = validated[:-1]
        require(
            len(sequence_rows) < len(EVENT_SEQUENCE),
            "completed capture cannot later become refused or confounded",
        )

    kinds = tuple(row["kind"] for row in sequence_rows)
    require(
        kinds == EVENT_SEQUENCE[: len(kinds)],
        f"invalid field-use event sequence: {kinds}",
    )
    require(len(kinds) <= len(EVENT_SEQUENCE), "field-use capture has extra events")

    start = sequence_rows[0]
    encounter = sequence_rows[1]
    start_payload = start["payload"]
    require(start["writer"] == FIELD_RUNTIME.as_dict(), "invalid field runtime writer")
    require(start["authority"] == "system_record", "invalid field start authority")
    require(start_payload.get("protocol_id") == PROTOCOL_ID, "field protocol id drift")
    require(
        start_payload.get("protocol_sha256") == PROTOCOL_SHA256,
        "field protocol pin drift",
    )
    mode = start_payload.get("mode")
    require(mode in MODES, "invalid captured mode")
    actor_id = _require_text(start_payload.get("actor_id"), "captured actor_id")
    encounter_observer_id = _require_text(
        start_payload.get("encounter_observer_id"), "captured encounter_observer_id"
    )
    require(encounter_observer_id != actor_id, "actor cannot observe its encounter")
    require(
        encounter["writer"] == Writer(encounter_observer_id, "observer").as_dict(),
        "encounter observer disagrees with declaration",
    )
    require(
        encounter["authority"] == "external_observation",
        "encounter requires external observation authority",
    )
    _validate_retained_artifact(encounter, "task_encounter")

    invocation_id = start["event_id"]
    encounter_id = encounter["event_id"]
    for index, row in enumerate(sequence_rows):
        if index == 0:
            require(
                row["scope"] == {"invocation_id": None, "encounter_id": None},
                "invocation start must be unscoped",
            )
            require(not row["causal_parent_ids"], "invocation start cannot have parent")
            continue
        require(
            row["scope"]
            == {
                "invocation_id": invocation_id,
                "encounter_id": encounter_id if index > 1 else None,
            },
            f"{row['event_id']}: field-use scope drift",
        )
        require(
            row["causal_parent_ids"] == [sequence_rows[index - 1]["event_id"]],
            f"{row['event_id']}: field-use causal chain drift",
        )

    if len(sequence_rows) >= 3:
        frozen = sequence_rows[2]
        require(
            frozen["writer"] == FIELD_CONTROLLER.as_dict(),
            "invalid pre-action freezer writer",
        )
        require(
            frozen["authority"] == "controller_transition",
            "invalid pre-action freezer authority",
        )
        expected_payload = _validate_consultation(
            mode, _plan_from_payload(frozen["payload"])
        )
        require(
            frozen["payload"] == expected_payload, "frozen consultation payload drift"
        )

    if len(sequence_rows) >= 4:
        action = sequence_rows[3]
        require(action["writer"] == FIELD_RUNTIME.as_dict(), "invalid action recorder")
        require(action["authority"] == "system_record", "invalid action authority")
        _validate_retained_artifact(action, "native_action")
        require(
            action["retention"].get("actor_id") == actor_id,
            "action reference actor disagrees with invocation",
        )

    if len(sequence_rows) >= 5:
        consequence = sequence_rows[4]
        require(
            consequence["writer"]["role"] == "observer", "consequence must be external"
        )
        require(
            consequence["writer"]["id"] != actor_id,
            "acting model cannot write its own consequence",
        )
        require(
            consequence["authority"] == "external_consequence",
            "invalid consequence authority",
        )
        if consequence["retention"]["mode"] == "inline":
            require(
                consequence["payload"].get("status") == "not_observed",
                "inline consequence must be explicit not_observed",
            )
            _require_text(consequence["payload"].get("reason"), "not_observed reason")
        else:
            _validate_retained_artifact(consequence, "native_consequence")

    if len(sequence_rows) == len(EVENT_SEQUENCE):
        completion = sequence_rows[5]
        require(
            completion["writer"] == FIELD_RUNTIME.as_dict(), "invalid completion writer"
        )
        require(
            completion["authority"] == "system_record", "invalid completion authority"
        )
        before_completion = sequence_rows[:-1]
        inline_bytes, referenced_bytes = _capture_cost(before_completion)
        require(
            completion["payload"]
            == {
                "capture_cost": {
                    "events_before_completion": len(before_completion),
                    "events_total": len(sequence_rows),
                    "inline_payload_bytes_before_completion": inline_bytes,
                    "referenced_artifact_bytes": referenced_bytes,
                    "wall_clock_used_as_outcome": False,
                },
                "captured_through_event_id": before_completion[-1]["event_id"],
                "claim_boundary": "operational capture only; no memory inference",
            },
            "completion capture cost drift",
        )

    if terminal_status is not None:
        terminal = validated[-1]
        require(
            terminal["writer"] == FIELD_RUNTIME.as_dict(), "invalid terminal writer"
        )
        require(terminal["authority"] == "system_record", "invalid terminal authority")
        _require_text(terminal["payload"].get("reason"), "terminal reason")
        require(
            terminal["payload"].get("stopped_after_phase")
            == EVENT_SEQUENCE[len(sequence_rows) - 1],
            "terminal phase marker drift",
        )
        previous = sequence_rows[-1]
        require(
            terminal["causal_parent_ids"] == [previous["event_id"]],
            "terminal event must follow the partial trace",
        )
        expected_scope = {
            "invocation_id": invocation_id,
            "encounter_id": encounter_id if len(sequence_rows) > 1 else None,
        }
        require(terminal["scope"] == expected_scope, "terminal scope drift")

    phase = terminal_status or EVENT_SEQUENCE[len(sequence_rows) - 1]
    return FieldCaptureState(
        phase=phase,
        mode=mode,
        actor_id=actor_id,
        invocation_id=invocation_id,
        encounter_id=encounter_id,
        terminal_status=terminal_status,
    )


class FieldUseCapture:
    """Manual, append-only capture for one independently motivated invocation."""

    def __init__(self, ledger_path: Path):
        self.ledger_path = Path(ledger_path)
        require(
            self.ledger_path.parent.name == "field_use"
            and self.ledger_path.parent.parent.name == "runs",
            "field-use ledger must live under runs/field_use",
        )
        self.repository_root = self.ledger_path.resolve().parents[2]
        self.store = LineageStore(
            self.ledger_path,
            projector=V02_POLICY_PROJECTOR,
        )

    @classmethod
    def start(
        cls,
        repository_root: Path,
        spec: FieldUseSpec,
        encounter: ArtifactReference,
    ) -> FieldUseCapture:
        _verify_protocol_pin()
        spec.validate()
        encounter.validate()
        require(
            encounter.artifact_kind == "task_encounter",
            "field-use start requires a task_encounter artifact",
        )
        repository_root = Path(repository_root).resolve()
        require(repository_root.is_dir(), "repository root does not exist")
        if encounter.mode == "reference":
            _resolve_reference(repository_root, encounter)
        ledger_path = (
            repository_root / "runs" / "field_use" / f"{spec.field_use_id}.body.jsonl"
        )
        require(
            not ledger_path.exists(), "field-use ledger already exists; retry refused"
        )
        capture = cls(ledger_path)
        start = capture.store.append(
            "invocation_started",
            writer=FIELD_RUNTIME,
            authority="system_record",
            payload={
                "protocol_id": PROTOCOL_ID,
                "protocol_sha256": PROTOCOL_SHA256,
                "evidence_class_claim": "wire_integration_only",
                "field_use_id": spec.field_use_id,
                "repository": spec.repository,
                "base_commit": spec.base_commit,
                "task_id": spec.task_id,
                "mode": spec.mode,
                "declared_by": spec.declared_by,
                "operator_id": spec.operator_id,
                "actor_id": spec.actor_id,
                "encounter_observer_id": spec.encounter_observer_id,
                "environment": dict(sorted(spec.environment.items())),
                "claim_boundary": "ordinary work capture; not an experiment",
            },
        )
        capture.store.append(
            "encounter_observed",
            writer=Writer(spec.encounter_observer_id, "observer"),
            authority="external_observation",
            causal_parent_ids=[start["event_id"]],
            invocation_id=start["event_id"],
            retention=encounter.as_retention(),
        )
        capture.validate()
        return capture

    @classmethod
    def open(cls, ledger_path: Path) -> FieldUseCapture:
        _verify_protocol_pin()
        capture = cls(ledger_path)
        capture.validate()
        return capture

    def validate(self) -> FieldCaptureState:
        return validate_field_capture(self.store.raw_rows())

    def _require_phase(self, expected: str) -> FieldCaptureState:
        state = self.validate()
        require(state.terminal_status is None, "field-use capture is terminal")
        require(
            state.phase == expected, f"expected phase {expected}, got {state.phase}"
        )
        return state

    def freeze_pre_action(self, plan: ConsultationPlan) -> dict[str, Any]:
        state = self._require_phase("encounter_observed")
        payload = _validate_consultation(state.mode, plan)
        _verify_consulted_sources(self.repository_root, self.ledger_path, plan)
        row = self.store.append(
            "field_use_pre_action_frozen",
            writer=FIELD_CONTROLLER,
            authority="controller_transition",
            payload=payload,
            causal_parent_ids=[state.encounter_id],
            invocation_id=state.invocation_id,
            encounter_id=state.encounter_id,
        )
        self.validate()
        return row

    def record_action(self, action: ArtifactReference) -> dict[str, Any]:
        state = self._require_phase("field_use_pre_action_frozen")
        action.validate()
        require(
            action.artifact_kind == "native_action", "expected native_action artifact"
        )
        if action.mode == "reference":
            _resolve_reference(self.repository_root, action)
        retention = action.as_retention()
        retention["actor_id"] = state.actor_id
        row = self.store.append(
            "field_use_action_referenced",
            writer=FIELD_RUNTIME,
            authority="system_record",
            causal_parent_ids=[self.store.rows()[-1]["event_id"]],
            invocation_id=state.invocation_id,
            encounter_id=state.encounter_id,
            retention=retention,
        )
        self.validate()
        return row

    def record_consequence(
        self,
        *,
        observer_id: str,
        consequence: ArtifactReference | None = None,
        not_observed_reason: str | None = None,
    ) -> dict[str, Any]:
        state = self._require_phase("field_use_action_referenced")
        observer_id = _require_text(observer_id, "consequence observer_id")
        require(observer_id != state.actor_id, "acting model cannot write consequence")
        require(
            (consequence is None) != (not_observed_reason is None),
            "provide exactly one consequence artifact or not_observed reason",
        )
        kwargs: dict[str, Any]
        if consequence is None:
            kwargs = {
                "payload": {
                    "status": "not_observed",
                    "reason": _require_text(not_observed_reason, "not_observed reason"),
                }
            }
        else:
            consequence.validate()
            require(
                consequence.artifact_kind == "native_consequence",
                "expected native_consequence artifact",
            )
            if consequence.mode == "reference":
                _resolve_reference(self.repository_root, consequence)
            kwargs = {"retention": consequence.as_retention()}
        row = self.store.append(
            "consequence_observed",
            writer=Writer(observer_id, "observer"),
            authority="external_consequence",
            causal_parent_ids=[self.store.rows()[-1]["event_id"]],
            invocation_id=state.invocation_id,
            encounter_id=state.encounter_id,
            **kwargs,
        )
        self.validate()
        return row

    def complete(self) -> FieldUseReceipt:
        state = self._require_phase("consequence_observed")
        rows = self.store.rows()
        inline_bytes, referenced_bytes = _capture_cost(rows)
        self.store.append(
            "invocation_completed",
            writer=FIELD_RUNTIME,
            authority="system_record",
            causal_parent_ids=[rows[-1]["event_id"]],
            invocation_id=state.invocation_id,
            encounter_id=state.encounter_id,
            payload={
                "capture_cost": {
                    "events_before_completion": len(rows),
                    "events_total": len(rows) + 1,
                    "inline_payload_bytes_before_completion": inline_bytes,
                    "referenced_artifact_bytes": referenced_bytes,
                    "wall_clock_used_as_outcome": False,
                },
                "captured_through_event_id": rows[-1]["event_id"],
                "claim_boundary": "operational capture only; no memory inference",
            },
        )
        self.validate()
        return self.receipt()

    def terminate(self, status: str, *, reason: str) -> FieldUseReceipt:
        state = self.validate()
        require(state.terminal_status is None, "field-use capture is already terminal")
        require(
            state.phase != "invocation_completed",
            "completed field-use capture cannot become terminal refusal",
        )
        require(status in TERMINAL_KINDS, "invalid field-use terminal status")
        rows = self.store.rows()
        self.store.append(
            status,
            writer=FIELD_RUNTIME,
            authority="system_record",
            causal_parent_ids=[rows[-1]["event_id"]],
            invocation_id=state.invocation_id,
            encounter_id=state.encounter_id,
            payload={
                "reason": _require_text(reason, "terminal reason"),
                "stopped_after_phase": state.phase,
                "claim_boundary": "partial operational trace; never replaced",
            },
        )
        self.validate()
        return self.receipt()

    def receipt(self) -> FieldUseReceipt:
        state = self.validate()
        require(
            state.phase == "invocation_completed" or state.terminal_status is not None,
            "field-use receipt requires a terminal capture",
        )
        rows = self.store.rows()
        start = rows[0]
        inline_bytes, referenced_bytes = _capture_cost(rows)
        return FieldUseReceipt(
            field_use_id=start["payload"]["field_use_id"],
            ledger_path=self.ledger_path,
            terminal_status=state.terminal_status or "completed",
            final_event_id=rows[-1]["event_id"],
            final_lineage_head=rows[-1]["event_hash"],
            event_count=len(rows),
            inline_payload_bytes=inline_bytes,
            referenced_artifact_bytes=referenced_bytes,
        )
