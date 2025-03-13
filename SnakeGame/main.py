from turtle import Screen, Turtle
turtle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake_segments = [(0,0),(-20,0),(-40,0)]
segments = []

for i in snake_segments:
    new_segment = Turtle("square")
    new_segment.penup() 
    new_segment.color("white")
    new_segment.setpos(i)
    segments.append(new_segment) 


while True:
    for i in segments: 
        screen.update()
        i.forward(1)    
    
screen.mainloop()

