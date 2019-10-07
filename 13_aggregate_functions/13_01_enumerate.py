'''
Demonstrate the use of the .enumerate() function.
'''


my_list = ["apple", "banana", "orange"]

obj1 = list(enumerate(my_list))

for index, item in obj1:
    print(f"{index}: {item}")

print(obj1)

