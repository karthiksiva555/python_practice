class MenuItem:
    def __init__(self, name, milk, water, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "milk": milk,
            "water": water,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 0, 50, 18, 1.5),
            MenuItem("cappuccino", 100, 250, 24, 3.0),
            MenuItem("latte", 150, 200, 24, 2.5)
        ]


    def get_items(self):
        items = ""

        for menuItem in self.menu:
            items += f"{menuItem.name}/"

        return items