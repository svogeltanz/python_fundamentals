'''
Write a script prints the number of times a vowel is used in a user input string.

'''

# take a string from the user
user_string = input("Please input a string: ")
user_vowel = input("Please enter a vowel to count: ")

# see if vowels are in the string
vowel_count = user_string.count(user_vowel)

# print the number of all vowels in the string
print(vowel_count)

