'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

# example for .enumerate
ex_list = ['one', 'two', 'three', 'four']

new_generator = (i for i in ex_list)  # use range(5) for example without enumerate
print(new_generator)

# for i in new_generator:
    # print(i)

for i, ii in enumerate(new_generator):
    print(f"{i}: {ii}")