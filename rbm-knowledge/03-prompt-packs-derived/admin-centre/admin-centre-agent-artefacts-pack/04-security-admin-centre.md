# Security Review — Admin Centre (Derived)

## Authority & Inputs
- Knowledge Baseline: v2.0.0
- Feature Definition: `rbm-knowledge/05-specifications-derived/admin-centre/admin-centre-feature-definition.md`
- Policy: RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md

## Threat / Abuse Cases
1. Privilege escalation via UI-only checks
2. Bulk changes causing systemic misconfiguration
3. Tampering with audit evidence / deletion of audit entries
4. Unauthorized access to configuration data or audit logs
5. Injection of invalid configuration values (e.g., JSON)

## Required Controls (Non-Negotiable)
- Server-side access enforcement (ACLs + capability checks)
- Immutable audit trail (no delete; minimal update)
- Guardrails for high-impact changes:
  - explicit confirmation
  - optional “two-step apply” pattern if supported
- Input validation for all configuration values (type + constraints)
- Full logging of failed attempts (including denied actions)

## Security Test Requirements (for QA + Build Agent)
- Verify Read-Only cannot mutate data (negative tests)
- Verify RBM Admin can only modify scoped records
- Verify RBM Platform Admin can modify platform-scope records
- Verify audit records written for success + failure paths
