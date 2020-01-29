'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]

'''

new_list = [1, 2, 2, 3, 3, 4, 5, "hello"]

from collections import Counter

appearances = Counter(new_list)
print(appearances)

unique_list = []

for value, key in appearances.items():
    if key == 1:
        unique_list.append(value)

print(unique_list)
