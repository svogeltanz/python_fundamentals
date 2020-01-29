'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
'''
# hint to Martin: very unrealistic! :P

runner_miles = 10
runner_km = runner_miles * 1.6

runner_time = 30.5

print(runner_km)

runner_km_per_hour = 60 * runner_km / runner_time

print("The average speed of this runner is: " + str(km_per_hour))
'''

user_miles = int(input("Please enter the latest distance you ran (in miles): "))
user_time = int(input("Please enter the time you needed for this distance (in minutes): "))
user_km = user_miles * 1.6
user_km_per_hour = 60 * user_km / user_time

print("You're average speed for " + str(user_miles) + " miles is: " + str(user_km_per_hour) + ".")