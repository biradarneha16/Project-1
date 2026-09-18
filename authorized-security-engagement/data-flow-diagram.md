# Data-Flow Diagram & Trust Boundaries

## Logical DFD

~~~mermaid
flowchart LR
    T[Authorized Tester Workstation] -->|Controlled test traffic| W[Vulnerable Web App]
    C[Test Client] -->|User requests| W
    W -->|Application queries| D[(Training Database)]
    W -->|Synthetic security events| L[Log Server]
    T -->|Log review| L
~~~

## Trust Boundaries

| Boundary | Description | Main concern |
|---|---|---|
| TB-1 | Tester Zone -> Application Zone | Scope expansion or unsafe input |
| TB-2 | Client Zone -> Application Zone | Authentication and authorization |
| TB-3 | Application Zone -> Data Zone | Database access and data integrity |
| TB-4 | Application Zone -> Monitoring Zone | Log integrity and disclosure |
| TB-5 | Lab -> Host/Internet | Accidental traffic leaving the lab |

## Data Classes
- Public: documentation and intentionally public lab metadata.
- Test: synthetic users, requests, sample records, and logs.
- Confidential-Test: synthetic secrets or credentials created only for the lab.
- Restricted: real personal, financial, institutional, or production information. **Prohibited in the lab.**
