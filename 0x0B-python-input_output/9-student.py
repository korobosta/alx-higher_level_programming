#!/usr/bin/python3
"""This module contains a class that class Student
    that defines a student.
"""


class Student():
    """Class Student that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age.

        Arguments:
            first_name {str} -- student first name.
            last_name {str} -- student last name.
            age {int} -- student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description with simple data
            structure (list, dictionary, string, integer and boolean)
            for JSON serialization of an object.

        Returns:
            dict -- dictionary.
        """
        return self.__dict__
