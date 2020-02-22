import unittest

from tdd import add, sub, multi, divide
# writing the tests for function which are built in 09_02_tdd


class MyFirstTest(unittest.TestCase):

    # function to test if the output is of the correct type
    # for the function divide
    def test_divide_raises(self):
        self.assertRaises(ZeroDivisionError)

    def test_divide_math(self):
        self.assertIsInstance(divide(10, 1), float)
        self.assertEqual(divide(10, 2), 5)

    # test the correct calculation of the functions add, sub and multiply
    def test_add(self):
        self.assertIsInstance(add(1, 1), int)
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertIsInstance(sub(2, 1), int)
        self.assertEqual(sub(2, 3), -1)

    def test_multi(self):
        self.assertIsInstance(multi(1, 1), int)
        self.assertEqual(multi(2, 3), 6)
        if multi(2, 3) == 8:
            print("The function calculates the power of instead of multiplying.")
