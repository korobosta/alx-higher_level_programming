#!/usr/bin/python3
"""This module contains a function that appends a string
    at the end of a text file (UTF8) and returns the number of
    characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
        and returns the number of characters added:

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        text {str} -- text (default: {""})

    Returns:
        Int -- number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
