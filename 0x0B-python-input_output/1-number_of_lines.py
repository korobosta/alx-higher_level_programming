#!/usr/bin/python3
"""This module contains a function that returns the number
     of lines of a text file.
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file.

    Keyword Arguments:
        filename {str} -- file name (default: {""})

    Returns:
        Int -- number of lines of a text file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return len(file.readlines())
