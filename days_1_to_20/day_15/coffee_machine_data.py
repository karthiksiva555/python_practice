COFFEE_KEY_NAME_MAP = { 'c': "cappuccino", 'e': "espresso", 'l': "latte" }
WATER = 'water'
COFFEE = 'coffee'
MILK = 'milk'
PRICE = 'price'
MONEY = 'money'
INGREDIENTS = 'ingredients'
REFILL_AMOUNT = { WATER: 1000, MILK: 500, COFFEE: 200}

MENU = {
    "espresso": {
        INGREDIENTS: {
            WATER: 50,
            COFFEE: 18,
        },
        PRICE: 1.5,
    },
    "latte": {
        INGREDIENTS: {
            WATER: 200,
            MILK: 150,
            COFFEE: 24,
        },
        PRICE: 2.5,
    },
    "cappuccino": {
        INGREDIENTS: {
            WATER: 250,
            MILK: 100,
            COFFEE: 24,
        },
        PRICE: 3.0,
    }
}