'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''





















input_dict = {"item1": 5, "item2": 6, "item3": 1}

sorted_dict = sorted(input_dict.items() , key = lambda x : x[1])
# Question for Johnny: What's going on with lambdas??

print(sorted_dict)
