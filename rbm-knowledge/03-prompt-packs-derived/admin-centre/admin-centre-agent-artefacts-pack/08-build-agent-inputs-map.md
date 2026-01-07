# Build Agent Prompt Inputs Map — Admin Centre (Derived)

## Purpose
Ensure each agent artefact is directly consumable as input to ServiceNow IDE / Build Agent prompts.

## Inputs (Artefacts in this pack)
1. Personas: `01-personas-admin-centre.md`
2. Journeys: `02-user-journeys-admin-centre.md`
3. Architect (tables + ACL intent): `03-architect-admin-centre-tables-acls.md`
4. Security review: `04-security-admin-centre.md`
5. Platform dev plan: `05-platform-dev-admin-centre.md`
6. Front-end dev plan: `06-frontend-dev-admin-centre.md`
7. QA plan: `07-qa-admin-centre.md`

## Prompt Wiring Guidance

### Prompt 1 — Data Model + ACLs (Platform build)
Include:
- From `03-architect-admin-centre-tables-acls.md`: Table specs + ACL model + enforcement points
- From `04-security-admin-centre.md`: required controls
- Output expectation: tables, dictionary, ACLs, server-side APIs, audit writer.

### Prompt 2 — UI Shell + Sections (Front-end build)
Include:
- From `01-personas-admin-centre.md`: persona constraints
- From `02-user-journeys-admin-centre.md`: journeys + acceptance criteria
- From `06-frontend-dev-admin-centre.md`: component tree and behaviours
- Output expectation: React + TS pages and components aligned to design system.

### Prompt 3 — QA & Evidence
Include:
- From `07-qa-admin-centre.md`: tests + negative cases
- From `04-security-admin-centre.md`: abuse cases
- Output expectation: tests and evidence artefacts.

## Non-negotiables to repeat in every prompt
- KB: v2.0.0 is authoritative
- Feature definition: `rbm-knowledge/05-specifications-derived/admin-centre/admin-centre-feature-definition.md`
- Policy: RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md
- React-first; RBM reference components first
- Server-side security + audit authoritative
- No new roles; reuse existing RBM roles
- No operational execution or live state control
