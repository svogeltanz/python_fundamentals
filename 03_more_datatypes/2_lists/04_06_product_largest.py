'''

Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

# while the length of the list is < 11
user_input_list = []
# take in a number and append it to the list
while len(user_input_list) < 10:
    user_input = int(input("Please enter a number for your list: "))
    user_input_list.append(user_input)

# print the list
print(user_input_list)

# find the largest number using max()
max_number = max(user_input_list)

# print the largest number
print("The max value of your list is: " + str(max_number))

# calculate the product of all numbers of the list using a for loop
result = 1
for number in user_input_list:
    result = result * number

print("The product of the whole list is: ", result)
