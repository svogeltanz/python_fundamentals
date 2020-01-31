'''
Write a script that takes a string from the user and creates a dictionary of letters that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

# import the Counter class
from collections import Counter

# get input from the user
user_input = input("Please enter a word: ")

# use Counter for the user_input and store it in a dictionary
my_dict = dict(Counter(user_input))

'''
Or use this way:

dict = {}
cnt = Counter(user_input)
for key, value in cnt.items():
    dict[key] = value
    
'''

print(my_dict)
