'''

Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

from functools import wraps


# build a decorator that wraps a given text into an html tag
def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


tag_list = ['title', 'header', 'h1', 'h2', 'body', 'p']


for tag in tag_list:
    print(f'{tag_list.index(tag)}: {tag}')
user_tag = input("Please type the tag you want to use: ")
user_text = input("And now type the text you want to pass in that tag: ")


@tags(f"{user_tag}")
def get_text(text):
    """returns some text"""
    return text


print(get_text(user_text))

