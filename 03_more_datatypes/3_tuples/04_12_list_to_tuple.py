'''

Write a script that takes a list and turns it into a tuple.

'''

# take an input as a list
user_string = input("Please enter a list separated by whitespace: ")

# splits a string at every whitespace
user_list = user_string.split()
print(user_list)

# convert list into tuple
user_tuple = tuple(user_list)
print(user_tuple)
