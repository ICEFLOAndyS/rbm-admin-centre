# ServiceNow IDE / Build Agent Prompt Pack — Admin Center (v1)

## Global Authority (paste into every prompt)
- Knowledge baseline ZIP is authoritative: v2.02
- Feature definition: `rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md`
- Development standards (AUTHORITATIVE): `rbm-knowledge/01-standards-authoritative/development/development-standards-authoritative.md`
- Policy (ID + canonical path): RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md
- React + TypeScript only; RBM reference components first
- Server-side enforcement (ACLs/capability checks) and immutable audit logging
- Admin Center is configuration-time only; no runbook execution or live-state control
- Reuse existing RBM roles only; no new roles

---

## PROMPT 1 — Platform: Tables + ACLs + APIs + Audit

Use these inputs:
- Architect: `03-architect-admin-center-tables-acls.md`
- Security: `04-security-admin-center.md`
- Platform plan: `05-platform-dev-admin-center.md`

Deliver:
1. Create/extend tables for Feature Flags, System Settings, Admin Audit (per Architect spec).
2. Implement ACLs per role model (reuse existing RBM roles).
3. Implement server-side APIs/resources for list/get/update with server-side paging/filter/sort.
4. Implement immutable audit writer called on success and failure (denied attempts logged).
5. Implement validation for setting values (type + constraints) and high-impact safeguards.

Output:
- List created/updated files and configuration steps.

---

## PROMPT 2 — UI: Admin Center Shell + Feature Flags + System Settings + Audit

Use these inputs:
- Personas: `01-personas-admin-center.md`
- Journeys: `02-user-journeys-admin-center.md`
- Front-end plan: `06-frontend-dev-admin-center.md`

Deliver:
1. React + TS Admin Center shell page with section navigation.
2. Feature Flags module:
   - list (server-side paging/filter/sort)
   - detail/edit with validation and high-impact confirmation
3. System Settings module:
   - list (server-side paging/filter/sort)
   - detail/edit with validation and high-impact confirmation
4. Audit module:
   - list/search (server-side filtering)
   - detail view showing actor/action/entity/before-after/evidence link (if present)
5. Ensure UI never enforces permissions; reflect server-authoritative outcomes.

Output:
- Component tree, created files, and how to run/verify.

---

## PROMPT 3 — QA: Tests + Evidence Pack

Use these inputs:
- QA plan: `07-qa-admin-center.md`
- Security: `04-security-admin-center.md`

Deliver:
1. Automated tests covering:
   - permission matrix (Read-Only denied writes)
   - success/failure audit logging
   - validation and rollback behaviours
2. Evidence artefact checklist for audit/evidence compliance.

Output:
- Test locations, commands, and coverage summary.
