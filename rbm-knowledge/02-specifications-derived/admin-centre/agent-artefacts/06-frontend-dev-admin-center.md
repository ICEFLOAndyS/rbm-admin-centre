# Front-End Developer Plan — Admin Center UI (Derived)

## Inputs
- Personas/Journeys: `01-personas-admin-center.md`, `02-user-journeys-admin-center.md`
- Feature definition: `rbm-knowledge/DEPRECATED-specifications-derived (DO NOT USE)/admin-centre/admin-centre-feature-definition.md`
- Design system constraints: RBM reference components (authoritative tree)

## UI Information Architecture
- Admin Center Shell
  - Sections: Feature Flags, System Settings, Audit
- Each section:
  - List view (server-side paging/filter/sort)
  - Detail/edit view (RBM reference form components where available)
  - Confirmation modal for high-impact changes

## UI Behaviours (Non-Negotiable)
- Never enforce security in UI; always call server APIs
- Show permissions-driven UI states (read-only views) but rely on server for enforcement
- Handle errors with safe messages; surface audit reference where available

## Build Agent Prompt Inputs
- Component tree outline
- Data fetching patterns (server-side pagination)
- Interaction patterns (edit, confirm, save, error)
