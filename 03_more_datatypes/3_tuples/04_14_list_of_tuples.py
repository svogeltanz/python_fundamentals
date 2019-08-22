'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

# take a string from the user
user_input_string = input("Please enter a phrase: ")

# separate the user input by whitespace and turn it into a list
user_input_list = user_input_string.split()
print(user_input_list)

# create a list for every word in the user list using a for loop and convert the list to tuples
tuple_list = []
new_list = []
user_tuple = tuple()

# create a list of tuples using two for loops to access the words of the user list and the letters
# after every word the list is stored as a tuple and appended to the tuple list
for item in user_input_list:
    for char in item:
        new_list.append(char)
    user_tuple = tuple(new_list)
    tuple_list.append(user_tuple)
    new_list.clear()

print(tuple_list)


