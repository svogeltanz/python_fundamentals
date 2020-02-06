'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''


# set up a list from 1 to 50
unsquared = []

for i in range(1, 51):
    unsquared.append(i)

for num in unsquared:
    print(num, " squared is: ", num**2)

