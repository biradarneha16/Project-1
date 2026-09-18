# Written Authorization & Scope

## 1. Authorization Record

This document establishes the governance boundary for an authorized security assessment of an intentionally vulnerable local training lab.

| Field | Approved Record |
|---|---|
| Lab owner | RabTech lab |
| Assessor | Student assessor |
| Approved assets | LAB-01 and LAB-02 only |
| Environment | Isolated localhost / private host-only network |
| Approval date | ____________________ |
| Approved window | Student-defined approved window |
| Emergency contact | ____________________ |
| Scope status | Pending owner/instructor sign-off |

**Authorization rule:** Never test a system that is absent from the approved asset inventory.

## 2. Approved Assets

The canonical asset list is maintained in authorized-lab-assets.csv.

- **LAB-01:** Local training web app — http://127.0.0.1:8080
- **LAB-02:** Deliberately vulnerable VM — 192.168.56.20

Both assets are marked as testing-allowed in the supplied asset specification.

## 3. Explicit Scope Exclusions

The following are outside the authorization boundary:

- Third-party targets or infrastructure.
- Public Internet systems.
- Any system not listed in the approved asset inventory.
- Denial-of-service activity.
- Destructive payloads.
- Persistence mechanisms.
- Credential reuse.
- Uncontrolled data extraction.
- Outbound traffic from the isolated lab.
- Real personal, financial, institutional or production data.

## 4. Authorization Conditions

- Testing occurs only inside the approved lab environment.
- The assessor uses only authorized lab identities and test data.
- Any proposed scope change requires owner/instructor approval and an updated inventory.
- Evidence is limited to the minimum required to support a finding.
- Unexpected impact or scope uncertainty requires immediate cessation and escalation.

## 5. Approval

| Role | Name | Signature / Approval | Date |
|---|---|---|---|
| Lab Owner | ____________________ | ____________________ | __________ |
| Assessor | ____________________ | ____________________ | __________ |
| Instructor / Reviewer | ____________________ | ____________________ | __________ |
