#These are few different Dictionary Methods

myDict = {
    "Name" : "Shruti Patel",
    "Hobbies" : ["Reading Books", "Jogging", "Thinking"],
    "Degrees" : {
        "BE" : "Pass",
        "MS" : "Pass",
        "PHD" : "Pursuing"
    },
    "Age" : 32
    
}
print("Type :", type(myDict))
print("Dictionary is :", myDict )
print("Dictionary Keys : ", myDict.keys())
print("List of Dict Keys : ", list(myDict.keys()))
print("List of Dict Values : ", list(myDict.values()))
print("Tuple Pairs : ", myDict.items())
print("Tuple Pairs : ", list(myDict.items()))

print(myDict["Name"])
print(myDict.get("Name"))

#print(myDict["Test"]) # This gives error as there is no Test attribute
print(myDict.get("Test")) 


# Update Dictionary
Dict2 = {
    "Test" : "Pass",
    "Sub" : "Python"
}
myDict.update(Dict2)
print(myDict)

Dict3 = {
    "Name" : "Akshay Sir"
}
myDict.update(Dict3)
print(myDict)
