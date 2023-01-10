#!/usr/bin/python3
"""This module contains a function that inserts a line of text
    to a file, after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
        specific string.

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        search_string {str} -- [description] (default: {""})
        new_string {str} -- [description] (default: {""})
    """
    str = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if search_string in line:
                str += line[:] + new_string
            else:
                str += line
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str)
