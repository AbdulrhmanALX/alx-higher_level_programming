#!/usr/bin/python3

"""Rectangle Class.

This module contains a class that defines a rectangle.


"""


class Rectangle:
    """Defines the blueprint of a rectangle"""

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """        
        self.__width = width
        self.__hight = height
    
    @property    
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return self.__width
    
    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _description_
            TypeError: _description_
        """        
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
     
    @property    
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return self.__hight
    
    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _description_
            TypeError: _description_
        """        
        if type(value) == int:
            if value >= 0:
                self.__hight = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
    