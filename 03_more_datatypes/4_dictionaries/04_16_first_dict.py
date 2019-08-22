'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

# create an empty dict
first_dict = {}

# create a list that takes 1-10
dict_list = []
for i in range(1, 11):
    dict_list.append(i)

print(dict_list)

# add values to the dict using a for loop
first_dict = {i: (i * i) for i in dict_list}

print(first_dict)
