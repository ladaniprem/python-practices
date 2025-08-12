import sys
import random
from enum import Enum

def play_rep():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "Enter...\n"
        "1 for Rock, or \n"
        "2 for Paper, or \n"
        "3 for Scissors :\n\n"
    )
    if playerChoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3")
        return play_rep()

    player = int(playerChoice)
    computerchoice = random.choice(["1", "2", "3"])
    computer = int(computerchoice)
    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    if player == 1 and computer == 3:
        print("🥳 You Win!")
    elif player == 2 and computer == 1:
        print("🥳 You Win!")
    elif player == 3 and computer == 2:
        print("🥳 You Win!")
    elif player == computer:
        print("😂 Tie Game!")
    else:
        print("😎 Python Wins!")

    while True:
        play_again = input("\nPlay Again?\nY for Yes or Q to Quit: ").lower()
        if play_again not in ["y", "q"]:
            continue
        if play_again == "y":
            return play_rep()
        else:
            print("\n🥳🥳🥳🥳")
            print("Thank you for playing!\n")
            sys.exit("Bye!")

# Start the game
play_rep()

    # value = input('please enter the value:\n')
    # print(value)
    # play_again = True  # renamed for readability
    #   while play_again:
    #print('')
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
# Uncomment the following line to start the game
# play_rep()

