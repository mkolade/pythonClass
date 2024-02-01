name = "dave"
 
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
    color = "Red"
    def printStuff(name):
        print(name, color)
    printStuff("Atolagbe")# Atolagbe Red
anotherFunc()