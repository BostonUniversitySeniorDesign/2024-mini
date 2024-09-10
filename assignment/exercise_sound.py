#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 22

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

# Define note frequencies (in Hz)
A_SHARP4 = int(466.16)  # A#4
G_SHARP4 = int(415.30)  # G#4
F_SHARP4 = int(369.99)  # F#4
E_SHARP4 = int(349.23)  # E#4 (enharmonic to F4)
D_SHARP4 = int(1244.51)  # D#4
C_SHARP4 = int(277.18)  # C#4
B3 = int(493.88)        # B3


tokyo_drift_melody = [
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (B3, 0.3),
    (D_SHARP4, 0.3),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (B3, 0.3),
    (D_SHARP4, 0.3),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (B3, 0.3),
    (D_SHARP4, 0.3),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (B3, 0.3),
    (D_SHARP4, 0.3),
    (A_SHARP4, 0.3), (None, 0.1),
    (A_SHARP4, 0.3), (None, 0.1),
    
]

def playtone(frequency: float, duration: float) -> None:
    if frequency is not None:
        speaker.duty_u16(1000)
        speaker.freq(frequency)
        utime.sleep(duration)
        quiet()                  # Stop sound after each note
    else:
        utime.sleep(duration)
    
def quiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.1  # seconds

print("Playing Tokyo Drift Melody:")

for note, duration in tokyo_drift_melody:
    playtone(note, duration)

# Turn off the PWM
quiet()
