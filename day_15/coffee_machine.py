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
    add_resource(WATER, REFILL_AMOUNT[WATER])
    add_resource(MILK, REFILL_AMOUNT[MILK])
    add_resource(COFFEE, REFILL_AMOUNT[COFFEE])


def add_resources_for_order(order):
    order_ingredients = MENU[order][INGREDIENTS]
    for ingredient in order_ingredients:
        if RESOURCES[ingredient] < order_ingredients[ingredient]:
            print(f"Refilling {ingredient}...")
            add_resource(ingredient, REFILL_AMOUNT[ingredient])

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


def add_money_to_till(money):
    add_resource(MONEY, money)


def process_money(order):
    order_price = MENU[order][PRICE]
    print(f"The price of {order} is ${order_price}.")
    total_money = get_money_from_user(0.0)
    print(f"The total money received: {total_money}")

    while total_money < order_price:
        print(f"You are {round(order_price - total_money, 2)} short to buy {order}. Insert more coins.")
        total_money = get_money_from_user(total_money)

    if total_money > order_price:
        print(f"Please collect your change: ${round(total_money - order_price, 2)}")

    add_money_to_till(order_price)

def update_resources(order):
    order_ingredients = MENU[order][INGREDIENTS]
    for ingredient in order_ingredients:
        add_resource(ingredient, -order_ingredients[ingredient])


def get_order():
    order = get_user_order()

    while not are_resources_enough(order):
        add_resources_for_order(order)

    process_money(order)
    update_resources(order)
    print(f"Enjoy Your {order}!")


def turn_on_coffee_machine():
    add_resources_to_machine()
    show_welcome_message()
    take_order = True

    while take_order:
        choice = input("Please enter your choice: o for order, r for report: ").lower()
        if choice == "off":
            take_order = False
            print("See you next time!")
        elif choice == "r":
            show_report()
        elif choice == "o":
            get_order()
        else:
            print(f"Your input {choice} is not valid. Please try again.")

turn_on_coffee_machine()