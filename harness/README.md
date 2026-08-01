# Harness

The harness creates forked memory conditions, contacts engines when explicitly
authorized, writes primary ledgers, and computes verdicts. The model under test
does not write its own evidence.

Start with [the project entrypoint](../README.md). Governing architecture is in
[PLAN_V1_BRANCH_AND_OFFER.md](../notes/PLAN_V1_BRANCH_AND_OFFER.md); cell rules
are in [RUBRIC_V1.md](../notes/RUBRIC_V1.md).

Safe wire checks that do not establish memory findings:

```bash
make smoke
make x1-test
make x2-test
make x2-fixture-check
make body-core-test
make body-core-x2-test
make body-core-m2-test
make body-core-m3-test
make body-sketch-test
make body-field-use-test
```

Verify the documentation archive and all historical manifest pins with:

```bash
make docs-archive-check
```

Check local links across the current documentation surface with:

```bash
make docs-route-check
```

The route check excludes archived documentation, the previous lab, generated
evidence, corpora, and substrate transcripts. Those spaces preserve historical
references; they are not the current read-in path.

Before running any engine-backed command, read its specification and admission
state. Mock output is wiring evidence only. Primary ledgers under `runs/` are
append-only; derived scorer sidecars may be regeneratable where their scorer
contract says so.
