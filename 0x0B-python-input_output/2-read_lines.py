#!/usr/bin/python3
"""This module contains a function that reads n lines
    of a text file (UTF8) and prints it to stdout.
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout.

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        nb_lines {int} -- lines to read (default: {0})
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for idx, line in enumerate(file):
                if idx == nb_lines:
                    break
                print(line, end="")
