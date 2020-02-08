'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"This is a rectangle with a length of {self.length} and a width of {self.width}."

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2*(self.width + self.length))

    def more_length(self):
        self.length += 1

    def more_width(self):
        self.width += 1

    def less_length(self):
        self.length -= 1

    def less_width(self):
        self.width -= 1


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"This is a circle with a radius of {self.radius}."

    def area(self):
        return (3.14*(self.radius**2))

    def circumference(self):
        return (2 * 3.14 * self.radius)

    def get_bigger(self):
        self.radius += 1

    def get_smaller(self):
        self.radius -= 1


bob = Rectangle(10, 5)
bob.area()
bob.perimeter()
print(bob)
bob.more_length()
bob.more_length()
print(bob)
print(f"The area is {bob.area()}.")

puh = Circle(15)
puh.area()
puh.circumference()
print(puh)
puh.get_bigger()
puh.get_bigger()
print(puh)

