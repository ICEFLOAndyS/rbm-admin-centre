# Admin Centre — Build Execution Plan (Post Gate 2)

## Authority
- Knowledge Baseline: v2.04 (ZIP authoritative)
- Feature Definition: rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md
- Development Standards (AUTHORITATIVE): rbm-knowledge/01-standards-authoritative/development/development-standards-authoritative.md
- Policy (ID + canonical path): RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md

## Objective
Deliver the **Admin Centre** feature as a **React + TypeScript** administrative UI and supporting server-side enforcement for configuration-time administration only, with full auditability.

---

## 1. Delivery Approach (Phased)

### Phase 1 — Foundation (Platform + Data)
1. Create/confirm Admin Centre navigation entry and routing (Admin Domain only).
2. Define configuration entities (tables) required for:
   - System settings
   - Feature flags
   - Reference/config data (as applicable)
3. Implement server-side access control (ACLs / role checks) using **existing RBM roles only**.
4. Implement server-side audit logging for all admin actions.

### Phase 2 — UI (React + RBM Reference Components)
1. Create Admin Centre shell page:
   - Left navigation / section list
   - Content area with list/detail
2. Implement list pages with:
   - Server-side filtering / sorting / pagination
   - RBM reference components first
3. Implement edit experiences using RBM reference components:
   - Forms with validation
   - Confirmations for high-impact changes

### Phase 3 — Guardrails, Evidence, QA
1. Add bulk-change safeguards (limits, confirmations, rollback paths).
2. Evidence capture where required (configuration & permission changes).
3. Automated tests per development standards:
   - Unit tests for utilities and handlers
   - Integration tests for API/resources
4. Produce audit evidence pack outputs required by governance.

---

## 2. Non-Negotiable Constraints (from Gate 1/2)

- Configuration-time only; **no operational runbook execution** or live-state control.
- **No new roles**; reuse existing RBM roles.
- Audit is **server-side authoritative** and immutable.
- React-first; RBM reference components first.
- Explicitly exclude UI Builder–only / Horizon-only implementations.

---

## 3. Definition of Done (Admin Centre)

Minimum acceptable completion:
1. Admin Centre accessible only to RBM Admin / RBM Platform Admin; read-only mode for RBM Read-Only.
2. At least two admin modules implemented end-to-end (recommended):
   - Feature Flags
   - System Settings
3. Every create/update/delete action:
   - Enforces server-side permissions
   - Writes audit record with principal attribution
4. UI uses TypeScript strict mode and follows RBM dev standards.
5. Evidence artefacts produced for sensitive change categories.

---

## 4. Build Agent Inputs (What to provide)

- Feature Definition (canonical)
- Gate 0/1/2 decision records
- Any existing table names and field definitions (if already present)
- RBM reference component catalogue pointers (from design system)

---

## 5. Execution Date
2026-01-05
