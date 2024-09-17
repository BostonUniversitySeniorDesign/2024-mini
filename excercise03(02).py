from machine import Pin
import time
import random
import urequests as requests  
import json
import network


SSID = "BU Guest (unencrypted)"

# constants
N = 10  # number of flashes per game
on_ms = 500  # LED on time in milliseconds
FIREBASE_URL = "https://mini-project-cd412-default-rtdb.firebaseio.com/response-times.json"  # Firebase URL

# connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(SSID)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected to:", wlan.ifconfig())

# call the WiFi connection function
connect_wifi()

# function to generate a random time interval between tmin and tmax
def random_time_interval(tmin: float, tmax: float) -> float:
    return random.uniform(tmin, tmax)

# function to blink the LED N times
def blinker(N: int, led: Pin) -> None:
    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)

# function to write results to a JSON file
def write_json(json_filename: str, data: dict) -> None:
    with open(json_filename, "w") as f:
        json.dump(data, f)

# function to compute response time statistics and upload data to Firebase
def scorer(t: list[int | None]) -> None:
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    # this is for the misses 
    t_good = [x for x in t if x is not None]

    # calculate minimum, maximum, and average response times
    if t_good:
        min_time = min(t_good)
        max_time = max(t_good)
        avg_time = sum(t_good) / len(t_good)
    else:
        min_time, max_time, avg_time = None, None, None

    print(f"Min time: {min_time} ms")
    print(f"Max time: {max_time} ms")
    print(f"Average time: {avg_time} ms")

    # stores the data
    data = {
        "min_time_ms": min_time,
        "max_time_ms": max_time,
        "avg_time_ms": avg_time,
        "misses": misses,
        "total_flashes": len(t),
        "non_misses": len(t_good),
    }

    # writes to jason files 
    now = time.localtime()
    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"
    print(f"Writing results to {filename}")
    write_json(filename, data)

    # uploading data to firebase
    try:
        response = requests.post(FIREBASE_URL, json=data)
        print(f"Data uploaded. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to upload data: {e}")

# main program
if __name__ == "__main__":
    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)  # Button connected to GP16

    t = []

    # 3 blinks indicates start game 
    blinker(3, led)

    # measures reponse fro n flashes
    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))  # Random delay before flashing the LED

        led.high()  # LED on
        tic = time.ticks_ms()
        t0 = None

        # checks if button was pressed
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:  # Button pressed
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()  # Turn off LED immediately when button is pressed
                break
        t.append(t0)

        led.low()  # Turn off the LED after the time interval

    # indicates end of game
    blinker(5, led)

    # time statistics
    scorer(t)
