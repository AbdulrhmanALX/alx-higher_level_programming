#!/usr/bin/python3
"""_summary_
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """_summary_

    Args:
        rectangle (_type_): _description_
    """
    def __init__(self, size):
        """_summary_

        Args:
            size (_type_): _description_
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """_summary_
        """
        return self.__size **2
    
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return f"[Square] {self.__size}/{self.__size}"