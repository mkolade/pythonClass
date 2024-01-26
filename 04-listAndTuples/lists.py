#LISTS

firstList = ["Mali",33,False]
secondList = ["Mali","Teqiat","Dave"]
emptyList = []

# print("Mali" in firstList)#True
# print(False in emptyList)#False
# print(firstList[2])#False
# print(firstList[-2])#33
# print(secondList[-2])#Teqiat
# print(secondList.index('Dave'))#2
# print(secondList[0:2])#['Mali', 'Teqiat']

secondList.append(44)
#print(secondList)
secondList += "MK"
#print(secondList)
secondList += ["MK"]
#print(secondList)#['Mali', 'Teqiat', 'Dave', 44, 'M', 'K', 'MK']  


firstList.extend("Monkey")
firstList.extend(secondList)
#print(firstList)
print(len(firstList))#16


secondList.insert(2,'mk')
#print(secondList)#['Mali', 'Teqiat', 'mk', 'Dave', 44, 'M', 'K', 'MK'] 

secondList[2:2] = ["YEEE","KAii"]
print(secondList)
secondList[1:4] = ["YEEE","KAii"]
print(secondList)

secondList.remove("Mali")
print(secondList)
print(secondList.pop())#MK
print(secondList.pop(-3))#44
#print(secondList)#['YEEE', 'KAii', 'mk', 'Dave', 'M', 'K']

# del secondList[1:4]
# print(secondList)
# #del secondList
# secondList.clear()
# print(secondList)#[]

secondList[4:4] = ["dave"]
secondList.sort()
#print(secondList)
#To sort all the strings regardless of their case
secondList.sort(key=str.lower)
#print(secondList)#['Dave', 'dave', 'K', 'KAii', 'M', 'mk', 'YEEE']

#The following proceses alter the list itself
nums = [33, 5, 22, 85, 3, 66]
nums.reverse()
print(nums)#[66, 3, 85, 22, 5, 33]

#To sort in descending order
# nums.sort(reverse=True)
# print(nums)#[85, 66, 33, 22, 5, 3]

#The above can also be done without altering thr original
print(sorted(nums,reverse=True))#[66, 3, 85, 22, 5, 33]

#To generate new copies of the List
newCopy = nums.copy()
# print(newCopy)#[66, 3, 85, 22, 5, 33]
listCopy = list(nums)
# print(listCopy)#[66, 3, 85, 22, 5, 33]
dotCopy = nums[:]
# print(dotCopy)#[66, 3, 85, 22, 5, 33]

#To get the type of a list
#print(type(nums))#<class 'list'>

#creating a list with the list constructor
someList = list([12,33,4,567,65])
#print(someList)#[12, 33, 4, 567, 65]