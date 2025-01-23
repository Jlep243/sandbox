from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import menu
MENU = menu.Menu.get_items()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

choice = input("What would you like? {MENU} ")

real_choice = choice.lower()

if real_choice == 'report':
    #reports money in machine
    money_machine.report()

    #reports resources of machine
    coffee_maker.report()
# elif real_choice == 