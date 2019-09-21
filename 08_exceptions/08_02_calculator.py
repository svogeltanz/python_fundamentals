'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    dividend = int(input("Please enter a dividend: "))
    divisor = int(input("Please enter a divisor: "))
    result = dividend / divisor
    print(result)
except ZeroDivisionError as zde:
    print("You cannot divide by 0.")
except ValueError as ve:
    print("This is not a number.")

