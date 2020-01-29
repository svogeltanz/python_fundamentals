'''
1 - Write and execute a script that prints "hello world!" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''




print("Hello world!")

name = input("Please enter your name: ")

print("And hello " + name + " as well. We do have a little exercise for you today!")

a = int(input("Please enter a number: "))
b = int(input("Please enter a second number: "))
c = int(input("Please enter a third number: "))

result = a + b + c

print("The sum of your numbers is: " + str(result) + ".")


# calculation how many seconds are in one year

days = 365
hours = 24
minutes = 60
seconds = 60

secondsPerYear = seconds * hours * minutes * days

print("In one year are: " + str(secondsPerYear) + " seconds.")
