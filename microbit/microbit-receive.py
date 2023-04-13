from microbit import *
import time

adc = pin0  # use pin0 to read analog signals
buffer = []
last_transmission_time = 0
BUFFER_DELAY = 50  # delay between each transmission in milliseconds

def receive_analog_signal():
    # read the analog signal
    analog_value = adc.read_analog()

    # check if the value is above a certain threshold (e.g. half of the max value)
    if analog_value > 512:
        buffer.append(1)
    else:
        buffer.append(0)

    # check if the buffer contains a complete transmission
    if len(buffer) == 8:
        byte_value = 0
        for i, bit_value in enumerate(buffer):
            byte_value |= bit_value << i
        char_value = chr(byte_value)
        print(char_value, end='')
        buffer.clear()
