'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

# create a function which adds the values for the same key
def dictAdd(dict1, dict2):
    dict_result = {**dict_1, **dict_2}
    for key, value in dict_result.items():
        if key in dict_1 and key in dict_2:
            dict_result[key] = value + dict_1[key]

    return dict_result

# merge two dictionaries
result_dict = dictAdd(dict_1, dict_2)
print(result_dict)
