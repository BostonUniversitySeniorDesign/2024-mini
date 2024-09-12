"""
Response time - single-threaded
"""
from machine import Pin
import time
import random
import json
import urequests  # For making HTTP requests to the Firebase

N = 10  # Set number of flashes to 10
sample_ms = 10.0
on_ms = 500

# Firebase configuration
firebase_url = "https://miniprojectec463-default-rtdb.firebaseio.com/scores.json"  # Firebase Realtime Database URL
firebase_api_key = "AIzaSyCNoL0F0a8lNjoSqAkw1A7UWRQRJoUJWUK"  # Firebase API key

def send_to_firebase(data: dict) -> None:
    """Sends data to Firebase using HTTP POST."""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {firebase_api_key}'  # API key for authentication
    }
    response = urequests.post(firebase_url, headers=headers, data=json.dumps(data))
    print("Firebase response:", response.text)
    response.close()




def random_time_interval(tmin: float, tmax: float) -> float:
    """Return a random time interval between max and min."""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    """Let user know the game started/is over by blinking the LED."""
    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)

def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file."""
    with open(json_filename, "w") as f:
        json.dump(data, f)

def send_to_firebase(data: dict) -> None:
    """Sends data to Firebase using HTTP POST."""
    headers = {'Content-Type': 'application/json'}
    response = urequests.post(firebase_url, headers=headers, data=json.dumps(data))
    print("Firebase response:", response.text)
    response.close()

def scorer(t: list[int | None]) -> None:
    """Collates and computes statistics and sends data to Firebase."""
    # Calculate statistics
    misses = t.count(None)
    t_good = [x for x in t if x is not None]
    
    if t_good:
        min_time = min(t_good)
        max_time = max(t_good)
        avg_time = sum(t_good) / len(t_good)
    else:
        min_time = max_time = avg_time = None

    # Prepare thedata dictionary
    data = {
        "misses": misses,
        "total_flashes": len(t),
        "min_time": min_time,
        "max_time": max_time,
        "avg_time": avg_time,
        "score": (len(t) - misses) / len(t),  # Score as a floating-point number between 0 and 1
        "timestamp": time.localtime()  # Add timestamp
    }

    # Make dynamic filename and write JSON locally (optional)
    now = time.localtime()
    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"
    write_json(filename, data)

    # Send data to Firebase
    send_to_firebase(data)

if __name__ == "__main__":
    # Using "if __name__" allows us to reuse functions in other script files.
    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    # Indicate game start
    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    # Indicate game over
    blinker(5, led)

    # Process results and send to Firebase
    scorer(t)
