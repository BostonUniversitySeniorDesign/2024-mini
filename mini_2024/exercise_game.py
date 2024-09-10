"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import requests
import struct
import network

N: int = 3
sample_ms = 10.0
on_ms = 1000


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


def generate_uuid4():
    # Generate 16 random bytes
    random_bytes = bytearray(random.getrandbits(8) for _ in range(16))

    # Set the version to 4 (UUID version 4)
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40

    # Set the variant to RFC 4122
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80

    # Convert bytes to a UUID string
    uuid_str = struct.unpack(">IHH8B", random_bytes)
    return f"{uuid_str[0]:08x}-{uuid_str[1]:04x}-{uuid_str[2]:04x}-{uuid_str[3]:02x}{uuid_str[4]:02x}-77{uuid_str[5]:02x}{uuid_str[6]:02x}{uuid_str[7]:02x}{uuid_str[8]:02x}{uuid_str[9]:02x}"


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    now = time.localtime()
    now_str = "-".join(map(str, now[:3])) + "T" + ":".join(map(str, now[3:6]))

    data_dict = {
        "id": generate_uuid4(),
        "user": [1],
        "timestamp": now_str,
        "max_time_s": max(t_good) / 1000.0,
        "min_time_s": min(t_good) / 1000.0,
        "average_time_s": float(sum(t_good)) / 1000 / len(t_good),
        "score": (float(N) - misses) / N,
    }

    # %% make dynamic filename and write JSON
    filename = f"score-{now_str}.json"

    print("write", filename)
    print(data_dict)

    # Write data to database with REST API
    database_api_url = "https://halara.cloud/pico/pico-data/"
    response = requests.post(database_api_url, json=data_dict)
    print(response)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    # Connect to Wi-Fi
    ssid = "EndlessSummer"
    password = "Nikiti77"

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    # Wait for connection
    while not station.isconnected():
        time.sleep(1)

    print("Connected to Wi-Fi")

    led = Pin("LED", Pin.OUT)
    button = Pin(15, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()  # type: ignore
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:  # type: ignore
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)  # type: ignore
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)
