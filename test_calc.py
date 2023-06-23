import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-5, 7), 2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(10, 5), 5)
        self.assertEqual(self.calc.sub(0, 0), 0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(-4, 5), -20)
        self.assertEqual(self.calc.mul(0, 10), 0)

    def test_div(self):
        self.assertEqual(self.calc.div(8,2), 4)
        self.assertEqual(self.calc.div(5, 2), 2.5)
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2,3), 8)
        self.assertEqual(self.calc.pow(3, 0), 1)
        self.assertEqual(self.calc.pow(5, -2), 0.04)
    
    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(100), 10)
        self.assertEqual(self.calc.sqrt(25), 5)
        #self.assertRaises(ValueError, self.calc.sqrt, -9)