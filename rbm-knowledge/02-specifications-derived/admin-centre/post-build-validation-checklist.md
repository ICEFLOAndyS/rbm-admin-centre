# Post-Build Validation Checklist — Admin Centre

## Functional Validation
- Feature Flags module works end-to-end
- System Settings module works end-to-end
- Audit UI displays immutable records

## Security & Access
- RBM Read-Only cannot mutate data
- RBM Admin limited to scoped writes
- RBM Platform Admin has full admin access

## Audit & Evidence
- All actions logged (success + failure)
- Audit records immutable
- Evidence captured where required

## Technical
- React + TypeScript only
- No UI-authoritative security
- Server-side pagination/filtering

## Sign-off
- QA complete
- Evidence pack available
- Ready for release
