# Quality Engineering Plan — Admin Center (Derived)

## Inputs
- Feature definition: `rbm-knowledge/05-specifications-derived/admin-centre/admin-centre-feature-definition.md`
- Security review: `04-security-admin-center.md`
- Architect spec: `03-architect-admin-center-tables-acls.md`

## Test Scope
### A. Access Control
- RBM Read-Only: list/detail only; all writes denied + logged
- RBM Admin: scoped writes only
- RBM Platform Admin: full writes

### B. Audit & Evidence
- On every create/update/delete attempt:
  - success writes audit
  - failure writes audit (status=failure + reason)
- Audit immutability: no delete permitted (except retention process if defined)

### C. Validation & Guardrails
- Type validation for system setting values
- High-impact confirmation path required
- Bulk change safeguards tested (limits + rollback)

## Automated Tests (minimum)
- Unit tests: validation utilities, audit writer
- Integration tests: API endpoints for list/get/update; permission matrix tests

## Build Agent Prompt Inputs
- Explicit acceptance tests and negative tests list
- Evidence artefact checklist (what to capture for Gate evidence)
