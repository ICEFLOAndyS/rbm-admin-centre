## Authority

- The full RBM knowledge system available under `/knowledge-base` is authoritative.
- All standards, governance rules, specifications, and artefacts MUST be read directly from the knowledge system folders.
- ZIP files are not authoritative execution sources and MUST NOT be relied upon.
- If any referenced file is missing, inconsistent, or inaccessible, STOP and raise a Gate failure.


## Inputs (read-only)

### Feature agent artefacts (canonical)
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/01-personas-admin-centre.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/02-user-journeys-admin-centre.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/03-architect-admin-centre-tables-acls.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/04-security-admin-centre.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/05-platform-dev-admin-centre.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/06-frontend-dev-admin-centre.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/07-qa-admin-centre.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/08-build-agent-inputs-map.md

### Feature specifications (canonical)
- /rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md
- /rbm-knowledge/02-specifications-derived/admin-centre/servicenow-ide-instructions.md


# PROMPT 1 — Platform Foundation (Tables, Dictionary, ACLs)

## Scope Declaration (MANDATORY)
- ORG_CODE = {{ORG_CODE}}
- SCOPE_TAG = {{SCOPE_TAG}}
- APP_SCOPE = x_{{ORG_CODE}}_rbm_{{SCOPE_TAG}}
- APP_PREFIX = x_{{ORG_CODE}}_rbm_{{SCOPE_TAG}}


Authority:
- KB v2.0.0 authoritative
- Feature Definition: /rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md
- Policy: RBM-POL-STATE-001 — /rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md

Task:
Create all Admin Centre configuration tables and ACLs per Architect spec.

Inputs:
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/03-architect-admin-centre-tables-acls.md
- /rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/04-security-admin-centre.md

Deliver:
- Tables + dictionary
- Table/field ACLs
- Role reuse only
- No audit logic yet

Output:
List created tables, fields, ACL rules.