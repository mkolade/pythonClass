#DICTIONARIES - very similar to javascript objects

#creating a dict
firstDict = {
    "Name": "Akolade",
    "Class": "Baller"
}
secondDict = dict(Name="Akolade", Class = "Baller")
# print(firstDict)#{'Name': 'Akolade', 'Class': 'Baller'}
# print(secondDict)#{'Name': 'Akolade', 'Class': 'Baller'}

#access dict items 
print(firstDict["Class"])
print(secondDict.get("Class"))

#other methods
#all keys
print(firstDict.keys())#(['Name', 'Class'])
#all values
print(firstDict.values())#dict_values(['Akolade', 'Baller']) 
#all items
print(firstDict.items())#dict_items([('Name', 'Akolade'), ('Class', 'Baller')])

print("Name" in firstDict)#True

#To update a dict
secondDict["Class"] = "Hustler"
secondDict.update({"Name" : "Muhkid", "Style":"On the Look"})
print(secondDict)#{'Name': 'Muhkid', 'Class': 'Hustler', 'Style': 'On the Look'}

#To remove an item
print(secondDict.pop("Style"))#On the Look
print(secondDict.popitem())#returns a tuple -('Class', 'Hustler')

#To delete and clear an item
secondDict["age"] = "Akan"
del secondDict["age"]
print(secondDict)#{'Name': 'Muhkid'}

firstDict.clear()
print(firstDict)#{}

#copying a dict
copy3 = secondDict.copy()
copy4 = dict(secondDict)
# print(copy3)#{'Name': 'Muhkid'}
# print(copy4)#{'Name': 'Muhkid'}