#Closure is a function having to the scope of its parent function
#function after the parent function has returned.

def parent_function(person,coins):
    #coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins>1:
            print("\n"+ person + " has " + str(coins) + "coins left.")
        elif coins == 1:
              print("\n"+ person + " has " + str(coins) + "coins left.")
        else:
              print("\n"+ person + " is out of coins. ")  

    return play_game

prem = parent_function("prem",3)
deep = parent_function("deep",5)

prem()
prem()

deep()

prem()
    

             