'''

Read in 10 numbers from the user. Place all 10 numbers into a list in order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

# use the source code of a earlier exercise
user_list = []

# while the length of the list is < 10
# take in a number and append it to the list

while len(user_list) < 10:
    user_input = int(input("Please enter a number for your list: "))
    user_list.append(user_input)

# print the list
print(user_list)

# define an order for the new list
new_order = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]

# re-order the input list by the predefined new order from the exercise
user_list = [user_list[i] for i in new_order]
print(user_list)
