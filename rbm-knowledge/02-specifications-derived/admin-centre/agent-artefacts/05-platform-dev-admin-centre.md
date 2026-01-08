# Platform Developer Plan — Admin Centre (Derived)

## Inputs
- Architect artefact: `03-architect-admin-centre-tables-acls.md`
- Security artefact: `04-security-admin-centre.md`
- Feature definition: `/rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md`

## Server-side Components (proposed)
1. Tables + dictionary:
   - feature flags
   - system settings
   - admin audit
2. ACLs:
   - table-level and field-level as needed
3. Business rules / script includes:
   - validate writes
   - write immutable audit event
   - rollback on partial failure
4. APIs for UI:
   - list endpoints with server-side pagination/filter/sort
   - get-by-id
   - update (with validation and audit)
   - create (if required)
   - delete (if permitted; prefer soft-delete)
5. Evidence capture hooks:
   - for configuration and permission changes as required by governance

## Build Agent Prompt Inputs
- Explicit file/module list to create
- Endpoints contracts (request/response)
- Audit schema and write pattern
