'''

Write a lambda function that does not take in an argument but returns a value. Print the return value.

'''

# solving the problem
exa = lambda: "This is the return of the function with no argument."

print(exa())


'''
squares = list(map(lambda x: x ** 2, range(10)))

compr_squares = [x**2 for x in range(10)]

special_squares = list(filter(lambda x: x > 5 and x < 50, squares))
compr_special_squ = [x for x in compr_squares if x > 5 and x < 50]

print(squares)
print(compr_squares)

print(special_squares)
print(compr_special_squ)


names = ['Alexander', 'Felix', 'Fabian', 'Martin', 'Rob', 'Florian', 'Jonas']

length = list(map(len, names))

compr_len = [len(x) for x in names]

f_names = list(filter(lambda s: s.startswith('F'), names))
compr_f_nam = [s for s in names if s.startswith('F')]

print(length)
print(compr_len)

print(f_names)
print(compr_f_nam)


locations = ['Lisbon', 'Valencia', 'Edinburgh', 'Fuerteventura']


def get_last_char(word):
    return word[-1]


print(sorted(locations, key=get_last_char))
print(sorted(locations, key=lambda x: x[-1]))
'''
