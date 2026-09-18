# Local Intentionally Vulnerable Lab Setup

## Goal
Create a deliberately vulnerable environment isolated from production and the public Internet.

## Example Topology
- Tester workstation: 192.168.56.50
- Vulnerable web application: 192.168.56.10
- Training database: 192.168.56.20
- Test client: 192.168.56.30
- Log server: 192.168.56.40

These addresses are examples only.

## Isolation Requirements
- Use a host-only/private virtual network.
- Never expose the vulnerable app publicly.
- Do not bridge lab machines to a production network.
- Take snapshots before testing.
- Use synthetic data and lab-only credentials.
- Disable unnecessary external integrations.

## Training Application
An instructor-approved intentionally vulnerable training application such as OWASP Juice Shop may be used. It must remain a local training target.

## Test Identities
Create separate lab-only accounts such as:
- student-user
- student-manager
- student-admin

Passwords must be unique to the lab and never reused from personal, college, or work accounts.

## Pre-Test Checklist
- [ ] Written authorization approved
- [ ] Asset inventory completed
- [ ] Lab network isolated
- [ ] Test accounts created
- [ ] Synthetic data loaded
- [ ] Snapshots/backups available
- [ ] Logging enabled
- [ ] Test window confirmed
- [ ] Stop conditions reviewed

## Post-Test Checklist
- [ ] Testing stopped at approved time
- [ ] Evidence sanitized
- [ ] Findings documented
- [ ] Lab restored if required
- [ ] Temporary credentials removed
- [ ] No real sensitive data retained
