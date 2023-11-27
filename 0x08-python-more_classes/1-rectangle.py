#!/usr/bin/python3

"""Rectangle Class.

This module contains a class that defines a rectangle.


"""


class Rectangle:
    """Defines the blueprint of a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__hight = height
        
    def width(self):
        return self.__width
    
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        
    def height(self):
        return self.__hight
    
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hight = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
    