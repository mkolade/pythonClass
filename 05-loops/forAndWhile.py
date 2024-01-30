#WHILE loop
value = 0
while value < 10:
    if (value == 5):
        break
    #print(value)#0 1 2 3 4
    value += 1
    
value = 0
while value < 10:
    value += 1
    if(value == 5):
        continue
    #print(value)#1 2 3 4 6 7 8 9 10
else:
    print("Shut tf up nigga " + str(value))

#FOR Loop
names = ["mk", "ak", "sk", "az"]
for name in names:
    if(name == "sk"):
        break
    #print(name)#mk ak

for name in names:
    if(name == "sk"):
        continue
    #print(name)#mk ak az

#RANGE
# for x in range(4):
#     print(x)#0 1 2 3
    
# for y in range(1,5):
#     print(y)# 1 2 3 4
    
# for(x) in range(0,25,5):
#     print(x)#0 5 10 15 20
# else:
#     print("Whew! that's over now")
    
#Nested loops
names = ["Moni", "Teni", "Tony"]
actions = ["Eats", "Sleeps", "Drinks"]
puncs = [".", ","]

for name in names:
    for action in actions:
        for punc in puncs:
            print(name + " " + action + punc)

#Result of nested loop -
# Moni Eats.
# Moni Eats,
# Moni Sleeps.
# Moni Sleeps,
# Moni Drinks.
# Moni Drinks,
# Teni Eats.
# Teni Eats,
# Teni Sleeps.
# Teni Sleeps,
# Teni Drinks.
# Teni Drinks,
# Tony Eats.
# Tony Eats,
# Tony Sleeps.
# Tony Sleeps,
# Tony Drinks.
# Tony Drinks,