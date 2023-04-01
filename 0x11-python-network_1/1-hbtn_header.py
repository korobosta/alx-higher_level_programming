#!/usr/bin/python3
"""This script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
from urllib.request import Request, urlopen
from sys import argv


def get_headers(header):
    """Displays the value of the specified header variable.

    Args:
        header (str): header variable to print.
    """
    with urlopen(req) as response:
        print(response.headers.get(header))


if __name__ == "__main__":
    req = Request(argv[1])
    get_headers("X-Request-Id")
