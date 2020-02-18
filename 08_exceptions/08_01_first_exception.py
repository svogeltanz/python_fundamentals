'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises an exception that needs to be handled.

'''


try:
    list = ["Hi there"]
    print(list[1])
except IndexError as err:
    print("Look at the length of the list!", err)

