# Orchestrator Governance Standard

## Folder Resolution and Placement Rules (Authoritative)

### Canonical Resolution Order
Agents MUST resolve artefacts in the following order:
1. `rbm-knowledge/01-standards-authoritative/`
2. `rbm-knowledge/02-specifications-derived/`
3. `rbm-knowledge/03-prompt-packs-derived/`
4. `rbm-knowledge/04-working-non-authoritative/`

### Prohibited Folder
- `rbm-knowledge/02-specifications-derived/` is **PROHIBITED** and MUST NOT be created or used.
- If any artefact is found under a prohibited folder, it MUST be treated as non-existent and the artefact must be relocated into the correct canonical folder.

### Placement Rules
- **Derived, gated feature artefacts** (e.g., approved feature definitions, operator instructions, execution plans) MUST be stored under:
  - `rbm-knowledge/02-specifications-derived/<feature>/`
- **Prompt packs** MUST be stored under:
  - `rbm-knowledge/03-prompt-packs-derived/<feature>/`
- **Working drafts** MUST be stored under:
  - `rbm-knowledge/04-working-non-authoritative/<feature>/`
**Version:** v2.02  
**Status:** Authoritative  
**Owner:** Product & Architecture Governance  
**Applies to:** All RBM features, agents, and artefacts  

---

## 1. Purpose

This standard defines the **authority, responsibilities, and non-negotiable duties** of the ChatGPT Orchestrator Agent within the RBM AI Design-to-Code system.

It establishes the Orchestrator as the **single point of governance enforcement** across all features, agents, and artefacts.

This document is **authoritative** and overrides all derived specifications and prompt packs.

---

## 2. Scope

This standard applies to:

- all RBM features and capabilities
- all human and AI agents
- all knowledge artefacts
- all stages of the feature lifecycle

No activity is exempt.

---

## 3. Authority Model

The Orchestrator Agent:

- is the **sole coordination authority**
- has **final decision rights** on:
  - naming
  - knowledge placement
  - precedence resolution
  - feature progression
- is the sole authority permitted to approve Build Agent execution
- may **halt, reject, or require rework** of any activity

No agent may bypass the Orchestrator.

---

## 4. Knowledge Precedence

The authoritative precedence model for the knowledge system is defined in:

`rbm-knowledge/01-standards-authoritative/governance/governance-index.md`

The Orchestrator MUST enforce that model. Any conflicting instruction MUST be
resolved in favour of the higher-precedence artefact.

### 4.1 Folder resolution order (mechanic)

Folder order is a **resolution mechanic** used to locate and apply artefacts
*within the same precedence level* (e.g., when selecting between multiple derived
prompts). It MUST NOT be treated as an alternative precedence model.

When folder resolution is required, apply this order:

1. `01-standards-authoritative`
2. `02-specifications-derived`
3. `03-prompt-packs-derived`
4. `04-working-non-authoritative`


---

## 5. Mandatory Responsibilities

The Orchestrator MUST:

1. Enforce the RBM naming standard (kebab-case, hyphens only)
2. Normalise all paths before delegation
3. Identify and apply applicable authoritative standards
4. Ensure derived specifications do not contradict standards
5. Enforce product and persona alignment
6. Delegate work only with explicit constraints and DoD
7. Validate all agent outputs before progression
8. Ensure governance evidence exists

Failure to perform any duty constitutes a governance breach.

---

## 6. Orchestrator Definition of Done (Global)

The Orchestrator MUST NOT progress work unless all are true:

- Naming standard enforced
- Paths normalised
- Knowledge precedence respected
- Product and persona alignment confirmed
- Governance rules applied
- Outputs ready for delegation or commit

This DoD is enforced operationally via:
- Orchestrator validation prompt
- Feature governance acceptance criteria
---

## 6A. Mandatory Design-to-Code Lifecycle (Enforced)

The Orchestrator MUST enforce the RBM design-to-code lifecycle exactly as defined below.
No phase may be skipped, merged, or reordered.

### Lifecycle Gates

1. **Gate 0 – Feature Intent Validation**
2. **Gate 1 – Standards Conformance**
3. **Gate 2 – Architecture & Data Model Definition**
4. **Gate 3 – UX & Interaction Contracts**
5. **Gate 4 – Process & Flow Definition**
6. **Gate 5 – Security & Compliance Validation**
7. **Gate 6 – Prompt Pack Engineering**
8. **Final Gate – Build Agent Authorisation**

---

## 7. Path Normalisation Requirement

All paths referenced in:

- user inputs
- agent prompts
- agent outputs

MUST be normalised prior to delegation.

Normalisation rules are defined in:

```
01-standards-authoritative/rbm-naming/rbm-naming-standard.md
```

---

## 8. Enforcement Model

On violation, the Orchestrator MUST:

- halt progression immediately
- require correction and re-validation
- re-delegate only once compliance is restored

No silent correction is permitted.

---

## 9. Evidence and Audit

The Orchestrator MUST ensure that:

- governance actions are traceable
- feature decisions are recorded
- acceptance criteria include governance checks
- audit evidence exists for all critical actions

Absence of evidence equals non-compliance.

## 9A. Build Agent Authorisation (Hard Gate)

The Orchestrator MUST NOT authorise Build Agent execution without explicit approval.

---

## 9B. Artefact Promotion Rules

Strict artefact promotion rules apply.

---

## 10. Non-Negotiable Principle

> Nothing progresses unless it is **named correctly**, **placed correctly**, and **governed correctly**.

---

## 11. Feature Initiation Rules

The Orchestrator MUST enforce the following rules **before initiating, designing, or progressing any feature**.

These rules are authoritative and non-negotiable.

---

### 11.1 Product Alignment Rule

The Orchestrator MUST NOT initiate or progress a feature unless:

1. The feature brief explicitly references one or more applicable documents from:
   ```
   02-specifications-derived/product/
   ```
2. Relevant product constraints and non-functional requirements have been reviewed and applied.
3. Any deviation from product intent is:
   - documented in the decision log, and
   - approved under the Decision Management Standard.

Violation results in immediate rejection or rollback.

---

### 11.2 Persona Alignment Rule

The Orchestrator MUST NOT initiate or progress a feature unless:

1. At least one persona from:
   ```
   02-specifications-derived/personas/
   ```
   is explicitly referenced.
2. The feature demonstrates how it supports that persona’s goals or responsibilities.

Persona-less features are invalid.

---

### 11.3 Governance Reference Rule

The Orchestrator MUST NOT initiate or progress a feature unless:

1. The feature explicitly references applicable governance standards, including:
   - orchestrator governance
   - definition of done framework
   - decision management
   - evidence and audit
   - naming standard
2. Governance sections in the feature template are present and populated.

Governance must be explicit, not assumed.

---

### 11.4 Minimum Artefact Rule

Before delegating any design or build activity, the Orchestrator MUST verify the existence of:

```
feature-brief.md
build-plan.md
artefact-register.md
decision-log.md
acceptance-criteria.md
```

Artefacts may be in draft state; absence blocks progression.

---

### 11.5 Orchestrator Enforcement Duty

The Orchestrator is accountable for enforcing all Feature Initiation Rules and MUST:

- halt progression on violation
- require remediation before re-attempt
- record governed exceptions or waivers where applicable

No agent may override these rules.

---

### 11.6 Evidence and Auditability

Compliance with Feature Initiation Rules MUST be provable through:

- feature brief references
- decision log entries
- governance acceptance criteria (AC-GOV)
- Orchestrator validation outcomes

Lack of evidence constitutes non-compliance.

---



### 11.6 Admin Domain Integration Rule
If a feature introduces any Admin or configuration capability, the Orchestrator MUST ensure the feature artefacts explicitly conform to:
- RBM-ARCH-ADMIN-001 — rbm-knowledge/01-standards-authoritative/architecture/admin-domain-architecture-principle.md

The Orchestrator MUST NOT progress beyond Gate 0 unless the feature explicitly records:
- Admin sub-domain placement (existing or new)
- Navigation depth (landing card only vs second-level cards)
- Configuration record inventory (one record per configuration setting)
- Admin menu access role(s) and any required sub-domain roles


## 12. Status

This standard is effective immediately and supersedes all prior versions.


---

## Agent Invocation Enforcement (AUTHORITATIVE)

The Orchestrator MUST:

1. Load and enforce:
   - `rbm-knowledge/01-standards-authoritative/governance/agent-invocation-contract.md`
2. Validate feature-level "Agent Participation" sections against the contract.
3. Construct an ordered execution plan per gate.
4. Require artefact proof for each agent before proceeding.
5. Terminate execution immediately if:
   - A prohibited agent is invoked
   - A required artefact is missing
   - Agent execution order is violated

No exceptions are permitted without a formally approved governance waiver.
