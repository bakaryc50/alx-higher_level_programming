#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib.parse import urlencode
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ", __file__, "URL", "email", file=sys.stderr)
        sys.exit(1)

    data = urlencode({"email": sys.argv[2]}).encode()
    with urlopen(sys.argv[1], data=data) as resp:
        print(resp.read().decode())
