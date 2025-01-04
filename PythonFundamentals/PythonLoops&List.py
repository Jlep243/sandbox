#For Loop

fruits = ["Apple","Peach","Pear"] #We have a list of fruits. Lists store multiple items in a single variable. They are also indexed and start at 0
x = 0

for fruit in fruits:
    """This is a For Loop and this for loop will print each item in the fruits list. It will also increment the variable of 
    x by one each time it loops"""
    print(fruit)
    x += 1 
    print(x)