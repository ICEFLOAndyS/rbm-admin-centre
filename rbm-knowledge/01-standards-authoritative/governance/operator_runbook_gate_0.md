# RBM Operator Runbook – Gate 0 Knowledge Bootstrap

Status: AUTHORITATIVE  
Last Updated: 2026-01-04
Audience: Human Operators / Product Owners / Architects

---

## 1. Purpose

This runbook provides a **simple, repeatable, operator-safe procedure** for
initiating a compliant ChatGPT session using the RBM Knowledge System.

It exists to ensure:
- Knowledge authority is correctly established
- Governance controls are enforced from the outset
- Outputs are auditable and defensible

This runbook implements **Gate 0 – Knowledge Bootstrap** as defined in:
- `/rbm-knowledge/knowledge-bootstrap.md`
- `docs/governance/governance-index.md`

---

## 2. When This Runbook Must Be Used

This runbook **must be followed** whenever:
- A new RBM knowledge ZIP is uploaded
- A VERSION change has occurred
- A new ChatGPT session is started for delivery, design, or analysis

Failure to follow this runbook invalidates all outputs.

---

## 3. Preconditions (Operator Checklist)

Before starting:

- [ ] Knowledge ZIP prepared with a single root folder (`/rbm-knowledge/`)
- [ ] `/rbm-knowledge/version` file present and correct
- [ ] `/rbm-knowledge/knowledge-bootstrap.md` present
- [ ] ZIP file finalised (no pending edits)

If any item is missing → **STOP**.

---

## 4. Gate 0 Execution Procedure (Step-by-Step)

### Step 1 — Start a New Chat Session

- Click **New Chat**
- Do not reuse an existing conversation
- Do not paste any prompts

This establishes a clean authority boundary.

---

### Step 2 — Upload the Knowledge ZIP

- Upload the ZIP file as the **first interaction**
- Wait for upload confirmation

Do not issue any prompts before upload.

---

### Step 3 — Issue the Authority Prompt

Paste the following text **verbatim** as the first message:

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

Do not add or modify text.

---

### Step 4 — Verify Assistant Confirmation

Proceed **only if** the assistant explicitly confirms:

- [ ] Knowledge ZIP loaded
- [ ] VERSION file detected (exact value stated)
- [ ] Authoritative policy locations identified
- [ ] Precedence rules acknowledged

If any confirmation item is missing or unclear → **STOP** and restart.

---

## 5. Evidence Capture (Mandatory)

The operator must retain:

- Knowledge ZIP file
- ZIP checksum (if available)
- VERSION value
- Assistant bootstrap confirmation response

These artefacts form the **AI knowledge configuration record**.

---

## 6. Optional but Recommended Validation

Immediately after Gate 0 completion, the operator should request:

- A full reference integrity audit
- Verification of policy ID + canonical path usage

This strengthens audit defensibility.

---

## 7. Prohibited Operator Actions

The following actions are not permitted:

- Uploading a new knowledge ZIP mid-session
- Proceeding without explicit bootstrap confirmation
- Reusing a chat session after a VERSION change
- Assuming prior agreement or context

---

## 8. Failure Handling

If Gate 0 fails:

1. Discard the session
2. Correct the knowledge ZIP
3. Start a new chat
4. Re-run this runbook from Step 1

No remediation within the same session is allowed.

---

## 9. Acceptance

By proceeding past Gate 0, the operator confirms:
- This runbook has been followed
- Governance controls are active
- Outputs produced are compliant

Non-compliance invalidates all outputs.

