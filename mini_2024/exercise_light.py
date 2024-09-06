#!/usr/bin/env python3
"""
Use analog input with photocell
"""

import time
import machine  # pylint: disable=import-error

# GP28 is ADC2
ADC2 = 28

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(ADC2)

BLINK_PERIOD = 0.01

MAX_BRIGHT = 44000  # hand covering the photocell
MIN_BRIGHT = 3300  # iPhone flashlight


def clip(value: float) -> float:
    """clip number to range [0, 1]"""
    if value < 0:
        return 0
    if value > 1:
        return 1
    return value


while True:
    reading = adc.read_u16()
    print(reading)
    # need to clip duty cycle to range [0, 1]
    # this equation will give values outside the range [0, 1]
    # So we use function clip()

    duty_cycle = clip((reading - MIN_BRIGHT) / (MAX_BRIGHT - MIN_BRIGHT))

    led.high()
    time.sleep(BLINK_PERIOD * duty_cycle)

    led.low()
    time.sleep(BLINK_PERIOD * (1 - duty_cycle))
