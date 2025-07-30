class MenuItem:
    def __init__(self, name, code, milk, water, coffee, cost):
        self.name = name
        self.cost = cost
        self.code = code
        self.ingredients = {
            "milk": milk,
            "water": water,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", "e", 0, 50, 18, 1.5),
            MenuItem("cappuccino", "c", 100, 250, 24, 3.0),
            MenuItem("latte", "l", 150, 200, 24, 2.5)
        ]


    def get_items(self):
        items = ""

        for menu_item in self.menu:
            items += f"{menu_item.code} for {menu_item.name}, "

        items = items.rstrip(", ")

        return items


    def is_valid_menu_code(self, code):
        exits = any(menu_item.code == code for menu_item in self.menu)
        return exits

    def get_menu_item_by_code(self, code):
        return next((item for item in self.menu if item.code == code), None)