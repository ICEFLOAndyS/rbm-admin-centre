# RBM Knowledge Bootstrap Contract
Version: v2.0.5
Status: AUTHORITATIVE
Last Updated: 2026-01-04

---

## 1. Purpose

This file defines the **mandatory bootstrap procedure** for initiating any
ChatGPT session that uses this knowledge package.

Its purpose is to:
- Establish a **clean authority boundary**
- Prevent **knowledge drift**
- Ensure **standards precedence**
- Create **reproducible, auditable AI outputs**

No design, build, or advisory activity is permitted until this contract
has been acknowledged and confirmed.

---

## 2. Authoritative Knowledge Declaration

This knowledge package is the **single authoritative knowledge source**
for the current chat session.

Rules:

1. The contents of this ZIP override all prior knowledge, assumptions,
   defaults, or model memory.
2. If any conflict exists between general knowledge and this package,
   **this package always wins**.
3. No inference may be made beyond what is explicitly defined here.
4. Missing or ambiguous information must result in a **STOP + CLARIFY**.
5. All outputs must comply with the standards, constraints, and policies
   defined in this package.

---

## 3. Mandatory Operator Startup Procedure

The operator **must** follow this sequence exactly:

### Step 1 — Start a New Chat
- A new chat session is mandatory.
- No prior context may be reused.

### Step 2 — Upload the Knowledge ZIP
- Upload the ZIP containing this file as the **first interaction**.
- Do not issue prompts before upload.

### Step 3 — Issue the Authority Prompt
Paste the following text verbatim as the first message:

```
AUTHORITATIVE CONTEXT — RBM KNOWLEDGE BASELINE

The uploaded ZIP file is the single authoritative knowledge source
for this chat session.

Rules:
1. The ZIP overrides all prior or general knowledge.
2. If conflicts exist, the ZIP always wins.
3. Do not assume information not explicitly present.
4. All outputs must comply with the ZIP’s standards and constraints.
5. If information is missing or ambiguous, stop and ask.

Confirm:
- The VERSION detected
- The authoritative policy files you will enforce
- Your readiness to proceed
```

### Step 4 — Wait for Explicit Confirmation
Proceed **only if** the assistant confirms:
- ZIP loaded successfully
- VERSION file detected
- Authoritative policy locations identified
- Precedence rules acknowledged

If confirmation is incomplete → **STOP**.

---

## 4. VERSION File Requirement

This knowledge package **must** include a VERSION file at:

```
/rbm-knowledge/version
```

The VERSION file defines:
- Knowledge baseline identifier
- Release immutability
- Audit traceability

If the VERSION file is missing or unreadable:
- All activity must halt
- Operator must correct the package

---

## 5. Authoritative Standards Hierarchy

Unless explicitly overridden within this package, the precedence order is:

1. **Bootstrap Contract**  
   `/rbm-knowledge/knowledge-bootstrap.md`
2. Standards marked **AUTHORITATIVE**
3. Governance and security policies
4. Design system constraints
5. Functional specifications
6. Advisory or illustrative content

No lower-order content may override a higher-order rule.


---

## 6. Mandatory Pre-Work Validation (Recommended)

Before initiating any design or build activity, the operator should request:

- A full reference integrity audit
- Verification of policy ID + canonical path usage
- Confirmation of internal consistency

This mirrors regulated change-initiation controls.

---

## 7. Prohibited Actions

The following actions are explicitly prohibited:

- Uploading a new knowledge ZIP mid-conversation
- Mixing knowledge from multiple ZIP versions
- Proceeding without explicit authority confirmation
- Assuming “latest” or “previously agreed” behaviour
- Overriding standards for convenience or speed

---

## 8. Audit & Evidence

This file, together with:
- The ZIP checksum
- The VERSION value
- The initial authority confirmation response

constitutes the **AI knowledge configuration record** for the session.

---

## 9. Acceptance

Use of this knowledge package implies acceptance of this bootstrap contract.

Non-compliant usage invalidates all outputs produced.

