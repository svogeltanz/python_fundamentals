'''

Write a script with a function that demonstrates the use of *args.

'''

# *args = Arguments and they are variable in length so you can pass in as many as you want


def add_num(*args):
    result = 0
    for num in args:
        result += num
    return result


# you cannot pass a list directly to it rather than passing multiple arguments
print(add_num(1, 2, 3, 4, 5, 6, 7))

