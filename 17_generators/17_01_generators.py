'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

new_generator = (i for i in range(50) if i % 2 == 0)
print(new_generator)

for i in new_generator:
    print(i)

