import turtle as t
import random

win =t.Screen()
t.bgcolor("dark blue")

tim = t.Turtle()
tom = t.Turtle()
timmy = t.Turtle()
tommy = t.Turtle()

racers = [tim,tom,timmy,tommy]

def rand_color():
    colors = ["red","blue","black","yellow","pink","purple"]
    for color in colors:
        return color


def racemode():
    i = 0
    for racer in racers:
        racer.penup()
        color = rand_color()
        i+=50
        racer.setpos(0,i)
        racer.color(color) 


racemode()

t.mainloop() 
