'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(list):

    '''Takes in a list and returns the sum'''

    result = 0

    for item in list:
        result += item

    return result

list = [0, 3, 5, 7, 11, 16]

print(sum(list))