# core.py
import serial
import time

class Arduino:
    """Class to manage Arduino connection and operations."""

    def __init__(self, port):
        """Initialize the Arduino connection."""
        self.port = port
        self.baud_rate = 9600  # Default baud rate
        self.serial = serial.Serial(self.port, self.baud_rate, timeout=1)

    def pin_mode(self, pin, mode):
        """Set the mode of a pin (INPUT/OUTPUT)."""
        command = f"pinMode({pin}, {mode})\n"
        self.serial.write(command.encode())

    def digital_write(self, pin, value):
        """Set the digital value of a pin (HIGH/LOW)."""
        command = f"digitalWrite({pin}, {value})\n"
        self.serial.write(command.encode())

    def close(self):
        """Close the serial connection."""
        self.serial.close()
