'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''


def decorator_func(initial_func):
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func  # returns the wrapper func ready to be executed


# decorated_pretty = decorator_func(prettify)
# decorated_pretty()  # executes wrapper function which executes prettify() func

@decorator_func # is the same as the commented above
def prettify():
    print("flowers for you")


@decorator_func
def feed():
    print("potato and vegan meat")


@decorator_func
def sports():
    print("running shoes for you! See you later!")


prettify()
feed()
sports()
