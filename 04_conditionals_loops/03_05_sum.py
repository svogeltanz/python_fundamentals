'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

sum = 0
num1 = int(input("Please enter a number as the bottom of a range: "))
num2 = int(input("Please enter another number as the top of a range: "))


# calculate the sum of the range of the user
for number in range(num1, num2+1, 1):
    sum += number

print("The sum of your range is: " + str(sum))