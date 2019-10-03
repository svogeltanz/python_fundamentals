import unittest
# check out how to properly import the other files from section 9 to make the tests work

class MyFirstTest(unittest.TestCase):

    # function for testing if the output is of the correct datatype
    def test_divide_raises(self):
        self.assertIsInstance(divide(10, 0), str)


    def test_divide_math(self):
        self.assertIsInstance(divide(10, 1), float)
        self.assertEqual(divide(10, 2), 5)

# test the other functions in 09_02
    def test_add(self):
        self.assertIsInstance(add(1, 1), float)
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertIsInstance(sub(2, 1), float)
        self.assertEqual(sub(2, 3), -1)

    def test_multi(self):
        self.assertIsInstance(multi(1, 1), float)
        self.assertEqual(multi(2, 3), 6)
        if multi(2, 3) == 8:
            print("The function calculates the power of instead of multiplying.")

