# Gate-aware Execution Checklist — Agent Participation & Artefact Proof

## Authority
- Knowledge Baseline: v2.02
- Subordinate to:
  - `rbm-knowledge/knowledge-bootstrap.md`
  - `rbm-knowledge/01-standards-authoritative/governance/agent-invocation-contract.md`
  - `rbm-knowledge/01-standards-authoritative/governance/orchestrator-governance.md`

## Purpose
Enforce deterministic agent participation per gate and require artefact proof prior to gate approval and prompt generation.

---

## Gate 0 — Feature Intent Validation

### Required agents (ordered)
1. Persona & User Journeys Agent

### Artefact proof (required)
- Personas artefact (stored as an individual `.md` file under `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`, canonical path recorded)
- User journeys artefact (stored as an individual `.md` file under `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`, canonical path recorded)

### Checklist
- [ ] Feature intent exists under `rbm-knowledge/04-working-non-authoritative/<feature>/`
- [ ] Personas artefact exists and is referenced by canonical path
- [ ] User journeys artefact exists and is referenced by canonical path
- [ ] No prohibited agents invoked

---

## Gate 1 — Constraints & Architecture

### Required agents (ordered)
1. ServiceNow Architect Agent
2. Security Agent

### Artefact proof (required)
- Architecture: tables + ACL intent + enforcement points (stored under `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`)
- Security: required controls + abuse cases + negative tests (stored under `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`)

### Checklist
- [ ] Architect artefact exists and is referenced by canonical path
- [ ] Security artefact exists and is referenced by canonical path
- [ ] Feature Agent Participation section reconciled with the contract
- [ ] No prohibited agents invoked

---

## Gate 2 — Build Authorisation

### Required agents (ordered)
1. Platform Developer Agent
2. Front-End Developer Agent
3. QA Agent
4. Prompt Engineer Agent

### Artefact proof (required)
- Platform design artefact (APIs, validation, audit, rollback) — `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`
- UI architecture artefact (React+TS, RBM components first) — `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`
- QA test plan + evidence checklist — `rbm-knowledge/04-working-non-authoritative/<feature>/artefacts/`
- Build Agent prompts as **individual `.md` files** in the feature folder under `rbm-knowledge/03-prompt-packs-derived/<feature>/` (includes Prompt 00 bootstrap + scope declaration).

### Checklist
- [ ] Platform design artefact exists and is referenced by canonical path
- [ ] UI architecture artefact exists and is referenced by canonical path
- [ ] QA artefact exists and is referenced by canonical path
- [ ] Prompt pack exists and includes:
  - [ ] Prompt 00 bootstrap with naming convention enforcement
  - [ ] Scope Declaration block in every prompt
  - [ ] Prohibited agent guardrails
- [ ] Decision index updated with decision ID + artefact canonical path + policy ID + canonical path
- [ ] No prohibited agents invoked

---

## Stop Conditions (hard fail)
Execution MUST STOP immediately if:
- a prohibited agent is invoked
- a required agent artefact is missing
- artefacts are not referenced by canonical path
- a gate is passed without artefact proof
