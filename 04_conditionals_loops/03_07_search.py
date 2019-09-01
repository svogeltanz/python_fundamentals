'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

import random

user_num = int(input("Please enter a number between 1 and 1 million: "))
found_number = False

# while loop to find the number; exit after finding and print it
while not found_number:
    guess_num = random.randint(1, 1000001) # create random number
    if guess_num == user_num: # compare numbers
        print("Congrats, you got it! The number is: " + str(guess_num))
        found_number = True
        break # get out of the loop
    else:
        print("Try again!")

# maybe do it again with num +1 and counting to million

