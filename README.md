# PENGUIn

PENGUIn (Pulse Encoding for Non-digital Generation of Unicode INformation) is a Python algorithm that encodes Unicode characters and transmits them as analog signals using a microcontroller board.

## Getting Started

To get started with PENGUIn, you will need the following components:

- 2 Microcontroller boards (e.g., Arduino Uno, Arduino Nano, BBC micro:bit)
*** DISCLAMER ***
** Only supports micro:bit as of this version **
- USB cable for programming the microcontroller
- Jumper wires for connecting the microcontroller to the signal source

## Installation

1. Connect the microcontroller board to your computer using a USB cable.
2. Install the required libraries for your microcontroller board. For example, if you're using an Arduino board, you will need to install the `pyserial` library.
3. Copy the `PENGUIn.py` file to your computer.

## Usage

1. Open the `PENGUIn.py` file in a Python editor.
2. Modify the `CHAR_VMAP` dictionary to include the mapping of characters to their analog signal representation.
3. Connect the microcontroller board to the signal source using jumper wires.
4. Upload the `PENGUIn.py` file to the microcontroller board.
5. Use the `transmit_string()` function in the `PENGUIn` module to transmit a Unicode string as analog signals.

```python
import PENGUIn

PENGUIn.transmit_string("Hello, world!")
```

This will transmit the string "Hello, world!" as analog signals.

## Contributing

Contributions to PENGUIn are welcome! If you find a bug or have a suggestion for improvement, please submit an issue or a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

