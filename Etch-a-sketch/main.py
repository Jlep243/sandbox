import turtle as t
win =t.Screen()

tom = t.Turtle()
tom.fillcolor("red")
tom.speed("fastest")
tom.screen.delay(0)
tom.pensize(5)


def right():
    tom.speed(0)
    tom.forward(5)
    
def left():
    tom.back(5)
    
def turn_up():
    tom.left(5)

def turn_down():
    tom.right(5)

win.onkeypress(turn_down,"Down")
win.onkeypress(turn_up,"Up")
win.onkey(left,"a")
win.onkey(right,"d")
win.listen()

win.mainloop()
