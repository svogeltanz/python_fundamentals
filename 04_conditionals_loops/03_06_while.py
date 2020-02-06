'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''


# use a while loop with in iterator
# every fifth number is divisible by 5 (%=0)

i = 1

while i <= 1000:
    if (i % 5) == 0:
        print(i)
    i += 1  # has to be outside the if-statement otherwise it would just count up the number which are correct
