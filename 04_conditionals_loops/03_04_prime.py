'''
Print out every prime number between 1 and 100.

'''

# create and fill a list up to 100
number_list = []
i = 2
while i <= 100:
    number_list.append(i)
    i += 1

print(number_list)


for number in number_list:

    if number > 1:
        # check if the number is divisible by any other number between 2 and itself
        for i in range(2, number):
            if (number % i) == 0:
                break
        # if there has been a breakout of the if-statement, the number is printed to the console
        else:
            print(number, " is a prime number!")



