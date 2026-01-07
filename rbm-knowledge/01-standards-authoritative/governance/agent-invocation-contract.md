# Agent Invocation Contract — Feature Delivery

## Authority
- Knowledge Baseline: v2.04
- Classification: AUTHORITATIVE
- Precedence: This contract overrides all feature, prompt, and advisory content.
- Purpose: Enforce deterministic agent participation and sequencing.

---

## Core Principles

1. **Allow-list first**: Only agents explicitly permitted may execute.
2. **Deny-list enforced**: Prohibited agents MUST NOT execute under any circumstances.
3. **Artefact proof**: An agent is considered executed only if its required artefacts exist.
4. **Ordered execution**: Agents MUST execute in the sequence defined for the gate.
5. **Fail-fast**: Any violation requires immediate halt.

---

## Agent Definitions

### Mandatory Agents (General)
- Persona & User Journeys Agent
- ServiceNow Architect Agent
- Security Agent
- Platform Developer Agent
- Front-End Developer Agent
- QA Agent
- Prompt Engineer Agent

### Optional Agents (Opt-in Only)
- Reporting Agent
- Data Migration Agent

### Prohibited Agents (Hard Exclusion)
- MS Teams Integration Agent
- Slack Integration Agent
- Email Integration Agent
- External API Integration Agent

Invocation of a prohibited agent MUST terminate execution.

---

## Gate-Based Agent Requirements

### Gate 0 — Feature Intent Validation
**Required Agents**
- Persona & User Journeys Agent

**Required Artefacts**
- personas.md
- user-journeys.md

---

### Gate 1 — Constraints & Architecture
**Required Agents**
- ServiceNow Architect Agent
- Security Agent

**Required Artefacts**
- architecture-tables-acls.md
- security-controls.md

---

### Gate 2 — Build Authorisation
**Required Agents**
- Platform Developer Agent
- Front-End Developer Agent
- QA Agent
- Prompt Engineer Agent

**Required Artefacts**
- server-side-design.md
- ui-architecture.md
- test-plan.md
- build-agent-prompt-pack.md

---

## Feature-Level Overrides

Features MAY restrict agent participation further via an explicit
"Agent Participation" section in the Feature Definition.

Features MAY NOT:
- Introduce new mandatory agents
- Override prohibited agents

---

## Compliance

Failure to comply with this contract invalidates:
- Gate approval
- Prompt generation
- Build Agent execution
