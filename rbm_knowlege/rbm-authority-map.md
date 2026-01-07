# RBM Authority Map
**File:** rbm-authority-map.md  
**Authority Level:** Tier-1 (Subordinate to Bootstrap Contract)  
**Status:** LOCKED  
**Applies To:** All RBM agents, repositories, and delivery artefacts  
**Change Control:** VERSION only

---

## 1. Purpose

This document defines the **authoritative precedence model** for the RBM knowledge system.

> **Non-negotiable:** If any conflict exists between this file and `rbm-knowledge/knowledge-bootstrap.md`, the Bootstrap Contract wins.

If any conflict exists between documents, prompts, agent outputs, or tooling:
> **The Bootstrap Contract (`rbm-knowledge/knowledge-bootstrap.md`) determines which artefact prevails.**
>
> This Authority Map is a *derived* representation and MUST NOT override the Bootstrap Contract.

No other document may override this file.

---

## 2. Authority Tiers

| Tier | Classification | Meaning |
|----|----------------|---------|
| **Tier-0** | Bootstrap Contract | Highest authority; defines precedence model |
| **Tier-1** | Standards (Normative) | Mandatory, enforceable rules |
| **Tier-2** | Governance & Process | Mandatory process controls |
| **Tier-3** | Reference | Informative only, never binding |

---

## 3. Precedence Rule (Non‑Negotiable)

All humans, agents, and tools MUST apply this order:

1. **Tier‑0** – Bootstrap Contract (`rbm-knowledge/knowledge-bootstrap.md`)  2. **Tier‑1** – Authoritative Standards  
3. **Tier‑2** – Governance & Process  
4. **Tier‑3** – Reference material  

If instructions conflict:
- Execution MUST halt
- The conflict MUST be flagged
- Resolution MUST occur before proceeding

---

## 4. Tier‑1 Authoritative Standards (Canonical)

### 4.1 Governance & Control

| Topic | Canonical Location |
|------|--------------------|
| Naming & casing | `01-standards-authoritative/governance/naming-and-casing-standard.md` |
| Decision management | `01-standards-authoritative/governance/decision-management-standard.md` |

| UI contract | `01-standards-authoritative/governance/ui-contract-standard.md` |

---

### 4.2 Development & Engineering

| Topic | Canonical Location |
|------|--------------------|
| Development standards | `01-standards-authoritative/development/development-standards-authoritative.md` |
| RBM design system | `01-standards-authoritative/rbm-design-system/` |
| Component disambiguation | `01-standards-authoritative/rbm-design-system/rbm-design-system.md` |
| Build Agent control | `01-standards-authoritative/development/build-agent/rbm-build-agent-prompt.md` |

---

### 4.3 Architecture

| Topic | Canonical Location |
|------|--------------------|
| State management policy | `01-standards-authoritative/architecture/state-management-policy.md` |
| Admin domain architecture principle | `01-standards-authoritative/architecture/admin-domain-architecture-principle.md` |

---

### 4.4 Security & Compliance

| Topic | Canonical Location |
|------|--------------------|

---

## 5. Tier‑2 Governance & Process

Tier‑2 artefacts define **how work is controlled**, not how solutions are designed.

Examples:
- Orchestrator governance
- Agent responsibility model
- Agent invocation matrix
- Quality gate checklists

Tier‑2 artefacts MUST NOT override Tier‑1 standards.

---

## 6. Tier‑3 Reference

Tier‑3 artefacts:
- Provide examples or guidance
- Are non‑binding
- MUST NOT introduce rules

Examples:
- Reference architectures
- Example flows
- Illustrative agent outputs

---

## 7. Mandatory Authority Signals

Authority MUST be declared using:
- Folder placement (e.g. `01-standards-authoritative/`)
- Explicit metadata inside documents
- This Authority Map

Authority MUST NOT be inferred from:
- Filename casing
- File naming emphasis
- Location outside Tier‑1 folders

(See: Naming & Casing Standard)

---

## 8. Mandatory Session Acknowledgement

All Orchestrator and Build Agent sessions MUST begin with:

> “RBM Authority Map acknowledged. Tier‑1 standards enforced.”

Failure to acknowledge invalidates the session.

---

## 9. Tools
The tools/ directory is infrastructure.
It must exist at repository root and must never be embedded inside rbm-knowledge or feature folders

## 10. Final Rule

> **When in doubt, stop. Authority must be explicit, documented, and enforced before proceeding.**