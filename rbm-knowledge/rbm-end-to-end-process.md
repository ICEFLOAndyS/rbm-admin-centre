# RBM End-to-End Controlled Delivery Process

**Applies to:** rbm-knowledge v2.04 (revised)  
**Authority:** Tier-1 (Normative)  

## Purpose
This process ensures that the ServiceNow Build Agent:
- Complies with RBM governance and standards
- Consumes outputs from upstream ChatGPT agents
- Cannot invent or infer architecture, data, or UI patterns

## Core Principle
The Build Agent MAY ONLY materialise code from APPROVED gate artefacts.
It MUST NOT design, infer, or optimise.

## Gate Model
| Gate | Owner | Mandatory Output |
|---|---|---|
| G0 | Orchestrator | Scope Definition |
| G1 | ServiceNow Architect | Data & Architecture Contract |
| G2 | Security Expert | Security & ACL Contract |
| G3 | UX / FE Architect | UI Contract |
| G4 | Platform Developer | API & Server Contract |
| G5 | Orchestrator | Build Authorisation |
| G6 | Build Agent | Code Only |

Build Agent invocation is FORBIDDEN before Gate 5.
