import random
import pandas


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

# Dictionary Comprehension
students = ["Alex", "Dave", "Lucy", "Mandy"]
student_score = { student: random.randint(1, 100) for student in students }
print(student_score) # {'Alex': 39, 'Dave': 28, 'Lucy': 85, 'Mandy': 22}

# Conditional Dictionary Comprehension
passed_students = { student:score for (student, score) in student_score.items() if score > 60 }
print(passed_students)

# dictionary looping
employees = {
    "Siva": 89,
    "Karthik": 68,
    "Navi": 85
}

for (name, rating) in employees.items():
    print(f"Employee {name} has rating {rating}")

# number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
print(words)
result = {word:len(word) for word in words }
print(result)

# Convert temperature from Celsius to Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = { day: (temp_c * 9/5)+32 for (day, temp_c) in weather_c.items() }
print(weather_f)

# iterate rows in data frame
students_scores = {
    "student": ["Siva", "Ram", "David", "Ayesha"],
    "score": [94, 85, 69, 35]
}
student_data_frame = pandas.DataFrame(students_scores)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(f"{row.student} has scored {row.score} at {index}")

# Get Siva's and David's score only
for (index, row) in student_data_frame.iterrows():
    if row.student == "Siva" or row.student == "David":
        print(f"{row.student} has scored {row.score}")




