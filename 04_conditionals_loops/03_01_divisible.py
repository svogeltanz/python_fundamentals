'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

# get user input and store it as a number
user_number = int(input("Please enter a number: "))

def checkIfNumber(number):
    # checks if the given number is in the correct range
    if type(number) == int and 1000000000 > number > 1:
        print("Thank you for your input!")
    else:
        print("Something went wrong. Please try again:")
        user_number = int(input("Please enter a new number between 1 and 1,000,000,000: "))
    return


def checkIfDivisible(number):
    # checks if the given number is divisible by three
    if number % 3 == 0:
        print("Your input is divisible by 3.")
    else:
        print("Your number cannot be divided by 3.")
    return


def doTheMath(number):
    # divides the given number by 3 and prints the result to the console
    result = number / 3
    print("Your number divided by 3 is: ", result)
    print("Your number was ", number)

checkIfNumber(user_number)
checkIfDivisible(user_number)
doTheMath(user_number)
