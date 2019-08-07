'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''


# take three words from the user into a list
user_list = [input("Please enter a string: "), input("Please enter a second string: "), input("Please enter a third string: ")]
print(user_list)

# use a for loop to count characters in string
for word in user_list:
    word = len(word)

# use max() to store the largest string
largest_string = str(max(user_list))

# print the largest string
print("The largest string of your given strings is: " + largest_string)
