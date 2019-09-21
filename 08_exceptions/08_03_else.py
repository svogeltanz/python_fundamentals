'''
Write a script that demonstrates a try/except/else.

'''

# I used the example from 08_02 and extended it with an else statement

try:
    dividend = int(input("Please enter a dividend: "))
    divisor = int(input("Please enter a divisor: "))
    result = dividend / divisor
except ZeroDivisionError as zde:
    print("You cannot divide by 0.")
except ValueError as ve:
    print("This is not a number.")
else:
    print("Everything went just fine!")
    print(f"The result is: {result}")

