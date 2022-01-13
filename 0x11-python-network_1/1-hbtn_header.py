#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the response
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(2)

    with urlopen(sys.argv[1]) as resp:
        print(resp.getheader("X-Request-Id"))
