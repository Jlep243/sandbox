import turtle as t
import random

win =t.Screen()
t.bgcolor("light blue")

tim = t.Turtle()
tom = t.Turtle()
timmy = t.Turtle()
tommy = t.Turtle()

racers = [tim,tom,timmy,tommy]

colors = ["red","blue","black","yellow","pink","purple"]
number_of_colors = 5

def rand_color():
    random_color = random.choice(colors)
    return random_color

def racemode():
    i = 0
    for racer in racers:
        color = rand_color()
        racer.color(color)
        colors.remove(color)
        racer.shape('turtle')
        racer.penup()
        i+=50
        racer.setpos(0,i)

racemode()

t.mainloop() 
