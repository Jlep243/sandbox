#from turtle import Turtle, Screen
from turtle import * #This imports everything from the module
import random

#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("purple")

#for _ in range(50):
    #timmy_the_turtle.forward(10)
    #timmy_the_turtle.penup()
    #timmy_the_turtle.forward(10)
    #timmy_the_turtle.pendown()

tim = Turtle()
tim.penup()
tim.goto(-40,20)
tim.pendown()

list_of_colors = ["FireBrick","MediumPurple","Orange2","DeepSkyBlue2"]


def shapes(start,end):
    for i in range(start,end):
        num_sides = i 
        degrees = 360/num_sides
        rand_color = list_of_colors[random.randint(0,3)]
        for _ in range(num_sides):
            tim.speed('fastest')
            tim.color(rand_color)
            tim.forward(20)
            tim.right(degrees)
    print("done!") 

shapes(1,10)
 

screen = Screen()
screen.mainloop()

