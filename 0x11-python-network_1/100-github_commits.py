#!/usr/bin/python3
"""This script list 10 commits (from the most recent to oldest) of a
    repository.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    for i in r.json()[:10]:
        print("{}: {}".format(
            i.get('sha'), i.get('commit').get('author').get('name')))
