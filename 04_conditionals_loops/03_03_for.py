'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

# create and fill a list up to 100
number_list = []
i = 1
while i <= 100:
    number_list.append(i)
    i += 1


# set up a loop
for number in number_list:
    if number % 2 == 1:
        print(number)
