# Authorized Security Lab — Rules of Engagement

## Written authorization

### Authorization record

| Field | Required value |
|---|---|
| Lab owner | RabTech lab |
| Assessor | Student assessor |
| Approved assets | LAB-01 and LAB-02 |
| Approval date | ____________________ |
| Approved window | Student-defined approved window |
| Emergency contact | ____________________ |

Testing is authorized only for assets explicitly listed in the approved asset inventory. Never test a system that is absent from the inventory.

### Approved assets

- **LAB-01:** Local training web app — http://127.0.0.1:8080
- **LAB-02:** Deliberately vulnerable VM — 192.168.56.20

## Permitted techniques

The following activities are allowed only within the isolated lab and approved window:

1. Asset and service reconnaissance against LAB-01 and LAB-02.
2. Safe identification of exposed services and application behavior.
3. Manual validation of authentication and authorization controls using lab-only identities.
4. Controlled, non-destructive input validation.
5. Safe review of application responses, logs and security controls.
6. Documentation of findings and risk rationale.
7. Non-destructive proof-of-concept validation where required to demonstrate a finding.

All reconnaissance must remain limited to the two approved assets. No third-party scanning is permitted.

## Explicit exclusions

The following activities are prohibited:

- Denial-of-service testing.
- Destructive payloads or destructive changes.
- Persistence mechanisms.
- Credential reuse.
- Third-party targets or scanning.
- Public or production system testing.
- Outbound traffic from the deliberately vulnerable VM.
- Uncontrolled data extraction.
- Collection of real personal, financial, institutional or production information.
- Malware deployment.
- Social engineering of real people.

These exclusions are mandatory and override any assumption that a technique is acceptable merely because it is technically possible.

## Testing window and stop conditions

### Testing window

**Start:** ____________________  
**End:** ____________________  
**Time zone:** IST (UTC+05:30)  
**Assessor:** ____________________

Testing outside the approved window requires renewed authorization.

### Rate limits

- Use conservative request rates.
- Avoid automated activity that could destabilize the lab.
- Do not perform denial-of-service testing.
- Stop automated activity immediately if abnormal resource consumption is observed.

### Emergency contact

**Primary:** ____________________  
**Secondary:** ____________________

### Immediate stop conditions

Stop testing immediately if:

1. A system outside LAB-01 or LAB-02 becomes reachable or is affected.
2. Traffic leaves the isolated lab unexpectedly.
3. Real personal, production or otherwise unauthorized data is encountered.
4. The lab becomes unstable or resource consumption becomes unsafe.
5. A test could cause destructive or irreversible changes.
6. Authorization expires.
7. The lab owner, instructor or emergency contact directs the assessor to stop.

After a stop, preserve minimum relevant evidence, notify the appropriate contact, and do not resume until scope and safety are reconfirmed.

## Evidence handling

Evidence must be limited to the minimum necessary to support each finding.

### Evidence controls

- Store evidence only in approved lab storage.
- Redact secrets, credentials, tokens and personal data.
- Use synthetic test data.
- Record asset ID and finding ID.
- Record collection date/time.
- Keep original evidence protected before creating a redacted copy.
- Do not publish confidential training evidence in this public repository.
- Define deletion timing before evidence collection begins.

**Deletion date:** ____________________  
**Evidence owner:** ____________________

### Suggested evidence naming

YYYYMMDD-HHMM-FINDING-ID-EVIDENCE-TYPE.ext

Example:

20260918-1030-F-001-screenshot.png

## Reporting

Every finding must record:

| Required field | Description |
|---|---|
| Asset | LAB-01 or LAB-02 |
| Finding ID | Unique identifier |
| Severity rationale | Why the severity was assigned |
| Reproduction steps | Safe, lab-only steps sufficient to reproduce |
| Impact | Confidentiality, integrity, availability or privilege effect |
| Evidence | Minimum supporting evidence |
| Remediation | Specific corrective control |

### Finding template

**Finding ID:** ____________________  
**Asset:** ____________________  
**Title:** ____________________  
**Severity:** ____________________  
**Severity rationale:** ____________________  

**Reproduction steps:**  
1. ____________________  
2. ____________________  
3. ____________________

**Impact:** ____________________

**Evidence:** ____________________

**Remediation:** ____________________

## Approval

| Role | Name | Signature / Approval | Date |
|---|---|---|---|
| Lab Owner | ____________________ | ____________________ | __________ |
| Assessor | ____________________ | ____________________ | __________ |
| Instructor / Reviewer | ____________________ | ____________________ | __________ |
