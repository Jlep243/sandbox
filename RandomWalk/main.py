import random
import turtle as t

tim = t.Turtle()

colors = ["blue","red","green","yellow","orange"]
directions = [90,0,180,270]
distance = range(1,100)
t.colormode(255)

def rand_colors():
    r = random.randint(0,250)
    g = random.randint(0,250)
    b = random.randint(0,250)
    random_color = (r,g,b)
    return random_color

def random_walk(num):

    for _ in range(num):
        rand_direction = random.choice(directions)
        tim.speed('fastest')
        tim.pensize(13)
        tim.color(rand_colors())
        tim.setheading(rand_direction) 
        tim.forward(30)
 
random_walk(1000)


screen = Screen()
screen.exitonclick()
