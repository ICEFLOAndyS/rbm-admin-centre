# PROMPT 2 — Platform Services (APIs + Audit + Rollback)

## Scope Declaration (MANDATORY)
- ORG_CODE = {{ORG_CODE}}
- SCOPE_TAG = {{SCOPE_TAG}}
- APP_SCOPE = x_{{ORG_CODE}}_rbm_{{SCOPE_TAG}}
- APP_PREFIX = x_{{ORG_CODE}}_rbm_{{SCOPE_TAG}}


Authority:
Same as Prompt 1

Task:
Implement server-side APIs/resources and immutable audit logging.

Inputs:
- 05-platform-dev-admin-centre.md
- 04-security-admin-centre.md

Deliver:
- Script Includes / APIs
- Audit writer (success + failure)
- Rollback on partial failure