# RBM Automation Pack (v2.03)

This pack implements an automated, template-driven, approval-gated system for creating RBM features.

## What you get
1) Tier-1 approved templates:
- `01-standards-authoritative/governance/feature-templates/*`

2) Deterministic scaffolder:
- `tools/scaffold/new-feature.py`

3) Pre-flight validator (approval-aware):
- `tools/validators/preflight-validator.py`

4) Optional GitHub automation:
- `.github/workflows/rbm-preflight.yml`
- `.github/CODEOWNERS.rbm-snippet`

## Where to place these files
Copy the folders into your RBM repo, preserving paths.

## How to use (end-to-end)
### A) Scaffold a new feature
From repo root:
```bash
python tools/scaffold/new-feature.py --name <feature> --created-by "<name>" --include-g0
```

### B) Populate gate artefacts
Use your ChatGPT Orchestrator flow to populate G1–G4 (and optionally G0).
Keep status as `DRAFT` until PR approvals are complete.

### C) Obtain approvals (recommended: PR + CODEOWNERS)
- Apply the CODEOWNERS snippet to enforce reviewer approvals per gate.

### D) Mark gates APPROVED
Once approvals are obtained, update each gate file:
- `## Status` -> `APPROVED`
- Fill out the `## Approval` block:
  - Approved by
  - Approved on
  - Approval ref (PR # / Decision ID / Change ID)

### E) Run preflight
```bash
python tools/validators/preflight-validator.py --feature <feature>
```

### F) Authorise the build (Gate 5)
- Set `Build Authorised: YES` in `g5-build-authorisation.md`
- Ensure Gate 5 is `APPROVED` and has a completed approval block

### G) Invoke ServiceNow IDE Build Agent
Use your controlled Build Agent bootstrap prompt and reference the approved gate artefacts by path.
Build Agent must implement only what the artefacts specify.

## Notes
- This pack assumes naming/casing: lowercase kebab-case.
- Template changes are Tier-1 controlled (VERSION-only change control).
Generated on: 2026-01-04

---

## Automated artefact-existence preflight (Build Agent readiness)

The preflight validator now additionally validates that Build Agent prompt files (`03-prompt-packs-derived/<feature>/prompt-*.md`)
reference feature artefacts by full canonical path, and that every referenced artefact exists under:

- `04-working-non-authoritative/<feature>/artefacts/`

Recommended evidence capture:

```bash
python rbm-knowledge/tools/validators/preflight-validator.py --root . --feature <feature> | tee rbm-knowledge/04-working-non-authoritative/<feature>/preflight-report.generated.md
```
