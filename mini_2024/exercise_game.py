"""
Response time - single-threaded
"""

import time
import random
import json
import struct
import requests
import network  # pylint: disable=import-error
from machine import Pin  # pylint: disable=import-error

N: int = 3
SAMPLE_MS = 10.0
ON_MS = 1000
LED = Pin("LED", Pin.OUT)
BUTTON = Pin(15, Pin.IN, Pin.PULL_UP)
SSID = "EndlessSummer"
PASSWORD = "Nikiti77"


def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(led: Pin, samples: int = N) -> None:
    """Blink the LED N times to indicate the start or end of the game."""
    for _ in range(samples):
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

    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def generate_uuid4():
    """Generate a random UUID version 4."""

    # Generate 16 random bytes
    random_bytes = bytearray(random.getrandbits(8) for _ in range(16))

    # Set the version to 4 (UUID version 4)
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40

    # Set the variant to RFC 4122
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80

    # Convert bytes to a UUID string
    uuid_str = struct.unpack(">IHH8B", random_bytes)
    return f"""{uuid_str[0]:08x}-{uuid_str[1]:04x}-{uuid_str[2]:04x}-{uuid_str[3]:02x}
    {uuid_str[4]:02x} -77{uuid_str[5]:02x}{uuid_str[6]:02x}{uuid_str[7]:02x}
    {uuid_str[8]:02x}{uuid_str[9]:02x}"""


def scorer(t: list[int | None]) -> None:
    """Scorer function to calculate the score of the game."""
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
        "user": ["rlagoy@gmail.com"],
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
    response = requests.post(
        database_api_url, json=data_dict
    )  # pylint: disable=missing-timeout
    print(response)


def main():
    """Main function to run the game"""
    # Connect to Wi-Fi

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(SSID, PASSWORD)

    # Wait for connection
    while not station.isconnected():
        time.sleep(1)

    print("Connected to Wi-Fi")

    t: list[int | None] = []

    blinker(LED, 3)

    for _ in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        LED.high()

        tic = time.ticks_ms()  # type: ignore, pylint: disable=no-member
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < ON_MS:  # type: ignore, pylint: disable=no-member
            if BUTTON.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)  # type: ignore, pylint: disable=no-member
                LED.low()
                break
        t.append(t0)

        LED.low()

    blinker(LED, 5)

    scorer(t)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files
    main()
