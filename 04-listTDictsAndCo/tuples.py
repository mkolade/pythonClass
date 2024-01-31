#TUPLE - unchangeable form of lists

#To create a tuple
firstTuple = tuple(('Hello', 'Mother-Fucker'))
secondTuple = tuple(('My', 'Name', 'Is'))
print(secondTuple)#('My', 'Name', 'Is')
#print(type(secondTuple))#<class 'tuple'>

#To change the contents of a tuple, you gotta get creative
tuListOne = list(firstTuple)
tuListTwo = list(secondTuple)

tuListOne += tuListTwo
print(tuListOne)
myPass = input("Enter Code to reveal NAME~: \n")
if myPass == '3':
    tuListOne.append("Yo mama's titties")
    myAppendedTuple = tuple(tuListOne)
    print(myAppendedTuple)
else :
    print("Wrong code")

#methods to run on a tuple
print(firstTuple.count("Hello"))#1
print(firstTuple)