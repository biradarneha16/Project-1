# Written Authorization & Scope

## Engagement Statement
This document authorizes security testing of an intentionally vulnerable **local training laboratory** only. Testing is permitted only against assets listed in the approved inventory and during the approved test window.

| Field | Value |
|---|---|
| Engagement | Legal Scope, Asset Inventory & Threat Model |
| Environment | Local isolated cybersecurity lab |
| Asset owner | Lab owner / course instructor |
| Security tester | Authorized student tester |
| Authorization | Written lab authorization |
| Test window | Scheduled lab sessions only |
| Evidence owner | Security tester |
| Escalation contact | Lab owner / course instructor |

## In Scope
- Vulnerable training web application
- Training database
- Test client
- Local log/monitoring service
- Authorized tester workstation

## Out of Scope
- Public Internet targets
- College, employer, government, banking, healthcare, or other production systems
- Third-party websites and APIs
- Personal devices belonging to other people
- Real customer or personally identifiable information
- Production cloud accounts
- Shared networks outside the isolated lab
- Any IP, hostname, application, account, or data store not in the approved inventory
- Uncontrolled denial-of-service testing
- Persistence, destructive changes, malware deployment, or credential theft

## Authorization Conditions
1. Testing begins only after the lab owner approves this scope.
2. New assets require explicit written approval.
3. Use lab-only credentials.
4. Collect minimum necessary evidence.
5. Stop immediately if an out-of-scope system could be affected.
6. Preserve the lab state and report unexpected impact.

## Scope Change
Record the asset, owner, reason, new risk, approval date, and approver for every scope change.
