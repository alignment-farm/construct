# Body Core v0.3 explicit-projection review

Status: **ENDORSED 2026-07-22; design and post-build passes complete**.

The bounded review ran in substrate thread `explicit-projection-boundary`.
`cursor/grok-4.5` and `claude/fable-5` first endorsed the kernel/policy seam,
then independently reviewed the frozen implementation and returned
**ENDORSE** without repair.

## Exact reviewed implementation

```text
notes/body_core_v03_implementation_manifest.json
b543e5c92d6a8ff2b7ea4d59732f9002f3045443bf122da8a69c828f99f13b87
```

Both reviewers recomputed all nineteen manifest file hashes and reran 66
focused plus 43 legacy checks, 109 total. Ruff lint, manifest-scoped format,
and `git diff --check` passed.

The historical-identity check was independently reproduced from the parent at
`10cdcd7736db18b6e7321142b00395f2202d4409`: both implementations produced 38
walking-skeleton rows and final view digest
`c2041076508d84b730d1bd8a486f6d0a8988448824921b25fd9d526ed6a23de3`.

## Reviewed conclusion

- Cognitive replay and view claims fail closed without explicit projector
  selection.
- Kernel-only validation cannot certify a cognitive view claim.
- Projector-bound clients retain append-time lifecycle and warrant refusals.
- Unowned kinds advance the canonical cursor without mutating policy state.
- The split preserves the literal `body-core-v0.2-provisional-policy` identity.
- No generic kind-to-authority rule, fourth adapter, registry, schema field,
  callback surface, or optimization entered.

The review licenses wire/integration preservation only. It creates no memory,
security, composition, engine-behavior, governance-cost, or reconstruction-cost
finding.

## Carried observations

1. Kernel-only writers can append structurally valid rows that make later
   policy replay refuse the ledger. This is fail-closed poisoning, not quiet
   acceptance; writer coexistence would be a separate design problem.
2. `Projector.projector_id` is descriptive at the kernel seam; Core neither
   binds nor logs it.
3. Pre-existing Ruff-format drift in `demo.py` and `correspondence.py` sat
   outside the reviewed manifest.

The implementation manifest freezes historical bytes. This later review record
and living-status updates are not expected to match those frozen documentation
hashes; the reviewed implementation itself remains unchanged.
