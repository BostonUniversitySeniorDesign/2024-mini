#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


notes = [
    466, 466, 466, 740, 1047, 932, 880, 784, 1397, 1047, 932, 880,
    784, 1397, 1047, 932, 880, 932, 784, 523, 523, 523, 740, 1047,
    932, 880, 784, 1397, 1047, 932, 880, 784, 1397, 1047, 932, 880,
    932, 784, 523, 523, 587, 587, 932
]
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

for i in range(len(notes)):
    freq = notes[i]
    playtone(freq, duration)

# Turn off the PWM
quiet()
