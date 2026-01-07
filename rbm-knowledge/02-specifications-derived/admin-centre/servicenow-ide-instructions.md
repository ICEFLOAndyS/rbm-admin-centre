# ServiceNow IDE Instructions — Admin Centre

## Authority & Status
- Feature: **Admin Centre**
- Knowledge Baseline: **v2.03** (authoritative ZIP)
- Gate Status: **Gate 2 APPROVED**
- Precedence: Subordinate to `rbm-knowledge/knowledge-bootstrap.md`, AUTHORITATIVE standards, governance & security policies, and RBM design system.

This document defines the **mandatory ServiceNow IDE execution instructions** for building the Admin Centre feature using the approved **v2.03 Build Agent prompt pack**.

---

## 1. Purpose

These instructions ensure that:
- ServiceNow IDE usage is **controlled, repeatable, and auditable**
- All Build Agent executions remain aligned to:
  - Gate 2 Feature Definition
  - Architect, Security, and QA artefacts
- No assumptions or ad-hoc fixes are introduced during build

---

## 2. Prerequisites (Hard Stop if Any Fail)

### 2.1 Scoped Application
- Scoped app exists (e.g. `{{APP_SCOPE}}`)
- App scope is active in ServiceNow IDE
- Correct update set / source control branch selected
- App is not locked or read-only

### 2.2 Knowledge Artefacts Available
Confirm the following canonical artefacts are available locally or in-repo:

- `rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md`
- Gate 0, Gate 1, Gate 2 decision records
- Admin Centre agent artefacts pack
- **Admin-Center-Build-Agent-Prompt-Pack-v2.03**

If any artefact is missing → **STOP**.

---

## 3. Role & Access Preconditions

### 3.1 Required Roles in Instance
The following roles **must already exist**:

- RBM Platform Admin
- RBM Admin
- RBM Read-Only

> No new roles may be created as part of this feature.

### 3.2 User Permissions
- Your user must have **RBM Platform Admin**
- You must be able to create:
  - Tables and dictionary entries
  - ACLs
  - Script Includes / APIs
  - React UI components

---

## 4. Non‑Negotiable Build Rules

The following rules apply to **all** Build Agent executions:

- React + TypeScript only
- RBM reference components first
- Server-side enforcement is authoritative
- UI must never enforce permissions
- All admin actions must produce audit records
- Admin Centre is **configuration-time only**
- No operational runbook execution
- No new roles or domains introduced

Violation of any rule invalidates the build.

---

## 5. Prompt Execution Order (Locked)

**IMPORTANT:** Prompt 00 is mandatory for all new scopes or prototype environments.


Execute the Build Agent prompts **exactly in this order**:

0. **prompt-00-app-bootstrap.md**  
   Application scope resolution (MUST RUN FIRST)

1. **prompt-01-platform-foundation.md**  
   Tables, dictionary, ACLs

2. **prompt-02-platform-services.md**  
   APIs, audit writer, rollback logic

3. **prompt-03-ui-shell.md**  
   Admin Centre shell and navigation

4. **prompt-04-ui-modules.md**  
   Feature Flags and System Settings modules

5. **prompt-05-audit-ui.md**  
   Audit list and detail UI

6. **prompt-06-qa-evidence.md**  
   Tests and evidence artefacts

Do not merge prompts. Do not skip prompts.

---

## 6. Post‑Prompt Validation (After Each Prompt)

After **each** prompt execution, verify:

- Only the expected artefacts were created
- No additional tables, roles, or permissions were introduced
- Server-side validation and audit logic exists
- UI reflects permissions but does not enforce them
- Failures are logged and rolled back where applicable

If validation fails → **STOP** and resolve before continuing.

---

## 7. Definition of Done (Admin Centre)

The Admin Centre is considered complete only when:

- Feature Flags module works end-to-end
- System Settings module works end-to-end
- Audit UI displays immutable audit records
- RBM Read-Only cannot modify any data
- All admin actions write audit records (success and failure)
- Automated tests pass
- Evidence artefacts are available for governance review

---

## 8. Failure & Recovery Rules

If a build fails:
- Identify the prompt that introduced the defect
- Re-run **only that prompt** after correction
- Do not patch manually outside the prompt flow
- Do not proceed to subsequent prompts until fixed

---

## 9. Governance Reminder

All changes remain subject to:
- RBM governance and audit standards
- Formal exception and waiver process (if required)

No deviation is permitted without explicit approval.

---

## 10. Document Control

- Location:  
  `rbm-knowledge/02-specifications-derived/admin-centre/servicenow-ide-instructions.md`
- Owner: ChatGPT Orchestrator Agent
- Status: Active


## 11. Prototype Teardown (Optional)

For prototype or sandbox scopes only, a controlled teardown is available:

- **prompt--1-scope-teardown.md**
- Must be run explicitly and manually
- Never permitted in production

This ensures prototype scopes can be safely removed without polluting long-lived environments.

## 4.1 Scope Naming Convention (Enforced)

All prototype builds MUST use the enforced naming convention defined in **PROMPT 00**:

- `APP_SCOPE = x_{ORG_CODE}_rbm_{SCOPE_TAG}`
- ORG_CODE: lowercase alphanumeric, 3–8 chars
- SCOPE_TAG: lowercase alphanumeric, 2–12 chars

Operators MUST supply:
- `{{ORG_CODE}}`
- `{{SCOPE_TAG}}`

No hard-coded or ad-hoc scope names are permitted.
