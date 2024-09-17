import machine
import utime

SPEAKER_PIN = 16

# we create a PWM object on the speaker pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

# this defines a function to plate the tone
def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)  # Set duty cycle for volume
    speaker.freq(int(frequency))  # Set the frequency
    utime.sleep(duration)    # Play the tone for the duration

# function is used rto turn off the LED 
def quiet():
    speaker.duty_u16(0)

# using the mario theme we define the notes
mario_theme = [
    (2637.02, 0.15),  # E7
    (2637.02, 0.15),  # E7
    (0, 0.15),        # Pause
    (2637.02, 0.15),  # E7
    (0, 0.1),         # Pause
    (2093.00, 0.15),  # C7
    (2637.02, 0.15),  # E7
    (0, 0.1),         # Pause
    (1567.98, 0.15),  # G6
    (0, 0.35),        # Pause
    (1318.51, 0.15),  # E6
    (0, 0.35),        # Pause
    (1760.00, 0.15),  # A6
    (1975.53, 0.15),  # B6
    (1864.66, 0.15),  # A#6
    (1661.22, 0.15),  # G#6
    (1760.00, 0.15),  # A6
    (0, 0.15),        # Pause
    (1567.98, 0.1),   # G6
    (1318.51, 0.1),   # E6
    (0, 0.35),        # Pause
    (2093.00, 0.15),  # C7
    (1760.00, 0.15),  # A6
    (1567.98, 0.15),  # G6
]

# we then create the sequence for the notes to play
for note, duration in mario_theme:
    if note == 0:  # this is to create a pause 
        quiet()
    else:
        playtone(note, duration)
    utime.sleep(0.05)  # used to create a short pasue between notes

# PWM is then turned off
quiet()
