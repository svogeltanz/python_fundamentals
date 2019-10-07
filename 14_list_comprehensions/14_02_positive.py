'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
pos_numbers = [number for number in numbers if number > 0]

'''
def transformList(list):

    # Adds the positive numbers of a list to a new list

    for number in list:
        if number > 0:
            pos_numbers.append(number)
'''

# transformList(numbers)
print(pos_numbers)