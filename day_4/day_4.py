# Day 4: Randomization and Lists

# Random module
import random

random_number = random.randint(1, 10)
print(random_number) # 1 to 10

# random()
random_float = random.random() # any between 0 and 1.0 excluding 1.0
print(random_float * 10) # any value between 0 and 9.99999

# uniform()
random_float_in_range = random.uniform(1, 10)
print(random_float_in_range) # any float between 1 and 10 including 10

# import a user defined module
import my_module

print(my_module.name)

# Lists
fruits = ["Kiwi", "Apple", "Pear"]
print(fruits) # ['Kiwi', 'Apple', 'Pear']
print(fruits[-1]) # Pear

fruits[1] = "Papaya" # update a list item
fruits.append("Orange") # add new item
print(fruits) # ['Kiwi', 'Papaya', 'Pear', 'Orange']
fruits.extend(["f1", "f2"])
print(fruits) # ['Kiwi', 'Papaya', 'Pear', 'Orange', 'f1', 'f2']

# Index Error
#print(fruits[10])

# Nested List
fruits = ["Kiwi", "Apple", "Pear"]
vegetables = ["Celery", "Spinach", "Chilli"]
grocery_list = [fruits, vegetables]
print(grocery_list)
# [['Kiwi', 'Apple', 'Pear'], ['Celery', 'Spinach', 'Chilli']]