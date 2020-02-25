'''
Demonstrate the use of the .enumerate() function.
'''

courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

# enumerate creates a list of tuples
for index, course in enumerate(courses, start=1):
    print(f"{index}: {course} Python")

print(list(enumerate(courses)))


# create a function that mirrors .enumerate
def my_enumerate(my_list):

    '''coding the same output without using .enumerate but a for loop instead'''

    index_courses = []
    i = 0

    for c in courses:
        tup = (i, c)  # works without an f""
        index_courses.append(tup)
        i += 1

    return index_courses


# same output as using .enumerate
print(my_enumerate(courses))

