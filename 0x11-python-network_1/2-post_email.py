#!/usr/bin/python3
"""This script that takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and displays the body of
    the response.
"""
from urllib.request import Request, urlopen
import urllib.parse
from sys import argv


def do_post(url, values):
    """Sends a POST request to the passed URL and values.

    Args:
        url (str): server url.
        values (dict): values to post.
    """
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    return Request(url, data)


if __name__ == "__main__":
    req = do_post(argv[1], {"email": argv[2]})
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
