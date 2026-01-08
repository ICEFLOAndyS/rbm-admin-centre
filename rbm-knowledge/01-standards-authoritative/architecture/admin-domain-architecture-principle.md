# RBM Admin Domain Architecture Principle

## Principle ID
RBM-ARCH-ADMIN-001

## Applies To
All RBM features, modules, extensions, and content packs (current and future).

## Principle Statement
Admin and configuration functions for all RBM features SHALL be embedded within a single
**Admin Domain**, accessible via a main menu option titled **“Admin”**.

## Mandatory Navigation Pattern
1. **Main menu entry**
   - A single top-level menu option titled **Admin** SHALL exist.
2. **Admin landing page**
   - The Admin landing page SHALL present a set of **cards**.
   - Each card SHALL include:
     - An icon (Horizon icon set / RBM icon standards)
     - An Admin Domain title (sub-domain title)
3. **Optional second-level cards**
   - For complex sub-domains, clicking a landing card MAY open a second page consisting of cards.
   - The second-level page SHALL follow the same card structure (icon + title).
4. **Terminal navigation**
   - Where a sub-domain does not require a second-level card page, clicking the sub-domain card SHALL open
     a **list of configuration records** for that sub-domain.
   - Each record SHALL represent a **single configuration setting** for that sub-domain.

## Mandatory Configuration Record Model
1. Each configuration setting SHALL be represented as a single record.
2. Configuration changes SHALL be auditable (created/updated metadata as minimum; additional audit per security standards where required).
3. Configuration data MUST be enforceable server-side; UI is not security-authoritative.

## Role and Access Model
1. The Admin menu option SHALL be visible to any user holding an **admin-related role**.
2. Each Admin sub-domain MAY define one or more **sub-domain roles** (e.g., read / write / admin) where least-privilege requires it.
3. All access control MUST be enforced via server-side roles/ACLs in accordance with RBM security standards.

## Feature Delivery Requirement (Non-Negotiable)
Every new feature SHALL explicitly consider required Admin/configuration functionality and SHALL implement
Admin integration consistent with this principle.

Minimum required outputs per feature (where applicable):
- Gate 0: Admin Domain impact documented (sub-domain placement, navigation depth, configuration records)
- Gate 2: Roles and ACLs defined for Admin menu and sub-domain
- Gate 3: UI contract includes Admin card(s) and configuration list behaviour
- Gate 4: API contract includes configuration record read/write interfaces where required

## Canonical Reference
RBM-ARCH-ADMIN-001 — /rbm-knowledge/01-standards-authoritative/architecture/admin-domain-architecture-principle.md
