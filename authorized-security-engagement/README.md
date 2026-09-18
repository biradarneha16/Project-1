# Legal Scope, Asset Inventory & Threat Model

## Authorized Security Engagement — Professional Lab Dossier

**Repository:** Project-1  
**Engagement type:** Authorized local security assessment  
**Environment:** Intentionally vulnerable training lab  
**Primary objective:** Establish a defensible scope, inventory authorized assets, model threats, and define safe operating rules.

> **Important:** This dossier is for an isolated training environment. Testing must never extend to systems, accounts, networks, or data that are not explicitly authorized.

## 1. Engagement Objectives

- Establish written authorization before any testing begins.
- Define approved assets and explicit exclusions.
- Inventory assets, owners, environments, endpoints, and evidence classifications.
- Identify trust boundaries and data flows.
- Build a STRIDE-based threat model with abuse cases and mitigations.
- Define permitted techniques, testing windows, evidence handling, reporting, escalation, and stop conditions.

## 2. Source-Controlled Scope

The approved asset baseline is maintained in authorized-lab-assets.csv and is derived directly from the supplied Authorized Security Lab asset specification.

**Rule:** Never test a system that is absent from the approved asset inventory.

| Asset | Environment | Address | Testing |
|---|---|---|---|
| LAB-01 | Isolated localhost | 127.0.0.1:8080 | Yes |
| LAB-02 | Private host-only network | 192.168.56.20 | Yes |

The addresses above are lab targets supplied for this engagement. They must remain inside the intended isolated environment.

## 3. Deliverables

| Deliverable | Purpose |
|---|---|
| authorization.md | Written authorization, owners, boundaries and approval |
| authorized-lab-assets.csv | Canonical approved asset inventory |
| asset-inventory.csv | Structured threat-model inventory |
| data-flow-diagram.md | Data flows and trust boundaries |
| stride-threat-model.md | STRIDE register, abuse cases and mitigations |
| rules-of-engagement.md | Operational rules aligned to the supplied ROE template |
| evidence-handling.md | Evidence minimization, redaction and retention |
| lab-setup.md | Local lab isolation and pre/post-test controls |

## 4. Security Governance Principles

1. **Authorization first:** no testing before approval.
2. **Explicit scope:** only approved assets may be tested.
3. **Least privilege:** use lab-only identities and minimum permissions.
4. **Non-destructive validation:** demonstrate findings without unnecessary impact.
5. **Evidence minimization:** collect only what is required.
6. **Immediate escalation:** unexpected scope or impact triggers a stop.
7. **Traceability:** findings must identify asset, rationale, reproduction, impact, evidence and remediation.
8. **Controlled disclosure:** this public repository contains documentation and synthetic examples only.

## 5. Completion Criteria

The engagement documentation is complete when:

- written authorization identifies the lab owner, assessor, approved assets and approval date;
- the canonical asset inventory is reviewed and approved;
- permitted techniques and explicit exclusions are documented;
- the test window, emergency contact, rate limits and stop conditions are defined;
- evidence handling and deletion timing are documented;
- STRIDE threats, abuse cases and mitigations are recorded; and
- every finding can be reported using the required reporting fields.
