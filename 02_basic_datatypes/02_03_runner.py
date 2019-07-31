'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

# hint to Martin: very unrealistic! :P

runner_miles = 10
runner_km = runner_miles * 1.6

runner_time = 30.5

print(runner_km)

km_per_hour = 60 * runner_km / runner_time

print("The average speed of this runner is: " + str(km_per_hour))