import turtle as t

tom = t.Turtle()

def right():
    tom.pensize(5)
    tom.forward(1)

def left():
    tom.pensize(5)
    tom.left(1)

t.delay(0)

t.speed("fastest")
t.onkey(left,"a")
t.onkey(right,"d")
t.listen()



t.done()
