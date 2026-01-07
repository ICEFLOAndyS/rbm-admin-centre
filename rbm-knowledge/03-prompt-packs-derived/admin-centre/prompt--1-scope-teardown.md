# PROMPT -1 — Prototype Scope Teardown (Optional)

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

## Parameters (MUST be supplied)
- APP_SCOPE = {{APP_SCOPE}}

## Task
1. Verify the scoped application exists with scope = APP_SCOPE
2. Enumerate artefacts owned by the scope:
   - Tables
   - Script Includes / APIs
   - UI components
3. Report findings and request confirmation before destructive action

## Destructive Action (ONLY AFTER CONFIRMATION)
4. If confirmed:
   - Delete the scoped application and all owned artefacts
   - Report completion status

## Constraints
- DO NOT run in production
- DO NOT infer scope
- DO NOT auto-confirm deletion

## Output
- Discovery report
- Confirmation prompt
- Final status
