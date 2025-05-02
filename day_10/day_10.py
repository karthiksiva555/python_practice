# function with output

def add(x, y):
    return x+y

z = add(10, 15)
print(f"The result of adding 10 and 15 is: {z}")

def get_formatted_name(first_name, last_name):
    """Takes fist and last name
    and returns a full name in title case"""
    first_name_title = first_name.title()
    last_name_title = last_name.title()

    return f"{first_name_title} {last_name_title}"


full_name = get_formatted_name("SIVA", "narisetty")
print(f"The full name after formatting: {full_name}") # Siva Narisetty

# Is leap year
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

print(f"The year 2020 is a leap year: {is_leap_year(2020)}") # True
print(f"The year 1989 is a leap year: {is_leap_year(1989)}") # False

# Print function prints None when function returns nothing
def get_discount(price):
    if price < 50:
        return # to be changed to 0
    else:
        return 5

print(f"your discount is: {get_discount(25)}") # None
print(f"your discount is: {get_discount(55)}") # 5

discount = get_discount(15)
print(discount) # None


