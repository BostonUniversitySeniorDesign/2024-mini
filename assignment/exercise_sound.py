#!/usr/bin/env python3
"""
PWM Tone Generator - Plays a simple song

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# Create a Pulse Width Modulation (PWM) object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

NOTES = {
    'C4': 261,
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

# Song: (Twinkle, Twinkle, Little Star)
melody = [
    ('C4', 0.5), ('C4', 0.5), ('G4', 0.5), ('G4', 0.5),
    ('A4', 0.5), ('A4', 0.5), ('G4', 1.0),
    ('F4', 0.5), ('F4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('D4', 0.5), ('D4', 0.5), ('C4', 1.0)
]

def playtone(frequency: float, duration: float) -> None:
    """Play a tone at a specified frequency and duration"""
    speaker.duty_u16(1000)  # Set volume (duty cycle)
    speaker.freq(frequency)  # Set frequency of the tone
    utime.sleep(duration)  # Play for the specified duration

def quiet():
    """Silence the speaker"""
    speaker.duty_u16(0)  # Set volume to 0

def play_song(melody: list[tuple[str, float]]) -> None:
    """Play a sequence of notes from a song"""
    for note, duration in melody:
        frequency = NOTES.get(note, 0)  # Get frequency of the note
        if frequency:
            print(f"Playing note: {note} (Frequency: {frequency} Hz)")
            playtone(frequency, duration)
        quiet()  # Silence between notes
        utime.sleep(0.1)  # Short pause between notes

if __name__ == "__main__":
    # Play the song
    play_song(melody)
    
    # Turn off the PWM to stop sound
    quiet()
