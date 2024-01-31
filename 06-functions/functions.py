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

#Functions with multiple args
def multipleArgs(*args):
    print(args)
    print(type(args))#<class 'tuple'>

multipleArgs("Hello", "Nigga", "Lol")

#proof that args are really tuples - The whole proof thing kinda suck. but you get the idea. Tuples are unchangeable form of lists
# def appendToTuple(*args):
#     someList = list(args)
#     anotherList = list(["Yoo mama mia"])
#     aTuple = tuple((anotherList))
#     backToList = list(aTuple)
#     someList += backToList
#     print( someList, len(someList))
# firstTuple = tuple(('Hello', 'Mother-Fucker'))
# appendToTuple(firstTuple)#[('Hello', 'Mother-Fucker'), 'Yoo mama mia'] 2


#so the idea is that these kwargs thingy are really dicts in disguise
def someKwargs(**kwargs):
    print(kwargs,type(kwargs))
    print(kwargs.popitem())#('first', '13')
    return

someKwargs(first = "13")