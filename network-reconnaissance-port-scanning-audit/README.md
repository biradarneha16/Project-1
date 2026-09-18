# 03 — Network Reconnaissance & Port Scanning Audit

**Project:** Authorized Security Engagement — Project-1  
**Status:** Ready for execution; evidence pending  
**Owner:** Neha Biradar  
**Repository:** https://github.com/biradarneha16/Project-1

## Objective

Perform controlled network reconnaissance and vulnerability-oriented scanning against an **authorized simulated/sandbox target only**, using Nmap and Wireshark.

## Required activities

1. TCP SYN reconnaissance.
2. UDP service discovery.
3. Service/version enumeration.
4. OS detection.
5. Wireshark packet-capture review.
6. Documentation of exposed ports, services, observations, and potential attack vectors.
7. Compilation of a formal Network Reconnaissance Findings Report.

## Evidence standard

This folder intentionally does **not** contain fabricated scan results or screenshots. Actual Nmap output and Wireshark screenshots must be collected from the authorized lab and inserted into the evidence directory.

### Deliverables

| File | Purpose |
|---|---|
| `scan-plan.md` | Controlled execution procedure and commands |
| `findings-report.md` | Formal report ready to populate with real evidence |
| `wireshark-analysis.md` | Packet-analysis procedure and evidence checklist |
| `evidence-index.csv` | Evidence register |
| `evidence/` | Nmap output, PCAP/PCAPNG and screenshots |

## Safety boundary

Use only an explicitly authorized sandbox/lab host. Do not scan public IP addresses, third-party systems, college infrastructure, or other hosts without written authorization.

## Completion criteria

The task can be marked **Completed** only after:

- all required scans have been run against the authorized target;
- raw outputs are preserved;
- Wireshark evidence is captured;
- findings are correlated with observed evidence;
- the report is reviewed;
- the final PDF is generated from the completed report.

> **Important:** The repository currently contains the professional documentation framework, not claimed scan results. This avoids presenting invented Nmap findings or Wireshark captures as real evidence.
