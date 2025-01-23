#Constructing objects and accessing their attributes and methods
import module
from module import x

print(x)
print(module.b)

from turtle import Turtle, Screen

#object = class: timmy is the object created from the turtle class
timmy = Turtle()
print(timmy)

#Getting attributes from an object
my_screen = Screen()
print(my_screen.canvheight) #The my_screen = object and the attribute = canvheight
#So, the my_screen.canvheight is an example of how we get an attribute from an object

#We can also get hold of Methods from objects like so,
#object = my_screen and method = exitonclick()
my_screen.exitonclick()
