def parentFunction(name, coins):
    #coins = 3
    def removeCoins():
        nonlocal coins
        coins -= 1
        if (coins > 1):
            print("\n" + name + " has " + str(coins) + " coins left")
        elif (coins == 1):
            print("\n" + name + " has just " + str(coins) + " coin left")
        else:
            print("\n" + "Sorry " + name + ", you're out of coins")

    return removeCoins

timmy = parentFunction("Timmy", 3)
jenny = parentFunction("Jenny", 5)
timmy()#Timmy has 2 coins left
timmy()#Timmy has just 1 coin 
timmy()#Sorry Timmy, you're out of coins 
timmy()#Sorry Timmy, you're out of coins

jenny()#Jenny has 4 coins left
