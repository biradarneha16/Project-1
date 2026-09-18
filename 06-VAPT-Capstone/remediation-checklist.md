# Remediation Checklist

## Developers
- [ ] Replace dynamic SQL with parameterized queries.
- [ ] Apply context-aware output encoding for XSS.
- [ ] Review authentication and session lifecycle.
- [ ] Use bcrypt/Argon2id/scrypt for password storage.
- [ ] Add rate limiting and secure cookie attributes.
- [ ] Add regression tests for every confirmed finding.
- [ ] Retest after deployment.

## Sysadmins
- [ ] Disable unnecessary services.
- [ ] Restrict management interfaces.
- [ ] Apply firewall and segmentation controls.
- [ ] Patch exposed software.
- [ ] Rotate compromised or exposed credentials.
- [ ] Enable centralized logging and monitoring.
- [ ] Verify backup and recovery procedures.
- [ ] Retest the affected asset.

## Closure
- [ ] Evidence attached.
- [ ] CVSS vector documented.
- [ ] OWASP mapping documented.
- [ ] Owner assigned.
- [ ] Remediation completed.
- [ ] Retest passed.
- [ ] Mentor review completed.
