#!/usr/bin/python3

"""Rectangle Class.

This module contains an empty class that defines a rectangle.


"""


class Rectangle:
    """Defines the blueprint of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'
    

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """   
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    
    def __str__(self):
        """_summary_
        """        
        rect = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += str(self.print_symbol)
                if i != len(range(self.__height)) - 1:
                    rect += '\n'
        return rect
    
    def __repr__(self):
        """_summary_
        """        
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """_summary_

        Raises:
            ValueError: _description_
            TypeError: _description_
            ValueError: _description_
            TypeError: _description_

        Returns:
            _type_: _description_
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1       
    
    @property
    def width(self):
        """_summary_
        """        
        return self.__width
    
    @width.setter
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
    
    @height.setter
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
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """_summary_

        Args:
            rect_1 (_type_): _description_
            rect_2 (_type_): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_

        Returns:
            _type_: _description_
        """        
        if isinstance(rect_1, Rectangle) == False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) == False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        return cls(size, size)        
        