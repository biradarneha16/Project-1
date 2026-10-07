import unittest
from unittest.mock import patch

from port_scanner import parse_ports, scan_host, scan_port


class FakeSocket:
    def __init__(self, code=0, timeout=False):
        self.code = code
        self.timeout = timeout
        self.closed = False

    def settimeout(self, _timeout):
        pass

    def connect_ex(self, _address):
        if self.timeout:
            raise TimeoutError("timed out")
        return self.code

    def close(self):
        self.closed = True


class PortScannerTests(unittest.TestCase):
    def test_parse_single_port(self):
        self.assertEqual(parse_ports("443"), [443])

    def test_parse_range(self):
        self.assertEqual(parse_ports("80-82"), [80, 81, 82])

    def test_parse_invalid_port(self):
        with self.assertRaises(Exception):
            parse_ports("0")

    @patch("port_scanner.socket.socket", return_value=FakeSocket(0))
    @patch("port_scanner.socket.getservbyport", return_value="http")
    def test_open_port(self, _service, _socket):
        result = scan_port("127.0.0.1", 80, 0.1)
        self.assertEqual(result.status, "OPEN")
        self.assertEqual(result.service, "http")

    @patch("port_scanner.socket.socket", return_value=FakeSocket(111))
    def test_closed_port(self, _socket):
        result = scan_port("127.0.0.1", 65000, 0.1)
        self.assertEqual(result.status, "CLOSED")

    def test_scan_host_is_sorted(self):
        def fake_scan(_host, port, _timeout):
            from port_scanner import ScanResult
            return ScanResult(port, "OPEN")

        with patch("port_scanner.scan_port", side_effect=fake_scan):
            results = scan_host("127.0.0.1", [3, 1, 2], 0.1, 2)
        self.assertEqual([r.port for r in results], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
