#!/usr/bin/python3
"""This module contains function that returns True if
the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """function that returns True if
    the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    Arguments:
        obj (obj) -- object
        a_class (cls) -- class

    Returns:
        boolean -- True / False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
