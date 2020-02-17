'''
Write a script that reads in the content of words.txt and writes the content in reverse
to a new file words_reverse.txt.
'''


# open a new file and read the reversed lines of the old file, print every line to the new file
with open("reversed_words.txt", "w") as fin:
    for line in reversed(list(open("words.txt", "r"))):
        # no rstrip() needed because the new line char "\n" should stay in the list
        fin.write(line)

