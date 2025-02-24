import turtle as t
import random

t.colormode(255)

def color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r, g, b)
    return rand_color

def square(loop):
    t.pensize(4)
    t.pencolor("red")
    for _ in range(loop):
        for _ in range(4):
            degrees = 360/4
            t.right(degrees)
            t.forward(100)

#def circle():
    #t.pensize(5)
    #t.pencolor('blue')
    #for _ in range(360):
        #t.right(1)
        #t.forward(1)

t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(color())
        t.circle(100)
        current_heading = t.heading()
        t.setheading(current_heading + size_of_gap)

draw_spirograph(4)

t.exitonclick()




