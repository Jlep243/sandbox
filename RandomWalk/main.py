import random
from turtle import *

tim = Turtle()

def random_walk():
    tim.pensize(10)
    tim.color("blue")
    tim.forward(1000000)

def square():
    tim.pensize(100)
    tim.color("red")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

#random_walk()
square()
screen = Screen()
screen.exitonclick()
