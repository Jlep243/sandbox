import turtle as t
import random

win =t.Screen()
t.bgcolor("dark blue")

tim = t.Turtle()
tom = t.Turtle()
timmy = t.Turtle()
tommy = t.Turtle()

racers = [tim,tom,timmy,tommy]

colors = ["red","light blue","black","yellow","pink","purple"]
number_of_colors = 5

def rand_color():
    random_color = colors[random.randint(0,5)]
    return random_color

def racemode():
    i = 0
    for racer in racers:
        racer.shape('turtle')
        racer.penup()
        i+=50
        racer.setpos(0,i)
        racer.color(rand_color()) 

racemode()

t.mainloop() 
