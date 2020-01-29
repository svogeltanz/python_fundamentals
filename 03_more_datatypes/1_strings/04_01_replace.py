'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# take string input
user_sentence = input("Please enter a sentence: ")

# take a symbol input
user_symbole = input("Please enter a symbol: ")

# replace  the first letter with the symbol
user_sentence = user_sentence.replace(user_sentence[0], user_symbole)

# print the result
print(user_sentence)

