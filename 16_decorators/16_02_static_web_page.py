'''

Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

from functools import wraps


# write a decorator that takes a function
def outer(func):
    def inner(func):
        # wrap func in html tag
        return func
    return inner


@outer
def text(msg):
    return msg

