from art import logo, coffee
from coffee_machine_data import *

RESOURCES = { 'milk': 0, 'water': 0, 'coffee': 0, 'money': 0 }

def show_welcome_message():
    print(coffee)
    print(logo)
    print(f"Welcome to the coffee nest!")


def get_user_order():
    order = input("What would you like? 'c' for Cappuccino, 'e' for Espresso, 'l' for Latte: ").lower()
    if order == 'c' or order == 'e' or order == 'l':
        return COFFEE_KEY_NAME_MAP[order]
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


def get_money_from_user(seed_money):
    if seed_money > 0:
        print(f"Current total: ${seed_money}")
    nickels = int(input("Enter the number if Nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    dollars = int(input("Enter the number of dollars: "))
    total_money = seed_money + dollars + (quarters / 4) + (dimes / 10) + (nickels / 20)
    return round(total_money, 2)


def process_money(order):
    order_price = MENU[order][PRICE]
    print(f"The price of {order} is ${order_price}.")
    total_money = get_money_from_user(0.0)

    while total_money < order_price:
        print(f"You are {round(order_price - total_money, 2)} short to buy {order}. Insert more coins.")
        total_money = get_money_from_user(total_money)

    if total_money > order_price:
        print(f"Please collect your change: ${round(total_money - order_price, 2)}")


def get_order():
    order = get_user_order()
    if not are_resources_enough(order):
        add_resources_to_machine()
    else:
        process_money(order)
        print(f"Enjoy Your {order}!")


def turn_on_coffee_machine():
    add_resources_to_machine()
    show_welcome_message()
    show_report()
    take_order = True

    while take_order:
        get_order()
        take_order = input("Continue with next order? (y for Yes, n for no): ").lower() == 'y'
        if not take_order:
            print("See you next time!")

turn_on_coffee_machine()