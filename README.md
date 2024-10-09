<<<<<<< HEAD
# myarduinowithpy

This package allows users to program Arduino boards using Python without any dependencies. All operations are done through simple commands.

## Installation

Just copy the `myarduinowithpy` directory into your project.
---
`pip install myarduinowithpy`

## Usage

```python
from myarduinowithpy.core import Arduino

# Set the serial port to your Arduino
port = '/dev/ttyUSB0'  # Change to your Arduino port
board = Arduino(port)

# Set pin mode for LED
board.pin_mode(13, 'OUTPUT')

# Blink LED
try:
    while True:
        board.digital_write(13, 1)  # Turn on LED
        time.sleep(1)                # Wait 1 second
        board.digital_write(13, 0)  # Turn off LED
        time.sleep(1)                # Wait 1 second
except KeyboardInterrupt:
    print("Program terminated.")

