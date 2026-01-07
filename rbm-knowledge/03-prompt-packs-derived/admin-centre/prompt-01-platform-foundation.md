# PROMPT 1 — Platform Foundation (Tables, Dictionary, ACLs)

## Scope Declaration (MANDATORY)
- ORG_CODE = {{ORG_CODE}}
- SCOPE_TAG = {{SCOPE_TAG}}
- APP_SCOPE = x_{{ORG_CODE}}_rbm_{{SCOPE_TAG}}
- APP_PREFIX = x_{{ORG_CODE}}_rbm_{{SCOPE_TAG}}


Authority:
- KB v2.0.0 authoritative
- Feature Definition: rbm-knowledge/05-specifications-derived/admin-centre/admin-centre-feature-definition.md
- Policy: RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md

Task:
Create all Admin Center configuration tables and ACLs per Architect spec.

Inputs:
- 03-architect-admin-center-tables-acls.md
- 04-security-admin-center.md

Deliver:
- Tables + dictionary
- Table/field ACLs
- Role reuse only
- No audit logic yet

Output:
List created tables, fields, ACL rules.