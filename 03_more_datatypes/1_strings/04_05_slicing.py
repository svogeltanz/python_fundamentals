'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

# take in the user's name
user_name = input("Please enter your name: ")
print(user_name)

# slicing the first char to a new variable and move it to the end. Add "ay" to the string finally
add_pig_latin = "ay"
user_name_first = user_name[0]
user_name_new = user_name[1:]
user_name_translated = user_name_new + user_name_first + add_pig_latin

# print the translated name
print(user_name_translated)
