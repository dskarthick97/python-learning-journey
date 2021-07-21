from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker_ = CoffeeMaker()
money_machine_ = MoneyMachine()


def process(user_choice):
    drink = menu.find_drink(user_choice)
    is_resource_enough = coffee_maker_.is_resource_sufficient(drink)
    if is_resource_enough:
        payment = money_machine_.make_payment(drink.cost)
        if payment:
            coffee_maker_.make_coffee(drink)


machine_state = True
while machine_state:
    user_choice = input(f"What would you like? {menu.get_items()}: ")

    if user_choice == "report":
        coffee_maker_.report()
        money_machine_.report()
    elif user_choice == "off":
        machine_state = False
    else:
        process(user_choice)
