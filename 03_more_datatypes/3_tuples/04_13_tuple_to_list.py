'''

Write a script that takes a tuple and turns it into a list.

'''

# take an input as a tuple
user_input = input("Please enter a tuple separated by whitespace: ")
user_list = user_input.split(" ")
user_tuple = tuple(user_list)
print(user_tuple)

user_list = []

for item in user_tuple:
    user_list.append(item)

print(user_list)
