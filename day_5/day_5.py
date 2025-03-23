# Loops
import random

# for with lists
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit) # Apple Banana Cherry

# technically, we don't have to loop through the list to print
print(fruits) # ['Apple', 'Banana', 'Cherry']

numbers = [4, 50, 3, 21, 8, 10]
print(f"Sum of all numbers is: {sum(numbers)}") # 96
print(f"Maximum number in the numbers list is: {max(numbers)}") # 50
reversed_numbers = list(reversed(numbers))
print(reversed_numbers) # [10, 8, 21, 3, 50, 4]
print(sorted(numbers)) # [3, 4, 8, 10, 21, 50]

scores = [20, 34, 56, 21, 4]
sum_scores = 0
for score in scores:
    sum_scores += score
print(f"Sum of all scores is: {sum_scores}") # 135

max_scores = 0
for score in scores:
    if score > max_scores:
        max_scores = score
print(f"Max of all scores is: {max_scores}") # 56

# for with range; (a, b] => 1 to b-1, excluding b
for number in range(1, 11):
    print(number) # prints from 1 to 10

# for with range and step
for number in range (1, 21, 2):
    print(number) # prints all the odd numbers starting with 1

# random.choice() to get an item from a list randomly
for number in range(1, 5):
    print(random.choice(fruits)) # prints random fruit from fruits list 4 times

# add a fruit with += vs append
fruits += "Pear"
print(fruits) # ['Apple', 'Banana', 'Cherry', 'P', 'e', 'a', 'r']
fruits.append("Papaya")
print(fruits) # ['Apple', 'Banana', 'Cherry', 'P', 'e', 'a', 'r', 'Papaya']

# random.shuffle(list)
characters = ['a', 'b', 'c', 'd']
random.shuffle(characters)
print(characters) # ['c', 'd', 'b', 'a']

characters = ['a', 'b', 'c', 'd', 'e']
characters_as_string = ''.join(characters)
print(characters_as_string) # abcde

nums = [2, 4, 6, 10, 15]
# nums += 20 # TypeError: 'int' object is not iterable
nums += [20]
print(nums)

# find the sum of numbers till 100

sum_numbers = 0
for num in range(1, 101):
    sum_numbers += num
print(f"Sum of 1 to 100 is: {sum_numbers}") # 5050


