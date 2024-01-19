import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))

playerValue = input("Enter... \n1 for Rock,\n2 for Paper or \n3 for Scissors:\n\n")
playerChoice = int(playerValue)

if playerChoice < 1 or playerChoice > 3:
    sys.exit("You must enter a value between 1 and 3")

compValue = random.choice("123")
compChoice = int(compValue)

print("")
print("You chose " + playerValue + ".")
print("Python chose " + compValue + ".")
print("")


if playerChoice == 1 and compChoice == 3:
    print("🎉 You win!")
elif playerChoice == 2 and compChoice == 1:
    print("🎉 You win!")
elif playerChoice == 3 and compChoice == 2:
    print("🎉 You win!")
elif playerChoice == compChoice:
    print("It's a draw 😲. Try again!")
else :
    print("Python wins! 🐍")