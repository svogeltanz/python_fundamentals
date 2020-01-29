'''

Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

# get some input from the user and use .split to create a list
user_input_list = input("Please enter any sentence: ").split(" ")
print(user_input_list)

# create two empty lists to fill up in the for loops
result_list = []
sparring_list = []

# create a list that turns list to tuple
tuple_list = tuple()


# build two for loops to access first the word and then every char and build a tuple of every word
# after the inner for loop the list has to be cleared for the next word
for word in user_input_list:
    for char in word:
        sparring_list.append(char)
    tuple_list = tuple(sparring_list)
    result_list.append(tuple_list)
    sparring_list.clear()

# print the final result
print(result_list)
