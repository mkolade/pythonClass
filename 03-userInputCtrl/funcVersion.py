import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS['ROCK'])
    # print(RPS.ROCK)
    # print(RPS['ROCK'].value)
    playerValue = input("\nEnter... \n1 for Rock 🥌,\n2 for Paper📜 or \n3 for Scissors ✂ :\n\n")
    if playerValue not in ["1", "2", "3"]:
        print("You must enter a value between 1 and 3 ‼‼")
        play_rps()
    playerChoice = int(playerValue)

    compValue = random.choice("123")
    compChoice = int(compValue)

    print("\nYou chose " + str(RPS(playerChoice)).replace("RPS.", '') + ".")
    print("Python chose " + str(RPS(compChoice)).replace("RPS.", '') + ".\n")

    if playerChoice == 1 and compChoice == 3:
        print("🎉 You win!")
    elif playerChoice == 2 and compChoice == 1:
        print("🎉 You win!")
    elif playerChoice == 3 and compChoice == 2:
        print("🎉 You win!")
    elif playerChoice == compChoice:
        print("It's a draw 😲. Try again!")
    else :
        print("Python wins! 🐍 \n")

    
    while True:
        playAgain = input("Wanna keep playing?\n Enter Y for yes\n Q to quit\n\n")
        if(playAgain.lower() not in ["y", "q"]):

            continue
        else:
            break
    if(playAgain.lower() == "y"):
        play_rps()
    else:
        print("🎉🎉🙌🎉🎉")
        print("Thanks for playing")
        sys.exit("I hope we see you again")
play_rps()