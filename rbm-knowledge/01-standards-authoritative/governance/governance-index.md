# RBM Knowledge System – Governance Index

Status: AUTHORITATIVE  
Last Updated: 2026-01-04

---

## 1. Purpose

This document is the **authoritative governance index** for the RBM Knowledge System.

It defines:
- Mandatory governance controls
- Authoritative documents and their precedence
- Required startup and usage rules for AI-assisted delivery

All users, agents, and automated processes **must comply** with this index.

---

## 2. Knowledge Bootstrap (Gate 0 – Mandatory)

### 2.1 Bootstrap Contract

All ChatGPT / AI-assisted usage of this knowledge system is governed by a
**mandatory bootstrap contract**.

**Authoritative file:**
```
/rbm-knowledge/knowledge-bootstrap.md
```

This file establishes the authority boundary for every chat session.

### 2.2 Mandatory Rules

1. A **new chat session** is required for each knowledge ZIP upload.
2. The knowledge ZIP is the **single authoritative source** for the session.
3. The bootstrap authority prompt defined in `knowledge-bootstrap.md` must be
   issued verbatim.
4. No design, build, analysis, or orchestration activity may begin until:
   - ZIP load is confirmed
   - VERSION file is detected
   - Authoritative policy locations are acknowledged
5. Outputs produced without bootstrap compliance are **invalid**.

This control represents **Gate 0** and cannot be bypassed.

---

## 3. Authoritative Document Hierarchy

Unless explicitly overridden, the following precedence order applies:

1. **Bootstrap Contract**  
   `knowledge-bootstrap.md`
2. **Standards marked AUTHORITATIVE**  
   (security, governance, development, design system)
3. **Governance policies and controls**
4. **Design systems and reference architectures**
5. **Functional specifications**
6. **Advisory or illustrative content**

Lower-order documents may not override higher-order rules.

---

## 4. VERSION Control and Immutability

Each knowledge package **must** include a VERSION file:

```
/rbm-knowledge/version
```

The VERSION value defines:
- Knowledge baseline identifier
- Release immutability
- Audit traceability

Any modification to authoritative documents requires:
- A VERSION increment
- A new ZIP release
- A new chat session

---

## 5. Orchestrator Agent Enforcement

The Orchestrator agent is responsible for enforcing all governance controls.

### Mandatory Responsibilities
- Enforce Gate 0 bootstrap compliance
- Halt execution on missing or ambiguous authority confirmation
- Prevent invocation of downstream agents prior to bootstrap completion
- Resolve conflicts in favour of the knowledge ZIP

Failure to enforce these rules invalidates all downstream outputs.

---

## 6. Audit Evidence Requirements

The following artefacts constitute the **AI knowledge configuration record**:

- Knowledge ZIP file
- ZIP checksum (where available)
- VERSION file value
- Bootstrap confirmation response
- Orchestrator enforcement confirmation

These artefacts must be retained for audit and assurance purposes.

---

## 7. Prohibited Practices

The following practices are explicitly prohibited:

- Uploading a new knowledge ZIP mid-session
- Mixing knowledge from different ZIP versions
- Proceeding without explicit bootstrap confirmation
- Assuming "latest" or "previously agreed" behaviour
- Overriding standards for speed or convenience

---

## 8. Change Control

Any change to:
- `knowledge-bootstrap.md`
- This governance index
- Authoritative standards or policies

requires:
1. VERSION increment
2. New ZIP release
3. New chat session

Non-compliant changes are void.

---

## 9. Acceptance

Use of this knowledge system constitutes acceptance of all controls defined in
this governance index.

Non-compliance invalidates all outputs produced.

