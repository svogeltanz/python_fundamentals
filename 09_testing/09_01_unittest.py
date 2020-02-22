'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

- Check for correct results by providing an example input
- Check that DivisionByZero errors get raised correctly

'''

import unittest


def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        return f"this won't work, {x} - {y} is 0 or lower."


class MyFirstTest(unittest.TestCase):

    # test for correct calculation and type of output
    def test_sub_divide(self):
        self.assertTrue(subtract_divide(1, 5, 3), 0.5)
        self.assertIsInstance(subtract_divide(1, 5, 2), float)

    # test for correct raise of the exception
    def test_exception(self):
        self.assertRaises(ZeroDivisionError)




