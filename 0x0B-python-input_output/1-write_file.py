#!/usr/bin/python3
"""This module contains a function that writes a string to a text
    file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
        the number of characters written.

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        text {str} -- text (default: {""})

    Returns:
        Int -- number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
