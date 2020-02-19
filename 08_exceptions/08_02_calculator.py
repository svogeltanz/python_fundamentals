'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    # take in two number and calculate the quotient
    dividend = int(input("Please enter a dividend: "))
    divisor = int(input("Please enter a divisor: "))
    result = dividend/divisor
    print(f"You want to divide {dividend} by {divisor}.")
    print(f"The result of your division is: {result}")
except ZeroDivisionError as zde:
    # catch the case if input is 0
    print("You cannot divide by 0. Please enter a positive number.")
except ValueError as ve:
    # catch the case if input is a string
    print("You did not enter a number. Please enter a number.")
except Exception as err:
    # catch anything else
    print("There has been a mistake: ", err)
