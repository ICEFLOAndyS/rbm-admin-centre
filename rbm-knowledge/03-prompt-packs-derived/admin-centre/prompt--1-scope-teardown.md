# PROMPT -1 — Prototype Scope Teardown (Optional)

## Authority
- Knowledge baseline ZIP is authoritative
- This prompt is OPTIONAL and MUST be executed manually
- Intended for prototype or sandbox environments only

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
