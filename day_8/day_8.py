# functions with input

def print_car_details(make, interior):
    print(f"{make} with {interior} interior.")

# Positional arguments
print_car_details("Audi", "Brown Leather")
# output: Audi with Brown Leather interior.

# problem with positional arguments
print_car_details("Brown Leather", "Audi")
# output: Brown Leather with Audi interior.

# keyword arguments
print_car_details(interior="Brown Leather", make="Audi")
# output: Audi with Brown Leather interior.

# Life in weeks exercise
def life_in_weeks(age):
    years_left = 90 - age
    weeks = years_left * 52
    print(f"You have {weeks} weeks left.")

life_in_weeks(20) # You have 3640 weeks left.
life_in_weeks(40) # You have 2600 weeks left.
life_in_weeks(80) # You have 520 weeks left.

# Love Score Exercise
def calculate_love_score(name1, name2):
    true_score = 0
    true_score += get_score(name1, "true")
    true_score += get_score(name2, "true")

    love_score = 0
    love_score += get_score(name1, "love")
    love_score += get_score(name2, "love")

    print(f"{true_score}{love_score}")

def get_score(name, true_or_love):
    true_or_love_array = list(true_or_love)
    score = 0

    for ch in name.lower():
        if ch in true_or_love_array:
            score += 1

    return score

calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Siva Karthik", "Vaishnavi")