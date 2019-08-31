'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def is_divisible_4or7(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    return False

def is_divisible_4and7(number):
    if number % 4 == 0 and number % 7 == 0:
        return True
    return False

user_input = int(input("Please enter a number between 1 and 1,000,000,000: "))

fourORseven = is_divisible_4or7(user_input)
fourANDseven = is_divisible_4and7(user_input)

print(f"Your number is divisible by 4 or 7: {fourORseven}\nYour number is divisible by 4 and 7: {fourANDseven}")