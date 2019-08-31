'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

# take a number from the user
user_input = int(input("Please enter a number: "))

# use dict to lookup value

# check the number with the month
if user_input != "":
    if user_input == 1:
        print("January")
    elif user_input == 2:
        print("February")
    elif user_input == 3:
        print("March")
    elif user_input == 4:
        print("April")
    elif user_input == 5:
        print("May")
    elif user_input == 6:
        print("June")
    elif user_input == 7:
        print("July")
    elif user_input == 8:
        print("August")
    elif user_input == 9:
        print("September")
    elif user_input == 10:
        print("October")
    elif user_input == 11:
        print("November")
    elif user_input == 12:
        print("December")
    elif user_input < 1:
        print("That is a small one!")
    elif user_input > 12:
        print("That is too big to handle for me!")
else:
    print("You have to enter a number! :) ")
