# Without list comprehension
numbers = [1, 2, 3]
new_numbers = []
for item in numbers:
    new_item = item + 1
    new_numbers.append(new_item)
print(new_numbers) # [2, 3, 4]

# with list comprehension
new_nums = [item + 1 for item in numbers]
print(new_nums) # [2, 3, 4]

# list comprehension with strings
name = "Karthik"
name_copy = [letter for letter in name]
print(name_copy) # ['K', 'a', 'r', 't', 'h', 'i', 'k']

# list comprehension with range
doubled_list = [n * 2 for n in range(1, 5)]
print(doubled_list) # [2, 4, 6, 8]

# Conditional list comprehension
odd_nums = [num for num in range(1, 10) if num % 2 != 0]
print(odd_nums) # [1, 3, 5, 7, 9]

names = ["Siva", "Karthik", "Dave", "Navi", "Aaradhya", "Vaishnavi"]
short_names = [name for name in names if len(name) < 5]
print(short_names) # ['Siva', 'Dave', 'Navi']

long_names_upper = [name.upper() for name in names if len(name) >= 5]
print(long_names_upper) # ['KARTHIK', 'AARADHYA', 'VAISHNAVI']