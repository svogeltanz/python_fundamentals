'''

Receive a number between 0 and 1,000,000,000 from the user.
Use a while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

import random

# get user input
user_number = int(input("Please enter a number between 0 and 1,000: "))

# set up a for loop to find the number
found = False

while not found:
    # create a random number
    guess_number = random.randint(0, 1000)
    # check if both match
    if guess_number == user_number:
        # print and exit the loop
        print("Your number was: ", user_number)
        found = True
        break



