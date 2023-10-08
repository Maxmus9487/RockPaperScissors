import sys
import random
from enum import Enum


def play_rps():
    
    class RPS(Enum):
        Rock = 1
        Paper = 2
        Scissors = 3


    playerchoice= input("Enter... \n 1 for rock,\n 2 for paper,\n 3 for scissors: \n\n")

    if playerchoice not in ["1","2", "3"]:
        print("you must enter 1, 2, or 3.")
        return play_rps()
    
    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("you chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    if player == 1 and computer == 3:
        print("🥳🎉 you win")
    elif player == 2 and computer == 1:
        print("🥳🎉 you win")
    elif player == 3 and computer == 2:
        print("🥳🎉 you win")
    elif player == computer:
        print("⧓ tie game")
    else:
        print("😞❌ you lose")

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \n Q for Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n Thank you for playing\n")
        sys.exit(" Bye!")

play_rps()
