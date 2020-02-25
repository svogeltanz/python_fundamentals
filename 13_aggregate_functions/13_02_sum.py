'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''


def sum_list(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(sum_list([1,2,3,4]))

