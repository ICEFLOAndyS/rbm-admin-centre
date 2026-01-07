# Build Agent prompt input canonicalisation report

## Scope
- Feature: `admin-centre` (example feature)
- Prompts reviewed: `03-prompt-packs-derived/admin-centre/prompt-*.md`

## Rules enforced
- All file references are expressed as full canonical paths beginning with `/rbm-knowledge`.
- All feature artefact references resolve to existing files under:
  `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/`

## Artefacts validated
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/01-personas-admin-center.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/02-user-journeys-admin-center.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/03-architect-admin-center-tables-acls.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/04-security-admin-center.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/05-platform-dev-admin-center.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/06-frontend-dev-admin-center.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/07-qa-admin-center.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/agent-artefacts/08-build-agent-inputs-map.md` ✅ exists

## Specifications referenced
- `/rbm-knowledge/02-specifications-derived/admin-centre/admin-centre-feature-definition.md` ✅ exists
- `/rbm-knowledge/02-specifications-derived/admin-centre/servicenow-ide-instructions.md` ✅ exists

## Changes applied
- Inserted `## Inputs (read-only)` into every Admin Centre Build Agent prompt.
- Normalised any legacy `rbm-knowledge/...` paths to `/rbm-knowledge/...`.
- Corrected deprecated `DEPRECATED-specifications-derived (DO NOT USE)` references (if present) to `02-specifications-derived`.
