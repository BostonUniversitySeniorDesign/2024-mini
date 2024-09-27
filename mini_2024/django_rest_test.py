import requests
import struct
import time
import random


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


now = time.localtime()
now_str = "-".join(map(str, now[:3])) + "T" + ":".join(map(str, now[3:6]))

score_list = [random.random(), random.random()]
data_dict = {
    "id": generate_uuid4(),
    "user": [2],
    "timestamp": now_str,
    "max_time_s": max(score_list),
    "min_time_s": min(score_list),
    "average_time_s": sum(score_list) / len(score_list),
    "score": 3,
}

print(data_dict)
database_api_url = "https://halara.cloud/pico/pico-data/"
response = requests.post(database_api_url, json=data_dict)
print(response.text)
