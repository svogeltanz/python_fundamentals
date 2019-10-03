'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

import unittest

# define function
def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return f"Error. Cannot divide by 0."


# --------------------------------------------
# TESTING





