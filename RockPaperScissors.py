import random

choices = ("rock", "paper", "sicssors")
player = None
computer = random.choice(choices)
running = True
while True:
    player = None
    computer = random.choice(choices)
    while player not in choices:
        player = input(("Enter... \n rock,\n paper,\n scissors: \n\n"))


        print("")
        print(f"Player:{player}")
        print(f"Python:{computer}")
        print("")

        if player == computer:
            print("⧓ Tie game")
        elif player == "rock" and computer == "sicssors":
            print("🥳🎉 You win")
        elif player == "paper" and computer == "rock":
            print("🥳🎉 You win")
        elif player == "sicssors" and computer == "paper":
            print("🥳🎉 You win")
        else:
            print("😞❌ You lose")

    replay = input("Play again? (Yes/No)").lower()
    if not replay =="Yes":
        running = False
    
    print("Thanks for playing!")