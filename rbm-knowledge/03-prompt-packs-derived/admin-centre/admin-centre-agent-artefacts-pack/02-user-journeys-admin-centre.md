# User Journeys — Admin Centre (Derived)

## Authority & Inputs
- Knowledge Baseline: v2.0.0
- Feature Definition: `rbm-knowledge/05-specifications-derived/admin-centre/admin-centre-feature-definition.md`
- Policy: RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md
- Dev standards: `rbm-knowledge/01-standards-authoritative/development/development-standards-authoritative.md`

## Journey J1 — Feature Flags (Enable/Disable a Capability)
**Actor:** RBM Platform Admin (primary), RBM Admin (scoped), RBM Read-Only (view only)

1. Navigate to **Admin Centre → Feature Flags**
2. List view loads with **server-side** paging/filter/sort
3. Actor selects a feature flag record (detail view)
4. Actor edits toggle + optional rationale/notes
5. System validates:
   - Role/capability (server-side)
   - Any additional guardrails (high-impact confirmation)
6. On save:
   - Change is persisted
   - **Audit log entry written (immutable)**
   - Evidence captured **only if required** by governance for the flag category
7. Actor sees success state; UI displays audit reference identifier

**Acceptance criteria**
- Read-Only cannot edit
- All failures logged
- Audit record includes actor, timestamp, entity, before/after

## Journey J2 — System Settings (Change a Configuration Value)
**Actor:** RBM Platform Admin (primary), RBM Admin (where permitted)

1. Navigate to **Admin Centre → System Settings**
2. List view loads with server-side paging/filter/sort
3. Actor opens a setting; sees current value + description + impact level
4. Actor modifies value; client-side validation runs (non-authoritative)
5. Server validates:
   - Role/capability
   - Allowed values / constraints
   - Impact safeguards (e.g., double-confirmation for “high impact”)
6. Save triggers:
   - Persist setting
   - Write **audit** entry
   - Capture **evidence** for sensitive settings as required
   - Ensure rollback safety if partial failure
7. Actor can open “View audit record” from the confirmation

**Acceptance criteria**
- High-impact settings require explicit confirmation
- Partial failure rolls back; audit captures failure reason
- Evidence required for configuration changes (per Gate 1/2)

## Journey J3 — Audit Review (Read-only)
**Actor:** RBM Read-Only / Compliance

1. Navigate to **Admin Centre → Audit**
2. Search audit logs (server-side filtering)
3. Open an audit event; view:
   - actor
   - action type
   - timestamp
   - target entity
   - before/after (or delta)
   - evidence link (if present)
4. Export (if permitted) or capture reference for audit evidence pack

**Acceptance criteria**
- Export respects role and data minimisation
- Audit entries immutable and attributable
