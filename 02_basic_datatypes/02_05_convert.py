'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user input values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#1 nothing is missing
int_to_float = float(2)
print(int_to_float)

#2 the numbers after the period is missing
float_to_int = int(5.0)
print(float_to_int)

#3 floor division cuts the part after the period
result = 5.0 // 3
print(result)

#4
user_one = int(input("Please enter a number: "))
user_two = int(input("Please enter a second number: "))

result_multi = user_one * user_two

print("The product of your numbers is: " + str(result_multi))