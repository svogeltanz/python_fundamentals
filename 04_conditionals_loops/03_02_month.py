'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

# try using a dictionary to lookup the value fo the month and print it

# create a dict with the values for the month
month_dict = {1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"}

month_keys = month_dict.keys()

# take a number as input
user_input = int(input("Please enter an number between 1 and 12: "))

# loop through the keys and find the match. Put that in a function to call it.


def monthFinder(number):

    ''' Checks if the given number is within the dictionary keys and prints the value for it.
        If the value is not in the dict: the user is asked a new number. '''

    # variable to check if everything worked out, has to be in the scope of the function
    result = False

    # loop through the keys and find the match, print the value
    for key in month_keys:
        if key == number:
            print("Your month is: ", month_dict[key])
            result = True

    # if the user input is not in the dict, ask for a new number and call the function again
    if not result:
        print("There has been a missunderstanding with your number. Please try again.")
        number = int(input("Please enter a new number between 1 and 12: "))
        monthFinder(number)
    return


monthFinder(user_input)
