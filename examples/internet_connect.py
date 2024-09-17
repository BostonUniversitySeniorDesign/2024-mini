"""
example of connecting to WiFi with the Pi Pico and getting the TLS version
"""

import json
import asyncio

import network
import urequests


# url = "https://www.whatsmyua.info/api/v1/ua"
url = "https://www.howsmyssl.com/a/check"
DNS = "8.8.8.8"

ssid = ""
# Fill in the SSID of your WiFi Hotspot or network

passw = ""
# other people can see this if you push it to Git!


def get_tls(jt: str) -> str:
    params = json.loads(jt)
    return params["tls_version"]


async def main():
    print(f"Connecting to WiFi {ssid}")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, passw)
    while not sta_if.isconnected():
        print(f"Still trying to connect to {ssid}")
        await asyncio.sleep_ms(1000)

    print(f"Setting DNS {DNS}")
    cfg = list(sta_if.ifconfig())
    cfg[-1] = DNS
    sta_if.ifconfig(cfg)

    print(f"Getting {url}")
    r = urequests.get(url)
    tls_version = get_tls(r.text)
    r.close()

    print(f"TLS version: {tls_version}")


asyncio.run(main())
