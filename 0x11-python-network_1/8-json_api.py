#!/usr/bin/python3
""" Script takes a letter and send a POST request
to http://0.0.0.0:5000/search_user
"""
import requests
import sys


URL = "http://0.0.0.0:5000/search_user"

if __name__ == "__main__":
    data = {}
    if len(sys.argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}
    resp = requests.post(URL, data=data)
    try:
        json = resp.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
