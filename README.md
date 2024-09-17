# 2024 Fall Miniproject

Exercise01:

Exercise02:
# Mario Theme Player using PWM on Raspberry Pi Pico

## 1. Project Overview
This project uses the Raspberry Pi Pico WH to play the Mario theme song using a Pulse Width Modulation (PWM) signal on a connected speaker. The sound output is created by varying the frequency of the PWM signal, and a series of notes is defined in a list representing the Mario theme song.

## 2. System Architecture
- **Hardware**: 
  - Raspberry Pi Pico WH.
  - Speaker connected to GPIO Pin 16 (`SPEAKER_PIN`).
  
- **Software Components**:
  - **PWM Module**: The PWM object is initialized on the `SPEAKER_PIN`. The duty cycle and frequency are adjusted to play different musical notes.
  - **Tone Playback**: A function `playtone(frequency, duration)` is used to play individual tones for specified durations. The `mario_theme` list holds tuples representing musical notes and their durations.

### Hardware Wiring
- **Speaker**: Connected to GP16 (Pin 21 on Raspberry Pi Pico).
  - One wire from the speaker goes to GP16.
  - Another wire is connected to the ground (GND) pin of the Pico.

## 3. Design Patterns
- **Modular Design**: The project is broken down into discrete functions:
  - `playtone()`: Plays a single note.
  - `quiet()`: Stops the sound by setting the duty cycle of the PWM to zero.
  
- **Loop and Control**: The `for` loop iterates over the `mario_theme` list, checking if the note is a pause (`note == 0`), and then either plays the tone or invokes a pause.

## 4. Key Design Decisions
- **PWM for Sound**: Using Pulse Width Modulation (PWM) to produce sound allows for control over both frequency and volume of the output signal.
- **Frequency Calculation**: The notes are defined by their frequency in hertz. For example, `2637.02 Hz` corresponds to the musical note E7.
- **Pauses Between Notes**: A `utime.sleep()` call is used to insert pauses between notes, creating a natural flow to the melody.

## 5. Code Explanation

### PWM Setup
We first set up a PWM object on the speaker pin (`SPEAKER_PIN`).

```python
import machine

SPEAKER_PIN = 16
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

Functions are explained in the code comments

## 6. Future Improvements
Add more songs or allow users to input their own.
Implement a feature that adjusts volume dynamically.
Allow control over the speed of the song.

## 7. Usage
To run this project, upload the Python script to your Raspberry Pi Pico WH using Thonny IDE and ensure your speaker is properly connected to the designated pin (GP16).

Exercise03:
## 1. Project Overview
This project is designed to measure human response times to random LED flashes using a button connected to the Raspberry Pi Pico. The system captures the response time, calculates statistics (minimum, maximum, and average response time), and uploads the data to a Firebase Real-Time Database. It also logs the results locally in JSON format.

## 2. System Architecture
Hardware Components
Raspberry Pi Pico WH: The main controller used to run the program and handle button inputs.
LED: Used to signal when the user should press the button.
Button: Connected to GPIO Pin 16 to record user input.
WiFi: Used to upload the collected data to Firebase.
Software Components
MicroPython: The programming language used to run the code on the Raspberry Pi Pico.
Firebase Real-Time Database: Used to store the response time data.
JSON Storage: The data is also stored locally in JSON format for future reference.

##3. Design Patterns and Key Decisions
WiFi Connection
The Pico connects to the WiFi network (BU Guest (unencrypted)) using the network.WLAN() module. Once connected, it uploads the response time statistics to Firebase.
Randomized LED Flashing
The time intervals between LED flashes are randomized using the random.uniform() function, which generates a random delay between 0.5 and 5 seconds. This adds unpredictability to the system and makes the test more challenging.
Response Time Calculation
The program measures how quickly the user presses the button after the LED turns on. If the user presses the button within the on_ms window (500 ms), the time difference is stored. If the user fails to press the button, the system records a "miss" (None value).
Data Handling
Firebase: After the game is finished, the response time data (min, max, avg) is uploaded to Firebase.
JSON File: A local JSON file stores the results with a timestamp-based filename.
Edge Cases
If the user does not press the button before the LED turns off, it is counted as a miss, and this is handled by filtering None values in the list of response times.

## 4. Snippets of code are explained in the comments

## 5.Testing Process
Connect to WiFi: Ensure that the Raspberry Pi Pico is connected to the WiFi network before starting the game. Once connected, a confirmation message with the IP address will be printed.
Start the Game: The LED blinks three times to indicate the start of the game. The LED will then flash randomly, and the user must press the button as quickly as possible.
Game Behavior: The game consists of 10 random LED flashes, and the user must press the button before the LED turns off (500 ms). If the button is pressed too late or not at all, a miss is recorded.
End of the Game: The LED blinks five times to indicate the end of the game.
Results: After the game, the minimum, maximum, and average response times are printed. The results are stored in a local JSON file and uploaded to Firebase.

Expected Output
The user should see the connection to WiFi printed first.
The LED will flash randomly, and the user’s response times will be captured.
At the end of the game, statistics will be displayed, and data will be uploaded to Firebase.
A JSON file with the results will be saved locally.

Testing the Edge Cases
Missed Flashes: If the user misses the flash (fails to press the button in time), the system should handle the None values and still compute the statistics based on valid responses.
WiFi Failure: If there is a failure to connect to WiFi or upload data, an error message should be printed without crashing the system.
