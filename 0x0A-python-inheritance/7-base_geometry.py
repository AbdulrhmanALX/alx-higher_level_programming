#!/usr/bin/python3
"""_summary_
"""
class BaseGeometry:
    """_summary_
    """    
    def area(self):
        """_summary_
        """
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_
        """
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError (f"{self.name} must be an integer")
        if self.value <= 0:
            raise ValueError (f"{self.name} must be greater than 0")