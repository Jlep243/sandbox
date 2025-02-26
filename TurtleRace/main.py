import turtle as t
import random
from tkinter import messagebox

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
        racer.setpos(-200,i)

def racestart():
    race = True
    bets = win.textinput("Place your bets!",f" Which turtle do you think will win? \n {tim.pencolor()},{tom.pencolor()}, {timmy.pencolor()},{tommy.pencolor()}")
    while race:
        for racer in racers:
            print(racer.pos())
            if racer.xcor() > 250:
                winner = racer.pencolor()
                if bets == winner:
                    messagebox.showinfo("Winner is!",f"The winner is {winner} and you win!")
                    return
                elif bets != winner:
                    messagebox.showinfo("Winner is!",f"The winner is {winner} and you lose!") 
                    return
            racer.forward(random.choice(speed))

racesetup()
racestart()
t.mainloop()
