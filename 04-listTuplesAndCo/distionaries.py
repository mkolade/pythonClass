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