'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(my_list):

    '''Takes in a list and returns the sum'''

    result = 0

    for item in my_list:
        result += item

    return result

my_list = [0, 3, 5, 7, 11, 16]

print(sum(my_list))

# no list as parameter, different name for it