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
    if frequency == 0:
        speaker.duty_u16(0)
    else:
        speaker.duty_u16(1000)
        speaker.freq(int(frequency))
    utime.sleep(duration)
    quiet()

def quiet():
    speaker.duty_u16(0)


star_wars_opening = [
    (392, 0.35), (392, 0.35), (392, 0.35), (311.1, 0.25), (466.2, 0.15),
    (392, 0.35), (311.1, 0.25), (466.2, 0.15), (392, 0.7),  
    (587.32, 0.35), (587.32, 0.35), (587.32, 0.35), (622.26, 0.25), 
    (466.2, 0.15), (369.99, 0.35), (311.1, 0.25), (466.2, 0.15), 
    (392, 0.7),
    (784, 0.35), (392, 0.25), (392, 0.15), (784, 0.35), (739.98, 0.25), 
    (698.46, 0.15), (659.26, 0.15), (622.26, 0.15), (659.26, 0.30), 
    (415.3, 0.2), (554.36, 0.35), (523.25, 0.25), (493.88, 0.15), 
    (466.16, 0.15), (440, 0.15), (466.16, 0.15), (311.13, 0.30), 
    (369.99, 0.35), (311.13, 0.25), (392, 0.15), (466.16, 0.35), (392, 0.25),
    (466.16, 0.15), (587.32, 0.7), (784, 0.35), (392, 0.25), (392, 0.15), 
    (784, 0.35), (739.98, 0.25), (698.46, 0.15), (659.26, 0.15), 
    (622.26, 0.15), (659.26, 0.30), (415.3, 0.15), (554.36, 0.35), 
    (523.25, 0.25), (493.88, 0.15), (466.16, 0.15), (440, 0.15), 
    (466.16, 0.30), (311.13, 0.15), (369.99, 0.35), (311.13, 0.25), 
    (466.16, 0.15), (392.00, 0.3), (311.13, 0.25), (466.16, 0.15), (392, 0.7)
]

#Adding short pauses between repeated notes
def play_song_with_pause(song):
    for i, note in enumerate(song):
        freq, duration = note
        playtone(freq, duration)
        
        if i < len(song) - 1 and song[i + 1][0] == freq:
            utime.sleep(0.05)
#Play the Star Wars opening theme
play_song_with_pause(star_wars_opening)

# Turn off the PWM
quiet()
