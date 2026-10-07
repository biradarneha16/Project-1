#!/usr/bin/env python3
"""Concurrent TCP port scanner for authorized security testing."""

from __future__ import annotations

import argparse
import logging
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ScanResult:
    port: int
    status: str
    service: str = "unknown"
    error: str = ""


def parse_ports(value: str) -> list[int]:
    """Parse a single port or inclusive range such as 22 or 1-1024."""
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("port specification cannot be empty")

    try:
        if "-" in value:
            start_text, end_text = value.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start > end:
                raise ValueError
            ports = range(start, end + 1)
        else:
            ports = [int(value)]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("use PORT or START-END") from exc

    ports = list(ports)
    if any(port < 1 or port > 65535 for port in ports):
        raise argparse.ArgumentTypeError("ports must be between 1 and 65535")
    return ports


def scan_port(host: str, port: int, timeout: float) -> ScanResult:
    """Attempt a TCP connection and classify the outcome."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        code = sock.connect_ex((host, port))
        if code == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "unknown"
            return ScanResult(port, "OPEN", service)
        return ScanResult(port, "CLOSED", error=f"socket error {code}")
    except socket.timeout:
        return ScanResult(port, "TIMEOUT", error="connection timed out")
    except OSError as exc:
        return ScanResult(port, "CLOSED", error=str(exc))
    finally:
        sock.close()


def scan_host(host: str, ports: Iterable[int], timeout: float, workers: int) -> list[ScanResult]:
    """Scan ports concurrently and return results in port order."""
    ports = list(ports)
    results: list[ScanResult] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(scan_port, host, port, timeout): port for port in ports}
        for future in as_completed(futures):
            results.append(future.result())
    return sorted(results, key=lambda result: result.port)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Concurrent TCP port scanner")
    parser.add_argument("host", help="hostname or IP address to scan")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--port", type=parse_ports, help="single TCP port")
    group.add_argument("--ports", type=parse_ports, help="TCP port or range, e.g. 1-1024")
    parser.add_argument("--timeout", type=float, default=1.0, help="socket timeout in seconds (default: 1.0)")
    parser.add_argument("--workers", type=int, default=50, help="maximum concurrent workers (default: 50)")
    parser.add_argument("--log-file", help="write scan results to this log file")
    parser.add_argument("--show-closed", action="store_true", help="print closed ports")
    parser.add_argument("--show-timeouts", action="store_true", help="print timed-out ports")
    return parser


def configure_logging(path: str | None) -> logging.Logger:
    logger = logging.getLogger("port_scanner")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s | %(message)s")
    if path:
        handler = logging.FileHandler(path, encoding="utf-8")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be greater than 0")
    if args.workers <= 0:
        parser.error("--workers must be greater than 0")

    ports = args.port or args.ports
    logger = configure_logging(args.log_file)

    try:
        ip = socket.gethostbyname(args.host)
    except socket.gaierror as exc:
        parser.error(f"cannot resolve host '{args.host}': {exc}")

    print(f"Scanning {args.host} ({ip}) — {len(ports)} TCP port(s)")
    logger.info("START host=%s ip=%s ports=%s", args.host, ip, len(ports))

    results = scan_host(ip, ports, args.timeout, args.workers)
    counts = {"OPEN": 0, "CLOSED": 0, "TIMEOUT": 0}

    for result in results:
        counts[result.status] += 1
        logger.info("port=%d status=%s service=%s error=%s", result.port, result.status, result.service, result.error)
        if result.status == "OPEN" or (result.status == "CLOSED" and args.show_closed) or (result.status == "TIMEOUT" and args.show_timeouts):
            suffix = f" ({result.service})" if result.status == "OPEN" else ""
            print(f"{result.port:5d}/tcp  {result.status:<7}{suffix}")

    summary = f"Summary: {counts['OPEN']} open, {counts['CLOSED']} closed, {counts['TIMEOUT']} timeout(s)"
    print(summary)
    logger.info(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
