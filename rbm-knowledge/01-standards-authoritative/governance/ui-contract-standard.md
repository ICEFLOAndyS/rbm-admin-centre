# RBM UI Contract Standard

**File:** ui-contract-standard.md  
**Knowledge Set:** rbm-knowledge v2.03  
**Authority Level:** Tier-1 (Normative)  
**Applies To:** All RBM UI delivery (React / TypeScript)  
**Status:** AUTHORITATIVE  

---

## 1. Purpose

This standard defines the **mandatory structure, content, and enforcement rules** for UI Contracts used in RBM feature delivery.

A UI Contract:
- Is a **gate-controlled artefact**
- Is **binding on the Build Agent**
- Explicitly constrains what UI components, patterns, and layouts may be implemented

No UI build may proceed without an **APPROVED UI Contract**.

---

## 2. Scope

This standard applies to:
- All RBM scoped applications
- All React + TypeScript UI implementations
- All Build Agent executions
- All human-authored UI specifications

This standard overrides:
- Generic ServiceNow UI guidance
- Generic React UI practices
- Reference examples

---

## 3. UI Contract Artefact Requirements

Each UI Contract MUST:

- Be a markdown file (`.md`)
- Be versioned and immutable once approved
- Declare status, decision ID, and scope
- Be stored under:

```
04-working-non-authoritative/<feature-name>/
```

---

## 4. Mandatory UI Contract Structure

Every UI Contract MUST contain the following sections.

### 4.1 Header

```md
# Gate 3 – UI Contract

## Status
APPROVED

## Decision ID
DEC-XXX-YYY

## Feature
<feature-name>
```

---

### 4.2 Approved RBM Components (Mandatory)

UI Contracts MUST list **only RBM reference components**, using **RBM-prefixed names**.

Example:

```md
## Approved RBM Components
- RBMDataGrid
- RBMSidePanel
- RBMForm
```

Rules:
- RBM-prefixed components are **custom RBM React components**
- Name similarity MUST NOT be used to infer ServiceNow components

---

### 4.3 Approved UI Patterns

UI Contracts MUST explicitly define allowed patterns.

Example:

```md
## Approved UI Patterns

### Admin Domain (RBM-ARCH-ADMIN-001 — rbm-knowledge/01-standards-authoritative/architecture/admin-domain-architecture-principle.md)
- Admin landing page card grid (icon + title)
- Optional second-level card grid for complex sub-domains
- Terminal navigation opens configuration record list for the sub-domain
- List → Detail via side panel
- Inline row actions
- Read-only summary header
```

---

### 4.4 Forbidden Components and Patterns (Mandatory)

The following MUST NOT appear in any UI Contract or implementation:

```md
## Explicitly Forbidden
- sn-datagrid
- now-side-panel
- now-modal
- UI Builder layouts
- Declarative Horizon UI definitions
- Jelly / XML UI macros
```

Any appearance of the above **invalidates Gate 3 approval**.

---

### 4.5 Layout and Interaction Rules

UI Contracts MUST specify:

- Primary layout type (list, detail, split, etc.)
- Editing approach (side panel, inline, read-only)
- Navigation constraints

Example:

```md
## Layout Rules
- No modal-based editing
- No multi-pane master/detail layouts
- Side panel width fixed and non-resizable
```

---

## 5. Build Agent Enforcement Rules

The Build Agent:

- MUST treat the UI Contract as authoritative
- MUST NOT introduce components or patterns not listed
- MUST halt if any ambiguity exists
- MUST refuse to substitute RBM components with ServiceNow components

If the UI Contract is missing, unclear, or contradictory:
> **The Build Agent MUST refuse to build.**

---

## 6. Governance and Gate Control

- UI Contracts are produced at **Gate 3**
- Approval is required before Gate 4 or Gate 5
- Any change requires a new decision ID and re-approval

Skipping or bypassing this gate is **forbidden**.

---

## 7. Compliance Statement

All UI Contracts defined under this standard are:
- Audit-relevant artefacts
- Subject to regulatory scrutiny
- Defensible under FCA / PRA OpRes and EU DORA

---

## 8. Final Enforcement Statement

This document is **normative and binding**.

If any conflict exists between a UI Contract and other documentation:
> **This standard and the approved UI Contract prevail.**