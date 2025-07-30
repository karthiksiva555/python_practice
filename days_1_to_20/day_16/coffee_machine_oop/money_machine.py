class MoneyMachine:
    def __init__(self):
        self.total_amount = 0.0


    def show_total_amount(self):
        print(f"The total amount collected: {self.total_amount}.")


    @staticmethod
    def get_money_from_user(seed_money):
        if seed_money > 0:
            print(f"Current total: ${seed_money}")
        nickels = int(input("Enter the number if Nickels: "))
        dimes = int(input("Enter the number of dimes: "))
        quarters = int(input("Enter the number of quarters: "))
        dollars = int(input("Enter the number of dollars: "))
        total_money = seed_money + dollars + (quarters / 4) + (dimes / 10) + (nickels / 20)
        return round(total_money, 2)

    def process_money(self, order_name, order_price):
        total_money = self.get_money_from_user(0.0)
        print(f"The total money received: ${total_money}")

        while total_money < order_price:
            print(f"You are {round(order_price - total_money, 2)} short to buy {order_name}. Insert more coins.")
            total_money = self.get_money_from_user(total_money)

        if total_money > order_price:
            print(f"Please collect your change: ${round(total_money - order_price, 2)}")

        self.add_money_to_till(order_price)

    def add_money_to_till(self, money):
        self.total_amount += money