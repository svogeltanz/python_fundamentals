'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


# open with 'with'
# make list of all words with len()
# make new list with len() min()
# print the list

































'''
# read from file words.txt
with open("words.txt", "r") as file_out:
    file_content = file_out.read()
    words = file_content.split()  # creates a list of words
    words.sort(key=len)
    # print(words)
    # sorted list should have the smallest at the front and the longest in the back
    short = int(len(words[0]))
    long = int(len(words[len(words)-1]))
    # create two new empty lists and append words with the same length
    shortest_words = []
    longest_words = []
    for word in words:
        if len(word) == short:
            shortest_words.append(word)
        if len(word) == long:
            longest_words.append(word)
    print()
    print(f"Here is a list with the shortest words: {shortest_words}")
    print()
    print(f"Here is a list with the longest words: {longest_words}")

    # find the total number of words in the file
    number = 0
    for word in words:
        number += 1

    print(f"The total number of words in the file is: {number}")


'''