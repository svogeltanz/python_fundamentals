'''
Code a game of rock paper scissors.

'''


# function to get hand based on number
def get_hand(number):
    number_to_hand = {0: "Scissor", 1: "Rock", 2: "Paper"}
    new_hand = str(number_to_hand.get(number))
    return new_hand

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, user):
    # create new string with both hands to use compare_hands dictionary
    both_hands = f"{computer} {user}"

    # keep the number of conditionals to a minimum using dictionaries
    # dictionary for determining the winner/loser
    compare_hands = {"Scissor Scissor": 2,
                     "Scissor Rock": 0,
                     "Scissor Paper": 1,
                     "Rock Scissor": 1,
                     "Rock Rock": 2,
                     "Rock Paper": 0,
                     "Paper Scissor": 0,
                     "Paper Rock": 1,
                     "Paper Paper": 2}

    if compare_hands[both_hands] == 0:
        result = "User wins!"
    elif compare_hands[both_hands] == 1:
        result = "Computer wins!"
    elif compare_hands[both_hands] == 2:
        result = "You tied!"
    else:
        result = "Something went wrong!"
    return result


# take in a number 0-2 from the user that represents their hand
user_number = int(input("Please enter a number between 0 and 2: "))

# generate a random number 0-2 to use for the computer's hand
import random
comp_number = random.randint(0, 3)

# call the function get_hand to get the string representation of the user's hand
user_hand = get_hand(user_number)

# call the function get_hand to get the string representation of the computer's hand
comp_hand = get_hand(comp_number)

# call the function determine_winner to figure out the winner
game_result = determine_winner(comp_hand, user_hand)

# print out the player hand and computer hand
print(f"The hand of the user is: {user_hand}")
print(f"The hand of the computer is: {comp_hand}")

# print out the winner
print(f"And the result of the game is: {game_result}")


