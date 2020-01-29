'''

Write a script that removes all duplicates from a list.

'''

list_with_doubles = [1, 2, 3, 4, 3, 4, 5, 6, 6, 6, 9, 9]

# convert a list to a set and back to a list
list_set = set(list_with_doubles)
list_new = [list_set]

print(list_with_doubles)

print(list_new)

# is there a different way to remove duplicates???
