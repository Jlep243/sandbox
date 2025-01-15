#Coffee machine project
from menu import MENU
from menu import resources

def transaction(choice_lower):
    #first implementation of function
    print(f"Please insert coins. That will be ${MENU[choice_lower]["cost"]}")
    #We need to figure out how to add these and give back the change
    #as well as give the coffee
    quarters = input("how many quarters?")
    dimes = input("how many dimes?") 
    nickels = input("how many nickels?")
    pennies = input("how many pennies?")
    
    
    

def resource(choice_lower):
    #Resources needed to make the drink chosen
    water_needed = MENU[choice_lower]["ingredients"]["water"]
    milk_needed = MENU[choice_lower]["ingredients"]["milk"]
    coffee_needed = MENU[choice_lower]["ingredients"]["coffee"]
    #Resources from the machine
    water = MENU[resource]["water"]
    milk = MENU[resource]["milk"]
    coffee = MENU[resource]["coffee"]
    #calculates resources
    water - water_needed
    milk - milk_needed
    coffee - coffee_needed

while resources["water"] > 0:
#function for picking coffee
    def coffee_choices():
        choice = input("Select a coffee: Espresso|Latte|Cappuccino \n")
        choice_lower = choice.lower()

        #If the choice is report it will return the resources of the machine that are available
        if choice_lower == 'report':
            print(f"water:{resources["water"]}")
            print(f"milk: {resources["milk"]}")
            print(f"coffee: {resources["coffee"]}")
        #if the choice is a type of coffee it will then charge
        elif choice_lower in {"espresso","latte","cappuccino"}:
            transaction(choice_lower)

    coffee_choices()
