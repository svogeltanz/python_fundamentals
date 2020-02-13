'''
Write a script that reads in the content of words.txt and writes the content in reverse
to a new file words_reverse.txt.
'''














































with open("words.txt", "r") as fout:
    content = fout.read()
    content_list = content.split()
    # print(content)
    reverse_list = []
    for word in content_list:
        reverse_list.insert(0, word)  # appends the word always at the beginning
        content_list.remove(word)  # takes hours! faster way?
    # print(reverse_list)

with open("words_reverse.txt", "w") as fin:
    for word in reverse_list:
        fin.write(word)

print(len(content_list))
print(len(reverse_list))


