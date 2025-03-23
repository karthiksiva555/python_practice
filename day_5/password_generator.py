import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many character would you like? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like?"))

password_list = []

for num in range(0, num_letters):
    password_list.append(random.choice(letters))

for num in range(0, num_numbers):
    password_list.append(random.choice(numbers))

for num in range(0, num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list) # shuffle to make password more random
password = ''.join(password_list)
print(f"Your password is: {password}")
