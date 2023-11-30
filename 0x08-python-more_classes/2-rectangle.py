#!/usr/bin/python3

"""Rectangle Class.

This module contains an empty class that defines a rectangle.


"""


class Rectangle:
    """Defines the blueprint of a rectangle"""

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """   
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """_summary_
        """        
        return self.__width
    
    @sitter.width
    def width(self, value):
        """_summary_
        """        
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
    
    @property
    def height(self):
        """_summary_
        """        
        return self.__height
    
    @sitter.height
    def height(self, value):
        """_summary_
        """        
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        
    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return self.__width * self.__height
    
    def perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)