#Coffee machine project
from menu import MENU
from menu import resources

#processes the transaction
def transaction(choice_lower):
    #first implementation of function
    print(f"Please insert coins. That will be ${MENU[choice_lower]["cost"]}")
    #We need to figure out how to add these and give back the change
    #as well as give the coffee
    quarters = input("how many quarters?") 
    dimes = input("how many dimes?") 
    nickels = input("how many nickels?") 
    pennies = input("how many pennies?") 
    coffee_type = choice_lower
    #checks for the right amount of money and gives change
    total = int(quarters)*0.25 + int(dimes)*0.10 + int(nickels)*0.05 + int(pennies)*0.01
    if total == MENU[choice_lower]["cost"] or total > MENU[choice_lower]["cost"]:
        change = total - MENU[choice_lower]["cost"]
        print(f"Here is your change: ${change}")
        print("Enjoy your drink")
        resource(coffee_type)
    elif total != MENU[choice_lower]["cost"]:
        print("Sorry you don't have enough money. Money refunded") 


#calculates the resources
def resource(choice_lower):
    #Resources needed to make the drink chosen
    water_needed = MENU[choice_lower]["ingredients"]["water"]
    milk_needed = MENU[choice_lower]["ingredients"]["milk"]
    coffee_needed = MENU[choice_lower]["ingredients"]["coffee"]

    #Resources from the machine
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    #calculates resources

    available_water = water - water_needed
    available_milk = milk - milk_needed
    available_coffee = coffee - coffee_needed

    resources["water"] = available_water
    resources["milk"] = available_milk
    resources["coffee"] = available_coffee

#Loops the function to select coffee
while 0 != 1:
#function for picking coffee
    def coffee_choices():
        choice = input("Select a coffee: Espresso|Latte|Cappuccino \n")
        choice_lower = choice.lower()

        #If the choice is report it will return the resources of the machine that are available
        if choice_lower == 'report':
            print(f"water:{resources["water"]}ml")
            print(f"milk: {resources["milk"]}ml")
            print(f"coffee: {resources["coffee"]}g")
        #if the choice is a type of coffee it will then charge
        # elif choice_lower in {"espresso","latte","cappuccino"}:
        #     transaction(choice_lower)
        # elif resources["water"] <= 0 or resources["milk"] <= 0 or resources["coffee"] <= 0:
        #     print(f"Sorry, there isn't enough")
# if resources["milk"] == 0:
#     print(f"Sorry there isn't enough {resources["milk"]}")
# if resources["coffee"] == 0:
#     print(f"sorry the isn't enough {resources["coffee"]}")


coffee_choices()