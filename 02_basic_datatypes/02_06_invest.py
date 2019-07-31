'''
Take in the following three values from the user:
    - investment amount
    - interest rate percentage
    - number of years to invest

Print the future values to the console.

'''

invest_user = float(input("Please enter an amount you want to invest: "))
interest_user = float(input("Please enter an interest rate percentage for your investment: "))
years_user = int(input("Please enter how long you want to invest (years): "))

percent_user = float(interest_user / 100)

future_value = invest_user*((1 + percent_user)**years_user)

print("The value of your investment will be: " + str(future_value))
