#!/usr/bin/python3
"""This module contains a class that class Student
    that defines a student. (based on 11-student.py)
"""


class Student():
    """Class Student that defines a student.
        (based on 11-student.py)
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

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data
            structure (list, dictionary, string, integer and boolean)
            for JSON serialization of an object.

        Returns:
            dict -- dictionary.
        """
        dic = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if hasattr(self, attr):
                dic[attr] = getattr(self, attr)
        return dic
