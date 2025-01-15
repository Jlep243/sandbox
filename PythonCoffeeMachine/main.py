#Coffee machine project
from menu import MENU
from menu import resources

def transaction(choice):
    print(f"Please insert coins. That will be ${MENU[choice]["cost"]}")
    quarters = input("how many quarters?")
    dimes = input("how many dimes?")
    nickels = input("how many nickels?")
    pennies = input("how many pennies?")

def resource(choice):
    #Resources needed to make the drink chosen
    water_needed = MENU[choice]["ingredients"]["water"]
    milk_needed = MENU[choice]["ingredients"]["milk"]
    coffee_needed = MENU[choice]["ingredients"]["coffee"]
    #Resources from the machine
    water = MENU[resource]["water"]
    milk = MENU[resource]["milk"]
    coffee = MENU[resource]["coffee"]
    #calculates resources
    water - water_needed
    milk - milk_needed
    coffee - coffee_needed

#function for picking coffee
def coffee_choices():
    choice = input("Select a coffee: Espresso|Latte|Cappuccino \n")
    choice.lower()
    #If the choice is report it will return the resources of the machine that are available
    if choice == 'report':
        print(f"water:{resources["water"]}")
        print(f"milk: {resources["milk"]}")
        print(f"coffee: {resources["coffee"]}")
    #if the choice is a type of coffee it will then charge
    elif choice in {"espresso","latte","cappuccino"}:
        transaction(choice)

coffee_choices()
