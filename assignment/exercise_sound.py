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
    speaker.freq(int(frequency))
    utime.sleep(duration)

def quiet(duration: float):
    speaker.duty_u16(0)
    utime.sleep(duration)

# Note frequencies from https://muted.io/note-frequencies/
E = 164.81
G = 196
D = 146.83
C = 130.81
B = 123.47
 
# Seven Nation Army by The White Stripes https://musescore.com/user/13141226/scores/7605833
bpm = 124
beat_dur: float = 60/bpm

# First part
while True:
    playtone(E, beat_dur)
    quiet(beat_dur)
    playtone(E, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(G, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(E, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(D, 0.5*beat_dur)
    quiet(.1*beat_dur)

    playtone(C, 2*beat_dur)
    quiet(.1*beat_dur)
    playtone(B, 2*beat_dur)
    quiet(.1*beat_dur)

    # Second part
    playtone(E, beat_dur)
    quiet(beat_dur)
    playtone(E, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(G, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(E, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(D, 0.5*beat_dur)
    quiet(.1*beat_dur)

    playtone(C, 1*beat_dur)
    quiet(.1*beat_dur)
    playtone(D, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(C, 0.5*beat_dur)
    quiet(.1*beat_dur)
    playtone(B, 2*beat_dur)