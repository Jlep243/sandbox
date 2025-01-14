enemies = 1

def increase_enemies():
    enemies = 2 
    print(f"enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function {enemies}")

#local scope    

def drink_potion():
    potion_strength = 2 
    print(potion_strength)

drink_potion()
print(potion_strength) #notice how potion strength isn't available you can only use it in the function above

#Global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()#notice how the players health is shown regardless of being in the function above

#!!!! Scope doesn't just apply to variable but also applies to functions and other things too.
