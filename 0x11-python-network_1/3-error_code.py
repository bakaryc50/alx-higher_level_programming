#!/usr/bin/python3
""" Script that sends a request to the URL and displays the body
"""
from urllib.error import HTTPError
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as resp:
            print(resp.read().decode())
    except HTTPError as e:
            print("Error code:", e.code)
            sys.exit(1)
