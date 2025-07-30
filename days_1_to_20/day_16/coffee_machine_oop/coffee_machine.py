from days_1_to_20.day_16.coffee_machine_oop.menu import Menu
from days_1_to_20.day_16.coffee_machine_oop.money_machine import MoneyMachine
from days_1_to_20.day_16.coffee_machine_oop.resources import Resources
from art import logo, coffee_mug

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
        print(coffee_mug)
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


    def make_order(self, coffee_code):
        coffee = self.menu.get_menu_item_by_code(coffee_code)

        if not self.resources.are_resources_enough(coffee):
            print(f"The resources are not enough to make {coffee.name}")
            self.resources.refill_resources(coffee)

        print(f"Please insert ${coffee.cost} to complete the order for {coffee.name}.")
        self.money_machine.process_money(coffee.name, coffee.cost)
        self.resources.update_resources_after_order(coffee)
        print(f"Here is your {coffee.name}. Enjoy!")


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