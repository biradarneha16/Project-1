# Evidence Handling & Retention

## Purpose

This procedure implements the supplied ROE requirement to store minimum evidence, redact secrets and personal data, and define deletion timing.

## Evidence Classification

The approved asset inventory classifies evidence from LAB-01 and LAB-02 as **Confidential training evidence**.

## Collection Rules

1. Capture only evidence necessary to support a finding.
2. Use synthetic training data only.
3. Never collect or retain real credentials, tokens, personal data or production information.
4. Record the source asset and finding ID.
5. Record date and time.
6. Preserve the original before redaction.
7. Create a sanitized copy for reporting.

## Evidence Register

| Evidence ID | Finding | Asset | Type | Timestamp | Classification | Redacted |
|---|---|---|---|---|---|---|
| EV-001 | F-001 | LAB-01 | Screenshot | __________________ | Confidential training evidence | Yes |
| EV-002 | F-002 | LAB-02 | Log/record | __________________ | Confidential training evidence | Yes |

## Integrity

Where appropriate, record a SHA-256 hash for collected files.

| Evidence ID | SHA-256 |
|---|---|
| EV-001 | ______________________________ |
| EV-002 | ______________________________ |

## Storage

- Store evidence only in approved lab storage.
- Restrict access to the assessor and authorized reviewer.
- Do not commit confidential evidence to this public GitHub repository.
- Keep only sanitized documentation and synthetic examples in the repository.

## Deletion Timing

**Evidence review completed:** ____________________  
**Deletion date:** ____________________  
**Deletion owner:** ____________________

At the deletion date, remove unnecessary evidence securely and confirm that no unauthorized data remains.

## Chain of Custody

For formal assessment, record:

- Evidence ID
- Collector
- Source asset
- Collection date/time
- Purpose
- Storage location
- Hash, where applicable
- Redaction/transformation performed
- Reviewer
