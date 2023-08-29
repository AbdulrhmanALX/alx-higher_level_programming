#!/usr/bin/python3
"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('1-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """Defines the blueprint of a square.

    Attribute:
        size: An integer indicating the size of the square object.
    """

    def __init__(self, size=0):
        """An object constructor method.

        Initiatilizes Square with size.

        Arg:
            size: A integer representing object size
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """A public object method.

        Returns:
            The current square area
        """
        return self.size ** 2