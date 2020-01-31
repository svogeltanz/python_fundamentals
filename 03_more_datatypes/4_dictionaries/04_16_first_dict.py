'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

# create an empty dictionary
# fill a list for the keys with numbers 1 to 10
# fill the dict with the previous list and square the values

my_dict = {}

list_of_keys = []

for i in range(1,11):
    list_of_keys.append(i)

print(list_of_keys)

my_dict = {i: (i*i) for i in list_of_keys}

print(my_dict)
