'''

Write a script that completes the following tasks:

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

'''

# function for 4 or 7
def isDivisibleBy4or7(num):
    if num % 4 == 0 or num % 7 == 0:
        return True
    return False


# function for both 4 and 7
def isDivisibleBy4and7(num):
    if num % 4 == 0 and num % 7 == 0:
        return True
    return False

# take an input as a number
input_number = int(input("Please enter a number from 1 to 1,000,000,000: "))

check4or7 = isDivisibleBy4or7(input_number)
check4and7 = isDivisibleBy4and7(input_number)

if check4or7:
    print("Your number is divisible by 4 or 7.")
elif check4and7:
    print("Your number is divisible by 4 and 7.")
else:
    print("Your number is not divisible by neither 4 nor 7.")

