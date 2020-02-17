'''

Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


# empty list
shortest_words = []
longest_words = []
word_list = []
number = 0

# open with 'with'//'as' and read the lines
with open("words.txt", "r") as file:
    content = file.read()
    word_list = content.split()
    word_list.sort(key=len)


# --- Task 1 ---
# finding the shortest word overall in the file
# word_list is sorted, that's why the shortest word is at the front
short = word_list[0]

# iterate trough the rest of the file and append every word that is as short as the shortest
for word in word_list:
    if len(word) <= len(short):
        shortest_words.append(word)

print(shortest_words)

# --- Task 2 ---
# finding the longest word overall in the file
# word_list is sorted, that's why the longest word is in the back
long = word_list[-1]

# iterate trough the rest of the file and append every word that is as long as the shortest
for word in word_list:
    if len(word) >= len(long):
        longest_words.append(word)

print(longest_words)

# --- Task 3 ---
for word in word_list:
    number += 1

print(f"The total number of words in 'words.txt' is: {number}")

