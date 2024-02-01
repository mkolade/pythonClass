name = "dave"
count = 3

# def printStuff(name):
#     color = "Red"
#     print(name)#Akolade
#     print(color)#Red

# #print(color)#NameError: name 'color' is not defined
# printStuff("Akolade")

# def anotherFunc():
#     printStuff("Atolagbe")# Atolagbe Red
# anotherFunc()

#Nested function
def anotherFunc():
    color = "Blue"
    #count += 2# UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    global count
    count += 2
    print(name)#dave
    print(count)#5
    def printStuff(name):
        nonlocal color
        color = "orange"
        print(name, color)
    printStuff("Atolagbe")# Atolagbe orange
anotherFunc()