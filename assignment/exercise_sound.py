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


freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

# for i in range(64):
#     print(freq)
#     playtone(freq, duration)
#     freq = int(freq * 1.1)

mario_theme_frequencies = [
    659, 659, 659, 523, 659, 784, 392, 523, 392, 330, 440, 494, 466, 440, 392, 659, 784, 880, 698, 784, 659, 523, 587, 494,
    523, 392, 330, 440, 494, 466, 440, 392, 659, 784, 880, 698, 784, 659, 523, 587, 494
]


mario_theme_durations = [
    0.125, 0.125, 0.125, 0.125, 0.125, 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.25,
    0.125, 0.125, 0.125, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.25, 0.125, 
    0.125, 0.125, 0.125, 0.125, 0.25
]



for i, freq in enumerate(mario_theme_frequencies):
    playtone(mario_theme_frequencies[i], mario_theme_durations[i] * 1.25)

# Turn off the PWM
quiet()
