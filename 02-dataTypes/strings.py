#Literal assignments
first  = "Dave"
last = "Gray"

# print(type(first))#<class 'str'>
# print(type(first) == "str")#true
# print(isinstance(first, str))#true
#   #Constructor functions
# pizza = str("Pepperoni")
# print(type(pizza))#<class 'str'>
# print(type(pizza) == "str")#true
# print(isinstance(pizza, str))#true

#Concatenation
fullName = first + " " + last
print(fullName) #Dave Gray
fullName += "!"
#print(fullName) #Dave Gray!
#print(fullName + 1980) #TypeError: can only concatenate str (not "int") to str

#Casting to string
yearOfBirth = str(1980)
#print(type(yearOfBirth))#<class 'str'>
#print("I Love " + fullName + " from the " + yearOfBirth + "s.")#I Love Dave Gray! from the 1980s.

#Multiple line statements
multiLine = """
Hello Fag.

How are you feeling today?

            Just checking on you asshole.
"""
#print(multiLine)

#Escaping special characters
sentence = 'I\'m back home.\tHey!\n\nWhere\'s my shit at\\located'
#print(sentence)

#STRING METHODS

# print(first)#Dave
# print(first.lower()) if first.isupper() else print(first.upper())#DAVE
# print(first)#Dave
multiLine = multiLine.title()
#print(multiLine)
#print(multiLine.replace("Asshole","Faggot"))
multiLine += "                   "
multiLine = "                   " + multiLine
# print(len(multiLine.strip()))#81  Gets rid of white spaces
# print(len(multiLine.lstrip()))#101
# print(len(multiLine.rstrip()))#101

#STRING INDEX
print(first[1])# a
print(first[-1])# e
print(first[0:-1])# Dav
print(first[0:] + "\n")# Dave

#Methods that return BOOLEAN
print(first.startswith("D")) # True
print(first.endswith("D")) # False

#More on BOOLEAN
myBool = True
myFalse = bool(False)
print(type(myBool)) #<class 'bool'>
print(isinstance(myFalse,bool)) # True