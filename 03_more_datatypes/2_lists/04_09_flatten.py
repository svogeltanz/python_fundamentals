'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9], [1, 6, 22, 444]]

flattened_list = []

# because there are more lists in the starting list
# we have to do two for loops and then append the items to a new list

for list in starting_list:
    for item in list:
        flattened_list.append(item)


print(flattened_list)
