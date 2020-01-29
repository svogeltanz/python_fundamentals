'''

From the previous example, move your calculation of how many seconds in a year to a python executable script.

'''

print("In this Script is calculated how many seconds are in one year. Therefore you have to enter the correct numbers "
      "for the days, hours, minutes and seconds")

days = int(input("Please enter the amount of days in one year: "))
hours = int(input("Please enter the amount of hours in one day: "))
minutes = int(input("Please enter the amount of minutes in one hour: "))
seconds = int(input("Please enter the amount of seconds in one minute: "))

secondsPerYear = seconds * hours * minutes * days

print("In one year are: " + str(secondsPerYear) + " seconds.")
