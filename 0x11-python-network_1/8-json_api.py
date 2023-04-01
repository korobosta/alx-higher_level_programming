#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        value = argv[1]
    else:
        value = ""

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": value})

    try:
        di = r.json()
        if len(di) == 0:
            print("No result")
        else:
            print("[{}] {}".format(di.get("id"), di.get("name")))
    except Exception:
        print("Not a valid JSON")
