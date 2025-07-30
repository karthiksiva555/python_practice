# Dictionaries

# Initialize a new empty dictionary
dictionary_empty = {}

# key and value can be any data type
dictionary_name = {
    "key1": "value1",
    2: "value2",
    False: "No"
}

# Get
print(dictionary_name["key1"])

# Set and Update
dictionary_name["key2"] = "value2"
dictionary_name["key1"] = "new value"

# clear the dictionary values
dictionary_name = {}

# the for loop by default gets the key of the dictionary, not the KVP
for key in dictionary_name:
    print(key)
    print(dictionary_name[key])

# Exercise
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def get_grade_by_score(score):
    if 90 < score <= 100: # instead of score > 90 and score <= 100
        return "Outstanding"
    if 80 < score <= 90:
        return "Exceeds Expectations"
    if 70 < score <= 80:
        return "Acceptable"
    return "Fail"

for student in student_scores:
    student_score = student_scores[student]
    grade = get_grade_by_score(student_score)
    student_grades[student] = grade

print(student_grades)
# {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}

# Nested Lists and Dictionaries

# list as a value
country_visited = {
    "name": "India",
    "cities_visited": ["Hyderabad", "Nellore", "Vijayawada"]
}
print(country_visited)

# dictionary as a value

country_visited = {
    "name": "India",
    "cities_visited_times": {
        "Hyderabad": 2,
        "Nellore": 15,
        "Vijayawada": 4
    }
}

# List of dictionaries
student_details = [student_scores, student_grades]
print(student_details)