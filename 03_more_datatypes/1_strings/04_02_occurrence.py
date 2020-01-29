'''
Write a script that takes a string of words and a letter from the user.
Find the index of the first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# take a sentence from the user; "input" is always a string except ohterwise stated
user_input = input("Please enter a sentence: ")

# take the letter which you want to find
user_letter = input("Please enter a letter of the sentence: ")

# find the index of the letter's first occurence
letter_index = str(user_input.index(user_letter))

# print the result
print("Result: " + letter_index)
