from art import logo, coffee
from coffee_machine_data import *

RESOURCES = { 'milk': 0, 'water': 0, 'coffee': 0, 'money': 0 }

def show_welcome_message():
    print(coffee)
    print(logo)
    print(f"Welcome to the coffee nest!")


def get_user_order():
    order = input("What would you like? 'c' for Cappuccino, 'e' for Espresso, 'l' for Latte (type ex to exit): ").lower()
    if order == 'c' or order == 'e' or order == 'l':
        return COFFEE_KEY_NAME_MAP[order]
    elif order == 'ex':
        return 'exit'
    print(f"Your input {order} is not valid")
    return get_user_order()


def set_resources(new_resource):
    global RESOURCES
    RESOURCES = new_resource


def add_resource(ingredient, amount):
    current_resources = RESOURCES
    current_resources[ingredient] += amount
    set_resources(current_resources)


def add_resources_to_machine():
    add_resource(WATER, WATER_REFILL_AMOUNT)
    add_resource(MILK, MILK_REFILL_AMOUNT)
    add_resource(COFFEE, COFFEE_REFILL_AMOUNT)


def show_report():
    resources = RESOURCES
    print(f"Coffee: {resources[COFFEE]}, Milk: {resources[MILK]}, Water: {resources[WATER]}, Money: {resources[MONEY]}")


def are_resources_enough(order):
    order_ingredients = MENU[order][INGREDIENTS]
    print(order_ingredients)
    for ingredient in order_ingredients:
        if RESOURCES[ingredient] < order_ingredients[ingredient]:
            print(f"There is not enough {ingredient}. Please refill the machine.")
            return False
    return True


def turn_on_coffee_machine():
    add_resources_to_machine()
    show_welcome_message()
    show_report()
    take_order = True

    while take_order:
        order = get_user_order()
        if order == 'exit':
            print(f"See you next time!")
            take_order = False
        elif not are_resources_enough(order):
            add_resources_to_machine()
        else:
            print("get money")

turn_on_coffee_machine()