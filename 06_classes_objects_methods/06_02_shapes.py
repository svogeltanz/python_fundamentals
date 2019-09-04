'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


# create class for rectangle; constructed by length and width
# write method to calculate area of both classes
# write method to calculate perimeter
class Rectangle:
    '''Class for a rectangle with two methods'''

    def __init__(self, length, width):
        '''Constructor which takes a length and width'''
        self.length = length
        self.width = width

    def area(self):
        '''Calculates the area of the rectangle'''
        result = self.length * self.width
        return result

    def perimeter(self):
        '''Calculates the perimeter of the rectangle'''
        result = (self.length + self.width) * 2
        return result


# create class for circle; constructed by radius
# write method to calculate circumference

class Circle:
    '''Class for a circle with two methods'''
    # set pi "globally" here to use it in all methods

    def __init__(self, radius):
        '''Constructor which takes a radius'''
        self.radius = radius

    def area(self):
        '''Calculates the area of the circle'''
        pi = 3.14
        result = pi * (self.radius**2)
        return result

    def circumference(self):
        '''Calculates the circumference of the rectangle'''
        pi = 3.14
        result = pi * self.radius * 2
        return result

r = Rectangle(10, 5)
print(r.area())
print(r.perimeter())

c = Circle(8)
print(c.area())
print(c.circumference())