'''
Write the necessary code to calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.
'''

# volume = pi * (r*r) * height

pi = 3.14159265359

r = 3.14

h = 5

vol = pi * (r*r) * h

# surface area	=	2π*r*r +	2π*r*h

area = (2*pi*r*r) + (2*pi*r*h)

print("Volume: " + str(vol))
print("Area: " + str(area))