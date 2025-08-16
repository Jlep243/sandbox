from turtle import Screen, Turtle
import time


class Snake:
    
    snake_bits = [(0,0),(-20,0),(-40,0)]
    
   def __init__(self): 
        self.create_snake()
        self.segments = []

    def create_snake(self):
        for segment in snake_bits:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(segment)
            segments.append(new_segment)

    screen = Screen()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
    
        for seg_num in range(len(segments)-1,0,-1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x,new_y) 

