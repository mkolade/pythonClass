import sys
import random
from enum import Enum

def rps():
    gameCount = 0
    playerWins = 0
    pythonWins = 0
    def play_rps():
        nonlocal playerWins
        nonlocal pythonWins

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

        def getWinner(player, computer): 
            nonlocal pythonWins
            nonlocal playerWins 
            if player == 1 and computer == 3:
                playerWins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                playerWins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                playerWins += 1
                return "🎉 You win!"
            elif player == computer:
                return "It's a draw 😲. Try again!"
            else :
                pythonWins += 1
                return "Python wins! 🐍 \n"

        theWinner = getWinner(playerChoice,compChoice)
        print(theWinner)
        nonlocal gameCount
        gameCount += 1
        print("\n\nGames played: " + str(gameCount))
        print("\n\nPlayer wins: " + str(playerWins))
        print("Python wins: " + str(pythonWins))
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
    return play_rps

startGame = rps()
startGame()