from day_16.coffee_machine_oop.menu import Menu
from day_16.coffee_machine_oop.money_machine import MoneyMachine
from day_16.coffee_machine_oop.resources import Resources
from art import logo, coffee

class CoffeeMachine:


    def __init__(self):
        self._on = False
        self.menu = Menu()
        self.resources = Resources()
        self.money_machine = MoneyMachine()


    def turn_machine_on(self):
        self._on = True


    def turn_machine_off(self):
        self._on = False


    def is_machine_on(self):
        return self._on


    @staticmethod
    def show_welcome():
        print(coffee)
        print(logo)


    def start_machine(self):
        try:
            self.turn_machine_on()
            self.show_welcome()
            self.resources.refill_all_resources()

            while self.is_machine_on():
                choice = self.get_user_choice()

                if any(choice == menu_item.code for menu_item in self.menu.menu):
                    self.make_order(choice)
                elif choice == "r":
                    self.show_report(self.resources, self.money_machine)
                elif choice == "off":
                    print("Turning the machine off... See you again!")
                    self.turn_machine_off()

        except Exception as ex:
            print(ex)


    def make_order(self, drink_code):
        drink = self.menu.get_menu_item_by_code(drink_code)

        if not self.resources.are_resources_enough(drink):
            print(f"The resources are not enough to make {drink.name}")
            self.resources.refill_resources(drink)

        print(f"Please insert ${drink.cost} to complete the order for {drink.name}.")
        self.money_machine.process_money(drink.name, drink.cost)
        self.resources.update_resources_after_order(drink)
        print(f"Making {drink.name}... Enjoy your drink!")


    def get_user_choice(self):
        menu_items = self.menu.get_items()
        choice = input(f"Please enter your choice: {menu_items}, r for report: ").lower()

        if self.menu.is_valid_menu_code(choice) or choice == "r" or choice == "off":
            return choice
        else:
            print(f"Your choice {choice} is not a valid input, please choose again.")
            return self.get_user_choice()


    @staticmethod
    def show_report(resources, money_machine):
        resources.show_report()
        money_machine.show_total_amount()


coffee_machine = CoffeeMachine()
coffee_machine.start_machine()