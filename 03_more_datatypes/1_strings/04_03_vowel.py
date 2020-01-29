'''
Write a script that prints the number of times a vowel is used in a user input string.

'''

# take a string from the user
user_string = input("Please input a string: ")
user_letter = input("Please enter a letter to count: ")

# see if vowels are in the string
letter_count = user_string.count(user_letter)

# print the number of all vowels in the string
print(letter_count)
