# Legal Scope, Asset Inventory & Threat Model

## Authorized Security Engagement Lab Dossier

This dossier defines a controlled, authorized cybersecurity assessment for an intentionally vulnerable **local lab**.

**Safety boundary:** Test only systems explicitly listed in the approved inventory. Never use this documentation against public, production, third-party, or otherwise unauthorized systems.

## Objectives
1. Establish written authorization and a precise testing boundary.
2. Inventory assets, identities, trust boundaries, data classes, and attack surfaces.
3. Model threats using STRIDE.
4. Define abuse cases and ranked mitigations.
5. Define rules of engagement, evidence handling, escalation, and stop conditions.

## Deliverables
- authorization.md — authorization and scope
- asset-inventory.csv — authorized asset inventory
- data-flow-diagram.md — DFD and trust boundaries
- stride-threat-model.md — STRIDE register
- rules-of-engagement.md — ROE
- evidence-handling.md — evidence procedure
- lab-setup.md — isolated local lab setup

## Scope
**In scope:** only assets listed in asset-inventory.csv and controlled by the lab owner.

**Out of scope:** public websites, production systems, third-party infrastructure, personal accounts, real customer data, unapproved cloud resources, and any unlisted host.

## Completion Criteria
Every in-scope asset has an owner and purpose; every trust boundary has threats; significant threats have mitigations; and the ROE defines testing windows, evidence handling, escalation, and safe stopping conditions.
