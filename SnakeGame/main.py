from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

#snake_bits = [(0,0),(-20,0),(-40,0)]
#segments = []


#for segment in snake_bits:
#    new_segment = Turtle('square')
#    new_segment.color('white')
#    new_segment.penup()
#    new_segment.goto(segment)
#    segments.append(new_segment)
#
#
#game_is_on = True
#Snake()

#while game_is_on:
#    screen.update()
#    time.sleep(0.1)
#
#    for seg_num in range(len(segments)-1,0,-1):
#        new_x = segments[seg_num - 1].xcor()
#        new_y = segments[seg_num - 1].ycor()
#        segments[seg_num].goto(new_x,new_y)


screen.mainloop()
