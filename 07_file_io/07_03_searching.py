'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''

import os

path = "/Users/sebastianvogeltanz/Desktop/example files"

jpg_files = []
mp3_files = []
pdf_files = []


for subdir, dirs, files in os.walk("/Users/sebastianvogeltanz/Desktop/example files"):
    for name in files:
        if name.endswith(".jpg"):
            # appends the file name to the path of the folder
            file = os.path.join("/Users/sebastianvogeltanz/Desktop/example files", name)
            jpg_files.append(file)
        elif name.endswith(".mp3"):
            # appends the file name to the path of the folder
            file = os.path.join("/Users/sebastianvogeltanz/Desktop/example files", name)
            mp3_files.append(file)
        elif name.endswith(".pdf"):
            # appends the file name to the path of the folder
            file = os.path.join("/Users/sebastianvogeltanz/Desktop/example files", name)
            pdf_files.append(file)


print(f"These are the JPG files: {jpg_files}")
print(f"These are the PDF files: {pdf_files}")
print(f"These are the MP3 files: {mp3_files}")

