"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import requests
import network

N: int = 10
sample_ms = 10.0
on_ms = 500

def connect_to_wifi(ssid):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid)
    
    if wlan.isconnected():
        print("Connected to WiFi")
    else:
        print("Failed to connect to WiFi")
        
ssid = 'BU Guest (unencrypted)'
connect_to_wifi(ssid)

database_api_url = "https://mini-c686c-default-rtdb.firebaseio.com/"

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    if t_good:
        min_time = min(t_good)
        max_time = max(t_good)
        avg_time = sum(t_good) / len(t_good)
        score = (len(t) - misses) / len(t)
    else:
        min_time = max_time = avg_time = score = 0
    data = {
        "min_time": min_time,
        "max_time": max_time,
        "average_time": avg_time,
        "score": score
        }

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)
    
    return data

def upload_to_firebase(user_number: str, data: dict) -> None:
    firebase_api_url = f"{database_api_url}/{user_number}.json"
    response = requests.put(firebase_api_url, json=data)
    if response.status_code == 200:
        print(f"Data successfully uploaded to Firebase")
    else:
        print(f"Failed to upload data. Status code: {response.status_code}, Response: {response.text}")


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

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

    blinker(5, led)

    data = scorer(t)
    current_time = time.localtime()
    user_number = "user_" + "_".join(map(str, current_time[:6]))
    upload_to_firebase(user_number, data)
