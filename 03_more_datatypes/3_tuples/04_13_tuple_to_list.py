'''
Write a script that takes a tuple and turns it into a list.

'''

# take an input as a tuple
user_string = input("Please enter a tuple separated by whitespace: ")
user_list = user_string.split()
user_tuple = tuple(user_list)
print(user_tuple)

# convert the tuple into a list
user_list = list(user_tuple)
print(user_list)

'''
another way to fill up a list

for item in user_tuple:
    user_list.append(item)
    
print(user_list)
'''