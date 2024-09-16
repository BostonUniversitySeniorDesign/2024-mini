import machine
import time
import random
import ujson
import network
import socket
import ssl

def load_config():
    try:
        with open('config.json', 'r') as f:
            config = ujson.load(f)
            return config
    except Exception as e:
        print("Error loading configuration:", e)
        return None

config = load_config()
if config is None:
    raise Exception("Configuration file not found or invalid.")
#CREDENTIALS IN CONFIG FILE
SSID = config.get("SSID")
PASSWORD = config.get("PASSWORD")
api_url = config.get("api_url")
device_api_key = config.get("device_api_key")
user_id = config.get("user_id")

#Initialize LED and Button
led = machine.Pin("LED", machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

N = 10  # Number of flashes

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(SSID, PASSWORD)
        timeout = 10  # seconds
        start_time = time.time()
        while not wlan.isconnected():
            if time.time() - start_time > timeout:
                print('Could not connect to Wi-Fi')
                return False
            time.sleep(1)
    print('Connected to Wi-Fi')
    print('Network config:', wlan.ifconfig())
    return True

def random_time_interval(tmin: float, tmax: float) -> float:
    return random.uniform(tmin, tmax)

def blinker(N: int, led: machine.Pin) -> None:
    for _ in range(N):
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)

def scorer(t: list[int | None]) -> dict:
    misses = t.count(None)
    t_good = [x for x in t if x is not None]
    if t_good:
        min_time = min(t_good)
        max_time = max(t_good)
        avg_time = sum(t_good) / len(t_good)
    else:
        min_time = max_time = avg_time = None

    data = {
        "user_id": user_id,
        "misses": misses,
        "total_flashes": len(t),
        "min_time": min_time,
        "max_time": max_time,
        "avg_time": avg_time,
        "score": (len(t) - misses) / len(t),
        "timestamp": time.time(),
        "response_times": t_good 
    }
    return data


def send_https_request(url, headers, data):
    try:
        print("Preparing to send data...")
        print("URL:", url)
        print("Headers:", headers)
        print("Data:", data)
        
        _, _, host, path = url.split('/', 3)
        print("Host:", host)
        print("Path:", path)
        addr_info = socket.getaddrinfo(host, 443)
        addr = addr_info[0][-1]
        s = socket.socket()
        s.connect(addr)
        s = ssl.wrap_socket(s, server_hostname=host)
        request = "POST /{} HTTP/1.1\r\nHost: {}\r\n".format(path, host)
        for k, v in headers.items():
            request += "{}: {}\r\n".format(k, v)
        request += "Content-Length: {}\r\n\r\n".format(len(data))
        request += data
        print("Request:\n", request)
        s.write(request.encode())
        response = s.read(1024)
        s.close()
        return response
    except Exception as e:
        print("Error sending data:", e)
        return None


if __name__ == "__main__":
    if not connect_wifi():
        raise Exception("Failed to connect to Wi-Fi")

    t: list[int | None] = []

    # Indicate game start
    blinker(3, led)

    for _ in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.on()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < 500:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.off()
                break
        t.append(t0)

        led.off()

    # Indicate game over
    blinker(5, led)

    # Process results and send to API
    data = scorer(t)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(device_api_key)
    }
    data_json = ujson.dumps(data)
    response = send_https_request(api_url, headers, data_json)
    if response:
        print("API response:", response.decode())
    else:
        print("Failed to receive a response.")

