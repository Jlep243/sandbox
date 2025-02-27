from turtle import Screen, Turtle

snake = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("black")

snake_bits = [(0,0), (-20,0), (-40,0)]

for position in snake_bits:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.mainloop()
