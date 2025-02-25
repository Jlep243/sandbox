import turtle as t
import random

win =t.Screen()
t.bgcolor("light blue")
win.screensize(100,100)

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
    bets = win.textinput("Place your bets!",f" Which turtle do you think will win? \n Tim: {tim.pencolor()}, Tom: {tom.pencolor()}, Timmy: {timmy.pencolor()}, Tommy: {tommy.pencolor()}")
    while tim.ycor()!=100 or tom.ycor()!=100 or tommy.ycor()!=100 or timmy.ycor()!=100:
        for racer in racers:
            racer.forward(random.choice(speed)) 
            return racer
racesetup()
racestart()
t.mainloop() 
