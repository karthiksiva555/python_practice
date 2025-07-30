from days_1_to_20.day_15.coffee_machine_data import REFILL_AMOUNT
from days_1_to_20.day_16.coffee_machine_oop.menu import MenuItem


class Resources:
    REFILL_AMOUNT = {'water': 1000, 'milk': 500, 'coffee': 200}


    def __init__(self):
        self.water = 0
        self.milk = 0
        self.coffee = 0


    def refill_water(self):
        print("Refilling water...")
        self.water += REFILL_AMOUNT['water']


    def refill_milk(self):
        print("Refilling milk...")
        self.milk += REFILL_AMOUNT['milk']


    def refill_coffee(self):
        print("Refilling coffee...")
        self.coffee += REFILL_AMOUNT['coffee']


    def refill_all_resources(self):
        self.refill_water()
        self.refill_milk()
        self.refill_coffee()


    def show_report(self):
        print(f"Coffee: {self.coffee}g, Milk: {self.milk}ml, Water: {self.water}ml.")


    def are_resources_enough(self, drink: MenuItem):
        return self.water >= drink.ingredients['water'] and self.coffee >= drink.ingredients['coffee'] and self.milk >= drink.ingredients['milk']


    def refill_resources(self, drink: MenuItem):
        """This method takes a menu item as input and refills the required resource(s)"""
        if self.water < drink.ingredients['water']:
            self.refill_water()

        if self.coffee < drink.ingredients['coffee']:
            self.refill_coffee()

        if self.milk < drink.ingredients['milk']:
            self.refill_milk()


    def update_resources_after_order(self, drink: MenuItem):
        print(f"Updating resources after order {drink.name}...")
        self.water -= drink.ingredients['water']
        self.milk -= drink.ingredients['milk']
        self.coffee -= drink.ingredients['coffee']
