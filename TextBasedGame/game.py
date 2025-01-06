
def game():
    def Manor():
         print("You approach the gates. A guard shouts 'State your business here!'")

    def Tavern():
         print("The smell of beer and sounds of music, people talking fills the air!")
         print("A man far off into the corner tries to catch your attetion")
         choice = input("Do you approach this man? Type 'y' for yest 'n' for no")
         if choice == 'y':
              print("you approach the man")
              print("Are you looking for work?")
              print("By the looks of you, you washed up ashore")
              print("I happen to have an opportunity for you. What do you say?")
              choice1 = input("1.Yes, 2. no, 3. Depends")
              if choice1 =="yes":
                   print("A man that doesn't ask questions. I like that.")
              elif choice1 == "No":
                   print("well then suite yourself")
                   return
              elif choice1 == "Depends":
                   print("I guess its only fair. Well I have a job that needs a particular set of skills")
                   print("This job requires somebody ending up dead and I think you fit the role")
                   print("you tense up a bit")
                   print("well of course I don't mean you")
                   print("we'll provide any weapon of your choosing")
             #add in dialog and make it to where you can choose weapon and loops the tavern function somehow with out
             #Except on the second time he no longer is there.

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