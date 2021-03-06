'''

Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

'''
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []


# not supposed to know that by now
def sort_tuple(tuple):
    sorted_list = sorted(tuple, key=lambda x:x[1])
    return sorted_list


sorted_list = sort_tuple(unsorted_list)

print(sorted_list)
'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 1)]

# write a function that gets the second element of the tuple (the number)
def getKey(item):
    return item[1]

# insert the getKey() function in the sorted method
sorted_list = sorted(unsorted_list, key=getKey)

print(sorted_list)
