#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""
import machine  # pylint: disable=import-error
import utime  # pylint: disable=import-error

# MUSIC THEORY
BPM = 120.0


class Note:  # pylint: disable=too-few-public-methods
    """A musical note with a pitch and a length"""

    def __repr__(self) -> str:
        return f"Note: {self.pitch} {self.length}"

    def __init__(self, pitch, length):
        self.pitch = pitch
        self.length = length


# Frequencies for the notes in the A major scale
# C/F/G sharp
SCALE: dict[str, float] = {
    "pause": 0,
    "C#3": 138.59,
    "D3": 146.83,
    "E3": 164.81,
    "F#3": 185,
    "G#3": 207.65,
    "A3": 220,
    "B3": 246.94,
    "C#4": 277.18,
    "D4": 293.66,
    "E4": 329.63,
    "F#4": 369.99,
    "G#4": 415.30,
    "A4": 440,
    "B4": 493.88,
    "C#5": 554.37,
    "D5": 587.33,
    "E5": 659.25,
    "F#5": 739.99,
    "G#5": 830.61,
    "A5": 880,
    "B5": 987.77,
}

LENGTHS: dict[str, float] = {
    "whole": 1.0,
    "half": 0.5,
    "quarter": 0.25,
    "quarter_dotted": 0.375,
    "eighth": 0.125,
    "eighth_dotted": 0.1875,
    "sixteenth": 0.0625,
}

# First few notes of Sweet Caroline
# https://musescore.com/user/34214067/sweet-caroline-2012-neil-diamond-piano-arrangement
SWEET_CAROLINE: list[Note] = [
    Note("G#4", "eighth_dotted"),
    Note("A4", "sixteenth"),
    Note("B4", "half"),
    Note("G#4", "eighth_dotted"),
    Note("A4", "sixteenth"),
    Note("B4", "eighth_dotted"),
    Note("A4", "sixteenth"),
    Note("G#4", "quarter"),
    Note("B4", "eighth_dotted"),
    Note("A4", "sixteenth"),
    Note("G#4", "quarter"),
    Note("D4", "eighth_dotted"),
    Note("E4", "sixteenth"),
    Note("F#4", "half"),
    Note("D4", "eighth_dotted"),
    Note("E4", "sixteenth"),
    Note("F#4", "eighth_dotted"),
    Note("E4", "sixteenth"),
    Note("D4", "quarter"),
    Note("F#4", "eighth_dotted"),
    Note("E4", "sixteenth"),
    Note("F#4", "eighth_dotted"),
    Note("G#4", "sixteenth"),
    Note("A4", "half"),
    Note("F#4", "eighth_dotted"),
    Note("G#4", "sixteenth"),
    Note("A4", "half"),
    Note("G#4", "half"),
    Note("C#5", "half"),
    Note("B4", "half"),
    Note("C#5", "quarter"),
    Note("C#5", "quarter"),
    Note("C#4", "eighth_dotted"),
    Note("D4", "sixteenth"),
    Note("E4", "eighth_dotted"),
    Note("E4", "half"),
]

# GP16 is the speaker pin
SPEAKER_PIN: int = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playnote(note: Note) -> None:  # pylint: disable=redefined-outer-name
    """Play a note for a given duration"""
    duration_s = BPM / 60.0 * LENGTHS[note.length]
    if note.pitch == "pause":
        speaker.duty_u16(0)
    else:
        speaker.duty_u16(1000)
        speaker.freq(int(SCALE[note.pitch]))
    utime.sleep(duration_s)


def quiet() -> None:
    """Turn off the PWM"""
    speaker.duty_u16(0)


for note in SWEET_CAROLINE:
    print(note)
    playnote(note)

# Turn off the PWM
quiet()
