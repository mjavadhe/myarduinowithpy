# myarduinowithpy

**Bridging Worlds: Introducing `myarduinowithpy` for Arduino-Python Integration**

The tech landscape is constantly evolving, and with it, our ways of interfacing with hardware and software. Enter `myarduinowithpy`, a cutting-edge package that simplifies the interaction between Arduino boards and Python.

## Overview
`myarduinowithpy` offers a seamless connection, enabling enthusiasts and professionals alike to program their Arduino boards using Python, a language celebrated for its simplicity and versatility.

**This package allows users to program Arduino boards using Python without any dependencies. All operations are done through simple commands.**

## Key Features
- **Ease of Use**: Simplifies the process of setting up and controlling Arduino pins.
- **Versatility**: Supports a wide range of Arduino functions, making it suitable for various projects.
- **Community Support**: Join a growing community of users who share tips, projects, and insights.

## Getting Started
To begin, install the package via pip and start experimenting with your Arduino boards in no time. Detailed documentation and examples are available on [GitHub](https://github.com/mjavadhe/myarduinowithpy).

## Installation
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

