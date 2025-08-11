# value = input('please enter the value:\n')
# print(value)
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    print('')
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)

    playerChoice = input("enter...\n1 for Rock, or \n2 for Paper, or \n3 for Scissors :\n\n")

    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1,2, or 3")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose "+ str(RPS(player)).replace('RPS.','') + ".")
    print("Python Chose " +str(RPS(computer)).replace('RPS.','') + ".")
    print("")

    if player == 1 and computer == 3:
        print("🥳 You Win !")
    elif player == 2 and computer == 1:
        print("🥳 You Win !")
    elif player == 3 and computer == 2:
        print("🥳 You Win !")
    elif player == computer:
        print(" 😂 Tie Game !")
    else:
        print("😎 python wins!")

    playagain_input = input("\nPlay again?\nY for Yes Or \nQ to Quit \n\n")

    if playagain_input.lower() == "y":
        continue
    else:
        print("\n 🥳🥳🥳🥳")
        print("thank you for playing \n ")
        playagain = False

    sys.exit("Bye !")
        