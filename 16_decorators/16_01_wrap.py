'''

Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''




























'''
# Solve the exercise!

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



from functools import wraps

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

'''