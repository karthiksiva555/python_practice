from art import logo, coffee
# fill resources in coffee machine

# prepare coffee data: milk, water, sugar and cost

# count coins and give change

# dispense requested drink and deduct from resources

COFFEE_KEY_NAME_MAP = { 'c': "cappuccino", 'e': "espresso", 'l': "latte" }
RESOURCES = { 'milk': 0, 'water': 0, 'coffee': 0, 'money': 0 }
WATER = 'water'
COFFEE = 'coffee'
MILK = 'milk'
MONEY = 'money'
COFFEE_REFILL_AMOUNT = 300
WATER_REFILL_AMOUNT = 1000
MILK_REFILL_AMOUNT = 500


def show_welcome_message():
    print(coffee)
    print(logo)
    print(f"Welcome to the coffee nest!")


def get_user_order():
    order = input("What would you like? 'c' for Cappuccino, 'e' for Espresso and 'l' for Latte: ").lower()
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

def turn_on_coffee_machine():
    add_resources_to_machine()
    show_welcome_message()
    show_report()
    order = get_user_order()
    print(order)


turn_on_coffee_machine()