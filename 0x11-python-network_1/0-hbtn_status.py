#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """


from urllib.request import urlopen


URL = "https://intranet.hbtn.io/status"

if __name__ == "__main__":
    with urlopen(URL) as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode())
