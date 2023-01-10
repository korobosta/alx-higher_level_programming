#!/usr/bin/python3
"""This module contains a function that reads a text file (UTF8)
    and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Keyword Arguments:
        filename {str} -- file name (default: {""})
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
