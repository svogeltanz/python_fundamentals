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

    def speed_increase(self):
        self.max_speed += 5

    def __str__(self):
        return f"Model: {self.model}, Year: {self.year}, Speed: {self.max_speed}"

speedy = Car("Lambo", 1994, 330)

james_bond = Car("Aston Martin", 1965, 230)

speedy.speed_increase()

speedy.speed_increase()

print(speedy)

