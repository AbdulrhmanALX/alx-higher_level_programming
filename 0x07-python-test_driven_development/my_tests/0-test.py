import unittest

class testAdd(unittest.TestCase):
    
    def test_a_int(self):
        self.assertRaises(TabError,lambda a,b: a + b if type(a) not in (int, float) raise TypeError("a must be in"), '1', '2')

if __name__ == '__main__':
    unittest.main()        