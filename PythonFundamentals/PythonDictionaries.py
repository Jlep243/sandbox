#Dictionaries are a what is called a {key:value} pairs
#   They are ordered and changeable. No duplicates.

#example     key       value
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals["India"]) #This would get us new delhi because dictionaries are identified by it's key

# Wipe an existing dictionary

capitals = {} #This would rewrite the dictionary
print(capitals)
