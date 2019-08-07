'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# take string input
user_sent = input("Please enter a sentence: ")

# take a symbol input
user_symb = input("Please enter a symbol: ")

# replace  the first letter with the symbol

user_sent = user_sent.replace(user_sent[0], user_symb)

# print the result
print(user_sent)

