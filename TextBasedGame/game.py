def game():
    print("You wake up to the blue of the sky and feel the warmth and grainy sands under you")
    print("You sit up and see a beach ahead of you.")
    
    travel_direction = input("you look around you and see a trail that goes north and another that goes east")

    if travel_direction == "north":
        print("you arrive at a town and see that there is \n")
        print("""There are multiple buildings that you can go to.\n 1.Cathedral \n 2.Tavern \n 3.""")
    elif travel_direction == "south":
        print("you arrive at a small tribe village \n")
        print("""There are places you can visit. \n 1.Village bonfire \n 2. Ritual hut \n 3.Drinking hut""")