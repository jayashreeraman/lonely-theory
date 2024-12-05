

import string
import random

url_map = {}

def generate_short_url(long_url, length=6):
    characters = string.ascii_letters + string.digits
    short_code = "".join(random.choice(characters) for _ in range(length))

    short_url = "https://short.url/" + short_code

    if short_code not in url_map:
        url_map[short_code] = long_url

    return short_url

def return_long_url(short_code):
    return url_map[short_code]


# Example usage:
long_url = "https://www.example.com/very/long/path/to/resource"
short_url = generate_short_url(long_url)
print(short_url)

retrieved_long_url = return_long_url(short_url.split('/')[-1])
print(retrieved_long_url)