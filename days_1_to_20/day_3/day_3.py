# Day 3: Conditional Operators, logical operators, code blocks and scope

name = "SIVA KARTHIK"
name_lowercase = name.lower()
print(name_lowercase)

fruit = "cherry"
r_count = fruit.count('r')
print(f"{fruit} has {r_count} r\'s")
# cherry has 2 r's

# if else
age = int(input("Enter your age"))
if age > 60:
    print("Eligible for Senior discount.")
else:
    print("Not eligible for Senior discount")

# if elif else
person_type = input("Enter if you are a student, or senior: ")
if person_type == 'senior':
    print("Person is a senior")
elif person_type == "student":
    print("Person is a student")
else:
    print("Unknown person type.")

# Comparison operators: ==, !=, <=, >=, <, >

if age != 60:
    print("Age of the person is not 60")

# Modulo operator
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Entered number is an Even number")
else:
    print("Entered number is an odd number")

# Logical Operators: and, or and not
if age > 60 or person_type == "senior":
    print("Person is eligible for senior discount")
elif age < 18 and person_type == "student":
    print("Person is eligible for young student discount")
elif not age < 90:
    print("Eligible for free ticket")
else:
    print("No discount")

if not age > 90:
    print("Eligible for Free ticket")



