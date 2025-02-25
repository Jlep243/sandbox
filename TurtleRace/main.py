import turtle as t
import random

win =t.Screen()
t.bgcolor("light blue")

tim = t.Turtle()
tom = t.Turtle()
timmy = t.Turtle()
tommy = t.Turtle()

racers = [tim,tom,timmy,tommy]
speed = [5,10,15,20,25,30,35]
colors = ["red","blue","black","yellow","pink","purple"]
number_of_colors = 5

def rand_color():
    random_color = random.choice(colors)
    return random_color

def racesetup():
    i = 0
    for racer in racers:
        color = rand_color()
        racer.color(color)
        colors.remove(color)

        racer.shape('turtle')
        racer.penup()
        i+=50
        racer.setpos(0,i)

def racestart():
    win.textinput("Place your bets!",f" Which turtle do you think will win? \n Tim: {tim.color()[0]}, Tom: {tom.color()[1]}, Timmy: {timmy.color()[0]}, Tommy: {tommy.color()[0]}")
    for racer in racers:
        racer.forward(random.choice(speed))

racesetup()
racestart()
t.mainloop() 
