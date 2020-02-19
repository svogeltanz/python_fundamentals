'''
Write a script that demonstrates a try/except/else.

'''


try:
    # take in two number and calculate the quotient
    dividend = int(input("Please enter a dividend: "))
    divisor = int(input("Please enter a divisor: "))
except ZeroDivisionError as zde:
    # catch the case if input is 0
    print("You cannot divide by 0. Please enter a positive number.")
except ValueError as ve:
    # catch the case if input is a string
    print("You did not enter a number. Please enter a number.")
except Exception as err:
    # catch anything else
    print("There has been a mistake: ", err)
else:
    result = dividend/divisor
    print("Your input is pretty good.")
    print(f"You want to divide {dividend} by {divisor}.")
    print(f"The result of your division is: {result}")
