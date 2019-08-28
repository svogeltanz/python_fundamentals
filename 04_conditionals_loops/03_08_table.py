'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''

# use one big loop instead?!

a = 0
b = a + 10
for x in range(a, b):
    print(x, end=" ")
print("")

c = b + 10
for x in range(b, c):
    print(x, end=" ")
print("")

d = c + 10
for x in range(c, d):
    print(x, end=" ")
print("")

e = d + 10
for x in range(d, e):
    print(x, end=" ")
print("")

f = e + 10
for x in range(e, f):
    print(x, end=" ")

