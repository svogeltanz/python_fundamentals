'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def pizza_r(**kwargs):

    for k, v in kwargs.items():
        print(f"{k}: {v}")


pizza_r(Ingredients=["Wheat", "Tomato", "Mushrooms", "Cheese"], Cooking_time="20", Kind="vegeterian")






