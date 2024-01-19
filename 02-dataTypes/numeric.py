import math
#Numeric Data types

#integers
myInt = 80
int2 = int(22)
print(type(myInt))# <class 'int'>
print(isinstance(int2, int), "\n")# True

#float
myFloat = 3.72
float2 = float(2.33)
print(type(myFloat) , "\n")# <class 'float'>

#Complex numbers
compNum = 3 + 7j
print(type(compNum))# <class 'complex'>
print(compNum.real)# 3.0
print(compNum.imag)# 7.0
print(type(compNum.real), "\n")# <class 'float'>

#Built-in functions
print(abs(myFloat))# 3.72
print(abs(myFloat * -2))# 7.44
print(round(myFloat))# 4
print(round(myFloat, 1), "\n")# 3.7
#with math module imported,
print(round(math.pi,3))#3.142
print(math.sqrt(64))# 8.0
print(math.floor(myFloat))#3
print(math.ceil(myFloat), "\n")#4

#casting string to num and vice-versa
myNum = 22
inStr = str(myNum)
print(inStr + "89u89")#string - 2289u89
print(int(inStr) * 2)#integer - 44
