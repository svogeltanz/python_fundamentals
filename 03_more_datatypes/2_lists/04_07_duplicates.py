'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5, 6, 6, 6, 9, 9]
print(list_)

# convert a list to a set and back to a list
list_set = set(list_)
list_new = [list_set]
print(list_new)

