#For Loop

fruits = ["Apple","Peach","Pear"] #We have a list of fruits. Lists store multiple items in a single variable. They are also indexed and start at 0
x = 0

# for fruit in fruits:
#     """This is a For Loop and this for loop will print each item in the fruits list. It will also increment the variable of 
#     x by one each time it loops"""
#     print(fruit)
#     x += 1 
#     print(x)


# student_scores = [10,24,86,199,120,89,185,65,78,59,150] #Here we have a list of students scores
# x = 0 #The x will eventually have the max score with the for loop below
# for student in student_scores:#For the variable student it will equal student_scores
#     if student > x: #If student is bigger than x than x will be equal to student.
#         x = student
# print(x) #Once the student score that is the highest is found and compared to all the numbers in the list it will be printed out

"""In this for loop we go through all the numbers within the range"""
range(1,11)

total = 0

for number in range(1,101): #we go through each number in the range and range will count from the first to the last number.
                           #Though it doesn't reach the number ten in this case unless we change it to eleven
    total += number
print(total)