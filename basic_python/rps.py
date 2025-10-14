import sys
import random
from enum import Enum

def rps():
   game_count = 0
   player_wins = 0
   python_wins = 0

   def play_rep():
    nonlocal player_wins
    nonlocal python_wins
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
    
    def decide_winner(player,computer):
       nonlocal player_wins
       nonlocal python_wins
       if player == 1 and computer == 3:
        player_wins +=1
        return("🥳 You Win!")
       elif player == 2 and computer == 1:
        player_wins +=1
        return("🥳 You Win!")
       elif player == 3 and computer == 2:
        player_wins +=1
        return("🥳 You Win!")
       elif player == computer:
        return("😂 Tie Game!")
       else:
        python_wins += 1
        return("😎 Python Wins!")

    game_result = decide_winner(player,computer)
    print(game_result)
    
    # global game_count
    nonlocal game_count
    game_count += 1

    print("\nGame count:"+str(game_count))
    print("\nPlayer wins:"+str(player_wins))
    print("\nPython wins:"+str(python_wins))
    
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

   return play_rep()

rps()
# Start the game
# play_rep()


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

