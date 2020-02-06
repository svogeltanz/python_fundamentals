'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''


# get input
user1 = int(input("Please enter the lower bound of a range: "))
user2 = int(input("Please enter the upper bound of a range: "))

result = 0

# calculate the sum of the number in the range
for num in range(user1, user2+1):
    result += num

print("The sum of your bound is: ", result)

