# Data-Flow Diagram & Trust Boundaries

## 1. Scope-Aligned Logical DFD

~~~mermaid
flowchart LR
    A[Authorized Assessor] -->|Approved assessment traffic| W[LAB-01 - Local Training Web App - 127.0.0.1:8080]
    W -->|Controlled application flow| V[LAB-02 - Deliberately Vulnerable VM - 192.168.56.20]
    X[Third-Party / Public / Production Systems] -.->|OUT OF SCOPE| W
~~~

## 2. Trust Boundaries

| Boundary | Description | Security Question |
|---|---|---|
| TB-01 | Assessor -> LAB-01 | Is assessment traffic limited to the approved application? |
| TB-02 | LAB-01 -> LAB-02 | Are application-to-VM interactions authorized and controlled? |
| TB-03 | Lab -> External systems | Can traffic accidentally leave the isolated environment? |

## 3. Data Classes

| Class | Description | Handling |
|---|---|---|
| Public | Project documentation | Safe for repository publication |
| Test | Synthetic lab requests/results | Use only for assessment |
| Confidential training evidence | Screenshots, logs and finding evidence | Minimize, redact and restrict |
| Restricted | Real personal/production data | Prohibited |

## 4. Data-Flow Controls

- Use synthetic training data only.
- Do not reuse personal, college, work or production credentials.
- Do not export uncontrolled data from the lab.
- Redact secrets and personal data from evidence.
- Verify isolation before assessment begins.
