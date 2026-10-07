# Syntecxhub Cyber Security Internship — Project 1

## TCP Port Scanner

This project implements a TCP port scanner using Python sockets and threads. It is based on the internship brief, which asks for a scanner that checks open ports on a host, supports a single host or port range, prints/logs results, and handles exceptions.

> **Authorization:** Run this tool only against systems you own or have explicit permission to test. The default examples use `127.0.0.1`.

## Features

- Scan one host and a single port or port range.
- Concurrent scanning with `ThreadPoolExecutor`.
- Classifies ports as `OPEN`, `CLOSED`, or `TIMEOUT`.
- Handles DNS errors, invalid input, connection errors, and unexpected socket errors.
- Console output plus optional log file.
- Optional `--show-closed` and `--show-timeouts` flags.
- Deterministic unit tests using mocked sockets; tests never contact external hosts.

## Requirements

- Python 3.9+
- Standard library only

## Usage

```bash
python port_scanner.py 127.0.0.1 --port 80
python port_scanner.py 127.0.0.1 --ports 1-1024 --workers 50
python port_scanner.py localhost --ports 20-100 --timeout 0.5 --log-file scan.log
python port_scanner.py 127.0.0.1 --ports 1-100 --show-closed --show-timeouts
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Exit status

- `0` — scan completed successfully (even if no ports were open).
- `1` — invalid arguments or a scanner-level error.

## Internship alignment

The supplied internship brief describes Project 1 as a TCP port scanner, with socket programming, threads, host/port-range options, printed/logged results, and exception handling. The implementation in this directory covers those requirements.
