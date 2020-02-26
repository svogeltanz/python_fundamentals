'''

Practice some stuff with decorators

'''

from functools import wraps


def decorator_func(org_func):
    def wrapper_func():
        print('I have got some ')
        return org_func()
    return wrapper_func  # returns the wrapper func ready to be executed


@decorator_func
def flowers():
    print('flowers for you')


@decorator_func
def food():
    print('hot fries with cheeeeeeese')


@decorator_func
def running():
    print('new running shoes for you! Let\'s go!')


flowers()
food()
running()


print('--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/--')

