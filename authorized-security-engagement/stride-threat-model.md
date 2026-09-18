# STRIDE Threat Model

## 1. Method

The model applies STRIDE to the authorized lab assets and their trust boundaries:

- **S — Spoofing:** impersonating an identity.
- **T — Tampering:** unauthorized modification.
- **R — Repudiation:** inability to establish accountability.
- **I — Information Disclosure:** unauthorized exposure.
- **D — Denial of Service:** loss of availability.
- **E — Elevation of Privilege:** gaining unauthorized permissions.

Because the supplied ROE explicitly excludes denial-of-service activity, availability risks are documented as threats but must not be actively exercised.

## 2. STRIDE Register

| ID | Asset | Boundary | Category | Abuse Case | Impact | Likelihood | Risk | Mitigation |
|---|---|---|---|---|---|---|---|---|
| S-01 | LAB-01 | TB-01 | Spoofing | A test identity is impersonated | High | Medium | High | Strong lab authentication and session controls |
| T-01 | LAB-01 | TB-01 | Tampering | Unauthorized application input changes test data | High | Medium | High | Server-side validation and authorization |
| R-01 | LAB-01/LAB-02 | TB-02 | Repudiation | A security-relevant action cannot be traced to a test identity | Medium | Medium | Medium | Timestamped audit logging |
| I-01 | LAB-01 | TB-01 | Information Disclosure | Error output exposes sensitive training details | High | Medium | High | Safe errors, redaction and least privilege |
| D-01 | LAB-01 | TB-01 | Denial of Service | Excessive activity could degrade availability | High | Medium | High | Rate limits and monitoring; no active DoS testing |
| E-01 | LAB-01/LAB-02 | TB-02 | Elevation of Privilege | Low-privilege identity reaches a restricted function | High | Medium | High | Server-side authorization and role checks |
| I-02 | LAB-02 | TB-02 | Information Disclosure | Application exposes unauthorized training records | High | Medium | High | Object-level authorization |
| T-02 | LAB-02 | TB-02 | Tampering | Unauthorized record modification occurs | High | Low | Medium | Authorization and transaction controls |
| R-02 | LAB-02 | TB-02 | Repudiation | Changes cannot be attributed to an identity | Medium | Low | Medium | Protected audit logs |
| D-02 | LAB-02 | TB-03 | Denial of Service | Resource exhaustion affects the VM | High | Low | Medium | Resource monitoring; no active DoS testing |
| I-03 | Lab boundary | TB-03 | Information Disclosure | Test traffic or evidence leaves the lab | High | Low | Medium | Host-only isolation and outbound controls |

## 3. Abuse Cases

### AC-01 — Identity Impersonation
A lab-only identity is used to attempt access as another test identity. Validation must use synthetic accounts.

### AC-02 — Unauthorized Data Access
A lower-privilege lab identity attempts to access data belonging to another synthetic identity. The expected security control is server-side authorization.

### AC-03 — Privilege Boundary Violation
A normal lab user attempts to access a restricted administrative function. The expected result is denial and an auditable event.

### AC-04 — Information Leakage
A controlled validation causes an application error. The expected result is a safe response without secrets or unnecessary internal details.

### AC-05 — Availability Risk
The model recognizes resource exhaustion as a threat, but the ROE prohibits active denial-of-service testing. Availability is therefore assessed through configuration, monitoring and safe non-disruptive observations.

## 4. Mitigation Register

| Priority | Control | Threats Addressed |
|---|---|---|
| 1 | Server-side authentication and authorization | S-01, E-01, I-02 |
| 2 | Least-privilege test identities | S-01, E-01 |
| 3 | Input validation and integrity controls | T-01, T-02 |
| 4 | Secure error handling and redaction | I-01, I-03 |
| 5 | Protected audit logging | R-01, R-02 |
| 6 | Rate limits and resource monitoring | D-01, D-02 |
| 7 | Host-only network isolation | I-03, D-02 |
