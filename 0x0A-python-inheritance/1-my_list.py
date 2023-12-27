#!/usr/bin/python3
"""_summary_
"""
class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """_summary_
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)      
    