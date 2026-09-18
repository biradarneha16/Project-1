# STRIDE Threat Model

Risk is recorded qualitatively using likelihood and impact.

| ID | Asset | STRIDE | Abuse Case | Impact | Likelihood | Risk | Mitigation |
|---|---|---|---|---|---|---|---|
| S-01 | LAB-WEB-01 | Spoofing | Use another lab identity | High | Medium | High | Strong authentication and session controls |
| T-01 | LAB-WEB-01 | Tampering | Unauthorized input or record modification | High | Medium | High | Server-side validation and authorization |
| R-01 | WEB/LOG | Repudiation | Action cannot be linked to an identity | Medium | Medium | Medium | Timestamped audit logs |
| I-01 | LAB-WEB-01 | Information Disclosure | Errors reveal synthetic secrets/internal details | High | Medium | High | Safe errors, redaction, least privilege |
| D-01 | LAB-WEB-01 | Denial of Service | Controlled excessive requests degrade the app | Medium | Medium | Medium | Rate limits and strict test limits |
| E-01 | WEB/DB | Elevation of Privilege | Low-privilege user reaches admin function | High | Medium | High | Server-side role and authorization checks |
| I-02 | LAB-DB-01 | Information Disclosure | User accesses another synthetic user's records | High | Medium | High | Object-level authorization |
| T-02 | LAB-DB-01 | Tampering | Unauthorized database record change | High | Low | Medium | Transaction authorization and auditing |
| R-02 | LAB-LOG-01 | Repudiation | Logs altered without accountability | Medium | Low | Medium | Restricted access and integrity monitoring |
| D-02 | LAB-LOG-01 | Denial of Service | Excessive logs overwhelm monitoring | Medium | Low | Medium | Quotas, rate limits, recovery plan |

## Abuse Cases
### AC-01 Account Impersonation
A lab user attempts to operate as another test identity. Use synthetic accounts only.

### AC-02 Unauthorized Record Access
A low-privilege test identity attempts to access another synthetic identity's record. Expected property: server-side authorization.

### AC-03 Administrative Function Access
A normal test identity attempts an administrative function. Expected result: denial and an auditable event.

### AC-04 Information Leakage
A controlled application error is generated. Expected result: no secrets, stack traces, or internal infrastructure details.

### AC-05 Controlled Resource Exhaustion
A limited lab-only test checks protective controls. Stop before instability threatens the host or any non-lab system.

## Mitigation Priorities
1. Server-side authentication and authorization.
2. Least-privilege lab identities.
3. Synthetic data and information-disclosure controls.
4. Reliable audit logging.
5. Resource limits and monitoring.
6. Network isolation.
