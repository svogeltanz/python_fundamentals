'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''

# create a lists to print
single_diggit = []


# fill the list with the numbers
for num in range(0, 50, 1):
    single_diggit.append(num)


# print the list with linebreaks at the end
for num in single_diggit:
    print(num, end=' ')
    if ((num+1) % 10) == 0 and num != 0:
        print("\n")

