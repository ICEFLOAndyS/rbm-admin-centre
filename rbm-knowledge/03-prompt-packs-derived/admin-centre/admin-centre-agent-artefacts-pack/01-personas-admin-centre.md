# Personas — Admin Centre (Derived)

## Authority & Precedence
- Knowledge Baseline: v2.0.0 (ZIP authoritative)
- Precedence: Subordinate to `rbm-knowledge/knowledge-bootstrap.md`, AUTHORITATIVE standards, governance/security, and RBM design system.
- Inputs:
  - Feature intent (non-authoritative): `rbm-knowledge/04-working-non-authoritative/admin-centre/admin-centre-feature-intent.md`
  - Feature definition (Gate 2 artefact): `rbm-knowledge/05-specifications-derived/admin-centre/admin-centre-feature-definition.md`
  - Agent invocation controls: `rbm-knowledge/01-standards-authoritative/agent-invocation-matrix.md`

## Personas (Role Reuse Only)

### P1 — RBM Platform Admin
- **Primary goal:** Configure RBM platform-wide administration safely and audibly.
- **Typical tasks:** Manage feature flags, system settings, permission scaffolding, configuration templates.
- **Constraints:** Must not perform operational runbook execution; actions must be auditable and server-authoritative.

### P2 — RBM Admin
- **Primary goal:** Administer RBM configuration within defined scope (not platform-wide).
- **Typical tasks:** Maintain reference/config data, scoped settings, view audit trail.
- **Constraints:** No privilege escalation; cannot override governance or security controls.

### P3 — RBM Read-Only (Audit / Compliance)
- **Primary goal:** Review administrative changes and evidence.
- **Typical tasks:** View change history, audit log search/export (where permitted), verify approvals/evidence links.
- **Constraints:** No create/update/delete privileges; visibility constrained to configuration-relevant entities.

## Key Journey Principles
- **UI is non-authoritative**; server-side enforcement and audit is authoritative.
- **Configuration-time only**; no interaction with live execution state.
- **Evidence-first** for sensitive changes (config + permission).
