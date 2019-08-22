'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

from collections import Counter

user_str = input("Please enter a word: ")
user_list = list(user_str)

# Counter counts the occurences of every element of the list and puts it in a dict
user_dict = Counter(user_list)

print(user_dict)
