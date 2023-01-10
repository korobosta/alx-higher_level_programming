#!/usr/bin/python3
"""This module contains a function that returns the JSON
    representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Arguments:
        my_obj {obj} -- object

    Returns:
        str -- Serialize obj to a JSON formatted str
    """
    return json.dumps(my_obj)
