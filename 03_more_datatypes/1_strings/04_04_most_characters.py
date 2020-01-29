'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''


# take three words from the user into a list
user_list = [input("Please enter a string: "), input("Please enter a second string: "),
             input("Please enter a third string: ")]
print(user_list)

# use the sort function for lists to bring it in a descending order
user_list.sort(reverse=True, key=len)
print(user_list)

# get the first element of the sorted list as the largest string
largest_string = user_list[0]

# print the largest string
print("The largest string of your given strings is: " + str(largest_string))


# try to solve in a different way
# using the len() method
