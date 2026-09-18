# Scan Plan — Authorized Sandbox

## 1. Scope

**Target:** Replace `<AUTHORIZED_TARGET>` with the IP address/hostname documented in the engagement authorization.

**Interface:** Replace `<INTERFACE>` with the lab capture interface when required.

**Date/time:** Record the actual execution time.

## 2. Pre-scan validation

Confirm that the target appears in the approved asset inventory and that the authorization covers:

- TCP SYN scanning
- UDP scanning
- Service/version detection
- OS detection
- Packet capture and analysis

Do not proceed if authorization or target identity is unclear.

## 3. Nmap execution

Run the following against the authorized sandbox target.

### TCP SYN scan

```bash
sudo nmap -sS -Pn -T3 <AUTHORIZED_TARGET> -oA evidence/nmap-tcp-syn
```

### UDP scan

For a controlled lab, start with the most relevant UDP ports or a documented port range:

```bash
sudo nmap -sU -Pn -T3 --top-ports 100 <AUTHORIZED_TARGET> -oA evidence/nmap-udp-top100
```

If the lab authorization specifically permits a broader UDP range:

```bash
sudo nmap -sU -Pn -T3 -p <AUTHORIZED_UDP_PORT_RANGE> <AUTHORIZED_TARGET> -oA evidence/nmap-udp
```

### Service/version detection

```bash
sudo nmap -sV -Pn -T3 <AUTHORIZED_TARGET> -oA evidence/nmap-service-version
```

### OS detection

```bash
sudo nmap -O -Pn -T3 <AUTHORIZED_TARGET> -oA evidence/nmap-os
```

### Combined audit scan

Only when allowed by the rules of engagement:

```bash
sudo nmap -sS -sV -O -Pn -T3 <AUTHORIZED_TARGET> -oA evidence/nmap-combined
```

## 4. Evidence preservation

Keep the generated `.nmap`, `.gnmap`, and `.xml` files. Do not manually edit raw output.

For each scan, record:

- command executed;
- target;
- timestamp;
- operator;
- source host;
- result filename;
- relevant observations.

## 5. Wireshark capture

Start Wireshark on the **authorized lab interface** before generating permitted test traffic.

Recommended display filters for analysis:

```
tcp
udp
http
ftp
telnet
dns
http.request
tcp.port == 80
tcp.port == 21
tcp.port == 23
```

Use protocol-specific filters only when relevant to the services actually observed.

## 6. Wireshark evidence

Capture screenshots showing:

1. packet list with timestamp/source/destination/protocol;
2. protocol details for a relevant packet;
3. Follow TCP Stream, only for an authorized lab flow where appropriate;
4. any clearly observable plaintext credential material or anomalous protocol behavior.

**Do not upload real passwords, tokens, cookies, API keys, or personal data. Redact sensitive values in screenshots.**

## 7. Interpretation rules

An open port is an observation, not automatically a vulnerability.

For each finding, distinguish:

- **Observed:** directly supported by Nmap/Wireshark evidence.
- **Potential risk:** security implication that follows from the observation.
- **Validation needed:** additional checks required before calling something a confirmed vulnerability.

## 8. Suggested evidence filenames

- `nmap-tcp-syn.nmap`
- `nmap-tcp-syn.xml`
- `nmap-udp-top100.nmap`
- `nmap-service-version.nmap`
- `nmap-os.nmap`
- `wireshark-overview.png`
- `wireshark-protocol-detail.png`
- `wireshark-plaintext-example-redacted.png`

