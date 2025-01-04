
def game():
    def Manor():
         print("You approach the gates. A guard shouts 'State your business here!'")
    def Tavern():
         print("The smell of beer and sounds of music, people talking fills the air!")
    def cathedral():
            print("you walk into the cathedral and hear the sounds of music. A chant. The words are foreign but sound peaceful.\n")

    def city_center():#This is where the player decides to go
        #Beginning of the game
        print("You wake up to the blue of the sky and feel the warmth of the grainy sands under you")
        print("You sit up and see a beach ahead of you.")
        travel_direction = input("you look around you and see a trail that goes north and another that goes east\n")

        if travel_direction == "north":
            #add image of city here
            print("you arrive at a town and see that there is \n")
            print("pick a number")
            city_choice = input("""There are multiple buildings that you can go to.\n 1.Cathedral \n 2.Tavern \n 3.Manor\n""")
            if city_choice == "1":
                cathedral()
            elif city_choice == "2":
                Tavern()
            elif city_choice == "3":
                Manor()
            return
        elif travel_direction == "south":
            print("you arrive at a small tribe village \n")
            print("pick a number")
            city_choice = input("""There are places you can visit. \n 1.Village bonfire \n 2. Ritual hut \n 3.Drinking hut \n""")
            return

        

    city_center()

# if city_choice == "1":
#     cathedral(city_choice)
# else:
#     pass

game()