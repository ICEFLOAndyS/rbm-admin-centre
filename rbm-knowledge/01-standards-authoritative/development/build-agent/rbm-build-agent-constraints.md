# RBM Build Agent — Allowed & Forbidden Actions

**File:** rbm-build-agent-constraints.md  
**Knowledge Set:** rbm-knowledge v2.0.5 (session revisions applied)  
**Status:** LOCKED / AUTHORITATIVE  
**Audience:** ServiceNow IDE Build Agent  
**Change Control:** Updates only when VERSION changes  

---

## 1. Mandatory Acknowledgement

Before generating any output, you MUST state:

> “RBM Authority Map v2.0.5 acknowledged. Tier-1 standards enforced.”

---

## 2. What You MAY Do

You MAY ONLY:
- Generate React + TypeScript code that implements explicitly approved artefacts and standards
- Use RBM reference components first
- Use non-RBM components only where Tier-1 standards permit and the contract allows

---

## 3. Hard Constraints (Non-Negotiable)

### 3.1 UI & Framework
- ✅ React + TypeScript ONLY
- ❌ UI Builder
- ❌ Declarative Horizon layouts
- ❌ Jelly / XML / legacy UI
- ❌ Inline styling unless explicitly permitted by Tier-1 standards

### 3.2 RBM vs ServiceNow Component Disambiguation
- RBM reference components (e.g. `datagrid`, `sidepanel`) are RBM-owned React components
- You MUST NOT substitute them with ServiceNow components by name similarity
- Explicitly forbidden unless a Tier-1 standard approves:
  - `sn-datagrid`
  - `now-side-panel`
  - `now-modal`

### 3.3 Server Authority
- Filtering: server-side only
- Sorting: server-side only
- Pagination: server-side only
- Validation: server-side only
- Security enforcement: server-side only

### 3.4 Data Integrity
- ❌ No invented tables/fields/relationships
- ❌ No domain separation
- ❌ No client table
- ✅ Referential integrity required
- ✅ Full auditability required

---

## 4. Mandatory Gate Inputs (When Applicable)

When a feature uses Gate artefacts, you MUST treat them as binding.  
For UI delivery, an APPROVED UI Contract is mandatory:
- `01-standards-authoritative/governance/ui-contract-standard.md`

If required artefacts are missing or unclear:
> STOP AND REFUSE TO BUILD.

---

## 5. Output Discipline

All outputs MUST be:
- Typed (TypeScript)
- Standards-aligned
- Deterministic
- Free of invented requirements

On completion, state:

> “Output generated in compliance with RBM Tier-1 standards. No deviations introduced.”
