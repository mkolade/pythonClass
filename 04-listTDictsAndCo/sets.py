#Sets - No duplicates allowed

#Creating a set
mySet1 = {1, 2, 3, 3, 4, 5, 5,7}
myOtherSet = set((1, 2, 3, 3, 4, 5, 5,7))
#print(mySet1, type(myOtherSet))#{1, 2, 3, 4, 5, 7} <class 'set'>

#For sets, 1 is considered a dupe of true and 0 a dupe of false
mySet3 = {True,1, 2,3,4,0, False}
#print(mySet3)#{0, True, 2, 3, 4}. True came bfr 1 so it's displayed. Also everything is arranged in ascending order

#checking for a value
print(1 in mySet3)#True
print(len(mySet3))#5

#Adding values to a set
aNum = {8,9}
aNum.add(6)
mySet1.update(aNum)
print(mySet1)#{1, 2, 3, 4, 5, 6, 7, 8, 9}

#Creating a new set from merging two different ones
one = {1, 2, 3}
two = {4, 5, 6}
theNewSet = one.union(two)
print(theNewSet)#{1, 2, 3, 4, 5, 6}

#Keeping only duplicates from 2 sets
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)#{2, 3}

#Keeping all except the duplicates from 2 sets
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)#{1, 4}