from microbit import *
import utime

# Define custom mapping of Unicode characters to voltage levels
CHAR_VMAP = {
    'A': 0.2,
    'B': 0.4,
    'C': 0.6,
    'D': 0.8,
    'E': 1.0,
    'F': 1.2,
    'G': 1.4,
    'H': 1.6,
    'I': 1.8,
    'J': 2.0,
    'K': 2.2,
    'L': 2.4,
    'M': 2.6,
    'N': 2.8,
    'O': 3.0,
    'P': 3.2,
    'Q': 3.4,
    'R': 3.6,
    'S': 3.8,
    'T': 4.0,
    'U': 4.2,
    'V': 4.4,
    'W': 4.6,
    'X': 4.8,
    'Y': 5.0,
    'Z': 5.2,
    'a': 0.1,
    'b': 0.3,
    'c': 0.5,
    'd': 0.7,
    'e': 0.9,
    'f': 1.1,
    'g': 1.3,
    'h': 1.5,
    'i': 1.7,
    'j': 1.9,
    'k': 2.1,
    'l': 2.3,
    'm': 2.5,
    'n': 2.7,
    'o': 2.9,
    'p': 3.1,
    'q': 3.3,
    'r': 3.5,
    's': 3.7,
    't': 3.9,
    'u': 4.1,
    'v': 4.3,
    'w': 4.5,
    'x': 4.7,
    'y': 4.9,
    'z': 5.1,
    ' ': 0.0,
    '.': 5.4,
    ',': 5.6,
    '!': 5.8,
    '-': 0.05,
    '#': 5.3,
}

# Set up analog output pin
pin0.set_analog_period(20)

# Function to transmit a single character as an analog signal
def send_char(char):
    if char in CHAR_VMAP:
        voltage = CHAR_VMAP[char]
        pin0.write_analog(int(voltage/3.3*1023))
    else:
        # If character is not in mapping, send a space
        pin0.write_analog(0)
        raise IndexError('Char Not Found in Char_VMAP')
    utime.sleep_ms(50)

# Function to transmit a string of characters as analog signals
def send_string(string):
    for char in string:
        send_char(char)
