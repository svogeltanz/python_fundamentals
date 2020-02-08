'''

Code a game of rock paper scissors. Update the instructions from the github repo!

- take in a number 1-3 from the user that represents their hand
- generate a random number 1-3 to use for the computer's hand
- call the function get_hand to get the string representation of the user's hand
- call the function get_hand to get the string representation of the computer's hand
- call the function determine_winner to figure out who won
- print out the player hand and computer hand
- print out the winner

'''

import random

print("Let's play a game of rock, paper, scissors! \n"
      "You can choose your hand first. Here are your options: \n"
      "1. Rock \n"
      "2. Paper \n"
      "3. Scissors")
user_hand = int(input("Please enter the number of your choice: "))

computer_hand = random.randrange(1, 4, 1)

# create a function to get the hand of a player's number
def get_hand(num):
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    elif num == 3:
        return "Scissor"
    else:
        return "Something went wrong"

# determine who won with a nested if-statement; or use a function to determine winner
def determineWinner(hand1, hand2):

    if hand1 == 1 and hand2 == 1:
        print("You tie!")
    elif hand1 == 2 and hand2 == 1:
        print("You win!")
    elif hand1 == 3 and hand2 == 1:
        print("You loose!")
    elif hand1 == 1 and hand2 == 2:
        print("You loose!")
    elif hand1 == 2 and hand2 == 2:
        print("You tie!")
    elif hand1 == 3 and hand2 == 2:
        print("You win!")
    elif hand1 == 1 and hand2 == 3:
        print("You win!")
    elif hand1 == 2 and hand2 == 3:
        print("You loose!")
    elif hand1 == 3 and hand2 == 3:
        print("You tie!")
    else:
        print("Something went wrong!")
    return


print("Your hand is: ", get_hand(user_hand))
print("The computer's hand is: ", get_hand(computer_hand))


determineWinner(user_hand, computer_hand)
