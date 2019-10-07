'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def pizza_rec(**kwargs):

    for k, v in kwargs.items():
        print(f"{k}: {v}")


pizza_rec(first="make dough", second="select sauce", third="select topping", fourth="make pizza")

