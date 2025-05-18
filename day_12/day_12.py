# local vs global scope
import math

cars_sold = 10 # global variable

def sell_car():
    cars_sold = 11 # local variable overshadows the global variable
    print(cars_sold) # 11

sell_car()
print(cars_sold) # 10

def start_game():
    def get_players_ready(): # An inner function local to start_game()
        print("Players are ready!")

    get_players_ready()
    print("game started")


start_game()
# get_players_ready() can't be called as its only local to start_game()

sold_price = 15.50

def calculate_discount():
    if sold_price > 10:
        discount_percent = 5

    print(f"You get {discount_percent}% discount")

calculate_discount()

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    sqrt_num = int(math.sqrt(num)) + 1
    print(f"looping till {sqrt_num}")
    for i in range(5, sqrt_num, 6):
        print(f"checking {i} or {i+2} is a divisor for {num}")
        if num % i == 0 or num % (i+2) == 0:
            return False

    return True

n = 523
print(f"{n} is a prime number: {is_prime(n)}")

sold_cars = 10

# bad practice
def sell_car():
    global sold_cars
    sold_cars += 1

sell_car()
print(sold_cars)

# good practice
def increment_sold_cars():
    global sold_cars
    sold_cars += 1

def sell_car_good():
    increment_sold_cars()
    print("a new car is sold")

sell_car_good()
print(sold_cars)

# global constants
BASE_URL = "https://example.com"
PI = 3.14159





