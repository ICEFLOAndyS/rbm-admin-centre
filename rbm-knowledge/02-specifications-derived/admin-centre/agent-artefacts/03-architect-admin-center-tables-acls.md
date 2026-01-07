# ServiceNow Architect Output — Admin Center (Derived)

## Authority & Inputs
- Knowledge Baseline: v2.0.0
- Feature Definition: `rbm-knowledge/DEPRECATED-specifications-derived (DO NOT USE)/admin-centre/admin-centre-feature-definition.md`
- Policy: RBM-POL-STATE-001 — rbm-knowledge/01-standards-authoritative/architecture/state-management-policy.md
- Dev standards: `rbm-knowledge/01-standards-authoritative/development/development-standards-authoritative.md`

## A. Data Model — Proposed Tables (Configuration Domain)

> Note: Exact table naming must conform to authoritative naming standards and scoped app prefixing.

### A1. Feature Flags
- **Table:** `{{APP_PREFIX}}_feature_flag` (proposed)
- **Purpose:** Capability toggles (enable/disable) and metadata.
- **Key fields (minimum):**
  - `name` (string, unique)
  - `key` (string, unique; stable identifier)
  - `enabled` (boolean)
  - `scope` (choice: platform / scoped)
  - `impact_level` (choice: low/medium/high)
  - `notes` (string or journal)
  - `updated_by`, `updated_on` (system)
- **Constraints:** Unique key; impact_level used for UI/guardrail prompts (UI non-authoritative).

### A2. System Settings
- **Table:** `{{APP_PREFIX}}_system_setting` (proposed)
- **Purpose:** Centralised configuration values with validation metadata.
- **Key fields (minimum):**
  - `name` (string)
  - `key` (string, unique)
  - `value_type` (choice: string/number/boolean/json)
  - `value` (string) and/or typed columns if required
  - `allowed_values` (string/json) optional
  - `min_value`, `max_value` (number) optional
  - `impact_level` (low/medium/high)
  - `description` (string)
  - `updated_by`, `updated_on` (system)

### A3. Admin Audit Event
- **Table:** `{{APP_PREFIX}}_admin_audit` (proposed)
- **Purpose:** Immutable record of admin actions; server-authoritative audit.
- **Key fields (minimum):**
  - `action_type` (choice: create/update/delete/enable/disable/permission_change/etc.)
  - `target_table` (string)
  - `target_sys_id` (string)
  - `before` (json/text)
  - `after` (json/text)
  - `status` (success/failure)
  - `error_message` (string) for failures
  - `actor` (reference to sys_user)
  - `occurred_on` (datetime)
  - `evidence_ref` (string/reference) optional

## B. Access Control (ACL) — Role Reuse Only

### Roles (existing)
- RBM Platform Admin — full admin center write
- RBM Admin — scoped write where permitted
- RBM Read-Only — read access to audit and view-only modules

### ACL model (high-level)
1. **Tables A1/A2**
   - Read: RBM Read-Only, RBM Admin, RBM Platform Admin
   - Write: RBM Admin (scoped records only), RBM Platform Admin
   - Delete: RBM Platform Admin only (if deletion is allowed at all)
2. **Audit table**
   - Read: RBM Read-Only, RBM Admin, RBM Platform Admin
   - Write: system-only (via server-side business rule / script include / API)
   - Delete: none (or system-only with retention controls)

## C. Server-side Enforcement Points
- Scripted APIs / Script Includes used by UI call path must enforce:
  - role/capability checks
  - field-level validation
  - audit write on success/failure
- UI is explicitly non-authoritative.

## D. Artefacts for Build Agent Prompt Inputs
- Table specs (above)
- ACL intent (above)
- Enforcement pattern requirements (audit on all actions)
