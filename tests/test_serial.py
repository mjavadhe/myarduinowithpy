# tests/test_serial.py

import unittest
from myarduinowithpy.utils import list_serial_ports

class TestSerialPorts(unittest.TestCase):
    def test_list_serial_ports(self):
        """Test if the serial ports are listed correctly."""
        ports = list_serial_ports()
        self.assertIsInstance(ports, list, "The result should be a list.")
        # You may want to check for expected ports depending on your setup.
        # For example:
        # self.assertIn('/dev/ttyUSB0', ports) or self.assertIn('COM3', ports)

if __name__ == '__main__':
    unittest.main()
