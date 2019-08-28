'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

# take a number from the user between 1 and 1,000,000,000
user_input = int(input("Please enter a number between 1 and 1,000,000,000: "))


# check if the number is in the proposed range
if user_input <= 1000000000 and user_input >= 1:
    # check if the number is divisible by 3 and print a statement if it is or is not
    if user_input % 3 == 0:
        print("Congrats! Your number is divisible by 3!")
    else:
        print("This number is not divisible by 3.")
else:
    print("Sorry that is a wrong number!")

