""" Coffee Machine Project """

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUATERS = 0.25
DIMES   = 0.10
NICKELS = 0.05
PENNIES = 0.01

MONEY   = 0.0


# check the resources sufficient?
def are_resources_sufficient(ingredients):
    for key, _ in ingredients.items():
        if resources.get(key) < ingredients.get(key):
            print(f"Sorry there is not enough {key}")
            return False

    return True


# process coins
def process_coins():
    monetary_value = []
    quarters = int(input("How many quarters?: "))
    monetary_value.append(QUATERS * quarters)
    
    dimes    = int(input("How many dimes?: "))
    monetary_value.append(DIMES * dimes)

    nickels  = int(input("How many nickels?: "))
    monetary_value.append(NICKELS * nickels)

    pennies  = int(input("How many pennies?: "))
    monetary_value.append(PENNIES * pennies)

    return sum(monetary_value)


# check transaction successful?
def transaction(cost_of_drink, monetary_value):
    if monetary_value < cost_of_drink:
        return False

    if monetary_value > cost_of_drink:
        global MONEY
        MONEY += cost_of_drink
        
        balance = monetary_value - cost_of_drink
        print(f"Here is ${round(balance, 2)} change.")
        
        return True


# make coffee
def make_coffee(user_chosen_drink):
    drink = MENU.get(user_chosen_drink)
    ingredients = drink.get("ingredients")
    are_resources_enough = are_resources_sufficient(ingredients)
    if are_resources_enough:
        cost_of_drink = drink.get("cost")
        monetary_value = process_coins()
        is_transaction_successful = transaction(cost_of_drink, monetary_value)
        
        if is_transaction_successful:
            for ingredient in ingredients:
                global resources
                resources[ingredient] = resources.get(ingredient) - ingredients.get(ingredient)
            
            print(f"Here is your {user_chosen_drink}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")


if __name__ == '__main__':
    should_continue = True
    while should_continue:
        # Prompt the user asking "What would you like? (espresso/latte/cappuccino): "
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == "report":
            for key, value in resources.items():
                print(f"{key.title()}: {value}")
            print(f"Money: ${MONEY}")
        elif user_choice == "off":
            should_continue = False
        else:
            make_coffee(user_choice)
