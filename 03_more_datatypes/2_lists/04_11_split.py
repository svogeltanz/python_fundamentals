'''

Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

# get a string from the user
user_string = input('Please enter any sentence you want: ')

# split the string into a list
listOfWords = user_string.split()
print(listOfWords)

# count the occurences of the string
from collections import Counter
dictOfWords = Counter(listOfWords)

print(dictOfWords)

# get the word with max occurences
values_list = dictOfWords.values()
max_value = max(values_list)
print(max_value)

# compare the max value with max occurences to find the value with the most occurences
for word, occurence in dictOfWords.items():
    if occurence == max_value:
        max_word = word

print("The word with the most occurences is: " + max_word)
