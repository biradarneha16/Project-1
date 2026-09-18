# Rules of Engagement (ROE)

## 1. Authorization
Testing is authorized only for assets listed in asset-inventory.csv. The lab owner must approve this ROE before testing.

## 2. Test Window
Approved window: ____________________
Time zone: IST (UTC+05:30)
Tester: ____________________
Approver: ____________________

Testing outside the approved window requires renewed authorization.

## 3. Permitted Activities
- Asset and service discovery inside the isolated lab
- Safe vulnerability identification
- Manual authentication and authorization checks using lab accounts
- Controlled input validation
- Synthetic log review
- Non-destructive proof-of-concept validation
- Documentation and risk analysis

## 4. Prohibited Activities
- Public Internet or third-party testing
- Production-system testing
- Real credential theft
- Real personal or financial data collection
- Malware or persistence
- Destructive changes
- Uncontrolled denial of service
- Social engineering of real people
- Attempts to bypass the authorization boundary

## 5. Evidence Handling
Capture only minimum necessary evidence. Use synthetic data, consistent timestamps, redaction, and approved storage. Do not publish credentials or sensitive evidence.

Suggested filename: YYYYMMDD-HHMM-FINDING-ID-EVIDENCE-TYPE.ext

## 6. Escalation
Immediately notify the lab owner if an out-of-scope host appears reachable, real sensitive data is encountered, the lab becomes unstable, traffic leaves the isolated network, or unexpected destructive effects occur.

## 7. Stop Conditions
Stop immediately when:
1. Scope becomes uncertain.
2. A non-lab system may be affected.
3. Real sensitive data is discovered.
4. Significant instability occurs.
5. A test could cause irreversible or destructive changes.
6. Authorization expires.
7. The lab owner requests a stop.

Resume only after the owner re-confirms safety and scope.

## 8. Recovery
Stop the test, preserve relevant evidence, record the time and affected asset, notify the owner, restore the lab snapshot/backup if needed, and document the event.

## 9. Acceptance
| Role | Name | Approval | Date |
|---|---|---|---|
| Lab Owner | __________________ | __________________ | __________ |
| Security Tester | __________________ | __________________ | __________ |
| Instructor/Reviewer | __________________ | __________________ | __________ |
