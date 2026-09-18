# Evidence Handling Procedure

## Purpose
Keep evidence useful, reproducible, minimal, and protected from accidental disclosure.

## Evidence Types
- Screenshots of lab-only behavior
- Sanitized request/response examples
- Synthetic application logs
- Asset/configuration observations
- Finding notes
- SHA-256 hashes where integrity verification is useful

## Collection Rules
1. Capture only what proves the finding.
2. Never include real passwords, API keys, tokens, personal data, or production information.
3. Use synthetic test accounts.
4. Record asset ID and finding ID.
5. Record collection time in IST.
6. Preserve original evidence before redaction.

## Example Evidence Record
| Evidence ID | Finding | Asset | Type | Timestamp | SHA-256 | Redacted |
|---|---|---|---|---|---|---|
| EV-001 | E-01 | LAB-WEB-01 | Screenshot | YYYY-MM-DD HH:MM IST | record hash | Yes |

## Storage and Retention
Store evidence only in approved lab storage. This public repository should contain sanitized documentation and synthetic examples only. At the end of the engagement, retain only required evidence and securely delete unnecessary material.

## Chain of Custody
For formal coursework, record Evidence ID, collector, date/time, source asset, purpose, hash where applicable, storage location, and any transformation/redaction.
