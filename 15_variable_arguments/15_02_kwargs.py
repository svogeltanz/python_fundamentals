'''

Write a script with a function that demonstrates the use of **kwargs.

'''

# **kwargs = keyword arguments and represent a key and a value (dictionary)
# it is also variable in length and you can pass in as many as you want


def travel_spots(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


# cannot pass in a dictionary directly
travel_spots(Germany='Freiburg', Brazil='Rio', Spain='Malaga', Portugal='Faro')

print('//////////////////////////////////////')


def pizza_r(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


pizza_r(Ingredients=["Corn", "Tomato", "Mushrooms", "Olives"], Cooking_time="20", Kind="vegeterian")






