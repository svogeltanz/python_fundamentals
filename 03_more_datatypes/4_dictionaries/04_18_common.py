'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 2, "c": 4 , "d": 2}

# define a function which adds the values together
def mergeDict(firstDict, secondDict):
    '''Combining two dictionaries and adding the values of equal keys'''

    # create a new dict to return at the end of the function
    thirdDict = {**firstDict, **secondDict}

    # check every key, value pair in the new dict
    for key, value in thirdDict.items():
        # check if the key of the given dicts is in both dicts
        if key in firstDict and key in secondDict:
            # if so, add the values together
            thirdDict[key] = value + firstDict[key]
    return thirdDict


dict3 = mergeDict(dict1, dict2)

print(dict3)
