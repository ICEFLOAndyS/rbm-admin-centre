# Feature Definition — Admin Centre

## Agent Participation

### Required Agents
- Persona & User Journeys Agent
- ServiceNow Architect Agent
- Security Agent
- Platform Developer Agent
- Front-End Developer Agent
- QA Agent
- Prompt Engineer Agent

### Explicitly Excluded Agents
- MS Teams Integration Agent
- Slack Integration Agent
- Email Integration Agent
- External API Integration Agent

### Enforcement
- This section is subordinate to:
  `/rbm-knowledge/01-standards-authoritative/governance/agent-invocation-contract.md`
- If any excluded agent is invoked, execution MUST STOP.
- A gate cannot pass without the required artefacts for its required agents.

## Authority & Status
- Authority level: Derived (Gate 2)
- Knowledge Baseline: v2.0.5
- Precedence: Subordinate to Bootstrap Contract, AUTHORITATIVE standards, governance & security policies, and RBM design system
- Gate 2: In progress

---

## 1. Feature Overview

### 1.1 Purpose
The **Admin Centre** provides a controlled, auditable administrative control surface for RBM configuration and system governance activities.  
It is explicitly **non-operational** and **configuration-time only**.

### 1.2 Non‑Goals
The Admin Centre does **not**:
- Execute runbooks
- Control live execution state
- Override governance gates
- Bypass audit or evidence requirements

---

## 2. Scope Definition

### 2.1 In Scope
- System and platform configuration settings
- Reference and configuration data management
- Feature flag and capability toggles
- Administrative metadata management
- Read-only access to administrative audit logs

### 2.2 Out of Scope
- Operational control of events or runbooks
- Live task execution or intervention
- Emergency or break-glass operational access

---

## 3. Domain Boundaries

- Domain: **Admin Domain**
- Cross-domain access: Read-only, configuration-relevant only
- All enforcement is server-side authoritative

---

## 4. Roles & Access Model

### 4.1 Role Reuse
Admin Centre capabilities map exclusively to existing RBM roles:
- RBM Platform Admin
- RBM Admin
- RBM Read-Only

No new roles are introduced.

### 4.2 Capability Enforcement
- Capabilities are role-based and enforced server-side
- UI presence does not imply permission

---

## 5. Audit & Evidence

### 5.1 Audit Logging
- All administrative actions are logged server-side
- Logs are immutable once written
- All actions are attributable to an authenticated principal

### 5.2 Evidence Capture
- Evidence required for configuration and permission changes
- Retention follows authoritative audit standards

---

## 6. Design & Implementation Constraints

### 6.1 UI & Technology
- React-first implementation
- RBM reference components used where available
- Standard React components only when no RBM reference exists

### 6.2 Explicit Exclusions
- No UI Builder–only implementations
- No Horizon-only abstractions
- No bypass of RBM design system constraints

---

## 7. Security & Governance Guardrails

- Segregation of duties enforced
- Guardrails on bulk or high-impact changes
- All failures logged, rolled back, and auditable

---

## 8. Gate Traceability

- Gate 0 Decision: RBM-GATE0-ADMIN-CENTER-001
- Gate 1 Decision: RBM-GATE1-ADMIN-CENTER-001

---

## 9. Gate 2 Declaration

This Feature Definition is complete and ready for Gate 2 validation and approval.

---

## Document Control
- Created: 2026-01-05
- Owner: ChatGPT Orchestrator Agent
