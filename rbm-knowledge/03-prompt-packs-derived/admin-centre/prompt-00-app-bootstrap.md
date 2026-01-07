# PROMPT 00 — Application Bootstrap (Scope Resolution)

## Scope Declaration (MANDATORY)
- ORG_CODE = {{ORG_CODE}}
- SCOPE_TAG = {{SCOPE_TAG}}
- APP_LABEL = {{APP_LABEL}}
- APP_DESCRIPTION = {{APP_DESCRIPTION}}

## Naming Convention (ENFORCED)
This build system enforces a deterministic prototype scope naming convention.

### Canonical Format
`x_{org_code}_rbm_{scope_tag}`

### Rules
- `org_code` MUST be lowercase alphanumeric, 3–8 chars: `^[a-z0-9]{3,8}$`
- `scope_tag` MUST be lowercase alphanumeric, 2–12 chars: `^[a-z0-9]{2,12}$`
- The resolved scope MUST match: `^x_[a-z0-9]{3,8}_rbm_[a-z0-9]{2,12}$`

### Derived Values
- APP_SCOPE = `x_{ORG_CODE}_rbm_{SCOPE_TAG}`
- APP_PREFIX = APP_SCOPE (table prefix equals app scope unless explicitly overridden in later prompts)

If ORG_CODE or SCOPE_TAG fails validation, STOP and request corrected values.
Do not infer or auto-correct values.

---

## Authority

- The full RBM knowledge system available under `/knowledge-base` is authoritative.
- All standards, governance rules, specifications, and artefacts MUST be read directly from the knowledge system folders.
- ZIP files are not authoritative execution sources and MUST NOT be relied upon.
- If any referenced file is missing, inconsistent, or inaccessible, STOP and raise a Gate failure.


## Inputs (read-only)

### Feature agent artefacts (canonical)
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/01-personas-admin-center.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/02-user-journeys-admin-center.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/03-architect-admin-center-tables-acls.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/04-security-admin-center.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/05-platform-dev-admin-center.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/06-frontend-dev-admin-center.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/07-qa-admin-center.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/08-build-agent-inputs-map.md

### Feature specifications (canonical)
- /rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md
- /rbm-knowledge/02-specifications-derived/admin-centre/servicenow-ide-instructions.md

## Task
1. Validate ORG_CODE and SCOPE_TAG against the enforced rules.
2. Construct APP_SCOPE from the canonical format.
3. Check if a scoped application exists with scope = APP_SCOPE.
4. If it exists:
   - Do not modify it
   - Report sys_id, scope, label
   - Status: EXISTING_APP_REUSED
5. If it does not exist:
   - Create a new scoped application with:
     - Scope = APP_SCOPE
     - Label = APP_LABEL
     - Description = APP_DESCRIPTION
     - Source control disabled (unless explicitly instructed)
   - Activate the scope
   - Report sys_id, scope, label
   - Status: NEW_APP_CREATED

## Constraints
- Do NOT create tables, roles, ACLs, or UI
- Do NOT proceed to feature build work

## Output
- Status (EXISTING_APP_REUSED | NEW_APP_CREATED)
- ORG_CODE / SCOPE_TAG
- APP_SCOPE
- sys_id
