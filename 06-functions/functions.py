#FUNCTIONS - Reusable blocks of code

def helloWorld():
    print("Hello World!")

helloWorld()

def sum(a=0,b=0):
    if(type(a) is not int or type(b) is not int):
        return
    return(a + b)

print(sum("aa",3))#None
print(sum())#0
total = sum(2,3)
print(total)#5