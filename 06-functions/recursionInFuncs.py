#defining a recursive function

def firstRecursion(num):
    if num >= 9:
        return num
    myTotal = num + 1
    print(myTotal)
    firstRecursion(num + 1)
    return 

firstRecursion(0)