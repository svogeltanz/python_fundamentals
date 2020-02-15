'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''

































'''
# /Users/sebastianvogeltanz/Desktop/example

import os

jpg_list = []  # can be used for every file extension

for file in os.listdir("/Users/sebastianvogeltanz/Desktop/example"):
    if file.endswith(".jpg"):
        file = os.path.join("/Users/sebastianvogeltanz/Desktop/example", file)  # builds a new string for the file name with the complete path
        jpg_list.append(file)  # adds the file name as a string to the list

print(jpg_list)
'''