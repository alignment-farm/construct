# Documentation archive

This directory preserves superseded documentation as immutable project lineage.
It is **not current authority** and is excluded from the default read-in path.

The first archive generation is
[`documentation-v1`](documentation-v1/MANIFEST.json). Its `files/` tree retains
each document at its former repository-relative path. The manifest records the
old path, archived path, byte count, SHA-256 digest, disposition, and current
replacement where one exists.

The manifest also audits 24 older document versions named by retained review
manifests. Twelve exact versions were recoverable from Git and are materialized
under `documentation-v1/pins/<sha256>/...`. Twelve were never committed or
retained as Git blobs; they are recorded as `unrecoverable_manifest_only`.
Those hashes identify missing working-tree states but cannot recreate their
bytes. Run `make docs-archive-check` to verify both the preserved objects and
the explicit losses.

Use the archive to inspect the final pre-migration wording, resolve a former
path, or understand why the current documentation changed. An older review
manifest may pin an earlier revision of the same path; retrieve those exact
bytes from Git using the manifest hash rather than assuming this archive
snapshot matches every historical pin. For present state and routing, return to
the root [README](../README.md).
