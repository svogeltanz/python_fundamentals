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


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name


print(get_text.__name__) # get_text
print(get_text.__doc__) # returns some text
print(get_text.__module__) # __main__

print(get_text("John"))
# prints "<p>Hello John</p>
