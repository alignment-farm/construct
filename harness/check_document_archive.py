"""Fail-closed integrity check for the documentation archive.

This verifies both archive layers:

1. final pre-migration snapshots moved from their former live paths; and
2. older SHA-256 versions named by historical review manifests.

Some review manifests pinned working-tree document states whose bytes were never
committed or retained as Git blobs. Those entries are preserved as explicit
``unrecoverable_manifest_only`` audit results. A digest proves identity only
when the corresponding bytes still exist; it cannot recreate them.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_MANIFEST = ROOT / ".archive" / "documentation-v1" / "MANIFEST.json"
SHA256 = re.compile(r"^[0-9a-f]{64}$")
SKIP_PARTS = {".archive", ".git", ".substrate", "runs"}


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _manifest_references(value: object, moved: set[str], out: set[tuple[str, str]]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in moved and isinstance(child, str) and SHA256.fullmatch(child):
                out.add((key, child))
            else:
                _manifest_references(child, moved, out)
    elif isinstance(value, list):
        for child in value:
            _manifest_references(child, moved, out)


def main() -> int:
    archive = json.loads(ARCHIVE_MANIFEST.read_text())
    snapshots = archive["entries"]
    moved = {entry["previous_path"] for entry in snapshots}

    for entry in snapshots:
        path = ROOT / entry["archived_path"]
        assert path.is_file(), f"missing archive snapshot: {path}"
        assert path.stat().st_size == entry["bytes"], f"byte-count mismatch: {path}"
        assert _digest(path) == entry["sha256"], f"digest mismatch: {path}"

    referenced: set[tuple[str, str]] = set()
    for path in ROOT.rglob("*.json"):
        if SKIP_PARTS.intersection(path.relative_to(ROOT).parts):
            continue
        try:
            value = json.loads(path.read_text())
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        _manifest_references(value, moved, referenced)

    pins = archive["historical_pins"]["entries"]
    indexed = {(entry["previous_path"], entry["sha256"]): entry for entry in pins}
    assert set(indexed) == referenced, (
        "historical pin index drift: "
        f"missing={sorted(referenced - set(indexed))} extra={sorted(set(indexed) - referenced)}"
    )

    materialized = 0
    unrecoverable = 0
    for key, entry in indexed.items():
        status = entry["status"]
        if status == "materialized_exact":
            path = ROOT / entry["archived_path"]
            assert path.is_file(), f"missing historical pin bytes: {key}"
            assert path.stat().st_size == entry["bytes"], f"pin byte-count mismatch: {key}"
            assert _digest(path) == entry["sha256"], f"pin digest mismatch: {key}"
            assert entry.get("source_commit"), f"materialized pin lacks source commit: {key}"
            materialized += 1
        elif status == "unrecoverable_manifest_only":
            assert entry.get("archived_path") is None, f"unrecoverable pin claims bytes: {key}"
            assert entry.get("bytes") is None, f"unrecoverable pin claims byte count: {key}"
            assert entry.get("source_commit") is None, f"unrecoverable pin claims commit: {key}"
            assert entry.get("audit"), f"unrecoverable pin lacks audit basis: {key}"
            unrecoverable += 1
        else:
            raise AssertionError(f"unknown historical pin status {status!r}: {key}")

    summary = archive["historical_pins"]["summary"]
    assert summary == {
        "total": len(indexed),
        "materialized_exact": materialized,
        "unrecoverable_manifest_only": unrecoverable,
    }, "historical pin summary drift"

    print(f"archive snapshots: {len(snapshots)} exact")
    print(f"historical pins: {materialized} materialized exact")
    print(f"historical pins: {unrecoverable} unrecoverable manifest-only")
    print("DOCUMENT ARCHIVE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

