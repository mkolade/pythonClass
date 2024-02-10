import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS['ROCK'])
# print(RPS.ROCK)
# print(RPS['ROCK'].value)

playAgain = True

while playAgain: 
    playerValue = input("\nEnter... \n1 for Rock,\n2 for Paper or \n3 for Scissors:\n\n")
    playerChoice = int(playerValue)

    if playerChoice < 1 or playerChoice > 3:
        sys.exit("You must enter a value between 1 and 3")

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

    playAgain = input("Wanna keep playing?\n Enter Y for yes\n Q to quit\n\n")
    if(playAgain == "y".lower()):
        playAgain = True
    else:
        print("🎉🎉🙌🎉🎉")
        print("Thanks for playing")
        playAgain = False
sys.exit("I hope we see you again")