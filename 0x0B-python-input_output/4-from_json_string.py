#!/usr/bin/python3
"""This module contains a function that returns an
    object (Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by
        a JSON string:

    Arguments:
        my_str (obj) -- json str

    Returns:
        obj -- object
    """
    return json.loads(my_str)
