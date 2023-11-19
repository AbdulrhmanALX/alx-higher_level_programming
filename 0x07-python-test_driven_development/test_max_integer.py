"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_len(self):
        self.assertEqual(max_integer([]),None)
    
    def test_basic_func(self):
        self.assertEqual(max_integer([-10,5,4]),5)
    
    def test_errors(self):
        self.assertRaises(Exception,max_integer,['5',5,3])
        self.assertRaises(Exception,max_integer,('5',5,3))
        self.assertRaises(Exception,max_integer,{'5',5,3})
        self.assertRaises(Exception,max_integer, 5)
    
    def test_float(self):
        self.assertEqual(max_integer([4.5,6,6.6]),6.6)
    
    def test_string(self):
        self.assertEqual(max_integer(["hi", "Zunk"]), "hi") #Uppercase letters have lower ASCII values than lowercase letters