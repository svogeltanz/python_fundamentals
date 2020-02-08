'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car:

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"This car is a {self.model} from {self.year} with a maximum speed of {self.max_speed}."

    def increase_speed(self):
        self.max_speed += 5
        return

    def decrease_speed(self):
        self.max_speed -= 5
        return


mercedes = Car("SL500", 2020, 290)
ferrari = Car("F50", 2013, 375)
aston = Car("DB9", 2009, 240)

mercedes.increase_speed()

print(mercedes)
print(ferrari)
print(aston)

mercedes.model = "McLaren"
mercedes.year = 1990
mercedes.max_speed = 370

print(mercedes)

