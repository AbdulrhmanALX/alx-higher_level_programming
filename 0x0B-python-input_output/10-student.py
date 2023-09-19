#!/usr/bin/python3
"""Module 9-student.
Creates a Student class.
"""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Returns: the dict representation of the instance.
        """
        if all([type(x) is str for x in attrs]) and type(attrs) is list:
            st_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    st_dict.update({i: self.__dict__[i]})
            return st_dict
        
        return self.__dict__.copy()
    