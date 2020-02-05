'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''


input_dict = {"item1": 5, "item2": 6, "item3": 1, "item4": 0, "item5": 100}

# sort the dict with the sorted function
result_list = sorted(input_dict.items(), key=lambda x: x[1])
# creates a sorted list by default

print(result_list)

