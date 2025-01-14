"""In this section we go over Functions that we can build but there are also built in functions"""
#Like so -----> https://docs.python.org/3/library/functions.html

#all functions work the same. They all have a name and parentheses 
#like so --> print(), len(),

#We could also make our own function. 
#We start with def my_function_name():

"""def my_function():
    print("hello")
    print("bye")"""

#Though when we make a function. It will not run by its own. 
#We need to call the function like we do with print function or the length function

"""my_function() """

#functions are blocks of reusable code

"""def happy_birthday():
    print("Happy birthday to you!")
    print("you are old!")
    print("Happy birthday to you!")"""

#This function can be called like so happy_birthday()

"""happy_birthday() #we can execute this code multiple times and get the same thing each time
happy_birthday()
happy_birthday()
"""
#We can also send data to functions. These are called arguments like so>
"""def Happy_Birthday(name, age):
    print(f"happy birthday to {name}")
    print("you are {age} years old") 
    print(f"happy birthday to you")"""

#Now we can pass it names and if we want age too
"""Happy_Birthday("joe",32)"""

#The order of the parameters do matter
"""def Happy_Birthday(age, name):
    print(f"happy birthday to {name}")
    print("you are {age} years old") 
    print(f"happy birthday to you")

Happy_Birthday("nick",80) #Which you can test here"""

#return is a statement used to end a function and can also send a result back to caller

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("seth", "rogen")

print(full_name)