#F-Strings
name = "Dave"
coins = 3

print("\n" + name + " has " + str(coins) + " coin left")#Dave has 3 coin left

message = "\n%s has %s coins left"%(name,coins)#Dave has 3 coin left
print(message)