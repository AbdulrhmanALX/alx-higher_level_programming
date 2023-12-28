#!/usr/bin/python3
"""_summary_
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """_summary_
    """    
    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
    
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def area(self):
        """_summary_
        """ 
        return self.__width * self.__height       
        
    