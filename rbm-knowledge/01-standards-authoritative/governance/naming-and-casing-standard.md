# RBM Naming & Casing Standard
**File:** naming-and-casing-standard.md  
**Authority Level:** Tier-1 (Normative)  
**Status:** LOCKED  
**Applies To:** All RBM repositories, knowledge systems, prompts, artefacts, and generated outputs  
**Change Control:** VERSION only

---

## 1. Purpose

This standard defines the **mandatory naming and casing rules** for all RBM files, folders, and artefacts.

Its purpose is to:
- Eliminate ambiguity
- Improve human and AI readability
- Prevent false signals of authority
- Ensure consistency across tooling, agents, and repositories

---

## 2. Core Principle (Non-Negotiable)

> **Authority is expressed by location, metadata, and governance — never by filename casing.**

Filename casing MUST NOT be used to imply:
- Authority
- Immutability
- Priority
- Special handling

---

## 3. File Naming Rules (Mandatory)

### 3.1 Casing
- **lowercase only**

#### 3.1.1 Exceptions (Controlled)
- `README.md` is permitted **only** where required for platform/tooling conventions (e.g., GitHub, SharePoint previews).
- Any additional exceptions MUST be explicitly approved via governance decision log and documented with rationale.
- **kebab-case** (`-`) separators
- No underscores
- No camelCase
- No ALL CAPS

✅ Correct:
```
rbm-authority-map.md
rbm-build-agent-prompt.md
ui-contract-standard.md
server-authority-model.md
```

❌ Forbidden:
```
RBM-AUTHORITY-MAP.md
rbmBuildAgentPrompt.md
ui_contract_standard.md
```

---

### 3.2 File Extensions
- Markdown standards and artefacts: `.md`
- No mixed-case extensions

---

## 4. Folder Naming Rules (Mandatory)

- **lowercase**
- **kebab-case**
- Semantic and descriptive
- Numeric prefixes allowed only for ordering (e.g. `01-`, `04-`)

✅ Correct:
```
01-standards-authoritative/
04-working-non-authoritative/
build-agent/
content-packs/
```

❌ Forbidden:
```
Standards/
WorkingFiles/
BuildAgent/
```

---

## 5. Authority Signalling (How Authority Is Declared)

Authority MUST be declared **inside the file**, not inferred from its name.

Every Tier-0 and Tier-1 document MUST include explicit metadata near the top:

```md
Authority Level: Tier-1 (Normative)
Status: LOCKED
Change Control: VERSION only
```

This metadata is the **only valid signal of authority**.

---

## 6. Scope-Specific Naming Guidance

### 6.1 Tier-0 / Tier-1 Standards
- Name describes **what is governed**
- Not how important it is

Examples:
```
rbm-authority-map.md
development-standards-authoritative.md
ui-contract-standard.md
naming-and-casing-standard.md
```

---

### 6.2 Bootstrap / Session Control Prompts
Bootstrap prompts are **standards**, not working artefacts.

Examples:
```
rbm-orchestrator-system-prompt.md
rbm-build-agent-prompt.md
```

---

### 6.3 Gate Artefacts (Working Outputs)
Gate artefacts MAY use structured prefixes **inside feature folders only**:

```
04-working-non-authoritative/content-packs/
├── g1-data-architecture.md
├── g2-security-acl.md
├── g3-ui-contract.md
├── g4-api-contract.md
├── g5-build-authorisation.md
```

Prefixes (`g1–g5`) indicate **process order**, not authority.

---

## 7. Explicit Prohibitions

The following are **forbidden** across the RBM system:

- ALL CAPS filenames
- Mixed-case filenames
- Using casing to imply authority
- Inconsistent naming for the same concept
- Renaming files to “emphasise importance”

Violations MUST be corrected.

---

## 8. Enforcement

- Orchestrator MUST flag naming violations
- Build Agent MUST NOT infer meaning from filename casing
- Reviewers MUST reject artefacts that violate this standard

Naming non-compliance is a **standards violation**, not a cosmetic issue.

---

## 9. Rationale (Summary)

Consistent naming:
- Reduces cognitive load
- Improves AI determinism
- Avoids platform-specific edge cases
- Strengthens regulatory defensibility

---

## 10. Final Rule (Authoritative)

> **If authority matters, declare it in metadata and enforce it in process — never in filename casing.**