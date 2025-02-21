#import colorgram
import turtle as t
import random
tom = t.Turtle()

t.colormode(255)

colors = [(55, 33, 25), (204, 147, 98), (134, 84, 61), (246, 235, 198), (240, 199, 122), (103, 49, 32), (179, 111, 84), (140, 147, 162), (153, 136, 143), (119, 91, 100), (42, 30, 33), (192, 125, 54), (148, 117, 125), (101, 96, 118), (145, 158, 151), (84, 62, 39), (237, 244, 233), (125, 123, 142), (77, 56, 60), (96, 101, 97), (219, 183, 167), (230, 225, 227), (37, 38, 43), (217, 223, 227), (59, 62, 71), (50, 52, 50), (121, 132, 124), (199, 187, 189), (184, 197, 185), (176, 197, 204)]

def rand_colors():
    random_color = random.choice(colors)
    return random_color

def color_dots():
    i = 0
    y = 50
    while i != 10:
        for num in range(0,11):
            tom.dot(20,rand_colors())
            tom.penup()
            tom.forward(50)
        tom.setposition(0,y)
        y += 50
        i += 1
             
color_dots()
t.exitonclick()
