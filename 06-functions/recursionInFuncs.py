#defining a recursive function

def firstRecursion(num):
    myTotal = num + 1
    if num >= 9:
        return ("(" + str(num) + " " + str(myTotal) + (')'))
    print("(" + str(num) + " " + str(myTotal) + (')'))#(0 1) (1 2) (2 3) (3 4) (4 5) (5 6) (6 7) (7 8) (8 9)
    return firstRecursion(num + 1)

#To get 9 and 10, yea i know i bungled things up a bit
get9and10 = firstRecursion(0)
print(get9and10)