# Wireshark Analysis Guide

## Purpose

Analyze traffic captured from the authorized sandbox environment and document evidence relevant to network exposure, plaintext protocols, authentication material, and anomalous behavior.

## Capture procedure

1. Verify the target is within the authorized asset inventory.
2. Start Wireshark on the lab interface.
3. Generate only permitted test traffic.
4. Stop capture after the defined test window.
5. Save the original capture as `evidence/network-audit.pcapng`.
6. Preserve the original capture; perform analysis on a working copy.

## Display-filter checklist

Use only filters relevant to the observed traffic:

```
tcp
udp
dns
http
ftp
telnet
http.request
tcp.port == 80
tcp.port == 21
tcp.port == 23
```

## What to inspect

### 1. Protocol identification

Record unexpected protocols or protocols inconsistent with the authorized test scenario.

### 2. Cleartext authentication

Look for authorized lab traffic where credentials may be transmitted without encryption. If present:

- record protocol and frame number;
- capture a screenshot;
- redact the credential value;
- do not copy the actual password/token into the repository.

### 3. TCP streams

Use **Follow → TCP Stream** for an authorized stream when it helps establish the security observation. Capture a screenshot of the relevant portion with sensitive values redacted.

### 4. Anomalous behavior

Consider:

- unexpected destination ports;
- unusual protocol use;
- repeated connection attempts;
- unexpected cleartext application traffic;
- traffic inconsistent with the documented lab scenario.

An anomaly is an observation requiring context, not automatically evidence of malicious activity.

## Screenshot checklist

- [ ] Packet list visible
- [ ] Relevant frame selected
- [ ] Protocol details visible
- [ ] Timestamp/frame number visible
- [ ] Source/destination shown where safe
- [ ] Sensitive values redacted
- [ ] Screenshot filename recorded in evidence-index.csv

## Evidence integrity

After collecting evidence, calculate SHA-256 hashes:

```bash
sha256sum evidence/*
```

Record the resulting hashes in `findings-report.md` and `evidence-index.csv`.

## Reporting language

Prefer:

> “Frame 184 shows an HTTP request containing an authentication parameter in cleartext.”

Avoid unsupported statements such as:

> “The host was hacked.”

The report should describe what the capture proves and clearly separate observations from interpretation.
