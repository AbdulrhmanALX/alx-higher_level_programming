def add_integer(a, b=98):
    """adds 2 ints

    Args:
        a : first int
        b : second int, Defaults to 98.

    Raises:
        TabError: if a,b are neither int not float

    Returns:
       int : sum of a and b
    """    if type(a) is not float and type(a) is not int:
        raise TabError("a must be an integer") 
    if type(b) is not float and type(b) is not int:
        raise TabError("b must be an integer") 
    if type(a) is float:
        int(a)
    if type(b) is float:
        int (b)
    return int(a + b)

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

#if __name__ == __main__:
#    import unittest
#    unittest.test_file()