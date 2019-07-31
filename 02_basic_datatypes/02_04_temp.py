'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''


user_fahrenheit = int(input("Please enter a temperature in Fahrenheit: "))

user_celsius = (user_fahrenheit - 32) * (5/9)

print("A temperature in Fahrenheit of: " + str(user_fahrenheit) + " is the same as " + str(user_celsius) + " in celsius.")